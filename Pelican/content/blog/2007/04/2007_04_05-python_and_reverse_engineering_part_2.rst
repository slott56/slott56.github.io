Python and Reverse Engineering, Part 2
======================================

:date: 2007-04-05 14:25
:tags: reverse engineering,PL/SQL,SQL,database
:slug: 2007_04_05-python_and_reverse_engineering_part_2
:category: Management
:status: published





A stored procedure isn't really very easy to
understand.  There's a profound fascination with triggers and stored procedures,
and they're both really bad ideas.  I can't say enough bad things about stored
procedures.  See `PL/SQL vs. Java - Which is REALLY faster? <{filename}/blog/2007/03/2007_03_23-plsql_vs_java_which_is_really_faster.rst>`_  and
`Over-Solving the Problem or When your architect is a
DBA... <{filename}/blog/2006/06/2006_06_20-over_solving_the_problem_or_when_your_architect_is_a_dba.rst>`_  for related
ranting.



The customer gave us a
300-line stored procedure, and said that it was broken.  After looking at it for
a while, I realized that it was uselessly incomplete.  We saw a demo of the
transaction.  I asked for the code which actually implemented the web page we
saw, and got a VB module of about 100 lines of code. 




When I got back to the office, I found
that the VB procedure they gave me called three other VB modules before calling
the stored procedure.  So, I had to ask for the additional code.  I now had more
code than I could comfortably read and process in my
head.



**What To Do?** 



Time to break out the Python
tools to see what we really had.  The good news is that VB is relatively easy to
parse.  The better news is that we aren't interested in a lot of details, just
the SQL statements.  The best news is that they consistently put SQL statements
into a variable named
SqlStr, making
the SQL statements easy to find.



Here's
some code for analyzing VB modules to try and locate some nuggets of useful
information.  We'll start out with a simplistic lexical analyzer to cope with
the _ statement continuation markers.



::

    import re, string
    
    def srcLine( text ):
        lineNo= 0
        line= ""
        firstLine= None
        for i in text.split('\n'):
            lineNo += 1
            i= i.rstrip()
            if not i: continue
            if i[0] == "'":
                continue
            elif i[-1] == '_':
                if line:
                    line += i[:-1].lstrip()
                else:
                    line= i[:-1]
                firstLine= firstLine or lineNo
                continue
            else:
                yield firstLine or lineNo, line + i
                line= ""
                firstLine= None
    
    def lex( text ):
        """Ultra-simple: whitespace or quotes strings or keyword/variable/number 
        or punctuation.  This tends to break up floating-point numbers into two tokens."""
        token= re.compile( '(\s+)|((?:"[^"]*")|(?:\w[\w%#]*)|(?:.))' )
        for num, s in srcLine( text ):
            m= token.match(s)
            while m:
                if m.group(2):
                    # Discards whitespace gracefully
                    yield num, m.group(2)
                s= s[m.end():]
                m= token.match(s)
            yield num, None # Visible end-of-statement





The
lex() function
will yield a stream of line numbers and tokenized statements, followed by a
None to
indicate that we've run out of statements (including continued
statements.)



Here's a simple token
aggregator that iterates through all of the VB statements, handling
continuations and multiple statements per line
gracefully.



::

    def vbstmt( text ):
        stmt= []
        firstLine= None
        for lineNo, token in lex( text ):
            if token:
                stmt.append( token )
                firstLine= firstLine or lineNo
            else:
                yield (firstLine or lineNo), stmt
                stmt= []
                firstLine= None





**Starting to Explore.** 



Here's a quick function
that demonstrates that we really can find SQL statements based on the variable
to which a string is assigned.  The output from this function proves that this
variable has only one purpose in the application.



::

    def sqlStr( text ):
        for num, line in srcLine( text ):
            pos= line.find("SqlStr")
            if pos != -1:
                print num, line[pos:].lstrip()





Here's a higher-level function that
uses an analytical function as an "analyzer", which it applies to the text of
several source files.



::

    def getSQL( analyzer=sqlStr ):
        import glob, os.path
        for nm in glob.glob("*.vb"):
            print nm
            f= file( os.path.join( "src", nm ), "r" )
            analyzer( f.read() )
            f.close()
            print
    
    getSQL( sqlStr )





**Moving Further Into the Unknown.** 



We need some complexity
metrics.  Here's a quick estimator that counts tokens in each source file. 
Given the frequency histogram of tokens, we can see which variables and
statement types are used.  We can locate the variables, modules and functions,
also.



