Genius Move -- Characteristic Functions
=======================================

:date: 2008-06-07 13:54
:tags: #python,database
:slug: 2008_06_07-genius_move_characteristic_functions
:category: Python
:status: published







The comment was eaten by Haloscan, but here's the text...




You need to read Rozhenstein on characteristic functions.  





..  code:

::

    select
    sum(case when a < .5 then 1 else 0 end) 'A'
    ,sum(case when a >= .5 and a < .75 then 1 else 0 end) 'B'
    ,sum(case when a >= .75 then 1 else 0 end) 'C'
    ,bar
    from foo
    group by bar






So, I googled it, and figured out what I'd been missing.




:strong:`Skip the Math` 




The Google page on characteristic functions is heavy going.  The issue here is to characterize the frequency distribution of some more-or-less random variable.  This is a real close fit with the formal definition of a characteristic function.




When should we apply the characteristic function?  Load time or query time?  The comment showed it at query time.  However, we could also do it at load time.




Here's the genius part.




If we define it as a separate function, we can defer this decision based on which implementation meets our performance guidelines.




We have this situation.




..  code:

::

    def c1( value ):
        a,b = divmod( int(value*100), 10 )
        if b == 0:
            return "== 0.%d" % ( a, )
        else:
            return "0.%d - 0.%d" % ( a, a+1 )





We can then use this during load or we can use it in a fetch loop.  Quite cool.  Very elegantly separated from other parts of the processing.







