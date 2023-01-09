Some "Duck Typing Can't Scale" crap-ola
=======================================

:date: 2008-05-24 11:05
:tags: architecture,design,complexity
:slug: 2008_05_24-some_duck_typing_cant_scale_crap_ola
:category: Architecture & Design
:status: published







This put me over the edge.   Go deh! has a deep analysis of in "`Duck Typing Done Right is Wrong <http://paddy3118.blogspot.com/2008/05/duck-typing-done-right-is-wrong.html>`_ ".  It took a minute to parse, but the article is excellent.   (A less obscure title would quote the original posting properly: '"Duck Typing Done Right" is Wrong', but that's less catchy).  The original "`Duck Typing Done Right <http://blogs.sun.com/bblfish/entry/duck_typing_done_right>`_ " plays the paranoia card: you can't trust "them" to understand your semantics without resorting to some kind of "context-free" reference, implicitly backed with a complete ontology.



It's a great new variation on the "defensive programming" position:  you can't trust anyone to follow your API.



This -- it turns out -- has nothing to do with API's, duck typing or dynamic languages.  This is a much, much simpler problem.



:strong:`Defensive Programming`



A few years back, I was trying to read some Java code that included two things that are generally a waste of time and money.  First was endless declarations of things that were private.  Second was batches of if-statements that effectively confirmed that internally referenced methods passed the right arguments back and forth.  



I don't have much use for Java private in in-house IT projects.  If you're not selling the .class files, private isn't helping.  I asked what it was about; who are we keeping it private from?  The programmer told me, with a straight face, that he was worried about "someone" using the classes improperly -- calling the methods wrong, bypassing the public interfaces, etc.



"Who?" I asked.



"You know", he replied, "another programmer who didn't really 'get' the class API's."



:strong:`Who, Specifically?`



I was alarmed at this weird paranoia.  First, it's in-house IT -- if you can't trust the folks in the next rack of cubes, who can you trust?  Second, it's a one-person project -- no one else was going to see the code in the foreseeable future.  Indeed, most in-house IT is maintained by the author and when the author leaves the code is replaced.



I had to sit through the author's long story about an interface (written in PL/SQL, not Java) where an incoming file had the wrong format.  What?  What does that have to do with anything?



To the programmer in question, it proved that "defensive programming" was essential to success.  To make this point, however, the programmer had to conflate "bad interface implementation" with "I can't trust myself to remember my own API".  Which sounds schizophrenic to me; private wasn't likely to help.



I asked, "Who Specifically?"; "Who, specifically, will abuse the API?"  The answer was the vague, hand-wringing "other programmers".



Similarly, in `Duck Typing done right <http://blogs.sun.com/bblfish/entry/duck_typing_done_right>`_ , there's the paranoid expression "Extend the context somewhat ".  As if someone, somewhere can't be trusted.  Who specifically, can't be trusted?



:strong:`Asking for Names`



I ask for names in these cases.  If we can find the programmer who's likely to subvert the API, or mis-implement the interface, we can ask them to do quality assurance on the API or interface specification.  It isn't hard to get them to buy in on the design.  And if they don't buy in, it's easy to get specific objections.



To subvert my approach toward clarity, people will raise up the "What about 'future' programmers?" question.  I'm baffled.  I ask, "Who, the ones who haven't been hired yet?"  What about the post-apocalyptic half-mutant flesh-eating apes?  Are they included in the 'future' programmers?



The point is this: I can't see the value in hand-wring about "others" or some "extended context".  I think it's essential identify these "others" or this "foreign code" which will break our design.



If we don't have a specific list of "others" or specific "foreign code", then... uh... we don't actually have a problem.  We have a potential problem.  A potential problem with a microscopic risk of occurring.



:strong:`Real Problems`



While real problems can arise from programming changes, we have better techniques than an external ontology or lots of bogus defensive programming parameter-checking.  We have ordinary API documentation and ordinary unittest cases.  This is simple quality assurance.



As "`Duck Typing Done Right is Wrong! <http://paddy3118.blogspot.com/2008/05/duck-typing-done-right-is-wrong.html>`_ " states, the ontology doesn't help.  A context-free name isn't understanding, it's just a name.  If you don't understand the meaning or intent behind a class structure,  names aren't really the root cause of the confusion; usually there are three root causes.



1.  :strong:`Shoddy API documentation`.  My policy is this: try to explain it to a manager, or Quentin the rabbit who lives in the back yard.  (They have the same attention span.)  If you can't get a pithy, tidy, no-diagrams explanation, you've got work to do.  Refactor and rewrite the doco until you can explain it without pictures.



2.  :strong:`An unwillingness to understand what's really going on in the API`.   Some programmers don't read well, and start off assuming things about the API; their reading reduces to looking for confirmation of their assumptions.  When they don't find the hoped-for confirmation they may proceed anyway (with lots of EPIC FAIL) -- often deadline-obsessed managers will force this situation.  Other times programmers will replace an effort at understanding with a superficial but scholarly-looking analysis of the documentation.  



When programmers are unwilling to learn, this often surfaces at complaints about "inconsistencies" in the documents.  Sometimes these are simply shoddy documentation.  More often, however, the inconsistency is a conflict between the programmer's assumption and what the documentation actually says.



3.  :strong:`No independent confirmation`.  No unit test, no audit, nothing.  I can have an ontology that makes claims about my classes.  By without evidence (i.e., unit test cases) that context-free name is just as much a lie as my context-dependent name.



:strong:`Where Duck Typing Could Fail`



Here's the quote "The main criticism of Duck Typing has been that what is gained in flexibility is lost in precision: it may be good for small projects, but it does not scale".  Here, the code-word scale stands for "apply well when we introduce 'others'".  Why doesn't it apply when we introduce "others"?  Because, the "others" don't get the context:  "The context in which the duck typing works is a hidden assumption".



Generally, the context for duck typing is not hidden.  I suppose it could be, but you'd have to produce malicious documentation that concealed the purpose of a class with the intent to confuse programmers who want to reuse it.  In the presence of this level of shoddiness, who's going to make an effort to reuse the class in the first place?



Or, there'd have to be no documentation at all.  Which, I find, is standard practice for in-house IT projects.



Oh wait, that's why interfaces break, too.  That's why the paranoid schizophrenics feel the need to write useless code to test all inputs of all methods.  There's no documentation; no explicit, written agreement on formats; no unit tests to confirm compliance with the agreement.



So here are the ingredients for the situation in which duck typing doesn't work.



1.  No documentation of the interface.  Or bad (incorrect, incomplete, misleading) documentation.



2.  No unit test to define conformance with the documentation.



3.  No effort to understand the interface.



Wait.  This has nothing whatsoever to do with duck typing.  This is all just ordinary software quality assurance.   These are the ingredients for failure in every kind of software development technique.  



The rules are simple.  Document (an ontology may help, but it doesn't solve the problem); provide proof with unittests (merely compiling means nothing); seek to understand, not confirm (your assumptions are always wrong).




