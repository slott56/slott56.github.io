Process Not Working -- Must Have More Process
=============================================

:date: 2009-10-27 11:25
:tags: configuration management,agile,architecture
:slug: 2009_10_27-process_not_working_must_have_more_process
:category: Technologies
:status: published

After all, programmers are all lazy and stupid.

Got his complaint recently.

    "Developers on a fairly routine basis check in code into the wrong
    branch."

Followed by a common form of the lazy and stupid complaint.
"Someone should think about which branch is used for what and
when." Clearly "someone" means *the programmers* and "should think
about" means *are stupid*.

This was followed by the "more process will fix this process
problem" litany of candidate solutions.

    "Does CVS / Subversion have a knob which provides the
    functionality to
    prevent developers from checking code into a branch?"

    "Is there a canonical way to organize branches?"

Really, this
means something like *what are the lazy, stupid programmers doing
wrong?*

Plus there where rhetorical non-questions to emphasize the lazy,
stupid root cause. "Why is code merging so hard?" (Stupid.) "If
code is properly done and not coupled, merging should be easy?"
(Lazy; a better design would prevent this.) "Perhaps the
developers don't understand the code and screw up the merge?"
(Stupid.) "If the code is not coupled, understanding should be
easy?" (Both Lazy and Stupid.)

Root Cause Analysis
-------------------

The complaint is about process failure. Tools do not cause (or
even contribute) to process failure. There are two possible
contributions to process failure: the process and the people.

The process could be flawed. There could be no earthly way the
programmers can locate the correct branch because (a) it doesn't
exist when they need it or (b) no one told them which branch to
use.

The people could be flawed. For whatever reason, they refuse to
execute the process. Perhaps they know a better way, perhaps
they're just being jerks.

Technical means will not solve either root cause problem. It will
-- generally -- exacerbate it. If the process is broken, then
attempting to create CVS / Subversion "controls" will end in
expensive, elaborate failure. Either they can't be made to work,
or (eventually) someone will realize that they don't actually
solve the problem. On the other hand, if the people are broken,
they'll just subvert the controls in more interesting, silly and
convoluted ways.

My response -- at the time -- was not "analyze the root causes".
When I first got this, I could only stare at it dumbfounded. My
answer was "You're right, your developers are lazy and stupid.
Good call. Add more process to overcome their laziness and
stupidity."

After all, the questioner clearly knows -- for a fact -- that more
process helps fix a broken organization. The questioner must be
convinced that actually talking to people will never help.

The question was not "what can I do?" The question was "can I
control these people through changes to CVS?" There's a clear
presumption of "process not working -- must have more process."

The better response from me should have been. "Ask them what the
problem is." I'll bet dollars against bent pins that no one tells
them which branch to use in time to start work. I'll bet they're
left guessing. Also, there's a small chance that these are
off-shore developers and communication delays make it difficult to
use the correct branch. There may be no work-orders, just informal
email "communication" between on-shore and off-shore
points-of-contact (and, perhaps, the points-of-contact aren't
decision-makers.)

**Bottom Line**. If people can't make CVS work, someone needs to
talk to them to find out why. Someone does not need to invent more
process to control them.



-----

Tools do not cause (or even contribute) t...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-10-28 08:51:10.818000-04:00

>> Tools do not cause (or even contribute) to process failure. There are
two possible contributions to process failure: the process and the
people.

When I was working in quality assurance and concentrating on process
improvement, we identified the following 6 factors affecting process
effectiveness.

1. procedures - How well do the established procedures work?

2. tools - Do the people have the tools that they need? Do the tools
work well?

3. training - Do the people doing the work have adequate training in the
procedures, how to use the machines, general background information?

4. the reward system - What are you actually rewarding? If management
\*says\* it wants a quality product, but promotes people who deliver a
product \*quickly\* regardless of product quality, then the de facto
reward system is rewarding speed, not quality.

5. the inputs to the process - If you are getting crappy inputs, you're
going to produce crappy outputs. (See yesterday's headlines: if a home
builder gets toxic drywall from China, he builds a toxic house)

6. the suitability of the people to the job - Here, the problem is your
hiring process. If you hire square pegs to fit in round holes, then of
course you will have problems.

Notice that there is no category for "lazy and stupid people". This is
not a useful category if you're actually trying to improve a process.
But this is, of course, the \*only\* category that Management has
traditionally recognized and used. Its use, of course, doesn't help
improve anything. All it does is to give a manager whose processes
aren't functioning well some place to shift the blame.

So: a few more tools to use when thinking about process issues.


Actually, I think SVN/CVS (i.e. tools) could be co...
-----------------------------------------------------

Ville<noreply@blogger.com>

2009-10-27 15:01:53.190000-04:00

Actually, I think SVN/CVS (i.e. tools) could be contributing to the
problem, as merging with them is a PITA.


Talking to people should <i>be</i> the process.

W...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-10-27 12:25:32.114000-04:00

Talking to people should *be* the process.

We recently added a lengthy new freeze stage to our release cycle.
Anyone who
wants to check in longterm code can use the newer branch, anyone who
needs to
get into the release about to land needs to request and be given a
"freezeok"
tag on their bug. I told them: "If you forget, you will be devoured by
zombies."

The first couple of times someone pushed code to the frozen branch
without the
tag I used http://diy.despair.com/motivator.php with an image of their
faces
superimposed on somebody being eaten by zombies. Everyone laughed.
Nobody did
it again.

Is that so damn hard?


In respect of your question:

&quot;Does CVS / Sub...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-10-27 21:51:11.786000-04:00

In respect of your question:

"Does CVS / Subversion have a knob which provides the functionality to
prevent developers from checking code into a branch?"

As far as I know, subversion itself doesn't. But if the repository is
served up by mod_dav_svn under Apache then it isn't that hard to
configure some Apache directives which block the HTTP method types
relating to update of a subversion directory for the appropriate part of
the URL namespace. We use this, and what it allows is for someone to
create a new tag, remove that whole tag, check out from that tag, but
not commit any changes into that tag.

I'm not at work today so don't have handy what the rules are, but if
remember will post them later.





