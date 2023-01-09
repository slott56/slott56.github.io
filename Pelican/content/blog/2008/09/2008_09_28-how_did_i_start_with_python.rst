How did I start with Python?
============================

:date: 2008-09-28 02:00
:tags: books,building skills,#python
:slug: 2008_09_28-how_did_i_start_with_python
:category: Books
:status: published







I can't find the exact question -- it was something along the lines of "Why did you start with Python?" or "How did you choose Python?"   It was probably one tagged with `programming-languages <http://stackoverflow.com/questions/tagged/programming-languages>`_ .



For several days, I couldn't recall why or how I started looking at Python.



At first, all I could recall was this.  When I first heard about Java, I collected a list of OO languages (C++, Java, Python, Smalltalk) and made an effort to get a grip on a few of them.  I knew C++.  I learned a little Smalltalk; this was a hard thing to do in the late 80's with just a clunky old Mac Plus at home.



:strong:`The Script-Based Challenge` 



I think that sometime in the '99 to '01 neighborhood I looked at a piece of software I'd written back in '92.  It was an application server that ran 24x7, and was written entirely as a massive shell script.  Really.  Several thousand lines of shell script to service requests.  The queue was a database table with inbound requests; the results were left in a directory to be downloaded.  It worked great, but was kind of slow.  



[I did have to make a Y2K change -- I had, foolishly, used last two years of the date as part of a file name, and the files would get out of order if I kept using that naming scheme.  My only Y2K design mistake.]



After 7 or more years of flawless, crash-free service [Bragging!], I recommended that they retire this and replace it with something a little smarter and smaller, written in C++. 



:strong:`C++, OS API's and Python` 



The legacy code -- being a shell script -- was packed full of the OS API calls that are made available to the shell through the various commands.  For a while, I waffled between recommending C++ and Java.  Java had lots of appeal.  C++, however, had ready access to the necessary API's.  



Priorities changed.  The project was tabled because of larger data warehouse implementation changes.



At some point, it began to dawn on me that what I wanted was 



- an object-oriented programming environment,



- garbage collection of Java,



- modern libraries of Java,



- OS API's of C (and C++).



That's when I started to look into Python.





