Technology and Compromise
=========================

:date: 2008-07-18 10:10
:tags: architecture,design,complexity
:slug: 2008_07_18-technology_and_compromise
:category: Architecture & Design
:status: published







Two recent conversations with the Non-Compromisers.



NC:  "I can't use Yahoo! mail"



Me:  "What?"



NC: "Yahoo! mail has a "Home" tab which isn't the inbox.  It always lands there."



Me:  "Yep.  That's a javascript thing.  The tab isn't bookmarkable."



NC:  "The fact that I can't land directly on the "Inbox" tab makes Yahoo! mail unacceptable."



--Omitted:  a long "can you explain why" digression that's frankly a strange thing.--



Me:  "Well, use Google Mail then."



NC:  "Can't do that either -- I've used the Yahoo! mail for so long that I can't change.  My only choice is to configure the POP reader in Yahoo!, but that's the Yahoo! plus and I don't want to pay for mail service."



Okay.  So no technology is acceptable here.  I'm stumped as to what to do.  Can't use Yahoo!  Must use Yahoo!.  This is going nowhere.



Here's another.



NC:  "I want to consolidate my iTunes libraries.  I opened the iTunes library folder on my office computer, dragged all the files into a CD and then dragged them into the iTunes library folder on my home computer, but now my library is all screwed up."



Me:  "Here's a hint: don't do that.  Use the iTunes import function."



NC:  "That's too slow."



Me:  "Dragging didn't work, so slow is your only choice."



NC:  "There has to be another way.  This is really popular software, there has to be something 'out there' that manages the iTunes library for you."



Me:  "There is."



NC:  "Really?  What?"



Me:  "iTunes.  Just use it like it's supposed to be used.  Don't work around it."



NC:  "I can't.  It's too slow."



Me:  "Then use something else.  By a Zune and use whatever Microsoft offers."



NC:  "I already have an iPod, so I have to use iTunes."



So, you must use iTunes and you can't use iTunes.  Okay.  This is going nowhere.



:strong:`The Prototype` 



Recently, I fielded some calls on building a prototype of an application.  But nothing was acceptable.



I find that prototypes are fun, I do a lot of them.  I use Django.  Why?  I can piece together a quick data model and just slap together page after page of views that actually work.  In many cases, the "update" use cases are so poorly defined that the default admin pages are fine.  The rest of the user experience is easy to build.  



Also, Django encourages learning.  Evolve the data model, rebuild the test cases and views, and you're up and running right away.  Sometimes with the customer sitting there.



In this case, however, the application was much, much more complex.  It had a stand-alone desktop component that used mostly web service requests.  It had a central web site, but that had  a small user interface.  The desktop applications had to work stand-alone with intermittent synchronization back to the central database.  Remote mobile computing.



Every prototype proposal was unacceptable.  But we still had to create a prototype.



:strong:`Who and Why?` 



They wanted a free prototype.  We can't really do that, since this isn't a "product line" that we're offering.  It's custom software.   



They weren't happy buying a prototype, so they threw out the following option: "A Scalable Prototype".  This made very little sense to anyone.



First -- and foremost -- I asked "Who's the decision-maker" and "How does a prototype help them make a decision?  What will they see in a prototype?"  The answer was uselessly vague -- the decision-maker is the funding organization (duh! that's more-or-less a matter of definition).  The decision is "they want to see a prototype, it will help secure funding."  That's not a very clear answer to "what do you need to know."  That's just a recapitulation of the situation.



Okay, they don't know what decision is being made.  They won't tell us who is making it.  But they have directed us to write a proposal for a "Scalable Prototype".



:strong:`Scalable in What Dimension?` 



They said the word "scalable".  It's an application with a desktop component and a server component.  What's scalable?  The volume of data on the desktop?  The volume of data required to synchronize desktop and server?  The number of clients the server can handle?  The total number of users?  What are we trying to scale?



None of those



"Scalable" doesn't mean scalable.  It means "extensible" or "evolvable".  They want us to do `Evolutionary Prototyping <http://en.wikipedia.org/wiki/Software_prototyping#Evolutionary_prototyping>`_ .  Okay, I think I get it.



They want a prototype that's free; something we don't do.



With limited input from them, we're supposed to build "something" which will evolve into a complete product.  We don't have any use cases or other analysis material.  That's part of a future contract that we'll win by doing a prototype.



So we're have a Non-Compromise conversation.



NC:  "It can't be a throwaway prototype"



Me:  "Fine.  What does it need to show?"



NC:  "Something to demonstrate the concepts so we can get funding."



Me:  "There are many concepts.  Do they want to see the database synchronization?"



NC:  "No.  Too technical."



Me:  "Do they want to see the server side in any way."



NC:  "No."



Me:  "Do they want to see the desktop application -- the thing we don't have specified."



NC:  "Not really.  Just the concept.  But in a form we can build on."



Me:  "You mean the desktop application framework.  That's what we build on."



NC:  "No, not the framework, the concept."



Me:  "So, screen shots of the desktop?"



NC:  "Screen :emphasis:`concepts` ."



Me:  "Sketches?  Wireframes?  The actual application?  Remember, we don't have any use cases, so actual is a little crazy."



NC:  "Not sketches.  Not real screens."



Me:  "Do you mean mockups.  In Visio."



NC:  "Not mockups."



So, it's not sketches, not mockups and not real screens.  I can't find any gaps along this spectrum to figure out what they're asking for.  It isn't a non-technical sketch; it isn't a semi-technical mock-up; it isn't a fully-realized SWING Frame.  What is it?



Whatever they want, it's none of the things I've mentioned.  And compromise is right out of the picture.  It's either the thing they want or the project -- prototype and all -- is cancelled.





