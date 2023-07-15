Good Design and Pragmatic Design
================================

:date: 2005-09-28 10:46
:tags: architecture,software design
:slug: 2005_09_28-good_design_and_pragmatic_design
:category: Architecture & Design
:status: published





Kenny YoungBuck approaches the Master and asks,
"What is good design?"



The Master
replies, "Kenny, you innocent little monkey, it's a wonder you haven't joined a
cult.  Good design maximizes business value while minimizing costs including
development, maintenance, adaptation and
operation."



"Master, are there
circumstances where this is not
true?"



By way of an answer, the Master
took out his
*shinai* 
and smacked Kenny on the head so hard that his ears rang like the aftershocks of
an earthquake.



"Master, where should I
check constraints on input
arguments?"



"Why Kenny, we've been over
this in essay 15, `Errors and Exceptions <{filename}/blog/2005/09/2005_09_19-essay_15_errors_and_exceptions.rst>`_ .  A class has this
responsibility for its own
inputs."



"Master, it seems simpler for
each client to validate data before sending it to my
class."



"Simpler for whom, Kenny?  Your
validation rules are now spread out into multiple classes, leading to duplicated
code, and increasing your maintenance costs.  Change is not localized, and
classes are tightly coupled."



"But
Master, I have an example of validation rules in the client that creates
business value.  Can't business value trump good
design?"



By way of an answer, the
Master took out his
*shinai* ;
Kenny, adroitly, jumped back before he was
smacked.



"Tell me, Kenny, how did the
client side validation rules create business
value?"



"They solved two problems in
sending batches of data to a vendor, Master.  First, they provided immediate
feedback on the quality of the data being sent.  Second, they provided clear
error messages for diagnosing the
problem."



"You must suspect this
solution is bad design, or you wouldn't be asking questions," the Master
replied.



"It violates the principle of
checking constraints only once," Kenny
said.



"Therefore, it was not the best
solution, was it?" the Master
replied.



"But Master, it creates
business value," Kenny said. "Isn't that the
goal?"



"Since the duplicated
constraints add maintenance cost, I hope that was balanced against the value of
early detection and better diagnosis of
problems."



Kenny, triumphant, replied
that cost and benefit had both been
considered.



"What, my furry little
friend, was the business
problem?"



"Why, the problem was bad
data being sent to the vendor," Kenny
replied.



The Master cracked Kenny
across the chops so hard that Kenny had to pick himself up off the
floor.



"That's a technical problem. 
What was the business problem?" The Master
asked.



"It took too long to discover
the bad data, and too long to diagnose the
errors."



"So, what else could have been
done?" the Master asked.



"What else?"
Kenny asked, flinching back and
cowering.



"You identified two problems:
timing and opacity of error messages.  Let's focus on one to solve: how can you
solve the timing problem?" the Master
asked.



"Timing?  The batch isn't
complete until late in the day."



The
Master raised the
*shinai* ,
Kenny ducked to the side, but the Master landed a
*mawashi-geri* 
on Kenny's head that dropped him like a bag of dirty
laundry.



"Do you mean, Master, that the
batch processing is part of the
problem?"



"Very good, Kenny," the
Master said.



"But Master, the vendor
can't process partial batches."



"Kenny,
Kenny, Kenny," the Master said.  "Good design and business management have
nothing to do with each other.  Just because the vendor is unwilling to change a
bad process does not invalidate good design
principles."



"But Master, in the face
of such a business context, what design should I use?  The right design won't
work because we can't change the vendor.  All we're left with is the bad
design."



"If it makes you feel better,"
the Master said, "call it pragmatic; or better, call it the interim
design."



"Interim?" Kenny asked,
forgetting to duck. The Master brained him with the
shinai.



"Once you know the root cause
and the real fix, that is the good design solution.  You did identify the proper
resolution, didn't you?"



"But Master,
it would be a huge project to fix the
interface."



"Really?  To fix a single
interface?"



"Well, we do have several
relationships with the vendor, Master, and we would have to fix all of them,"
Kenny said



"Why?" the Master asked. 
"One interface should be message oriented to save time and reduce errors.  What
do the other interfaces have to do with
this?"



"Even changing one interface
would be a large project.  Where duplicating the constraints was a small
project.  How can you justify all that development effort for a small
problem?"



The Master put down the
*shinai* .
Kenny stopped cowering and looked at the Master, who appeared lost in thought. 
With a sudden
*tsuki* ,
the Master knocked Kenny back onto his kiester.  Kenny fell like a load of
gravel pouring off a dump truck.



"Which
is cheaper: development or maintenance?"




"But Master," Kenny coughed, "labor
costs are the same."



"Which has the
bigger duration?  What is the life-span of
software?"



"Years?" Kenny asked, just
before being pounded back down to the
tatami.



"Decades, my little monkey,"
the Master said.  "Decades.  You're wringing your hands over one-time
development cost that will be returned hansomely over years of flawless
operation.  Instead of a single investment in good design, you endure the
ongoing extortion  of bad design."



With
that, the interview was over; the master left the dojo.








