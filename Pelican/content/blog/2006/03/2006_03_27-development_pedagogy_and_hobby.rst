Development, Pedagogy and Hobby
===============================

:date: 2006-03-27 15:35
:tags: architecture,software design,complexity
:slug: 2006_03_27-development_pedagogy_and_hobby
:category: Architecture & Design
:status: published





In
*Rat-holes of Lost Time*  [`Rat-Holes of Lost Time <{filename}/blog/2006/02/2006_02_24-rat_holes_of_lost_time.rst>`_ ], I thought out loud about software
development and how the resulting software product may or may not be of any
value.  In SEI terminology [`view_qm <http://www.sei.cmu.edu/str/taxonomies/view_qm.html>`_ ], this is Need Satisfaction.  Sometimes I
call it **Solving The Problem** ™.



I
tried to distinguish two dimensions of need satisfaction: viability and
applicability.  Is it viable (workable, useful, valuable), and does it even
apply to the problem at hand?  They are, IMO, separate, and they lead to
different kinds of rat-holes and require different kinds of
interventions.



**Comments.** A comment suggests that software development can be
done for pedagogical purposes, listing two examples.  I wasn't sure how to take
this because pedagogy and software development aren't the same thing.  They're
both "programming" exercises, but they have very different purposes.  If we're
going to conflate software development with other activities, why stop at
pedagogy?



I'm not sure what -- precisely -- the comment meant, but I can see this from the comment: I didn't
make the distinction clear enough.  So, here's a summary that may clarify
things.  

-   Software development builds **software**.

-   Pedagogical exercises build **skills**  in software development.



My point remains that building software to solve a problem can involve pursuing
technology that would never actually solve the problem, or pursuing a solution
in a way it isn't really viable.  By a non-viable solution, I mean that it lacks
the quality attributes necessary to make it valuable. 




The comment notes that pedagogical exercises come in a variety of forms:

-   Learning the language.

-   Learning the libraries (I think this is
    what "demo a certain ability" means).



But why stop there?  There are
many other things we need to learn.

-   Learning the layers of the technology
    stack (e.g., web servers, LDAP servers, etc.)

-   Learning to lessen resource use (or any
    of the SEI cost-focused quality measures like cost of ownership to name a
    few)

-   Learning to get the largest of any of the
    other SEI value-focused quality measures (including maintainability,
    adaptability)



But why stop there? 
There are still higher-level things we need to learn.

-   Learning to allocate functionality appropriately.

-   Learning design patterns.



Beyond pedagogy, there's also
the hobby of programming, which is yet another very bothersome thing
masquerading as software development.



When it comes to software
development, we can even split a hair between a software product that is
"bespoke" and belongs in one and only one context, and "product" which is more
generic and usable in a variety of contexts by a number of customers.  However,
there aren't dramatically different skills or lost-time rat-holes when we split
this hair.



**Practice makes Permanent**. The craft or sullen art of
programming can be applied to a number of situations.  Software development is
the one I'm interested in because that's where the cost and value are.  Skill
building is tangential to my original post, but it does lead to the following
considerations of rat-holes and
learning.



Skill-building in software
development is a very touchy subject because there is so much to learn.  In
addition to the language, library, layers, leasts and largests, we also have to
learn how to manage our time, design something that will work, debug something
that doesn't work, and write test cases to demonstrate how well it works.  And
we haven't even touched on asset management issues like configuration control,
change control and documentation.



So, let's take the comment as meaning that "pedagogy can have rat-holes, too."
That seems as good an interpretation as any.



We make permanent what we practice.
If we have shoddy pedagogical practices, the skills we build are
shoddy skills.  Practice only makes perfect if we are practicing perfect things.
If we are practicing the wrong things, we will build poor skills and make those
non-skills permanent personal
liabilities.



If pedagogy has rat-holes, how do we manage those rat-holes?




**Learning to Capture Knowledge**.   The answer is the same.  When we
learn to program (or learn the libraries, layers, leasts and largests), we are
focused on knowledge capture and using that captured knowledge appropriately. 
We need to keep our heads out of the rat-holes and look at our
goals.



We aren't focused on knowledge
capture of the language itself.  We are focused on knowledge capture in the
problem domain, on behalf of the users, for benefit of the users.  It's hard to
say this enough times to make it clear as crystal.  But we aren't capturing
knowledge on the technology, we are capturing knowledge in the area to which the
technology is applied:  we are capturing application
knowledge.



For example, if we practice
writing the fewest lines of source code, we perfect obscurity.  We can claim we
are doing an optimization to use the least resources, but that may be a false
economy because the short, obscure statement may also be slower.  We can claim
we are learning nuances of the language, but that may be of no value, since we
write for the benefit of maintainers and adapters, who may not care about
language nuances.



We could, for
example, dive into rat-holes to exploit things we don't understand fully;
perhaps the buzzwords appealed to us.  Design patterns are notorious for giving
us large hammers that make every problem look like a nail.
We could go **State** -happy, or **Strategy** -happy,
and have an application with a useless level of flexibility.  Indeed, this is a
common indictment of OO programming: it's too complex for simple problems.  I
think this is true because of the rat-hole of design
patterns.



We could implement things in
inappropriate places in the technology stack because it's the part we understand
or want to play with.  We put everything in JSP because we understand how it
extends HTML, and don't want to learn Java and Struts and all that OO
mumbo-jumbo.



Or, we struggled to learn
XML and XSLT, so now we want to find a use for it.  Since it is a pretty general
programming model, it looks like the ultimate solution to all the world's
problems.  I don't know if XSLT is a Turning-complete programming language; even
if it is, it's opaque for the most part, and it becomes a real rat-hole of lost
time.  It can be slow, and it can be obscure; is it solving our
problem?



**Course Corrections**. The most important course correction comes
from having a goal.  If we are developing software, we have a goal.  If we are
learning, we have to establish goals, or we're doomed to chasing around in the
rat-warrens.  If, on the other hand, this is a hobby, goals don't matter -- code
away.



Establishing goals for learning
isn't too difficult.  One source is the on-line tutorials to help a vendor (or
an open-source project) sell their product.  The other source for goals is the
actual source for open-source projects.  Even a commercial framework (like
Micro$oft .Net) has tons of open-source projects associated with it.  Use these
projects to establish a standard of professionalism.  Avoid pursuing every
buzzword, every inappropriate piece of technology, every non-viable solution,
and every non-solution.  Instead, aspire to the standards set by open-source
projects.

















