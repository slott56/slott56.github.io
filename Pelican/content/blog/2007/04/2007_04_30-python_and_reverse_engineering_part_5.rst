Python and Reverse Engineering, Part 5
======================================

:date: 2007-04-30 13:25
:tags: management
:slug: 2007_04_30-python_and_reverse_engineering_part_5
:category: Management
:status: published





Python is a top-shelf toolset for creating sample
data to do performance testing.



Let's
say that you need to validate a data warehouse design, and you need a million
facts that join with thousands of dimension entities across a half-dozen
dimensions.  You'll be generating data for seven different tables, and the data
must have all of the relational integrity in
place.



This technique applies to
transactional applications, also.  In the case of transactional data, the volume
is lower, and the referential integrity issues are more complex.  The underlying
architecture for doing the necessary testing, however, doesn't
change.



What we wind up creating is the
following kind of architecture:

-   The Data Model.  This is one or more
    Python modules which embody the various tables.  The `Django <http://www.djangoproject.com/>`_  or
    `SQLAlchemy <http://www.sqlalchemy.org/>`_   object-relational mapping (ORM) are
    big helps here.  We'll return to the value of ORM below.

-   An ETL-like data loader.  This will
    generate "random" data that has the appropriate volume and relationships.  This
    is your Mock Data generator.

-   Reporting.  This will do SQL queries to
    retrieve the target reports from the warehouse.  This is your Mock Application. 
    If you are doing transactional applications, this will be more than simple SQL
    queries:  it will be representative
    transactions.



**The Data Model.** 



An ORM-supported data model
is essential to successfully creating mock data.  Here's
why.



First, if we design in SQL (using
CREATE TABLE statements) or their equivalent Entity-Relationship Diagram (ERD)
constructs, we often miss essential features of the problem.  It helps to design
in objects, with proper relationships, independent of the limitations of the
relational model.  Too often, the foreign-key relationship restrictions lead us
to create a design that reflects the technology, not the
requirements.



Yes, the final
implementation will have to live with these limitations.  No, don't start with
those limitations in mind.  Start with the real problem in mind, and adjust the
implementation as needed.



Second, if we
have a tool that maps objects to SQL-based RDBMS, we can prototype the solution
quickly and simply.  It is very freeing to make changes to a data model, loader
and queries in one language, like Python, which is tied to the business
problem.



Yes, the final implementation
will be in vendor-specific SQL.  No, don't start with Oracle or DB2 or MySQL. 
Start with a Python object model that reflects the real problem, and get the
model correct.  Not good enough to hack together some software, but reasonably
complete, consistent and clear.  This takes about as long to do in Python as it
does to draw endless E-R diagrams.  And, the Python actually works, where the
diagrams are merely the starting point for conversations with
programmers.



Third, we can use our ORM
tool to -- trivially -- build loads, reports (and transactions.)  These model
(or prototype or proof-of-concept) applications can be thrown together very
quickly.  We can tweak this model by adding or changing indexes, doing
statistics gathering, etc.  We can also explore the numerous design alternatives
before we invest large piles of money based on paper diagrams with no real
quantitative science to back them
up.



**Mock ETL.** 



Given a data model, defined in
SQLAlchemy's notation or Django's model, we can work up loads relatively simply.
There are a few considerations that make load programs easier to
write.



First, it is simpler to create
in-memory dimensional entities, and then persist these to the database.  We can
create simple Python collections (lists or dictionaries) of the independent
entities.  These are saved to the database, but also used to create the
dependent entities and the facts.



In
the case of a data warehouse, the dimensions are independent of each other.  In
many cases, a dimension will be an exhaustive enumeration of combinations of
attribute values, meaning that the test data dimension will likely
**be**  the
production set of values.  All of the dimension entities (except for
"snowflaked" dimensions like Customers) can be fit into simple in-memory
collections (like dictionaries) with few
problems.



Here are a few tables from a
sample dimensional model.



