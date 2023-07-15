KTLO Management
===============

:date: 2007-06-28 19:20
:tags: architecture,software design,complexity,management
:slug: 2007_06_28-ktlo_management
:category: Architecture & Design
:status: published







We wind up in this situation from time to time.



**Customer**:
    [X] is broken, what will it cost to fix it?



**Us**:
    Depends, but put $$$ in your budget.



**Customer**:
    I can't afford $$$, I can barely afford to Keep The Lights On™!



At this point, the conversation is usually over.  There is more to talk about, much more.  However, most customers simply stop talking.  Even if try to respond along the line of the following, the conversation is usually over.



**Us**:
    What do you need to know about the cost?  Software projects can grow without limit, so there's no practical upper bound.  Even with a tiny scope, you can polish and gold-plate that scope until it's too costly to consider.  Do you have some budget already in mind and want to know if I agree with it?  For any amount (even a silly amount like a week's revenue) something positive can be accomplished.



Somewhere there's this (false) expectation that given a vague statement of "requirements" there's a fixed, single dollar figure that will implement those requirements.  What's irritating is the "Keep The Lights On" rational for preventing progress.  



Where does this come from?  Why is it so paralyzing?



The Situation
-------------



When it costs a fortune to KTLO, it usually means that a lot of labor is squandered on "break fix" work.  It's like paying a union electrician to replace the 10A fuse every time you use the 12A drill press.  If the motor was in a good position and there's not much load, the draw may be under 10A -- or over 10A for a short-enough period of time -- and everything's fine. 



When I get called in, it's because the drill press isn't doing everything people want it to do.  The changes will require rewiring the drill press.  The customer, however can't afford to rewire anything because the electrician is fully occupied changing fuses.



The Remedy
----------



So, if we have drill press and power problems, we'll need to fix the power distribution infrastructure first.  That will free up the electrician to rewire the drill press.



The sensible thing to do is to replace the fuse panel with higher-rated fuses.  This makes sense to me.  And it makes superficial sense to the customer and the electrician.  However, the customer has a kind of fundamental brain damage that makes this simple, sensible, incremental work impossible.



The Choke
----------



The customer, for some reason, chokes on this.  Rather than just do it, we get into hand-wringing and justification.  In order to make it "palatable" to executives or peers or someone else, we have to fold in more features.



A simple fuse upgrade turns into task to replace the fuses with circuit breakers.  There are fewer safety issues.  In someone's mind, an end-user can flip the breaker, and we don't need a skilled, union electrician to put fuses in.



The Choke After the Choke
-------------------------



An IT manager has taken a simple task, choked, and made it more complex than is required.  Often, they choke a second time.  This second choke is the killer.



Rather than upgrade the fuse, we tried to replace the fuse box with a breaker panel.  But we then run out of time (or money or both) and stop the project.



We now have a half-rebuilt fuse box and a half-installed breaker panel.  We haven't freed up the union electrician.  We now need him on permanent overtime to sort out the wiring mess that was created by the second choke.  Each time a tool stops, we have to figure out if it is a fuse or a breaker, then make the necessary repair.



It's this crazy double-choke that raises the cost of KTLO, and makes progress impossible.



Conclusion
----------



At some point the cost of KTLO prevents work from being done.  Everyone is tied up replacing fuses, tracking down wiring messes, and trying to troubleshoot production machinery which doesn't work correctly.



Eventually, after enough frustration and turnover, this is "business as usual."  Nothing can get done because we're so busy keeping the lights on.





