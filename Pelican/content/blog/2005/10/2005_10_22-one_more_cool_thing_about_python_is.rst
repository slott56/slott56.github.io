One More Cool Thing About Python Is...
======================================

:date: 2005-10-22 15:25
:tags: books,building skills,#python
:slug: 2005_10_22-one_more_cool_thing_about_python_is
:category: Books
:status: published





So, confronted with 1.4M records of questionable
data, what do we do?

1.  We'll need a production program that can run
    daily from now until the end of time to cleanse the data and reject the truly
    evil records.

2.  We don't have a good fix on what the data is.



We have some "specifications" but
they're little more than a wish list of cleansing
suggestions.



What to do? 




Well, step 1 is obviously analysis to
fully define the problem.  What data do we have?  What is the platonic ideal? 
What forms of badness are represented where data does not meet the
ideal?



So, how do we analyze?  We can't
throw it into Excel.  We can barely open the file in Textpad. 




**Python to the rescue.** 



While the final application
must be delivered in Java, Java's a terrible way to analyze unknown data.  We
would have a cycle of write, debug, build, test, run and scratch head over a
fairly complex piece of Java code just to do simple frequency
histograms.



The Python program we used
was something on the order of



..  code:

::

    fq= {}
    for line in file( 'sample.csv', 'r'):
        fields= line.split(',')
        aSuspect= fields[4].split()
        fq.setdefault( aSuspect[3], 0 )
        fq[ aSuspect[3] ] += 1
    print fq





Given this template we can move
around, analyzing fields individually or in groups, looking for the domain of
badness and formulating a cleansing
strategy.



Python reduces the
development cycle to type-run-think analysis cycle which goes very quickly.  And
we can easily produce things we don't mind throwing away.  We haven't invested
much, we don't have the Urge to
Preserve.



We can then dry-run our
cleansing approach in a type-run-think design cycle.  Again, the Urge to
Preserve is negligible when there's such a tiny
investment.



Compare the 8 lines of code
above with the equivalent in Java.  It would be, perhaps twice the size.  The
strong type checking slows development, and causes you to marry a class
hierarchy that isn't really correct because it's too expensive to
change.



And when we're done, we can
simply translate to Java.  I like this Python thing, it works.










