Consequences of Reverse Engineering
===================================

:date: 2008-03-13 23:43
:tags: architecture,software design,unit testing,test-driven reverse engineering
:slug: 2008_03_13-consequences_of_reverse_engineering
:category: Architecture & Design
:status: published







Here's one recent example of a significant bug.



The code said A is not NULL OrElse A != " ", which doesn't do anything useful.  If A has non-NULL data, this is true.  The second part of the clause (A != " ") is only evaluated if A is NULL.  If A is NULL, no other comparison makes sense.  That's what NULL means.



The usual form of this is  A is not NULL AndAlso A != " ".  The inverse is A is NULL OrElse A = " ".  Any other variation on these two is a common logic error.  



So, what test cases are we inserting to show we reverse engineered this correctly?



Craposity
----------



All I can do is gripe about the level of craposity that accretes around VB.  A colleague noted that the .NET environment doesn't do this, it's just shoddy craftsmanship.



I noted that it seems to be all I ever see -- really spankingly shoddy VB code. Indeed, I got a brain cramp of the first magnitude yesterday looking at the example shown above; code that -- merely by inspection -- could be shown to do nothing useful.  And, of course, most VB products as a whole was built with COPY-Relocate-and-PASTE (**CRAP**\ ™) reuse.



I have to agree that it probably isn't the toolset.  That leads me to deduce that either all VB programmers are idiots or my sample is biased.  It must be that I only look at code that's "too expensive to maintain in its current form".



But It Solves A Problem
------------------------



This means that any random idiot is capable of solving a business problem with a program that's an atrocity in .EXE format.



That leads me to conclude that business problems (generally) are so Huge and Obvious that it doesn't take any skill at all to find and solve them.  Which leads me to ask why we require armies of Business Analysts, Program Managers, Directors of Software Development and what-not.  All of that management oversight doesn't stop a class-A idiot from writing a deeply disturbing pile of code which becomes an organizational lynch-pin.



Or, is all that management oversight the cause of the idiocy, not a failure to stop the idiocy?



Magic Management
-----------------



JB noted that some programmers work through a process of voodoo and witchcraft, and don't really understand much of what they're doing.  Hence the prevalence of COPY-Relocate-and-PASTE reuse.  They can't refactor because they're not sure it's really appropriate.



Management, of course, forces this to happen by imposing nutball schedules and demanding that useful work stop because it's "gold plating".  While lack of skills is the cause, management's policy is to enable bad behavior.



I guess that improvements can only happen by magic.




