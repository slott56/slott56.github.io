My Bias is Showing
==================

:date: 2007-10-10 10:23
:tags: FOSS,open-source
:slug: 2007_10_10-my_bias_is_showing
:category: FOSS
:status: published







Why Python, indeed?



"It's clear that *you* find it easier and quicker to use Python, and that's fine. It's often quickest for people to use the tools that they know best."



As they say on Fark.com, "This".  



However, the Python advantage doesn't stem from knowing Python better than Java.  It's a wash, actually.  I know both quite well, and I'm paid to write Java.



What is the Python advantage?



Hacknot has a great analysis of the `Invasion of the Dynamic Language Weenies <http://www.hacknot.info/hacknot/action/showEntry?eid=93>`_ .  It's a bit over-the-top, but it's quite scathing in it's analysis of a few truly ridiculous claims.  The article totally rejects all value for dynamic languages, which flies in the face of experience.  But, it also deprecates all non-numeric, qualitative experience as "delusion", so it lacks some important perspective on what programming is.



Programming is knowledge capture.  "Productivity" -- lines of code per day -- is just a part of the value of a programming language.  The problem here is that programming is an inherently communicative activity, similar to writing Blog posts in English.  It isn't an exercise like sailing where velocity made good (VMG) is the key metric for success.



:strong:`Some Claims` 



The best part about the Hacknot article is a specific list of dynamic language claims.  The attempted refutations of those claims, in most cases, is incomplete or narrowly focuses on exactly one kind of evidence.  Additionally, not all of the argument is strictly linear.  One refutation conflates code volume and development speed together, another treats them separately.  We'll borrow the topics, since they're the most useful part of the posting.




-   Dynamic Typing Increases Development Speed

-   Interpretation Increases Development Speed

-   Reduced Code Volume Increases Development Speed

-   Support From Major Companies Legitimizes DLs

-   As The Problems Change, People Use New Languages

-   You Can Assess Productivity By Feel

-   Syntax Can Be Natural

-   A Strength Of My Language Is Its Community

-   No Harm, No Foul

-   






We'll look at each of these from a narrow Java vs. Python perspective.  I can't speak about Ruby; I don't like PERL or PHP, so I can't address DL's in general.   See `Python &amp; Java: Side by Side Comparison <http://www.ferg.org/projects/python_java_side-by-side.html>`_  for additional information.





:strong:`Dynamic Typing Increases Development Speed` 





This is manifestly true.  Claims are exaggerated (and the exaggeration should be refuted.)  Duck typing has some advantages over static typing.  Specifically, here's an example that bugs me in Java.






..  code:

::

    class Something { 
        class MyKey implements Comparable { 
            String aField; int anotherField; ... } 
        Map theRealPoint = new TreeMap(); 
        ... 
    }





In Python, this isn't interesting enough to justify all the static typing declarations.




..  code:

::

    class Something: 
        def __init__( self ): 
            self.theRealPoint= {}





A map's key can be a simple Python tuple; I don't need to create a unique class to simply collect a bunch of objects together to create a composite key.  Java forces a kind of overhead that doesn't clarify much to the reader.  The overhead just keeps the compiler happy.



:strong:`Interpretation Increases Development Speed` 



This, too, is manifestly true.  Also, claims are often exaggerated.  The issue isn't the time saved by skipping the compile (or compile and link) step(s).  The issue is direct interaction with data structures.  



In exploring a new part of the libraries in Java, I have to write test cases that are really technology spikes.  They simply demonstrate how the API works with an example that is focused on my problem.



In exploring a new part of the libraries in Python, I can just type stuff interactively into the interpreter and watch it work.  Similarly, I can debug more easily by evaluating expressions in the interpreter directly.  The whole single-step into a method kind of debugging tends to obscure the semantic link between language and meaning by introducing the grubby details of how the virtual machine works.



This is worth hours of development time.  New development :emphasis:`always`  means a technical unknown.  We don't write new software unless some part of the problem domain or technology chosen as the solution is a complete unknown.  Discovery is part of the knowledge capture process.  Interpreted languages facilitate exploration and discovery.



:strong:`Reduced Code Volume Increases Development Speed` 



Of course.  It also reduces the maintenance cost.  And it reduces the intellectual burden of coming to grips with what the software means.  The Python code volume is smaller than the Java code volume.  I could show one or two amazing results.  Instead, I'll say that Python is universally 10% to 20% smaller.



