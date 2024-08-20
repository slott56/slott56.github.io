Python and Reverse Engineering, Part 3
======================================

:date: 2007-04-17 14:26
:tags: reverse engineering,C,compiler
:slug: 2007_04_17-python_and_reverse_engineering_part_3
:category: Management
:status: published





The client said, "We have this program, largely
in C, which we can no longer support.  It doesn't really meet our business needs
and it doesn't fit our technology skill set."  As part of rewriting the
requirements, the question of what it
*really* 
did came up.



Actually, they had more to
say about the author's tendency toward "clever for the sake of being clever",
and "intentionally obscure."  Leaving the invective aside, they had a pile of C
and SQL.  What does it
*really* 
do?  How big is the conversion
effort?



**What To Do?** 



Time to break out the Python
tools to see what we really had.  The good news is that C is relatively easy to
parse.  The `PLY <http://www.dabeaz.com/ply/>`_   package, for example, contains a basic ANSI
C lexical scanner and parser than can be adapted to the code base at
hand.



The bad news is that the PLY
package doesn't help much with the C pre-processor (CPP) syntax.  We can,
clearly, just run the CPP on the code to get "pure" C, but we lose a little bit
of semantic richness when we do this.  Our alternative is to implement a quick
and dirty CPP-like processor to handle the
#ifdef
constructs.   Since we have the Makefile, we know which options are used and
which #ifdefs
are relevant.



The other bad news is
that embedded SQL in C has yet another pre-processor.  The SQL precompiler runs
first; it creates SQL-free C code that is handled by the CPP and finally the C
compiler, itself.  This means that we are really dealing with 3 different
languages in a single source file: the embedded SQL language, the CPP language
and the C language.



First, we'll look
at a simple side-issue in lexical scanning, the processing of new type names. 
Then we can peer into the pre-processor problem and close the loop on lexical
scanning.  We'll look at parsing in another posting.




**Lexical Scanning.** 



We need to extend PLY's
lexical scanner to recognize
typedef names. 
There are a number of alternatives here.  One choice is to relax the grammar
slightly, removing the distinction between type ID's and plain old ID's. 
Another choice is to have the parser update the lexical scanner's list of type
ID's as
typedefs are
seen.  



Instead of these two choices,
which are appropriate for the more general problem, we can simply hard-code a
list of known typedef names, and hack this list into shape as we parse the
source.  This is limiting in some respects, but it is really quick and
appropriate for a one-time use tool.  It also saves us from having to dwell on
correctly parsing the
.h
files.



There is a short list of
standard C typedefs
(size_t,
time_t,
sem_t,
ushort,
FILE, 
va_list) which
are in common use.   Similarly, the SQL precompiler only introduces
varchar and
asciz.



Here's
the revision to the
t_ID function
in
clex.py.



::

    typedefs = [
        'va_list', 'time_t', 'sem_t', 'FILE', 'size_t', 'ushort', # Standard C type names
        'varchar', 'asciz', # SQL precompiler type names
        ]
        
    def t_ID(t):
        r'[A-Za-z_][\w_]*'
        if t.value in typedefs:
            t.type = "TYPEID"
        else:
            t.type = reserved_map.get(t.value,"ID")
        return t





Before we can talk about the rest of
clex, we need to digress on the precompiler issues.  We'll tackle the SQLPC
issues first.  



**SQL Precompiler.** 



First, embedded SQL is
a foreign syntax mashed into our C program.  It has distinct lexical rules,
which apply only to the SQL blocks, not to the rest of the C program.  In
essence, we have to break the source text into two kinds of regions: SQL
regions, to which SQL syntax rules apply and host language regions (C, in this
case).



Once we've identified a SQL
statement, we don't care about most of the SQL syntax.  Indeed, we only want to
identify "declarative" SQL statements, which leave no residue in the resulting
C.  The remaining SQL statements are imperative, and will typically include a
SQL statement that is central to the processing of the program, usually a DML
statement of some kind.



