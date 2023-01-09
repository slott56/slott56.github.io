Duct Tape Programmers
=====================

:date: 2009-10-01 09:14
:tags: software process improvement,tdd
:slug: 2009_10_01-duct_tape_programmers
:category: Technologies
:status: published

See Joel On Software: `The Duct Tape
Programmer <http://www.joelonsoftware.com/items/2009/09/23.html>`__: he
lauds the programmer who gets stuff done with "duct tape and WD-40".

Here's why: "Shipping is a feature. A really important feature. Your
product must have it."

Dave Drake sent the link along with the following:

This "speaks of coding for the rest of us, who are not into building
castles in the air, but getting the job done. Not that there is
anything wrong with better design, cleaner APIs, well-defined
modularity to ease the delegation of coding as well as post-delivery
maintenance. But damn, I wish I had a nickel for every time I sat in
a design meeting where we tried to do something the fancy way, and it
broke in the middle of the development cycle, or testing, or even the
builds, and always in the demos."

**However**

There is one set of quotes that falls somewhere on the continuum of
wrong, misleading and flamebait.

"And unit tests are not critical. If there’s no unit test the
customer isn’t going to complain about that."

This -- in my experience -- is wrong. For Joel or the author of the
quote (Jamie Zawinski) this may be merely misleading because it was
taken out of context.

It's absolutely false the customers won't complain about missing unit
tests. When things don't work, customers complain. And one of the
surest ways to make things actually work is to write unit tests.

I suppose that genius-level programmers don't need to test. The rest
of us, however, need to write unit tests.

**Unit Testing Dogma**

On Stack Overflow there are some questions that illustrate the value
of misinformation on unit testing. On one end, we have Zawinski (and
others) who says that Unit Tests don't create enough value. On the
other end we have questions that indicate the slavish adherence to
some unit test process is essential.

See `How to use TDD correctly to implement a numerical
method? <http://stackoverflow.com/questions/1463632/how-to-use-tdd-correctly-to-implement-a-numerical-method/1463677#1463677>`__
The author of the question seems to think that TDD means "decompose
the problem into very small cases, write one test for each very small
test, and then code for just that one case and no others." I don't
know where this process came from, but it sounds like far too much
work for the value created.

It's unfair to say that unit testing doesn't add value and claim that
customers don't see the unit tests. They emphatically **do** see unit
tests when they see software that works. Customers don't see unit
tests in detail. They don't see dogmatic process-oriented software
development.

When there are no tests, the customer sees shoddy quality. When the
process (or the schedule) trumps the feature-set being delivered, the
customer sees incomplete or low-quality deliverables.

**Conclusion**

The original blog post said -- clearly -- that gold-plated technology
doesn't create any value.

The blog post also pulled out a quote that said -- incorrectly --
that unit tests doesn't create enough value.



-----

Version control is another thing that the users do...
-----------------------------------------------------

Marius Gedminas<noreply@blogger.com>

2009-09-30 12:24:58.885000-04:00

Version control is another thing that the users do not see; I wonder
what Joel thinks about it. It is possible to ship code without using
version control but I would not wish to be on the team that tries it.


The user doesn&#39;t (normally) see any code eithe...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-09-30 09:32:48.540000-04:00

The user doesn't (normally) see any code either, that doesn't mean you
can do without.


I know quite a few genius-level programmers.  They...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-09-30 00:36:27.359000-04:00

I know quite a few genius-level programmers. They write tests. In fact,
they write tests first, before writing the code, which is a really
ingenious thing to do.


It is nice blog,Thanks for sharing resources relat...
-----------------------------------------------------

Itsolusenz<noreply@blogger.com>

2009-10-10 08:42:57.257000-04:00

It is nice blog,Thanks for sharing resources related to `website
design <http://www.itsolusenz.com>`__





