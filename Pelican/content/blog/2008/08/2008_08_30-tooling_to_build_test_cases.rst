Tooling to Build Test Cases
===========================

:date: 2008-08-30 13:11
:tags: architecture,design,unit testing,tdre
:slug: 2008_08_30-tooling_to_build_test_cases
:category: Architecture & Design
:status: published







Here's a recipe for transforming a pile of similarly-formatted source spreadsheets into a suite of unittest test cases.



:strong:`Some Use Cases`



1.  The subject matter experts will tinker with the spreadsheets.  They'll invent new cases, revise old cases, retract cases.  You'll be regenerating the test suite constantly.



2.  The subject matter experts cannot reliably produce spreadsheets in a consistent format.  Get over it.  You'll be endlessly adjusting the conversion from spreadsheet to test suite.



3.  You'll be evolving the test cases as your application evolves.  You'll need to regenerate the whole test suite as you refactor your API's.



:strong:`Components`



To read spreadsheets, download `xlrd <http://www.lexicon.net/sjmachin/xlrd.htm>`_ .



To write the JUnit framework TestCase code, download `Mako <http://www.makotemplates.org/>`_ .  There are many template engines (`Cheetah <http://www.cheetahtemplate.org/>`_ , `Django <http://www.djangoproject.com/>`_ , `Myghty <http://www.myghty.org/>`_ , `Genshi <http://genshi.edgewall.org/>`_  and `Kid <http://www.kid-templating.org/>`_ ).