To be specific,
a declarative statement like EXEC SQL INCLUDE
SQLCA; creates some well-known definitions, but
has no real impact on the resulting C program.  Similarly
EXEC SQL WHENEVER NOTFOUND
CONTINUE; adjusts the way C code is generated; it
declares some semantics, but doesn't change what we are measuring about the
resulting source text.



On the other
hand, an imperative statement like EXEC SQL
UPDATE sometable SET...; is significant.  We need
to capture this statement, and also replace the embedded SQL text with valid C
source text.



**Embedded SQL Patterns.** 



Here are some regular
expressions for tracking down Embedded SQL in C.  These aren't actually
complete, but they work well enough to analyze a large pile of source.




Note that we define the patterns as
sequences of ( token-name, pattern-text ) tuples.  Borrowing a technique from
PLY, we flatten this list of tuples into a single composite regular expression. 
The list of tuples has pleasant, easy-to-read syntax.  The resulting RE isn't
too difficult to read, but is long-winded and
repetitive.



::

    top_level_REs = (
        ( 'p_comment', r'/\*(.|\n)*?\*/' ),
        ( 'p_exec1', r'EXEC\s+SQL\s+EXECUTE\s+BEGIN\s(.|\n)*?\sEND\s*;\s+END\-EXEC;[ \t]*' ),
        ( 'p_exec2', r'EXEC\s[^;]*?;[ \t]*' ),
        ( 'p_host', r'.|\n' ),
    )
    compositeRE= '|'.join( [ '(?P<%s>%s)' % pair for pair in top_level_REs ] )
    patterns= re.compile( compositeRE, re.M|re.I )
    
    sql_REs = (
        ( 'p_sqlInclude',r'^\s*EXEC\sSQL\s+INCLUDE' ),
        ( 'p_oracleOption', r'^^\s*EXEC\sORACLE\s+OPTION' ),
        ( 'p_sqlBegin', r'^\s*EXEC\sSQL\s+BEGIN' ),
        ( 'p_sqlEnd', r'^\s*EXEC\sSQL\s+END' ),
        ( 'p_sqlDeclare', r'^\s*EXEC\sSQL\s+DECLARE' ),
        ( 'p_sqlWhenever', r'^\s*EXEC\sSQL\s+WHENEVER' ),
        ( 'p_sqlType', r'^\s*EXEC\sSQL\s+TYPE' ),
    )
    compositeRE= '|'.join( [ '(?P<%s>%s)' % pair for pair in sql_REs ] )
    sqlPatterns= re.compile( compositeRE, re.M|re.I )





The
patterns
variable contains a compiled RE which will break the source into two kinds of
regions: SQL regions, which we can examine more closely, and host-language
regions which we pass on without making any changes. 




To bound the SQL regions, we have to
recognize two kinds of SQL statements.  In the source we were given, all
procedure calls are wrapped in formal
BEGIN-END
blocks, and have
END-EXEC
markers.  All other statements are in simple
EXEC SQL
statements, with no
END-EXEC
marker.



The
sqlPatterns
variable contains a compiled RE which will make a
good guess at the kind of SQL statement.  In principle, we could include the
complete SQL language here, and actually parse the SQL.  Parsing the SQL is far
too complex for a quick overview of the code.  Instead, we treat the SQL as pure
text and hope it doesn't confuse our regular expression
patterns.



**Simulating the SQL Precompiler.** 



Here's a function
which simulate a few features of the SQL Precompiler.  This will return two
things: the host language text and a list of the embedded SQL
statements.



