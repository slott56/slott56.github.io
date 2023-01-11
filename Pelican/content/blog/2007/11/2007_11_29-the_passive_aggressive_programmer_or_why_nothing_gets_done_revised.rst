The Passive-Aggressive Programmer or Why Nothing Gets Done (Revised)
====================================================================

:date: 2007-11-29 11:00
:tags: architecture,design
:slug: 2007_11_29-the_passive_aggressive_programmer_or_why_nothing_gets_done_revised
:category: Architecture & Design
:status: published







I see organizations stymied by a few individuals that seem to subvert initiatives and prevent progress.  Or they somehow evade being useful and spend all their time in hand-wringing and "yeah-but"-ing.  I'm not sure how to exploit what they can do, while getting past the stalls and evasions.



Here's a conversation that I'm labeling as "passive aggressive".  What I think I'm hearing is a developer with some kind of private agenda, coupled with an unwillingness to actually say anything.  Instead, we have this weird non-communication.



Me: "We'd like to do X to solve this set of problems."



PAP:  "I don't understand the problem."



Me: "I sent you the list of 38 things which are broken, all of which are different examples of a few specific architectural problems.  We're solving that set of problems.  Indeed, I see you brought the list to this meeting."



PAP:  "Fine.  What do you need from me?"



Me:  "Can you do X to solve those problems?  Or, more precisely, what would it cost to do X to solve those problems?"



PAP:  "I don't see how X solves these problems."



Me:  "Good point.  What solution do you have?"



PAP:  Shrugs.  Shakes head.  Rolls eyes.



Me:  "Do you have an alternative?  If so, we need to know what that is."



PAP:  "No, nothing."



Me:  "Okay, back to my question: can you do X to solve these problems?"



And that's as far as the conversation gets.  PA responses vary from "I don't understand the problem" to "I don't see how X solves the problem" to "I don't see how X would work" to "I have situation where X can't work" to "I guess I'll just have to see it first" to "Good luck with that."



And yes, there was a "specific" complaint.  It was actually several use cases rolled into one complaint about X.  It took some doing, but each complaint was of the form "If we follow this process, we'll wind up in a situation where the process breaks down because we'll always, inevitably do the wrong thing."



Doomed To Failure



This PAP's point was that a defied process so narrowly constrains us that we loose all ability to think.  Some PAP's lament the loss of "creativity" in a defined process.  Other PAP's lament the inability to make rational cost-benefit decisions within a defined process.



My question in this case was, "Why won't we apply your kind of good decision-making?"  The first response sounded like "we never learn."  The second response was a "Well, I understood that..." followed by some unsubstantiated pronouncement about the process.  The pronouncement wasn't a misinterpretation, it wasn't even a rumor.  It was a pronouncement that -- at the time -- seemed out-of-left-field random.  For example "I thought a tool did all this" or "I always expected that the API's worked like this" or "I need a GUI to remove user involvement" or some such.



In short, it was really "this process won't work."  Or perhaps "process, in general, doesn't solve problems, I solve problems."  Since it isn't their process, it's **Doomed to Failure**\ ™.  This kind of evasion is closely allied with the next, and I lump them both into the category of having a private agenda.



The Real Answer
---------------



In another example, we spent an amazing amount of time trying to work out a plan for solution X.  Since we had a Passive Aggressive Programmer involved, solution X was doomed.  The planning didn't really matter, since it wouldn't really work.  There was no "solution" because we don't know enough.  What we didn't know enough about varied through time, but we never knew enough.



It's not that we lack details.  It's just that we never have the right details.  And the missing details are dependent on other imponderables.  In the long run, this isn't aligned with the PAP's private agenda, and can't be done.



Direct questions get no answer at all.



However, hints were dropped.  Specifically, the lead-off Passive-Aggressive questions: "Why are we here?" and "What Problem Are We Solving?"  These are hints that the PAP doesn't agree.  Indeed, the PAP has a better idea.  However, the true hallmark of the passive part of this is that there is no usable answer to a direct question.



However, parsing the asides, non-answers, and By The Ways revealed a "consideration" or "side issue" that is a potential alternative solution.  This is a potentially viable alternative.  It hasn't worked before;  which is why I'm involved.  However, the point of being Passive-Aggressive (from my point of view) is that their approach is better, but they'll only passively make aggressive moves against any other idea.



While there's a real answer, and it has some merit, the PAP seems to have two competing directions.  They want to follow their own agenda, but they don't want any real responsibility.  As near as I can tell, they just want to be left alone.  They don't want to cooperate, lead or follow.  They want to be followed, but don't want to do very much to assure that they take the lead.



The Wall Of Fog
---------------



