Python and Reverse Engineering, Part 4
======================================

:date: 2007-04-18 15:47
:tags: reverse engineering,C,compiler
:slug: 2007_04_18-python_and_reverse_engineering_part_4
:category: Management
:status: published





At this point, we have
clex.py, which
uses
sqlpreproc.py
to create a proper lexer for C source code.  We use `PLY <http://www.dabeaz.com/ply/>`_  's ANSI C
parser
(cparse.py) as
the backbone of our own analysis of
C.



**The C Language.** 



Separate from the lexical
structure of C (the spelling and punctuation part) and separate from the
semantic structure of C (what it does at run-time), there's a syntactic
structure of C.  These are the constructs we "mean" when we write C source;
these constructs have a structure at compile time, which generates behavior at
run time.



Principally, a C source file
is a series of declarations.  We declare variables and functions.  One of those
functions,
main, is
special.



To model this, we'll define a
module,
language, which
has class definitions for various syntax structures.  We'll use this language
module in our ANSI C parser
(cparse) to
build useful objects that we can use for reporting and
analysis.



**The Declaration.** 



Here's a simplistic
superclass for the family tree of C declarations.  This covers just enough
structure to capture the essence of the declaration.  We're not compiling,
merely analyzing.



Since PLY makes it so
easy to simply use tuples, many of the syntax rules will create normalized
tuples with
None filling in
for missing or optional elements of the language.



::

    class Declaration( object ):
        """Built from a 3-tuple: ( 'decl', type, declList )"""
        def __init__( self, typeSpec, declList ):
            self.typeSpec= typeSpec
            self.declList= declList
            self.body= [] # Empty = not a function declaration
            if self.declList == None: return
            for d in self.declList:
                if d[0] == '=':
                    # 3-tuple: ( '=', decl, init )
                    # analyze this declaration to get the variable name
                    # analyze the initializer to locate function calls
                    _, decl, init = d
                    # Dig into the initializer and build an Expression.instance
                    _, initBody= init
                elif d[0] == 'decl':
                    # analyze this declaration to get the variable name
                    decl= d
                    init= None
                else:
                    raise Exception( decl )
                # decl is 3-tuple( 'decl', pointer, directDecl )
                # init is 2-tuple( 'init', expr )
        def __str__( self ):
            return "%s %s" % ( self.typeSpec, self.declList )
        def symbol( self ):
            return None
        def references( self ):
            # TODO: initializers can involve function calls!
            # However, in C they have to be "constant" expressions which can be evaluated
            # at compile time, so the cross-references are rarely very interesting.
            # In C++ (and Java) they aren't restricted in this way.
            return []





Within
cparse, we use
this as follows.  We'll extend the
p_external_declaration_2
rule with a call to build a Declaration from the
syntax accumulated in the parser state tuple,
t.



::

    import language as C
    
    def p_external_declaration_2(t):
        'external_declaration : declaration'
        #print 'declaration', t[1]
        t[0]= C.Declaration( *t[1] )





**The Function Declaration.** 



Really, we're
interested in function declarations more than variables or references.  A
function declaration is a subclass of declaration that introduces some
additional details, like a body, and some analysis
methods.



::

    class Function( Declaration ):
        """built from 5-tuple: ( 'def', specifiers, declarator, declaration_list, statement )"""
        def __init__( self, defStr, declaration_specifiers, declarator, declaration_list, compound_statement ):
            self.spec= declaration_specifiers
            _, self.ptr, direct_declarator = declarator
            if direct_declarator[0] == 'ddecl()':
                # New-style function declaration
                _, direct_declarator, self.args = direct_declarator
                _, self.name= direct_declarator
            else:
                self.name= declarator # actually a TUPLE of stuff
                self.args= declaration_list
            self.defs= compound_statement.decl
            self.body= compound_statement.body
        def __str__( self ):
            if self.defs:
                defsTxt=";\n".join( map( str, self.defs ) )
            else:
                defsTxt=""
            bodyTxt= ";\n".join( map( str, self.body ) )
            return "def %s %s (%s) {\n%s\n%s\n}" % ( 
                self.spec, self.name, self.args, defsTxt, bodyTxt )
        def symbol( self ):
            return self.name
        def references( self ):
            # TODO: The declarations in self.defs could involve function calls!
            refs= set()
            for stmt in self.body:
                #print " ", stmt
                refNames= [ r[1] for r in stmt.references() ]
                refs |= set(refNames)
            return refs





