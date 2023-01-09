Control Break Reporting
=======================

:date: 2006-02-06 23:49
:tags: books,building skills,#python
:slug: 2006_02_06-control_break_reporting
:category: Books
:status: published





Control Break Reporting is a design pattern that
has been around since the earliest days of business applications.  It solves the
problem of producing a report on nested (or hierarchical) data, the kind often
found in a chart of accounts.  



The
result of control break reporting is a properly nested set of reports, each of
which has localized subtotals.  The details add up to a deeply nested subtotal. 
The subtotals add up to higher and higher level totals, and the top-level totals
add to a grand total.



The classical
algorithm for control break reporting, however, tends to hide the basic
hierarchy under a welter of details about keys and totals and subtotals.  It
can't produce "heading" totals or counts, only footing totals or counts.  As
soon as you want additional features, you may as well ditch the classical
algorithm.



**The Problem is the Sort** 



The most important thing I
dislike about the classical control break algorithm is the sort that's required.
Sorting is an expensive operation.  Rarely does a control break report show all
of the detail with all of the nested totals, so why should I sort all that data
only to produce higher-level
subtotals?



The sorting seems so logical
and necessary.  Often our data isn't in the desired order, so sorting it makes
superficial sense.  More to the point, however, is that no one wants all the
data in a single report.  Even if I did produce a PDF file with all 21,000
accounts in the general ledger, people only want their little section of
details, or they want a slice down to a depth of 3 from where their ownership of
the finances starts.  



The CFO wants
the top-most totals.  The manager of production wants her costs, and the next
few levels of summary data.  Her shift supervisors want the details for their
specific times and production areas.    No one wants ALL of the data.  If no one
wants all of the data, why sort all of
it?



**The Data is Dimensional** 



Most of the interesting
reporting problems have a combination of two features: dimensions and
hierarchies.  The basic numeric measurements (dollars, hours, pounds, pallets,
and the like) are the facts on which we are reporting.  Each fact has a number
of relevant dimensions along which that fact is measured.  We might, for
example, have sales dollars by product, by fiscal period, by sales person; this
is a three-dimensional analysis.  We could group these three dimensions in any
of 6 different orders, and produce a number of hierarchies with different kinds
of totals.  



In additional to the
independent dimensions of a fact, each dimension may be a hierarchical grouping
of data.  Time, for example, has groupings of days, weeks, months, quarters and
years.  Sales people may be organized into territories, regions and countries. 
Products may be organized into lines and
families.



In the Cookbook example from
ASPN, they have one dimension: the sales organization.  This is broken into
branches and sales people.  This forms a tidy hierarchy, good for a simple
example.



In most kinds of reporting,
however, there are often a large number of dimensions.  Worse, there may be
complex relationships within a dimension.  For example, the calendar has weeks
and months, but months don't fall on nice weekly boundaries.  Similarly, our USA
office may have many regions in a single country, but our European office may
combine several countries in a region. 




**The Solution is a Mapping** 



The right way to handle
Control Break reporting in Python is through a design pattern that is a
variation on the Index or the Inverted Database.  I prefer to call it the
Dimensional Map, because that's a better clue as to how it
works.



Let's look at the data we have
in the ASPN example:



..  code:

::

    records = [("branch1",  "sales1", 100),
               ("branch1",  "sales1", 50),
               ("branch1",  "sales2", 10),
               ("branch2",  "sales1", 104),
               ("branch2",  "sales2", 56),
               ("branch2",  "sales2", 156)]





In this case, we have two keys (branch
and sales person), and one fact (the sales dollars).  What we will make is a Map
of the branches.  Each entry in the branch-level Map is a Map of the sales
people.  Each entry in the person-level map is a list of their detailed sales
dollars.  We can then traverse these nested maps to write the report we want to
see, correctly labeled with headers and footers.  We can, without too much extra
work. have totals in the header as well as the footer.  I'll leave that as an
exercise.



It works like
this:



..  code:

::

    branchMap= {}
    for branch, person, dollars in records:
        branchMap.setdefault( branch, {} )
        personMap= branchMap[ branch ]
        personMap.setdefault( person, 0 )
        personMap[person].append( dollars )
    
    branchList= branchMap.keys()
    branchList.sort()
    for branch in branchList:
        print "header Branch", branch
        personMap= branchMap[branch]
        personList= personMap.keys()
        personList.sort()
        for person in personList:
            print "header Person", person
            for data in personMap[person]
                print data
            print "footer Person"
        print "footer Branch"
    print "grand Total"





