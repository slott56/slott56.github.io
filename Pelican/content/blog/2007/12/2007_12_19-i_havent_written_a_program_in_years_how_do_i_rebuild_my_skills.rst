I haven't written a program in years.  How do I rebuild my skills?
==================================================================

:date: 2007-12-19 13:42
:tags: books,building skills,#python
:slug: 2007_12_19-i_havent_written_a_program_in_years_how_do_i_rebuild_my_skills
:category: Books
:status: published







Here's part of a recent email, subject "Antique Programmer in search of face lift and/or brain transplant as appropriate...".  It was from a VP/Director kind of person who'd been away from hands-on technology for a few years.



"I’ve got a new Vista PC with dual drives so I’m going to add Linux to it. If I wanted to “freshen” my skills a bit what stack should I be looking at?"



Then, I had a conversation similar to the following:



Jim: "I've got to do some data cleansing.  I haven't written a program in decades.  I think I can do this with Excel and Access."



Me: "I think I've got something simpler than loading a spreadsheet and looking at each row.  Look at Python."



Jim: "Maybe.  I was a pretty good Fortran programmer, many years ago."



Me: "This won't be so brain-crampingly hard.  I'll post some stuff on the CSV package.  You'll like it."



And, I got the following question from a reader in Belgium "I'm a beginner, but I like python. I heard about it from the people that develop Gramps, a genealogy program. So maybe I should choose your python book? However, your 'programming' book is much more recent. Is it better?".



Getting Started with Python
----------------------------



First, do a little bit of self-reflection.



How are your computer skills?  Have you programmed before?  If so, look at `Building Skills in Python <http://www.itmaybeahack.com/homepage/books/python.html>`_ .  This book assumes you know how to do some programming.   If you have no background in programming at all, you'll need to look at `Building Skills in Programming <http://www.itmaybeahack.com/homepage/books/nonprogrammer.html>`_  -- it's for the non-programmer; the n00b, as they are affectionately known.



How is your bias?  Are you looking for the perfect language?  The one that is so far superior to others that it is the final word in programming?  If so, stop now.  There is no such thing.  If you are going to do side-by-side comparison between Python and {your language here}, you'll find enough gaps, overlaps, and differences that you can easily label Python as incomplete, fat with features or more of the same.  



What is your environment?  In a corporate, for-profit, "who-do-we-sue?" world, you'll find that Python has the taint of open source.  Sure, you use Apache and Java, but they are different.  I don't see how, but your CIO approves of those open source packages, but won't approve of Python.  Use Java.  It is free from taint.



What is your tool preference?  I've had people explain that the Visual Studio environment is so productive that it makes up for the problems in Visual Basic.  Since the actual code is what endures (not the tool used to produce the code), I'm confused by using Visual Studio as the justification for VB.  Some people claim that all that "text" in a conventional programming language is confusing and unsuitable for human beings -- glyphs and icons are better.  I've had people lecture me on the evils of using whitespace to properly format a program.  



Some First Steps
----------------



Here's the short version of `chapter 2 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/ch02.html>`_ :



1.  Download a Python installer from `Python.org <http://www.python.org>`_ .

#.  You may want a good editor.  Currently, I'm a fan of `Komodo Edit <http://www.activestate.com/Products/komodo_edit/>`_ .  Download and install it, too.  (This isn't in the book -- yet.)  It requires some configuring to locate your Python installation and run Python programs neatly; we'll get to that in a moment.



You're pretty much ready to roll at this point.



Your First Program
------------------



Here's your hello world program.

::

    #!/usr/bin/env python
    """ My First Program """
    import sys
    print(sys.version)
    print("Hello, World!")






To make this run neatly and cleanly, there's some Komodo setup you should do.




1.  Create a Project.




2.  Create a new file in that project; use the basic Python template.




3.  Create a new Command in that project.  The command text can be "%(python) %f".  The "Start In" should be  "%D".  Give it a clever name like "Python".




Now you can simply double-click the Komodo command to run your program.  You can also map this to a key, like F5, by opening the command and looking at the Key Binding tab.




Here's what I got as output.




::

    2.5.1 (r251:54863, Oct  5 2007, 21:08:09)
    [GCC 4.0.1 (Apple Inc. build 5465)]
    Hello, World!





While the book is 2.4.1, I'm getting ready for the next round of revisions to get to 2.5.  After that will be a major rewrite for 3.0.



A CSV Read/Process Example
--------------------------



Here's the skeleton of Jim's program to work with some spreadsheets of raw data.

::

    #!/usr/bin/env python
    import csv
    
    srcFile = open("some.csv", "r")
    srcCSV = csv.reader(srcFile)
    for row in srcCSV:
        if row[0] == "Col A Title":
            # A Title row
            pass
        elif row[1] == "Col B Footer":
            # A Footer
            pass
        else:
            # All the other rows
            pass # do some validation, some calculation, whatever...
        print(row)
    srcFile.close()





This illustrates a few key Pythonic concepts.



1.  Everything interesting is in the library, not the language.  The Python book only has `part 1 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/pt01.html>`_  focused on the language.  `Part 2 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/pt02.html>`_ , `part 3 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/pt03.html>`_  and `part 4 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/pt04.html>`_  are on data structures, objects and the library.

#.  File processing is easy.  It's all the related stuff that's hard.  `Chapter 18 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/ch18.html>`_  is basic files.

#.  CSV parsing is layered onto basic file processing as simply as possible.  `Chapter 19 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/ch19.html>`_  is a bunch of file-handling modules, including details on CSV.    `Chapter 31 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/ch31.html>`_  is other file formats.

#.  The ``for``  statement processes anything "iterable".  This includes files.  Cleverly, the CSV reader is also iterable.  There's no bookkeeping, overhead, logic testing, or anything else required for basic sequential processing of most kinds of data.  While the basic syntax is a `Chapter 7 <http://www.itmaybeahack.com/homepage/books/python/htmlchunks/ch07.html>`_  item, the profound nature of "iterable" has to be revisited throughout part 2.

#.  The if/elif/else construct can have as many (or as few) conditions as you need.  Why add a "switch" or "case" statement and clutter up the syntax?  Chapter 7 covers this, too, because it's so elegantly simple.




I can't say enough about the value of having a language that makes simple things so easy to accomplish.  I almost feel guilty writing things in Python -- to get them to work -- and then rewriting them into Java because customers prefer Java.  




That's why I recommend Python to anyone retooling their skills.  It's productive and usable right out of the box.  It's a toy that comes with batteries included.













