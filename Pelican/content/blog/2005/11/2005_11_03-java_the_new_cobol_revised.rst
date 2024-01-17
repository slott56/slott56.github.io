Java - the new COBOL (Revised)
==============================

:date: 2005-11-03 14:55
:tags: management
:slug: 2005_11_03-java_the_new_cobol_revised
:category: Management
:status: published





Kontrawize says http://kontrawize.blogs.com/kontrawize/2005/11/java_is_the_new.html that Java is the new assembler.




/dev/null http://www.haloscan.com/comments/slott/E20051101105604/#27166 says "While we are willing to expose and
discuss the problems in Java, we do it because we want to improve it, not
because we need to cut & run".  Taken out of context, I could twist this to
mean that Java is no longer looked at merely technology to build a solution, but
has developed an independent existence and a rabidly patriotic following. 




I think /dev/null is being a Java
realist ("it has problems, but it solves some problems well").  I think
Kontrawize's point isn't quite right; really the point is that Java is sometimes
applied to the wrong problems.



While
Java is the next big legacy, some of Kontrawize reasons are wrong.  Comparing
Java to Assembler as low-productivity toolsets, misses the mark.  Assembler is
only low-productivity if you're using it for the wrong thing.  If you're writing
I/O drivers, assembler rules.  If you're writing a multi-media presentation,
assembler is the pits.  It's the "mismatch between levels of abstraction"
problem.



In the IT shops I've been in
over the last few decades, assembler is a legacy that leads to absolute
deer-in-the-headlights paralysis.  The few shops that still had some assembler
had to treat it as a black box.  The software had to be documented without
reference to internal structure, and the replacement had to involve the
potential for business change, since the nuances of the assembler were already
lost forever.



COBOL, on the other hand,
is more like Java.  IT shops have lots of legacy COBOL folks, and when you try
to introduce something new (like Java or Python) to them, they fight back every
step of the way.  They often cling to old work processes, unwilling to consider
that the brave new world is upon
them.



One example:  We build the entire
Java application system and turn over four JAR files that are put into
production.  The COBOL folks ask questions like:

-   Why turn over everything?  Why not just
    turn over the "program" which changed?

-   Why recompile everything?  Wouldn't be
    "simpler" ("more efficient" was also used) to recompile only the "program" that
    changed?

-   Why don't you have proper application
    main programs?  Why do you have these reusable packages that are recombined
    every which way?  Wouldn't it be "simpler" to use "copy books" (a/k/a/ include
    files) so you could more easily track the dependencies among your programs and
    the reusable bits?

-   What's wrong with shell scripts?  They're
    just like JCL and we use JCL all the
    time.



I think the idea that Java will
become the next COBOL is very important.  One consequence will be the
"Technology Freeze Play": we're an All-Singing-All-Dancing-All-Java shop and you
can take your silly Python (or Open Source components) and just stick it in your
ear.  We measure effectiveness by our entrenched skill set, not cost to solve a
business problem and value of the business problem being
solved.



When I taught C programming, I
remember one conversation about upgrading the skills of some of the COBOL people
in addition to bringing in new C programmers.  "We don't really plan on
upgrading our COBOL programmer's skills", I was told.  My response: "Why not? 
Were they born
stupid?"



Addendum.



Is
it arrogant to suggest that COBOL programmers can or perhaps
*should* 
learn C?



Or, is it arrogant to suggest
that COBOL programmer should not be
pigeon-holed?



Or, is it arrogant to
suggest that pigeon-holing COBOL programers is the same as labeling them "born
stupid" and, therefore, untrainable?



It
is probably arrogant to suggest that COBOL programmers are being
*maliciously* 
held back from learning new technology.  Sometimes, they aren't offered the
training because of the huge legacy maintenance burden that they have to support
while new technology is being introduced
elsewhere.



This, I think, is why Java
will become like COBOL -- a legacy which we hate but must support.  The people
supporting Java will be pigeon-holed.  New technology efforts will be focused
elsewhere, leaving these people behind.  Not because they're literally born
stupid, but because they've had the bad luck to be supporting the technology
that became the reviled legacy.