::

    from django.db import models
    
    class StudentPopulation(models.Model):
        ethnicity = models.CharField(maxlength=30)
        disability = models.CharField(maxlength=30)
        gender = models.CharField(maxlength=8)
        giftedAndTalented = models.CharField(maxlength=30)
        class Admin:
            pass
        def __str__( self ):
            return "%s %s %s %s" % (
                self.ethnicity, self.disability, self.gender,
                self.giftedAndTalented, )
        
    class Date(models.Model):
        year = models.PositiveIntegerField()
        month = models.PositiveSmallIntegerField()
        day= models.PositiveSmallIntegerField()
        class Admin:
            pass
        def __str__( self ):
            return "%s/%s/%d" % ( self.year, self.month, self.day )
    
    class Student( models.Model ):
        studentId = models.CharField(maxlength=10)
        ssn= models.CharField(maxlength=10)
        lastName = models.CharField(maxlength=30)
        firstName = models.CharField(maxlength=30)
        middleName = models.CharField(maxlength=30,null=True)
        suffix = models.CharField(maxlength=30,null=True)
        birthDate = models.ForeignKey(Date,null=True)
        demographic= models.ForeignKey(StudentPopulation,null=True)
        class Admin:
            pass
        def __str__( self ):
            return "%s, %s %s (%s)" % ( self.lastName, self.firstName,
                self.middleName, self.studentId )





Here is a sample load script which
shows how these dimensions can be populated.



::

    from dimension.models import *
    from loadstar import *
    
    def loadStudentPopulations():
        for eth in ('white', 'asian', 'black', 'other', ):
            for dis in ( '', 'mental', 'physical', ):
                for gen in ( 'male', 'female', ):
                    for gat in ( '', 'G&T;', ):
                        pop= StudentPopulation.objects.get_or_create(
                            ethnicity= eth, disability= dis, gender= gen,
                            giftedAndTalented= gat )
    
    def loadDates():
        loadDate= Date.objects.get_or_create( year=2006, month=7, day=14 )[0]
    
    @requires(loadStudentPopulations)
    def loadStudents():
        populations= StudentPopulation.objects.all()
        for i in range( 50 ):
            pop= random.choice( populations )
            bd= Date.objects.get_or_create( year= 1990, month= i%12+1, day= i%30+1 )[0]
            try:
                stu= Student.objects.get( stateStudentId= str(i) )
            except:
                stu= Student( stateStudentId= str(i),
                    ssn= (str(i)*9)[:9],
                    lastName= 'Student%d' % ( i, ),
                    firstName= 'First%d' % ( i, ),
                    birthDate= bd,
                    demographic= pop,
                    )
                stu.save()





This load uses a mixture of
techniques.

-   For the StudentPopulation dimension, it
    enumerates all possible combinations of attribute vales.

-   For Date, we only load a single date;
    other dates will be built during fact loading.

-   For Student, we create a Date, which is
    conformed to the Date dimension.  We also select a StudentPopulation from the
    in-memory list of population
    objects.



**More Complex Loading.** 



Once we have the
independent entities populated, we can create dependent entities.  These include
bridge tables and facts.  Bridge tables often fit into memory, since they are
typically of the same cardinality as a given dimension.  However, a fact table
may be quite large, and may not conveniently reside in memory during data
generation.



In the case of snowflaked
dimensions, we have to generate these large dimensions before generating the
relevant facts.  Often, there is a relatively simple relationship between a
large dimension (e.g. Customer) and the fact (e.g. Account Balance).  We can
often generate these in parallel, producing a Customer dimension row and a dozen
Fact rows which are then persisted in the
database.



**Fact Loading.** 



Here's a sample fact table
that we'd like to load.  This depends on the dimensions shown above, plus
several others.