::

    def tokenCount( text ):
        total= 0
        count= 0
        tokenFreq= {}
        for num, stmt in vbstmt( text ):
            #print num, len(stmt)
            for t in stmt:
                tokenFreq.setdefault( t, 0 )
                tokenFreq[t] += 1
            count += 1
            total += len(stmt)
        print "total", total
        print "count", count
        print "tokens/line", total/float(count)
        tList= tokenFreq.items()
        tList.sort(lambda a,b:-cmp(a[1],b[1]))
        cumulative= 0
        for t,f in tList:
            cumulative += f
            print t,f,cumulative
    
    getSQL( tokenCount )





**The Curse of Dynamic SQL.** 



Since the SQL is assembled as
a large character string, we need to derive what the effective SQL statement is.
This means interpreting the VB assignment statement (to the extent possible.) 
This gives us a clearer picture of what the SQL is, and where the dynamic
elements are inserted.



This function
evaluates the assignment statement, returning the assembled SQL text, and the
variables which were inserted into the SQL text.



::

    def qdEval( stmt ):
        """Quick and dirty eval of a dynamic SQL statement."""
        buffer= ""
        variables= []
        stmt.pop(0)
        stmt.pop(0)
        while len(stmt) >= 1:
            t= stmt.pop(0)
            if t == '+':
                pass
            elif t[0] == '"':
                # literal
                buffer += t[1:-1]+"\n"
            elif t[0] in string.ascii_letters:
                # Look ahead one token.
                if stmt and stmt[0] == '(':
                    # This is a function call, which ends with ')'.
                    funcall= stmt.pop(0)
                    while funcall != ')':
                        t += funcall
                        funcall= stmt.pop(0)
                    t += funcall
                elif stmt and stmt[0] == '!':
                    # This is an object reference
                    t += stmt.pop(0) # the "!"
                    t += stmt.pop(0) # the attribute name
                else:
                    # This is a simple identifier
                    pass
                buffer += "{%s}" % ( t, )
                variables.append( t )
            else:
                raise Exception( "Can't parse %r" % ( t, ) )
        return buffer, variables





This analyzer locate the SQL
statements, and uses
qdEval to
produce a summary of the overall SQL work done by a given
module.



::

    def sqlDetl( text ):
        def assignment( stmt ):
            global sqlCount, variables
            sqlCount += 1    
            print num
            try:
                buffer, varList = qdEval( stmt )
                print buffer
                for v in varList:
                    variables[v]= True
            except Exception, e:
                print "##", e
                print "##", stmt
        def statement( stmt ):
            if len(stmt) > 2 and stmt[1] == '=':
                if stmt[0] == 'SqlStr':
                    assignment( stmt )
            elif stmt[0] == 'If':
                # Is there a Then _ continuation?
                while stmt and stmt[0] != 'Then':
                    stmt.pop(0)
                if stmt:
                    assert stmt[0] == 'Then'
                    stmt.pop(0)
                if stmt:
                    statement( stmt )
            else:
                #print num, stmt[0]
                pass    
        global variables, sqlCount
        variables= {}
        sqlCount= 0
        for num, stmt in vbstmt( text ):
            statement( stmt )
        print "Bind Variables:", variables.keys()
        print "SQL Statements:", sqlCount
    
    getSQL( sqlStr )





While we don't know everything, we now
know quite a bit more.  We've got 3,000 lines of code, 157 distinct SQL
statements, amounting to about half the code volume.  We can identify 20
distinct tables involved in the entire
process.



**Discovery with Python.** 



With Python, I was able to
analyze 3,000 lines of VB in a day or two, and provide metrics in which we were
completely confident.  We could show precisely how the 300 line problem they
started with was really a 3,000 line problem.  And, we could also show that this
still wasn't really in the ballpark for what was
needed.



Best of all, I have reused this
code to analyze other VB programs to gather similar statistics.  Universally,
the "simple" application that needs to be rewritten is at least an order of
magnitude more complex than the glib assertions of our
customers.



**Bottom Line.** 



We had to given them a price
which was unacceptably large.  The legacy program, while 10x as large as the
originally claimed, isn't all that big.  However, those VB modules fit into a
larger business process.



Looking
outside the narrow VB and SQL world, they described 15 use cases for at least
three kinds of actors.  Without doing detailed domain analysis, we have to
assume that each relational table is (approximately) one object class.  [Yes,
relational tables can be only a portion of a composite class, or a "pre-join" of
multiple classes.  However, we don't know otherwise, so we have to assume
something.]



Building the 15 use case
application, coupled with reverse engineering, will take close to a person-year
of effort.



**Customer Value.** 



Of course, no one is happy
with this kind of result.  They thought that they had 300 lines of code, and it
would take a few months.  We found 3,000 lines of code.  We also found that
there were 14 other use cases in addition to the one they claimed was
relevant.



Were we wrong to expand the
scope?  Yes, because it wasn't what the customer expected.  No, because we
couldn't have accomplished what the customer demanded.





