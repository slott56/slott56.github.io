One of Those Things
===================

:date: 2011-07-26 08:00
:tags: #python,template
:slug: 2011_07_26-one_of_those_things
:category: Technologies
:status: published

Check out this question on Stack Overflow: "`Python: replace a string by
a float in txt
file <http://stackoverflow.com/questions/6789230/python-replace-a-string-by-a-float-in-txt-file/6789735#6789735>`__".

The question is confusing, but it appears to be a longish and confused
description of simple formatting or template substitution.  It's hard to
be sure, but it sounds like one of Those Things™ (TT).

Most of Those Things (TT) are standard problems with standard solutions.

Until you've seen a lot TT's, it seems like your problem is unique and
special.  It's hard to see TT's for what they are.

In this case, the problem appears to be solved by Python's
`string.Template <http://docs.python.org/library/string.html#template-strings>`__
class with minor modifications.  The documentation for customizing
string.Template isn't clear, so here's an example.

::

    from string import Template
    class MyTemplate( Template ):
        delimiter= '@'
        pattern=
    r"@(?P<escaped>@)|@(?P<named>[_a-z][_a-z0-9]*)@|@(?P<braced>[_a-z][_a-z0-9]*)@|@(?P<invalid>)"

That appears to be the standard solution to the standard problem.

Define a new delimiter ('@') and some slightly different delimiter
parsing rules and away you go.

This can be used as follows to replace any '@x@' variables in any
template file.  What's important is that very little actual code is
needed, since it's one of Those Things that's already been solved.

::

    with open( 'a.txt', 'r' ) as source:
        t = MyTemplate(source.read())
        result= t.substitute( x=15 )
        print result



-----

I think this is a rather over-engineered solution....
-----------------------------------------------------

Paul<noreply@blogger.com>

2011-07-26 13:08:26.374000-04:00

I think this is a rather over-engineered solution. As the accepted
answer on the question shows, the replace method is vastly more obvious
and less verbose than that frightening regular expression.