[I chose Mako because it is relatively lightweight and works well as a stand-alone component.  Cheetah, for instance, is hard to control for small, specialized jobs -- it seems to prefer having the ability to create relatively complex intermediate files.  Django's template can be separated from the rest of Django, but why download all that when you just want something simple.]



:strong:`Pattern`



The overall design pattern for this is a :strong:`Translator`.  This has three elements: the :strong:`Deep Structure`  -- the actual meaning -- plus a :strong:`Reader`  and a :strong:`Writer`.  The Reader builds a Deep Structure from external data in one representation.  The Writer emits the Deep Structure in another representation.



It's important to keep these three things disentangled.  You are likely to have several source spreadsheet formats, all of which lead to the same essential test case.  Similarly, you will have several test case formats that you are emitting.



Here's a piece of the spreadsheet we're starting with.  This has a Source section that defines three attributes ("Name", "Batch" and "Count") and two entities.  It has a Result section that defines one entity with the same three attributes.  



..  csv-table::

    ":strong:`Source` ","",""
    "Name","Batch","Count"
    "SomeLongName","1","1"
    "some_long_name","2","2"

    ":strong:`Result` ","",""
    "Name","Batch","Count"
    "SomeLongName","1","3"















[Let's pretend this is sample data for some kind of complicated matching algorithm that uses names, batch id numbers and counts to determine how things match.]









:strong:`Deep Structure`





Each test case generator will have a unique deep structure.  For the purposes of showing this recipe, we need to pick some kind of data model.  One common feature is that your test cases will be based on data entities.  The entities are more-or-less explicitly defined by row in the spreadsheet.  The overall test case, however, is usually implied by a series of rows with -- perhaps -- headers or notes or trailers or something to provide context.





Your actual situation will obviously vary so widely that it's dangerous even providing a sample data model.





..  code:

::

    class Entity( dict ):
        name= property( lambda self: self['name'] )
        batch= property( lambda self: self['batch'] )
        count= property( lambda self: self['count'] )

    class Case( object ):
        def __init__( self, fileName, sheetName ):
            self.fileName= fileName
            self.sheetName= sheetName
            self.source= []
            self.result= []
        def __str__( self ):
            return "%s:%s" % ( self.fileName, self.sheetName )
        def addEntity( self, entity ):
            self.source.append( entity )
        def addResult( self, entity ):
            self.result.append( entity )





This shows the Entity and the Case classes.  Yes, Entity is essentially a dict.  It's handy to conceive of the data coming from a spreadsheet as a dict.  Think of the csv package DictReader as the "standard" API.  Then develop a method for using xlrd to produce dict structures.



The properties allow us to say entity.name instead of entity['name'].  We could write a more generic version of __getattr__, but that generally leads to more complexity in handling overrides and exceptions.  Most business Entities will have rather complex definitions with many attributes and methods. 



The test Case, in this example, has some identifying information, some source Entities from the spreadsheet and a result Entity. 



:strong:`The Reader`



You'll have a Reader.  (Sometimes you'll have a class hierarchy with multiple readers, depending on how well your SME's can produce sample data.)  The Reader's job is to parse the spreadsheet and yield Cases.  It does as little as possible to build the Case.  Most data conversion or calculation is part of the Case or the Writer.

..  code:

::

    class Reader( object ):
        def __init__( self, aFileName ):
            self.fileName= aFileName
            self.wb= xlrd.open_workbook( aFileName )
            self.log= logging.getLogger( "Reader" )
        def rowIter( self, sheet ):
            """Yield all rows of a given sheet."""
            for r in range( sheet.nrows ):
                self.log.debug( "Input %d: %r", r, sheet.row(r) )
                yield r, sheet.row(r)
        def getCases( self, *sheetNames ):
            """Process given sheets to yield all Cases in this file."""
            sheetList= [ self.wb.sheet_by_name(n) for n in sheetNames ]
            for sheet in sheetList:
                rows= self.rowIter( sheet )
                for c in self.parseCase( self.fileName, sheet.name, rows ):
                    yield c
        def parseCase( self, fileName, sheetName, rowIter ):
            """Yield cases from this sheet's row iterator."""
            case= Case( fileName, sheetName )
            # Find the Source line
            for r, row in rowIter:
                if is_string(row[0]) and row[0].value == 'Source':
                    break
            # Next line is the source column headings
            r, header= rowIter.next()
            labels= [ c.value.lower() for c in header ]
            # Entities defined until the Result line
            for r, row in rowIter:
                if is_blank( row ): continue
                if is_string(row[0]) and row[0].value == "Result": break
                values= [ c.value for c in row ]
                rowDict= dict( zip( labels, values ) )
                self.log.debug( 'entity %d: %r', r, rowDict )
                e= Entity( rowDict )
                case.addEntity( e )
            # Next line is the result column headings
            r, header= rowIter.next()
            labels= [ c.value.lower() for c in header ]
            # Remaining lines are the result entities
            for r, row in rowIter:
                if is_blank( row ): continue
                values = [ c.value for c in row ]
                rowDict= dict( zip( labels, values ) )
                self.log.debug( 'result %d: %r', r, rowDict )
                e= Entity( rowDict )
                case.addResult( e )
            yield case





This shows the typical structure for a Reader.  You use it with the following kind of loop.

..  code:

::

    r= Reader( fileName )
        for c in r.getCases("Sheet1","Summary","Exception"):
            print c





Why list the sheets explicitly?  Depends on the structure of :strong:`your`  source files.  You may be able to simply iterate through the sheets.  Or you may have sheets that have to be skipped.



:strong:`Utility Functions`



Here are the three utility functions the Reader uses.

..  code:

::

    def is_empty( aCell ):
        return aCell.ctype == xlrd.XL_CELL_EMPTY
    def is_string( aCell ):
        return aCell.ctype == xlrd.XL_CELL_TEXT
    def is_blank( aRow ):
        return all( [ is_empty(c) or is_string(c) and len(c.value) == 0 for c in aRow ] )





:strong:`The Template-Based Writer`



Ideally, you'll have one standard writer that covers all of the test cases.  Of course, there may be exceptions or alternatives or other complexities.  Here's a Writer that uses Mako Templates to generate a Java JUnit TestCase.

..  code:

::

    class Writer( object ):
        def __init__( self ):
            self.template= Template( """\
    <%
        import datetime
        now = datetime.datetime.now()
        e1= case.source[0]
        e2= case.source[1]
        r1= case.result[0]
    %>\
    // Generated from ${case.fileName} ${case.sheetName}
    // On ${now}
    // By Unittest/generator.py ${version}
    package some.app.test.${case.sheetName};
    import junit.framework.TestCase;
    import some.app.model.Entity;
    import some.app.view.SomeClass;

    /**
     * Unit test ${case.sheetName}:
     * exercises SomeClass.aMethod on two entities.
     * <p> ${e1}
     * <p> ${e2}
     * <p> Expected result: ${r1}.
     */
    class Test_${case.sheetName} extends TestCase {
        Entity e1, e2;
        SomeClass sc;
        public void setUp() {
            e1= Entity( "${e1.name}", ${e1.batch}, ${int(e1.count)} );
            e2= Entity( "${e2.name}", ${e2.batch}, ${int(e2.count)} );
            sc= SomeClass();
        }
        public void testProcess() {
            aResult= sc.aMethod( e1, e2 );
            assertEquals( "${r1.name}", aResult.name );
            assertEquals( ${r1.batch}, aResult.batch );
            assertEquals( ${int(r1.count)}, aResult.count );
        }
    }
    """
            )
        def source( self, aCase ):
            return self.template.render( case=aCase, version=__version__ )





This shows a single, simple template.  Note that most of the code is the giant string with the Java code in it.  Mako reads files nicely, in case this inline string becomes uncomfortably long and complex. 



Note that we do some processing in the Writer, some of which might be better defined in the Entity or the Case.



Generally, you'll have to mix and match Mako processing with your Writer class hierarchy and processing you do in your Entity and Case class definitions.  You want to minimize the processing in Mako, just because it's a bit obscure inside the template.  On the other hand, you don't want to push everything into the business Entity or test Case classes, since they're the :strong:`Essential Meaning`  that is represented either as a spreadsheet or a JUnit unit test.



:strong:`The Main Program`



The main program is just a wrapper that binds an instance of Reader and Writer to create some test cases from source files.

..  code:

::

    def main( fileName, *sheets ):
        log= logging.getLogger( "main" )
        r= Reader( fileName )
        w= Writer()
        for c in r.getCases(*sheets):
            log.info( "Case %s", c )
            print w.source( c )

    if __name__ == "__main__":
        import sys
        logging.basicConfig( stream=sys.stderr, level=logging.INFO )
        main( "TestCase.xls", "Sheet1" )





This is the small script version of the main program.  This could be expanded to do complex parameter-parsing.  However, in these cases, it's sometimes just as simple to have an explicit list of which files and which sheets are being processed for the current release.



Also, the "print"-based solution isn't really the best.  One might prefer to open appropriate files and write the rendered template to them.  However, there are change-control issues with overwriting previous tests; you do need to confirm that the new tests compile, for example, before replacing the old tests.



:strong:`Use Case Review`



When the test cases change, it's easiest to simply slap the XLS files into subversion.  Then, subversion's youngest version number identifies the suite of test cases.  We can simply regenerate the JUnit source with our generator tool.  We have to run a quick "do the tests work?" sanity check and see what has changed.  If the changes are understood, this becomes the new suite of tests.  



Since the spreadsheets will have inconsistencies, the "simply regenerate" never works out very well.  Each release of the source may require adjusting the generator to cope with someone's inability to copy and paste consistent column names.  Sigh.  We have split our design so that our Reader can evolve and change without breaking the deep structure or the test case Writer.



When the application changes, the template will change.  We can simply regenerate the JUnit source.  After our quick "do the tests work?" we have made wholesale changes to the test cases.