::

    def quoteC( aString ):
        return aString.replace( '"', r'\"' ).replace( '\n', '' )
    
    def sqlpreproc( text ):
        """Simulate a few features of the SQL pre-processor."""
        
        output= StringIO.StringIO("")
        sqlStatements= []
        match1= patterns.match(text)
        lineno= 1
        while match1:
            groups= match1.groupdict()
            #print groups
            if groups['p_comment']:
                # Comment is all host text, and may contain SQL, which is ignored.
                token= match1.group('p_comment')
                output.write( token )
            elif groups['p_host']:
                hostText= match1.group( 'p_host' )
                output.write( hostText )
            elif groups['p_exec1'] or groups['p_exec2']:
                # SQL statements interrupt host text
                sqlText= match1.group( 'p_exec1' ) or match1.group( 'p_exec2' )
                sqlTextStrip= sqlText.strip()
                sqlStatements.append( sqlTextStrip )
                if sqlPatterns.match( sqlTextStrip ):
                    # comment only
                    output.write( "/** %d: %r **/\n" % ( lineno, sqlTextStrip, ) )
                else:
                    # place-holder function for syntactic completeness
                    output.write( 'sql(%d, "%s");\n' % ( lineno, quoteC(sqlTextStrip) ) )
            else:
                raise Exception("whoops")
            lineno += match1.group(0).count('\n')
            match1= patterns.search(text, match1.end())
    
        result= output.getvalue()
        output.close()
        return result, sqlStatements





We replace imperative SQL statements
with a sql()
function call, just to preserve the original SQL text for further processing. 
The declarative SQL statements are replaced with
comments.



There are two potential gaps
with this technique.  Since we replace cursor declarations with a simple
comment, not a
sql() function call, the SQL source for the
SELECT
statement will tend to get lost.  Further, when SQL statements are built
dynamically and analyzed with EXEC SQL
PREPARE or EXEC
SQL DESCRIBE, we don't have any clear way of
analyzing source to determine the statement which gets
built.



And yes, we do raise the
**Whoops Exception** ™ in case we've done something
brain-dead like add a pattern without adding a clause to the if-statement to
handle that pattern.  This is an example of a design error that cannot be
detected until run-time; an interesting subject in it's own
right.



**Simulating the C Preprocessor.** 



The C preprocessor
has it's own unique language which has two elements:  the preprocessor
statements, which begin with #, and the host-language statements, which are
everything else.  Similar to the SQL preprocessor, we can break the source into
two kinds of regions: #-statements and everything else. 




Generally, we only care about the
#ifdef and
#ifndef
statements, since these determine the subset of C source text which is actually
compiled.  This is not universally true, since an included file could contain --
well -- anything.   However, in the case of the source presented, the author was
very well-disciplined, and the
#include files
are purely declarative; we don't need expand them in their source
context.



Here are some regular
expressions for tracking down CPP statements.  These aren't actually complete,
but they work well enough to analyze a large pile of source.  Specifically, we
recognize just enough of the
#define syntax
to get past some rather complex macro definitions.




Note that we define the patterns as
sequences of ( token-name, pattern-text ) tuples. 




::

    cpp_REs = (
        ( 'ifdef', r'\#ifdef[ \t]+(?P\w+)\n' ),
        ( 'ifndef', r'\#ifndef[ \t]+(?P\w+)\n' ),
        ( 'else', r'\#else\n'),
        ( 'endif', r'\#endif[ \t]*(?P\w*)\n' ),
        ( 'define', r'\#define\s+(?P\w+)[ \t]*(?P((?:\\\n)|.)+)?\n' ),
    )
    compositeRE= '|'.join( [ '(?P<%s>%s)' % pair for pair in cpp_REs ] )
    cppPatterns= re.compile( compositeRE, re.M )





**Condition Evaluation.** 



Each line of
host-language code, then, is surrounded by zero or more
#ifdef or
#ifndef
conditions.  We can assume an outer-most
#ifdef
condition which is always true.  As we encounter
#ifdef and
#ifndef
statements, we push additional conditions onto a
stack.  As we encounter
#endif blocks
we pop conditions from the stack.  An
#else block
pops the inner-most condition and pushes the inverse of that
condition.



The essential rule is
simple:  if all of the conditions are true, then the host language code segment
is present in the output; if any condition is false, the code segment is not
included in the output.  Here is our function for simulating the
CPP.



