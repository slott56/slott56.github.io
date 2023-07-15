Django Capacity Planning -- Reading the Meta Model
==================================================

:date: 2009-10-16 14:34
:tags: Django,database design,capacity planning
:slug: 2009_10_16-django_capacity_planning_reading_the_meta_model
:category: Technologies
:status: published

I find that some people spend way too much time doing "meta"
programming. I prefer to use someone's framework rather than (a)
write my own or (b) extend theirs. I prefer to learn their features
(and quirks).

Having disclaimed an interest in meta programming, I do have to
participate in capacity planning.

Capacity planning, generally, means canvassing applications to
track down disk storage requirements.

Back In The Day
---------------

Back in the day, when we wrote SQL by hand, we were expected to
carefully plan all our table and index use down to the kilobyte. I
used to have really sophisticated spreadsheets for estimating --
to the byte -- Oracle storage requirements.

Since then, the price of storage has fallen so far that I no
longer have to spend a lot of time carefully modelling the
byte-by-byte storage allocation. The price has fallen so fast that
some people still spend way more time on this than it deserves.

Django ORM
----------

The Django ORM obscures the physical database design. This is a
good thing.

For capacity planning purposes, however, it would be good to know
row sizes so that we can multiply by expected number of rows and
cough out a planned size.

Here's some meta-data programming to extract Table and Column
information for the purposes of size estimation.

::

     import sys
     from django.conf import settings
     from django.db.models.base import ModelBase

     class Table( object ):
        def __init__( self, name, comment="" ):
            self.name= name
            self.comment= comment
            self.columns= {}
        def add( self, column ):
            self.columns[column.name]= column
        def row_size( self ):
            return sum( self.columns[c].size for c in self.columns ) + 1*len(self.columns)

     class Column( object ):
        def __init__( self, name, type, size ):
            self.name= name
            self.type= type
            self.size= size

     sizes = {
        'integer': 4,
        'bool': 1,
        'datetime': 32,
        'text': 255,
        'smallint unsigned': 2,
        'date': 24,
        'real': 8,
        'integer unsigned': 4,
        'decimal': 40,
     }
     def get_size( db_type, max_length ):
        if max_length is not None:
            return max_length
        return sizes[db_type]

     def get_schema():
        tables = {}
        for app in settings.INSTALLED_APPS:
            print app
            try:
                __import__( app + ".models" )
                mod= sys.modules[app + ".models"]
                if mod.__doc__ is not None:
                    print mod.__doc__.splitlines()[:1]
                for name in mod.__dict__:
                    obj = mod.__dict__[name]
                    if isinstance( obj, ModelBase ):
                        t = Table( obj._meta.db_table, obj.__doc__ )
                        for fld in obj._meta.fields:
                            c = Column( fld.attname, fld.db_type(), get_size(fld.db_type(), fld.max_length) )
                            t.add( c )
                        tables[t.name]= t
            except AttributeError, e:
                print e
        return tables

     if __name__ == "__main__":
        tables = get_schema()
        for t in tables:
            print t, tables[t].row_size()

This shows how we can get table and column information without too
much pain. This will report an estimated row size for each DB
table that's reasonably close.

You'll have to add storage for indexes, also. Further, many
databases leave free space within each physical block, making the
actual database much larger than the raw data.

Finally, you'll need extra storage for non-database files, logs
and backups.