In another example, we wasted considerable time trying to work out a definition of the actual problem.  Since we had a Passive Aggressive Programmer involved, we can't fully define something.  Instead, we have endless rounds of the Yet Another Subtlety™ game.



Me: "So the process needs to do X".



PAP:  "Essentially."



Me: "You say that like there's something else."



PAP: "Actually, it's X and Y."



Me:  "So, the process needs to do X and Y?"



PAP:  "What do you mean by Y?"



Me:  "You brought it up, what did you mean?"



PAP:  "It could mean Y1 or Y2.  Some people go one way, some people go the other way.  What do you mean by Y?"



Me:  "You brought it up, not me.  What do you mean?  Let's try this.  We're talking about requirements.  What is required?  Think of it this way.  As an outside consultant, I'm selling you X and Y1.  Would you pay money for that?"



PAP:  "No, we'd only pay for X.  In that sense, Y's of no tangible value."



Me:  "Okay.  So the process needs to do X."



PAP:  "Essentially...."



And so, we never come to an actual understanding.  There's nuance piled on top of nuance.  It seems like the nuance card is really saying "I know this, and only I know this; you can never understand it.  Just leave me alone."



What's charming is that the PAP's solution to X wasn't working and couldn't easily be made to work.  There was this `Rat Holes of Lost Time <{filename}/blog/2006/02/2006_02_24-rat_holes_of_lost_time.rst>`_ ™ that was sucking up resources and things never quite worked. My approach is to stop digging a deeper hole.  Climb out and look all around.  Perhaps there's another, more productive, less error-prone approach.



But, since we can't identify all the requirements, we can't talk about alternatives.  It's a clever strategy for maintaining control without actually saying anything.



The Political Shield
--------------------



My final example is from the developers who are absolutely convinced that politics is the number one consideration in any discussion of a solution.  The conversation works like this.



PAP:  "I need help with X."



Me:  "Why on earth are you doing that?"



PAP:  "It is the only politically acceptable solution."



Me:  "It would be simpler to implement Y."



PAP:  "Unacceptable."



Me:  "Do you actually know how Y works?"



PAP:  "Doesn't matter how brilliant Y is, it's unacceptable."



Me:  "How about we extract some important lessons from Y, and apply them to improving X."



PAP:  "It would still be unacceptable, since Y is tainted by ... "  The reasons amount to nothing more than "It's not X", or more accurately, "It's not my original idea, therefore, it is **Doomed To Failure**.



Unshakable Beliefs
------------------



The Political Animals seem to have the least shakable belief system.  When their pet solution doesn't work well, we have to engage in a pointless conversation about alternatives.  I say pointless because I try to lift up alternatives, and they provide a large number of relatively irrational reasons why politics is more important than anything else.



Indeed, to try and get the conversation on track, I try to help them prioritize.  Often, politics winds up at the top of the list of important considerations.  Correct Functionality, Optimal Use of Resources, Maintainability, Adaptability and Cost are -- often -- lumped as "technical," and are secondary to politics.



The conversation often devolves into PAP lecturing me about the "real world."  This often includes the "perception is reality" justification.  Since perception is reality, only politically sensitive perceptions matter.  And the fact that they can't be made to work is just lack of cleverness or effort on my part.



I'm partial to the "someone else must have had this problem; in all of your company's consultants, you can't find anyone who can solve this problem?"  That's generally when I find a way to excuse myself.  Clearly, they're right.  Someone else knows this, and it isn't me.  Further, there isn't anyone in their entire company.



Patterns of Non-Performance
---------------------------



I've seen the **Secret Plan**  folks.  They don't provide input, and they don't actually help, either.  I've seen the **Wall of Fog**  folks who seem to flip-flop between the paralysis of analysis and pitching a non-solution because it's the only idea they've got.  I've also seen the **Political Shield**  folks who have such a profound (and unshakable) trust in organizational politics that rationality can't seem to enter the conversation.



What to do?  Listening is important, even if they're not talking.  Secret Plan folks will eventually tip there hand.  They just won't tip it to me.  



**Lesson 1**.
    Never go to meetings alone.  Have a quiet colleague, someone who takes notes, and can be confided in.  Often, that's my job.  Recently, I've had to bring people along to do that.



**Lesson 2**.
    Cut off the worrying.  Analysis of problems and enumeration of alternatives is fun for a while, but has a diminishing value.  At some point the problem statement is good enough.  Faced with this, you have to design a good solution, since requirements will erupt forever from a professional "yeah-but"-er.



**Lesson 3**.
    Transcending politics is just hard.  Looking at a "hypothetical" solution that is free from political constraints is often impossible.  The Political Animals seem to be the best at having a Secret Plan, and erecting a Wall of Fog.  I think that the Political Shield is really a way to defend one of the other strategies.