::

    def allTrue( context ):
        x= True
        for c in context:
            x = x and c
        return x
        
    def cpp( text, defs=set() ):
        """Simulate a few features of the CPP.
        This will leave a pre-processor-like marker in the code
        to provide a hint about removed source.
        """
        output= StringIO.StringIO("")
        definitions= []
        context= [ True ]
        match1= cppPatterns.search( text )
        while match1:
            groups= match1.groupdict()
            hostText= text[:match1.start()]
            # Check the context stack to see if we emit this or suppress it
            # if all of stack is True, emit
            if allTrue(context):
                output.write( hostText )
            else:
                output.write( "# %d lines removed by cpp\n" % ( hostText.count('\n'), ) )
            if groups['ifdef']:
                # push context stack condition
                context.append( groups['ifdefname'] in defs )
            elif groups['ifndef']:
                # push context stack condition
                context.append( groups['ifndefname'] not in defs )
            elif groups['else']:
                cond= context.pop() # pop context stack condition 
                # push reversed context stack condition
                context.append( not cond )
            elif groups['endif']:
                cond= context.pop() # pop context stack condition
            elif groups['define']:
                # just soak these up
                definitions.append( (groups['defname'],groups['defbody']) )
                #print groups
            else:
                raise Exception('Unknown preprocessor directive')
            text= text[match1.end():]
            match1= cppPatterns.search( text )
        output.write( text )
        
        result= output.getvalue()
        output.close()
        return result, dict(definitions)





As with the SQL Precompiler, we return
the resulting source, and some additional information gathered during
processing.  In this case, we return a dictionary of
#define
statements encountered.



Note that we
emit little #
*n* 
lines removed... messages in the C source.  The
PLY lexical scanner will remove these silently.  They are helpful for debugging,
however.  Generally, the CPP preserves all newline characters, so the line
numbers are preserved between input and output.  We don't take great pains with
this, since the SQL precompiler has already made a hash of our line
numbers.



The CPP does have #line
command, which many SQL precompilers use to keep the original source line
numbers consistent through every step of processing.  While important for real
compilation, we're only gathering information about the source, and can omit
this detail.



**Preprocessing Pipeline.** 



Here's what the two-part
SQL and CPP processing looks like.



::

    def demonstration():
        text= file(r"legacySource\x\y.c",'r').read()
        sqlPPText, stmts = sqlpreproc(text)
        # print sqlPPText
        flags=['DYNAMICSQL','REREAD','SUB_COMMIT','MACRO_LOCK','MATCH_PATH']
        general=['USE_HIGHEST','PARAMETER_FILE']
        cppText, definitions = cpp( sqlPPText, set(general+flags) )
        print cppText





The list of flags comes from the
Makefile.  The list of "general" definitions comes from a
general.h file
which is included everywhere.  Consequently, the output from this demonstration
function is the complete source that is being compiled in production
today.



**Building the Lexer.** 



The PLY approach allows us
to define a number of patterns and functions.  These are then built into a
single lexer object.  To cope with CPP and SQLPC, we need to define a
sqlpreproc
module which contains the
sqlpreproc and
cpp functions
outlined above.   Once we have that module, we can call those functions to
prepare input to the lexer.



The
following to demonstrates how our lexer is used.



::

    lexer = lex.lex()
    
    if __name__ == "__main__":
        #lex.runmain(lexer)
        makeFlags=['DYNAMICSQL','REREAD','SUB_COMMIT','MACRO_LOCK','MATCH_PATH']
        headerDefs=['USE_HIGHEST','PARAMETER_FILE']
        source= file(r"..\legacySource\x\y.c","r").read()
        sqlPP, statements = sqlpreproc.sqlpreproc(source)
        cpp, definitions = sqlpreproc.cpp(sqlPP,set(headerDefs+makeFlags))
        lexer.input(cpp)
        while 1:
            tok = lexer.token()
            if not tok: break      # No more input
            print tok





**Preliminary Analysis.** 



From this, we can start
to gather some preliminary data on our customer's program.  We can locate about
10,000 lines of source.  This has about 150 SQL statements scattered around. 
Really, the program is not terribly big.  However, there is dynamic SQL being
built, so some care must be taken to reverse engineer this
correctly.



C programs are just a big
collection of functions.  We'll need to know about those function definitions,
so we can get a cross-reference of function use.  Further, well-written C
programs are object-like and make extensive use of structure definitions that
stand in for proper class definitions.  We'll need to analyze these structures,
and where they are used in the program.