Common statements (expression and assignment) are generally the same size.  However, compound statements like :strong:`for`  and :strong:`if`  statements, function and class definitions are wordy in Java.  The :strong:`for`  statement, in particular, can be irritatingly wordy in Java.  Most Python collection classes have proper iterators that are usable by the :strong:`for`  statement; in Java I have to explicitly create and manage the Iterator.



:strong:`Support From Major Companies Legitimizes DL's` 



For me, this is irrelevant.  Few of my customers would ever consider Python; it has the taint of open source.  My customers align randomly with "major companies".  They'll claim they're all Microsoft, but most of their in-house programming is actually Oracle PL/SQL stored procedures.



This doesn't impact my productivity.  



:strong:`As The Problems Change, People Use New Languages` 



This is an interesting point, but not really part of the dynamic-static debate.  It's more about Domain Specific Languages (DSL) than it is about Dynamic Languages.  In the Java vs. Python conversation, it has no real purpose.  Both are general-purpose programming languages, neither is particularly well-suited or ill-suited to a given problem.



:strong:`You Can Assess Productivity By Feel` 



While completely true, it is an uncomfortable issue.  As pointed out to me, "It's often quickest for people to use the tools that they know best.".



The Hacknot post decries this as "delusion" and "emotion".  It's as if to say "programming is not knowledge capture; it is not communication among a community of developers, maintainers and users."  I have to reject this implicit premise.  Programming includes a "feel" factor.  If the representation of the knowledge is opaque, we didn't capture it very well.  If we capture knowledge quickly, and it passes all the unit tests, but we can't interpret the resulting code, we've failed.



We have to be careful what we mean by "productivity".  Lines of code per day isn't a terribly useful metric.  We have to fold in the various quality attributes like need satisfaction, maintainability, adaptability, resource use and overall cost of ownership.  Many of these are based on people's skills, preferences and experiences.  Eventually we might be able to measure all of this, but presently, that's too ambitious.



Lacking a theory of software development, and associated observations, we still have to make some progress.  Rather than refute "feel", we should work up a theory that includes feel and try and measure feel.  Until we have the theory, we have a starting point, and that's a narrative that puts feel into context of "got something done", "understood it", "optimized it", "adapted it", "corrected it" kinds of things.



:strong:`Syntax Can Be Natural` 



This is trivially true.  However, if English isn't your natural language, then Python's syntax won't appear natural.  There is no natural language that aligns with Java.



The natural syntax counter-example is to hold up Ruby examples to an English-reading audience.  Ruby wasn't created by someone with English as their first language.  Ruby looks odd to English-reading eyes.  



Python, however, was created by someone who said that Python should look like English, eschewing cryptic techno-babble.  The Python style guide specifically emphasizes the natural language look.



Java was created to be familiar to C programmers.  



:strong:`A Strength Of My Language Is Its Community` 



Language defines community; and conversely a community is often defined by a common language.  For artificial languages, like Python or Java, this is still true.  



However, the match between language and community is only of value in the context of  some specific, well-defined community.  Since most of my customers use Java, that's the community I'm aiming at.  Deliverable code must be in Java, because that's the community's common language.



I can do drafts, experiments, tools and utilities in Python.  I just can't easily deliver that.



:strong:`No Harm, No Foul` 



This is often a final milksop apology for hyperbole.  My preference for Python over Java has nothing to do with having another tool in the toolbox.  My claims are pretty specific:




-   Duck Typing makes my life easier;

-   An interpreter makes programming faster; 

-   Less code is better (no code is best); 

-   Feel and natural syntax help.





:strong:`Some Additional Resources` 





This is one of those topics that is a constant balancing act in the software development world.  People like to label it a "religious war" because they refuse to give up their position, and there isn't an easy metric that provides a properly scientific-looking answer.





See, for example, the `Bizarro Static Typing Debate <http://c2.com/cgi/wiki?BizarroStaticTypingDebate>`_ , `pl patterns: Static Vs. Dynamic Typing <http://plpatterns.blogspot.com/2007/08/static-vs-dynamic-typing.html>`_  for some additional commentary.





This debate isn't "technical" or even "scientific".  It is a consequence of being at the leading edge of human capabilities.  What is language?  What is knowledge?  How does language map to knowledge?  These are fundamental epistemological questions that don't have tidy answers.  We aren't measuring velocity made good.  We don't even have a context in which VMG kinds of metrics are central.  I'm not sure we can ever measure "comprehensibility", "actionability", "finite", "definite", or "effective".









