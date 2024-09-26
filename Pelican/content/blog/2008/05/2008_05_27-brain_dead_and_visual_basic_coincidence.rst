Brain Dead and Visual Basic: Coincidence?
=========================================

:date: 2008-05-27 23:04
:tags: building skills,#python,visual basic
:slug: 2008_05_27-brain_dead_and_visual_basic_coincidence
:category: Books
:status: published







Don't ask why.  I can't explain it without violating a Non-Disclosure Agreement.



However, check this out.  Search for NMEA Checksum VB.



-   `http://www.experts-exchange.com/Databases/GIS_GPS/Q_21413235.html <http://www.experts-exchange.com/Databases/GIS_GPS/Q_21413235.html>`_

-   `http://www.codepedia.com/1/Calculating+and+Validating+NMEA+Checksums <http://www.codepedia.com/1/Calculating+and+Validating+NMEA+Checksums>`_

-   `http://www.codepedia.com/1/Taking+Out+the+Garbage:+NMEA+Checksums <http://www.codepedia.com/1/Taking+Out+the+Garbage:+NMEA+Checksums>`_

-   `http://www.xtremevbtalk.com/showthread.php?t=145902 <http://www.xtremevbtalk.com/showthread.php?t=145902>`_

-   `http://www.bluetoque.ca/articles/nmea-checksum-in-csharp.html?Itemid=9 <http://www.bluetoque.ca/articles/nmea-checksum-in-csharp.html?Itemid=9>`_



Almost everyone is copying off everyone else's paper, and propagating the same lame mistake.



There's no earthly reason for programs of the form:

::

    cs = some initial value
    for ....:
        if cs == some initial value:
            do the initialization
        else:
            do everything else






This structure is one of those "you're kidding, right?" kind of structures.




NMEA sentences have a relatively simple structure.  They're all on one line.  They start with a "$" or "!".  The may end with "*" and some hex digits for a checksum.  The characters in the middle are used to compute the checksum; they are a sequence of comma-separated values.  




It doesn't seem that complex.  Yet, the VB examples make it look scary.




My Reference Implementation
----------------------------




In Python, we have something simple like the following.  Encapsulated messages (like !AIVDM and !AIVDO) are a bit more complex because they have their own unique Base64 algorithm in addition to their unique NMEA checksum.



::

    def validate(aLine):
        sentence, star, checksum = aLine.rpartition('*')
        assert sentence[0] in ( '$', '!' )
        if star == '*':
            cs = 0
            for c in sentence[1:]:
               cs ^= ord(c)
            assert int(checksum,16) == cs
        return sentence[1:].split(',')






The points are the following:




1.  There are usually string functions for finding the right-most "*".  They're always more efficient than your explicit loops.  Use the string library.  In my case, the rpartition method was not easy to find in the library reference manual.  It is, however, *precisely*  what is called for.




2.  Initialization is something you have to do in front of the loop, not buried in an if-statement inside the body of the loop.  Period.  There's a bigger principle here.  The initial value has to be the value you'd compute if the loop was executed zero times.  The initial value isn't some goofy proxy that's a value you use until the real initial value can be computed.




3.  Skipping the first character of the sentence (the "$" or "!") isn't an extra if-statement inside the loop; it's part of the range of values for the loop structure itself.




There's an even shorter formulation in Python.  See /dev/random: `NMEA checksum in Python <http://blog.lucanatali.it/2006/12/nmea-checksum-in-python.html>`_  for a very short version.  This version, however, doesn't help clarify the perfectly awful VB programs.




Root Causes
-----------




Why are the VB examples so wrong?  And why are the wrong examples the first things coughed up by Google?




Are these examples widely referenced?  Do they have some authority?  




It can't be that VB programmers -- themselves -- are brain dead.  I've met smart people who know and use VB.  For some reason, they're on sites that have some weight with Google, even though these specific snippets of code are not very good.




What's left is that these examples are all unthinking reimplementations of some initially flawed algorithm.  




Which tells me that VB programmers are habituated to copy-and-paste reuse.  Rather than define, share and reference a library, they copy and paste code freely.  I've seen many other examples of copy-and-paste programming in VB.