This little script is essentially
hard-wired for this simple two-dimensional analysis.  It doesn't take too much
cut-and-paste to expand this to the desired number of levels.  It isn't,
however, the most general solution.  For that, we need a better class
design.



**Expanding On The Pattern** 



The real problem with
Control Break reporting is the recursion.  Any level of the report (except the
numeric facts) is a recursive structure: it contains a Map of the next lower
level of detail.  We can define a class, Dimension, which does two things for
us. 

-   Dimension carries the data elements for
    that Dimension, the key and the next lower level Dimension object with the
    details.  A Dimension's key may contains a Fact object which has a simple
    unkeyed list of values. 

-   Dimension handles the recursive structure
    implied by the hierarchy.  We have methods which process data recursively,
    treating each subsidiary Dimension (or Fact) in a uniform
    way.



A simple tail recursion technique
assures that each Dimension contains subsidiary Dimensions, and the most
deeply-nested item is the basic Fact.  This leads to programs that fit the
recursive model of a number of dimensions, terminated by a single
fact.



To keep the classes polymorphic,
both Dimension and Fact must implement an
append() method
that loads data and a
report() method
that produces the final report on the data. 




Further, to keep this example simple,
we'll make each object a combination of data and meta-data.  The data is the
mapping of key to details or the list of facts.  The metadata is the column name
and the relationship with the lower-level dimensions.  The metadata is a
universal truth about the data. 



We
have multiple instances of each object: there are multiple branches and multiple
people.  We'll need to create additional collections to hold the data.  We'll do
this by cloning the object definition.  There's a better way to do this by
separating the metadata from the actual detailed numeric data, but that is a
more complex solution, not a simple recipe.



..  code:

::

    import copy
    
    class Fact( object ):
        """A Fact is a measurable quantity."""
        def __init__ ( self, name ):
            self.name= name
            self.data= []
            self.total= 0
        def append( self, item ):
            self.data.append( item[0] )
            self.total += item[0]
        def values( self ):
            return self.data
        def report( self, depth=0 ):
            for d in self.data:
                print depth*' ', d        
    
    class Dimension( object ):
        """A Dimension is a value to group Facts or Dimensions."""
        def __init__( self, name, child=None ):
            self.name= name
            self.map= {}
            self.child= child
            self.total= 0
        def append( self, row ):
            """The first value is the key for this dimension.
            The remaining values are other dimension keys or the fact value.""
            key= row[0]
            values= row[1:]
            self.map.setdefault( key, copy.deepcopy(self.child) )
            self.map[key].append( values )
        def keys( self ):
            keyList= self.map.keys()
            keyList.sort()
            return keyList
        def get( self, value ):
            return self.map.get( value )
        def report( self, depth=0 ):
            """Report this dimension, relying on other Dimensions or Facts."""
            self.total= 0
            for k in self.keys():
                print depth*' ', self.name, k, 'header'
                self.map[k].report( depth+1 )
                self.total += self.map[k].total
                print depth*' ', k, 'total', self.map[k].total





Loading this structure with data is
pleasantly simple.  We define the nested structure of our Dimensions and the
Fact which they contain.  This same recursive structure can then be used to
break up each record into a key and the data associated with that
key.



..  code:

::

    analysis= Dimension( "branch", Dimension( "person", Fact( "dollars" ) ) )
    
    for row in records:
        analysis.append( row )





Reporting, similarly, relies on the
recursive structure of Dimension objects nested within Dimension
objects.



..  code:

::

    analysis.report()
    print analysis.total





**More Generalization** 



Since some people
are uncomfortable with the recursion, and would prefer this to use a flat list
of Dimension and Fact objects.  This flat list can be used with explicit
for-loops to parse the input and assign an appropriate structure.  We'll post
this solution in the future,
perhaps.



Additionally, it would be nice
to allow for multiple Facts and not force the file to be kept with the columns
in order from most general to most specific.  The first improvement (multiple
facts for reporting) is a pretty simple generalization.  The second, however, is
a matter of a simple map to switch the order in which the columns are examined
to create the various levels of
detail.



Finally, the separation of
meta-data from the real application data would shift the complexity around.  It
would make some of this simpler, but it would introduce more classes into the
solution.









