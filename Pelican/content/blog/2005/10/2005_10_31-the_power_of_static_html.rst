The Power of Static HTML
========================

:date: 2005-10-31 02:00
:tags: web,cms
:slug: 2005_10_31-the_power_of_static_html
:category: Technologies
:status: published





**PROBLEM** 



I
need to display my product catalog according to a number of dimensions but the
data changes slowly and isn't very complex.  Is a relational database and a web
application really appropriate?  Or can I get away with something
simpler?



**CONTEXT** 



Some
small product catalogs evolve slowly.  A detailed data model exists, including a
relational database implementation. 




**FORCES** 



On
the one hand, we have a complete relational database.  However, the traditional
RDBMS Query capability isn't very valuable when each result set only has a few
rows.  A pin-point query actually makes product comparisons
difficult.



On one hand, a sophisticated
search can produce a page with a list of related products.  However, for the
relevant dimensions, a relevant set of search results can all be computed and
stored statically with the content.  While a user might go outside these
pre-comuted indexes, it is an unlikely accident.  Further, the catalog is not
too complex; fixed lists will facilitated navigation through simplified of the
dimensions.



**SOLUTION** 



Static
HTML can represent the entire catalog.  You don't really need an active
application to do searches.



Each
dimension of presentation (by product family, by designer, by size, by cost,
whatever) can be a separate index
page.



**CONSEQUENCE** 



The
catalog has to be modeled using a dimensional star schema.  This may require
some minor changes to the database that maintains the master
catalog.



The catalog has to be
transformed into a number of parallel index structures.  This is an interesting
little programming problem in its own right. 