Within
cparse, we use
this as follows.  We'll extend the
p_external_declaration_1
rule with a call to build a Function from the
syntax accumulated in the parser state tuple,
t.



::

    import language as C
    
    def p_external_declaration_1(t):
        'external_declaration : function_definition'
        t[0]= C.Function( *t[1] )





**Expressions.** 



The
body of a function declaration is a sequence of statements.  A statement either
is an expression, or contains expressions.  The expression is the lowest-level
unit of grammar that we're interested in.  Here's a declaration for an
Expression class to support analysis of expressions in
C.



::

    class Expression( object ):
        def __init__( self, tree ):
            self.tree= tree
        def __str__( self ):
            return str( self.tree )
        def refsList( self ):
            # any calls? must dig recursively into the expression's syntax tree
            return self.walkTree( self.tree )
        def walkTree( self, aTree ):    
            refs= []
            if isinstance(aTree,tuple) and aTree[0] == 'call':
                # AHA! - a function call
                refs.append( aTree )
            # Even if we found a call, descend into the arguments, also.    
            if isinstance(aTree,tuple):    
                for subExpr in aTree[1:]:
                    if subExpr and isinstance(subExpr,tuple):
                        sub= self.walkTree( subExpr )
                        if sub: refs.extend( sub )
            return refs





While this could be used in
cparse as each
expression is parsed, we're too lazy to do that properly.  Instead, we'll build
expressions as part of assembling each Statement.  The idea is to build a small
syntax tree with only the parts we're going to analyze, ignoring numerous other
details of the C
language.



**Statements** .



C
has a large number of statement types.  We won't dig into each type, but will
show a few representative types and how they are built by our
parser.



The Statement superclass has
the following definition.



::

    class Statement( object ):
        def __init__( self, tree ):
            self.tree= tree
        def __str__( self ):
            return str( self.tree )
        def references( self ):
            # any calls? must dig recursively into the statement's syntax tree
            raise NotImplementedError( repr(self.tree) )





When we recognize a statement in the
parser, we use the following factory function to map the syntax into a useful
subclass of Statement.  The global
stmtFactory
dictionary isn't complete, but it handles the statements in the 10,000 lines of
source we're analyzing.  Whenever we fail to find an appropriate subclass of
Statement, we use the superclass, which (eventually) throws a
NotImplementedError,
and we can then define the needed Statement
subclass.



::

    stmtFactory = {
    '{': CompoundStatement, 
    'return': Return, 
    'for': For, 
    'while': While, 
    'do': While, # Same structure, different semantics
    'if': If,
    'switch': Switch,
    'case': Case, 
    'default': Default, 
    'break': Empty, 
    'continue': Empty, 
    'goto': Empty,
    'cast': Cast, 
    'call': Call, 
    '+=': Assignment, 
    '-=': Assignment, 
    '=': Assignment, 
    '--': IncDec,
    '++': IncDec, 
    'expr': ExprStmt,
    }
    
    def makeStatement( *args ):
        # Factory for subclasses of Statement
        try:
            cn= stmtFactory.setdefault( args[0], Statement )
            return cn( args )
        except TypeError, e:
            import sys, traceback
            print "***"
            print e
            print repr(tree)
            raise





Here's are two typical
cparse rules
for recognizing statements and using
makeStatement
to create a Statement
instance.



::

    # iteration_statement:
    def p_iteration_statement_2(t):
        'iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement '
        t[0]= C.makeStatement( 'for', (t[3], t[5], t[7]), t[9] )
    
    # expression-statement:
    def p_expression_statement(t):
        'expression_statement : expression_opt SEMI'
        t[0]= C.makeStatement( 'expr', t[1] )





**Statement Subclasses.** 



Rather than present all
of the subclasses of Statement, here are two that match the
iteration_statement
and
expression_statement
syntax categories.



::

    class For( Statement ):
        def __init__( self, tree ):
            super( For, self ).__init__( tree )
            _, exprTuple, self.body = self.tree
            ex1, ex2, ex3 = exprTuple
            self.ex1= Expression( ex1 )
            self.ex2= Expression( ex2 )
            self.ex3= Expression( ex3 )
        def references( self ):
            refs= self.ex1.refsList() + self.ex2.refsList() + self.ex3.refsList()
            refs.extend( self.body.references() )
            return refs
    
    class ExprStmt( Statement ):
        def __init__( self, tree ):
            super( ExprStmt, self ).__init__( tree )
            _, expr= self.tree
            self.expr= Expression( expr )
        def references( self ):
            return self.expr.refsList()