::

    from django.db import models
    from dwdemo.dimension.models import *
    
    class TestScore( models.Model ):
        student= models.ForeignKey( Student )
        demographic= models.ForeignKey( StudentPopulation )
        date= models.ForeignKey( Date )
        school= models.ForeignKey( School )
        grade= models.ForeignKey( GradeLevel )
        subject= models.ForeignKey( Subject )
        test= models.ForeignKey( Test )
        scoreType= models.CharField(maxlength=30)
        scoreRaw= models.FloatField(max_digits=5, decimal_places=2)
        scoreNorm= models.FloatField(max_digits=5, decimal_places=2)
        profLevel= models.FloatField(max_digits=5, decimal_places=2)
        ranking= models.CharField(maxlength=30)
        class Admin:
            pass
        def __str__( self ):
            return "%s = %s %f" % ( self.student, self.scoreType, self.scoreRaw )





Here's a load procedure to populate
facts based on the dimensional model in place.



::

    import random
    
    from dimension.models import *
    from testscore.models import *
    
    for score in TestScore.objects.all():
        score.delete()
    
    loadDate= Date.objects.get_or_create( year=2006, month=7, day=14 )[0]
    
    # Generate TestScore facts, conform and load
    schools= School.objects.all()
    grades= GradeLevel.objects.all()
    tests= Test.objects.all()
    subjects= Subject.objects.all()
    for stu in Student.objects.all():
        # StudentPopulation derived from Student
        stuPop= stu.demographic
        # School, GradeLevel, Subject and Test
        sch= random.choice( schools )
        gr= random.choice( grades )
        sub= random.choice( subjects )
        test= random.choice( tests )
        # random entry events for all students
        fact= TestScore(
            student= stu, demographic= stuPop, condition= stuCond,
            date= loadDate, school= sch, grade=gr, subject= sub,
            test= test, 
            scoreType= "1-100", scoreRaw= random.randint( 50,100 ), 
            scoreNorm= random.random(),
            profLevel= 70,
            ranking= ("Top", "Third", "Second", "Bottom")[stu.id%4],
        )
        print fact
        fact.save()





Once we have the model, and the mock
data, we can now determine how well we can produce the required reports. 
Additionally, we can experiment with ETL processing in the cases where our
source data don't fit the dimensional model very well.  Since we have sample
data, and a database, we can do meaningful comparisons between
designs.



**Mock Application.** 



For data warehousing,
the Mock Applications are simple: they are the queries that comprise the
warehouse.  Here's an example.  In this case, we bypass the ORM part of Django,
and execute SQL directly to better reflect the final implementation via a
SQL-centric reporting package.



::

    from django.db import connection
    tests= connection.cursor()
    tests.execute( """SELECT testName FROM dimension_test""" )
    for test in tests.fetchall():
        print test
        subjects= connection.cursor()
        subjects.execute( """SELECT subjectName FROM dimension_subject""" )
        for sub in subjects.fetchall():
            print ' subject:', sub
            grades= connection.cursor()
            grades.execute( """SELECT grade FROM dimension_gradelevel""" )
            for gr in grades.fetchall():
                print '  grade:', gr
                ranks= connection.cursor()
                ranks.execute( """SELECT DISTINCT ranking, count(*)
                FROM testscore_testscore tst, dimension_date dt,
                dimension_gradelevel gr, dimension_subject sub, dimension_test test
                WHERE tst.date_id=dt.id AND dt.year='2006'
                AND tst.grade_id=gr.id AND gr.grade=%s
                AND tst.subject_id=sub.id AND sub.subjectName=%s
                AND tst.test_id=test.id AND test.testName=%s
                GROUP BY tst.ranking
                """, [gr[0], sub[0], test[0]] )
                for name,count in ranks.fetchall():
                    print '   ', name, count
            print
            grades.close()
        subjects.close()
    tests.close()





**Consequences.** 



The
most important consequence is a concrete performance model with a full-sized set
of data.  This can be used on a desktop to explore design alternatives.  The
generated data sets can be used to populate a development database and explore
implementation alternatives (bit-mapped index vs. tree index, statistics
gathering, etc.)



Since the experiments
are concrete and specific, the design will be more robust than a paper model
drawn out as an ERD.  Any programming discussions can be resolved by looking at
the Mock Objects to see what the intent was behind a particular construct or
technique.  



Finally, alternatives can
explored rapidly and inexpensively.  Once a design performs well with this mock
environment, we have reason for confidence in the final production
implementation.













