More Programming for n00bz
==========================

:date: 2008-02-23 20:18
:tags: books,building skills,#python
:slug: 2008_02_23-more_programming_for_n00bz
:category: Books
:status: published







Back in December, I posted "`I haven't written a program in years <{filename}/blog/2007/12/2007_12_19-i_havent_written_a_program_in_years_how_do_i_rebuild_my_skills.rst>`_ ..." with a tidy little example, suitable for someone who used to program.  The intent was to help them get a quick program written, leveraging their legacy skills using new tools.



And (bonus to me) it helps me to update `Chapter 39 <http://www.itmaybeahack.com/homepage/books/nonprog/htmlchunks/ch39.html>`_  of `Programming for Non-Programmers <http://www.itmaybeahack.com/homepage/books/nonprogrammer.html>`_  with a real-world example.  Also, it validates the examples in `Building Skills in Python <http://www.itmaybeahack.com/homepage/books/python.html>`_ , `chapter 34 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/ch34s02.html>`_ .



Recently, I was heard of a cool programming exercise from a composer, `Xander Lott <http://www.myspace.com/xanderlott>`_  (disclosure: my son; full disclosure: alcohol was involved).  He had a concept for a piece that involved selection of random elements from a small palette of alternatives.  Being a musician, not a programmer, he was using a deck of cards for the random element selection.



He was talking about a program that looked something like the following.

..  code:

::

    import random
    
    noteSetChoices= ["C-E-G", "C-F-A", "C-E-A",
        "D-F-A", "D-F-B", "D-G-B", "E-G-B", "F-A-C"]
    beatChoices= ["1 - - -", "- 2 - -", "- - - 4"]
    octaveChoices= [1, 2, 3]
    techniqueChoices= ['Fingered', 'Harmonic']
    
    for n in range(48):
        note= random.choice(noteSetChoices)
        beat= random.choice(beatChoices)
        octave= random.choice(octaveChoices)
        technique= random.choice(techniqueChoices)
        print octave, note, technique, beat






For performance modeling, I wind up writing data generators like the above program.  Here, four specific dimensions are identified, and a sequence of random points are generated in this space.  Xander says that a number of details are unspecified -- the details the composer fills in to transform this from noise to something that has a musical texture even though parts of the musical structure are random.




:strong:`Fit with cSounds` 




I think that there may be a fit with the Python interface of `cSounds <http://www.csounds.com/>`_ .  I haven't explored this -- it would be too much of the wrong kind of fun.  But I expect that he may be able to define the cSounds instruments and use this kind of rule-based generator to create the "score".




The issue is that real music involves a fairly large number of rather complex rules.  Perhaps more complex rules than a newbie can encode in simple Python programs -- some rules are tough to articulate and amount to vague things like "it sounds better" or "I needed the piece to have some direction".  Xander was using the random generation for certain elements, but he planned to fold in other elements based on his own artistic tastes.




But for an n00b example that is (a) real world and (b) can be used to build skills in programming, it has a lot of appeal.  Thanks, Xander.