**How It Fits.** 



Here's a quick review of how
the whole process fits together.  Essentially, the main function is the parser,
inside
cparse.py.  The
parser is called
yacc.parse, and
is built secretly when
cparse is
imported.  The parser consumes a sequence of tokens, produced by the lexer. 
When the parser recognizes a specific syntax construct, it executes the body of
a function which is tied to that syntax rule.  This function may create a
Declaration, a Function or a call c.makeStatement to create an appropriate
subclass of Statement.  Some parser functions accumulate tuples of other syntax
elements, saving them until the higher-level constructs get
created.



The lexer,
clex, is used
by the parser to break C language source into individual tokens: keywords,
identifiers, punctuation marks.  The lexer, in turn, relies on
sqlpreproc to
handle the embedded SQL and CPP constructs mashed into the C source
code.



**Analytical Programs.** 



Here's an analytical
program which examines the C source files the client gave us.  Note the
extension to the typedef handling described in `Part 3 <{filename}/blog/2007/04/2007_04_17-python_and_reverse_engineering_part_3.rst>`_ .  As the parser trips over typedefs, we
accumulate the list manually, rather than correctly hand new type names from
parser to lexer.  The
parse function
parses a single file, and returns the sequence of declarations (the syntax tree)
in that file.   The
analyzeDefCall
function examines each declaration looking for function definitions and function
calls.



::

    """Parse and Analyze the legacy source."""
    
    import clex
    import cparse
    import sqlpreproc
    import language
    
    import pprint, os.path
    
    # HACK: rather than examine typedef statements, we simply force the type names
    # into the lexical scanner.
    clex.typedefs.extend( [ 'AccountType', 'PaymentType', 'SettleType', 
        'LogLevel', 'Condition', 'MethodType', 'ConditionPtr',
        'VISIT',
        'Parameter', # subtle issue here--- this is a typedef in the .c file :-(
        'DocCombo',
        'InvoiceType', 'ModeType', 'StatusType', 'FlagType'
    ] )
    
    def parse(fileName,debug=0):
        source= file(fileName,"r").read()
        makeFlags=['DYNAMICSQL','REREAD','SUB_COMMIT','MACRO_LOCK','MATCH_PATH']
        headerDefs=['USE_HIGHEST','PARAMETER_FILE']
        sqlText, statements = sqlpreproc.sqlpreproc(source)
        cppText, definitions = sqlpreproc.cpp(sqlText,set(headerDefs+makeFlags))
        print "SQL: ", len(statements)
        pprint.pprint( statements )
        tree= cparse.yacc.parse(cppText, debug=debug ) 
        return tree
    
    def analyzeDefCall( tree ):
        print "----Analysis----"
        symbols= {}
        for decl in tree:
            if decl.symbol():
                symbols[decl.symbol()]= decl
        pprint.pprint( symbols )
        print "XREF"
        for decl in tree:
            if decl.body:
                print "%s\t%s" % ( decl.name, "\t".join(decl.references()) )
            else:
                print "Calls in", decl
    
    def analyzeSource( dir, debug=0 ):
        import glob
        files= glob.glob(os.path.join(dir,'*.c')) 
        for f in files:
            print
            print f
            tree= parse( f, debug )
            analyzeDefCall( tree )





The
analyzeSource
function is the top-level main analysis function. 




**Results.** 



We
know that there are 162 distinct functions defined.  We can, based on source
file and other hints, narrow this to about 93 functions that are truly relevant.
Within these functions, we can extract cross reference information that serves
as a checklist to be sure that each function is completely
analyzed.



Additionally, we can
partition the function definitions into "primitive" and "moderate" and
"complex".  About one third of the definitions appear to be primitive functions
that call two or fewer other functions, and seem to have a simple, clear
purpose.  Another third are complex functions that reference seven or more other
functions, and are difficult to characterize.  The remaining third of the
functions call between three and six other functions, and are of moderate
complexity.



This analysis helps us
narrow our focus to about 20% of the function definitions (31 out of 162) which
seem to do all the work.  This is not a subjective evaluation, but is based on
simple scanning of the syntax using extremely powerful analytical tools.  Python
allows us to rapidly modify, extend and adapt these tools, producing useful,
relevant outputs with minimal effort.





