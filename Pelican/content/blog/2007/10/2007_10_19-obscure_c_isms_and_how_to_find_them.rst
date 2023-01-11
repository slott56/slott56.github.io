Obscure C-isms and How To Find Them
===================================

:date: 2007-10-19 14:05
:tags: architecture,design,unit testing,tdre
:slug: 2007_10_19-obscure_c_isms_and_how_to_find_them
:category: Architecture & Design
:status: published







This is not a Python to the rescue story.  This is a true, deeply horrible situation.  I was rescued by a reframing technique I'll call **Extraction**.



First, the function had nested if's without enough else's -- the kind of thing that handles two of the four possible conditions.





::

    if( a ) {
        if( b ) {
            do something
        }
    } else if( c ) {
        if( d ) {
           do something
        }
    }





What about the other two conditions, (*a*  &amp;&amp; !*b*) as well as (*c*  &amp;&amp; !*d*)?



Second, the function had double negatives.  It had the famous if(a == FALSE) kind thing.



Unit Test Hell
---------------



Once I thought I had it, I wrote out the unit tests.  There are, with some analysis, 36 combinations of inputs.  The variable names, the context, the overall problem domain gave numerous hints as to what should happen.



But it just didn't.  I couldn't get more than a few of the 36 cases to pass.  



So now I've got two problems:



1.  I can't reason out what the program does.

#.  I'm not sure I even have the unit tests correct.



Reframing Techniques
--------------------



When my head starts getting a flat spot from beating it on the wall, there are a number of techniques I use for reframing the problem.  My favorite is **Predicate Calculus**.  In this case, however, the conditions got complex and drifted too far from the essential semantics of the function.  It became a kind of algebra exercise, not giving me any insight.



**English Specification**  isn't a bad way to reframe things.  However, in this case, the English didn't make any sense either.  The C was just too obscure.



**Python**, however, looked promising.  In a few minutes I had transliterated the C to Python, and had something that looked like it was producing meaningful results.  I revised the Python to write both a tidy .CSV summary as well as Java test case methods.  The CSV was a functional summary, the test case methods were cut and pasted into the Java TestCase.



This is not a Python to the rescue story.  The Python unit test cases didn't look really right.



Reframing Through Extraction
-----------------------------



Once the user test cases arrived, it became painfully clear that my reverse engineering was not even close.  My glib and easy reframing techniques hadn't worked.



With my back up against the wall, I pulled out the big gun in reverse engineering -- **Extraction**.  I extracted this function and began to put together enough stuff to get it to compile and run in isolation.  This is time consuming and doesn't readily resolve semantic problems.  Once you have something running, you are rarely any closer to knowing what it meant.



Isolation, BTW, means complete isolation.  All dependencies (except for stdio.h) have to be resolved and the example has to fit in a single file.  There's nothing quite as clarifying as a one-file program.



The process of doing **Extraction**  is insight-producing.  The trick is to trust nothing.  First you pull out the function from the source file.  Then, when it won't compile, you start pulling things out of the various .h files and pasting them into the extraction.  After 20 minutes of cut and paste, I finally found the following nugget of pure evil.

::

    #define TRUE 0
    #define FALSE -1





Are You Kidding?
-----------------



No, apparently they were not kidding.  This clarified many things.  It made the if(a == FALSE) more clear.  It also pointed out many places where TRUE and 0 were used interchangably.  Inconsistency helped make it more obscure than it already was.



Making this substitution into the Python gave me test cases that made some sense.  This allowed me to rewrite the Java to at least work.  The resulting class includes a few "XXX - Refactor" comments.



When I told the client what I'd learned, one of their programmers sent me the following link:  `How to Write Unmaintainable Code <http://www.web-hits.org/txt/codingunmaintainable.html>`_ .  Now that I'm past the most horrible part of the program, this is funny.  Down in the section titled "Miscellaneous Techniques", item 11 is this exact technique.



What's funnier (or scarier) is anyone allowing this through their QA procedures, putting it into production and using it for years.  Clearly, code inspections are not on anyone's to-do list.




