Don't Solve My Problem. 
========================

:date: 2019-03-19 08:00
:tags: Design Principles
:slug: 2019_03_19-dont_solve_my_problem
:category: Technologies
:status: published


Two and a half examples of "Don't solve the problem I described.
Provide the implementation I dream about."

Can't Use Enums for Constants
-----------------------------


I was asked to see this because sometimes there's just too much
abstraction
https://stackoverflow.com/questions/2668355/how-much-abstraction-is-too-much

The accepted answer links to some useful design principles. Read the
answer. It's useful.

The question objects to abstract superclasses without much (or any)
actual implementation.  I've seen folks toy around with frameworks
where there are classes that introduce a name, but little else. So I
understand the complaint. I once tried to use Python classes as
surrogates for Java interfaces. It was a bad idea. And irrelevant to
solving the underlying problem.

The problem that lead to the "yet another abstraction" complaint,
however, was **not** related to a design with empty layers of
framework abstractions. It was **not** related to classes used to
define an interface-like feature in Python. It wasn't related to
\*anything\* in the Stack Overflow question or answer.

The "yet another abstraction" complaint was based on Python not having
constants. Seriously. How did we get here? Right. They don't want a
solution. They want to complain.

I lift this situation up to folks who are trapped in conversations
where things devolve into bizarro-world like "Yet Another Abstraction
is bad" when we're not talking about abstractions. The solution is
simple, but, it's not what they wanted so, it's labeled as bad in some
way.

The solution is bad because it's unexpected. Consequently peripheral,
tangential, weird-ass nonsense will show up in trying to avoid an
unexpected solution.

Can't Assign Numbers
--------------------


There's an API to load some data.  They have 100's of clients happily
loading data. In some cases, the clients must assign numbers in
addition to names; it's a disambiguation thing. Most of the time, the
name is good. In a few cases, (name, number) is a two-part key because
they have multiple instances with the same name.

We're good here. The data structure's key can be (name, number) and
the default number is zero. Works for almost everyone.

Almost everyone. Exception they have one client who cannot count or
enumerate their data.

Really.

The client can't even pre-process the data to add numbers because
reasons.

The stated reason is "the data originates off-line and the numbers
might be inconsistent." The key needs a number. It doesn't need to
consistent. The point is asking the client to own the identity -- a
name and a number.

The solution seemed easy. Assign a number. If your data comes from a
spread-sheet, use the row number. The =row() function works. Use that.
If your data doesn't come from a spread-sheet write a tiny utility to
laminate a number into the data. This doesn't seem hard. And then the
client owns the object identity.

Nope.

Can't do it. The web service will have to assign the number for them.

It's not a **difficult** feature to add. It's a complicated, stateful
default value. This will turn into trouble tickets in the future when
the numbers are unacceptable because they change with each load or
something even more obscure than that.

Can't Fork a Repo
-----------------


This isn't recent, and I may not have the details right. But.


The team had evolved an approach where they had several different
pieces of software spread among multiple branches in a single Git
repository.


This was weird. And they were -- of course -- about to start having
CI/CD problems as they moved away from manual builds into a world of
git commit hooks and relatively fixed CI/CD pipelines.


And they were really unhappy. They liked having multiple branches in
a single repo. The idea of forking this into separate repos was
unacceptable. Unworkable. Breaks everything. (Breaks **everything**
they had. **Everything** they needed to replace. Or so they claimed.)


They had some vision of having the CI/CD jobs all reworked to move
beyond the common dev/master world into their uniquely odd world of
lots of parallel branches, each it's own private "master". But all in
one repo.


They seemed to have locked into a strange world view, and weren't
happy discarding it. The circular discussions of how multiple repos
would break something something in their something was more examples
of tangential, irrelevant discussion to cloak empty whining.

tl;dr
-----


I think there are people who don't really want a "solution." They want
something else.

There are people who have a vision: How Things Should Be (HTSB™,) They
seem to be utterly unwilling to consider something that is not
literally their (narrow) vision of HTSB.

It's very much as "Don't confuse me with facts, my mind is made up"
situation. It's exasperating to me because of the irrelevant
side-channel discussions they use to avoid confronting (or even
stating) the actual problem.



-----

<a href="https://galido.net/blog/best-tech-blogs/"...
-----------------------------------------------------

Star moon<noreply@blogger.com>

2019-03-25 14:15:06.714000-04:00

`Technology <https://galido.net/blog/best-tech-blogs/>`__\ Technology is
constantly changing. It is an industry that moves so fast, things can
become obsolete within weeks. Thus it is essential to always stay on top
of `news and information <https://galido.net/blog/best-tech-blogs/>`__,
whether it be by newsletter, following RSS feeds and blogs, tutorials or
going back to school.
Click here to know more information `Tech
Blogs <https://galido.net/blog/best-tech-blogs/>`__


Can't we paint the bikeshed blue, And by it le...
-----------------------------------------------------

smitty1e<noreply@blogger.com>

2019-03-19 08:30:55.041000-04:00

Can't we paint the bikeshed blue,
And by it let my pony chew,
Eternally, cow-like, its cud,
While we wallow in our FUD?





