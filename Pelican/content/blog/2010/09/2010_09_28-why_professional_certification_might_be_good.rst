Why Professional Certification Might Be Good
============================================

:date: 2010-09-28 16:00
:tags: floating-point,integer,#python
:slug: 2010_09_28-why_professional_certification_might_be_good
:category: Technologies
:status: published

Sometimes I think we need professional certification in this industry. I
supported the `ICCP <http://www.iccp.org/>`__ for a long time.

In addition to certification, which requires ongoing educational
credits to maintain, there ought to be a process for revoking one's
certification, requiring them to pass their exams again.

Here's three strikes against two clods who wasted hours on -- perhaps
-- the dumbest things possible.

Strike 1. Counting From Zero
----------------------------

    I then ponited out that the Microsoft doco is weird because
    the highest
    number allowed by ulong is 18,446,744,073,709,551,615 which
    ends in an odds
    number

    I remineded him that 2**64 = 18,446,744,073,709,551,616

Apparently, this was the first time anyone realized how counting from
zero works. If they had actually thought about this, they could have
tried a smaller example. For example three bits. :math:`2^3 = 8`. When you
enumerate the values you get 0, 1, 2, 3, 4, 5, 6, 7. The highest
value is :math:`2^3-1`. It's not "weird". It's a trivially obvious
mathematical fact.

It works like this: :math:`n` values have numbers from 0 to :math:`n-1`. Didn't
know that? Consider your certification revoked. Even hobbyists know
this.

Strike 2. Wrong Tools and Wrong Approach
----------------------------------------

This is more subtle and involves two strikes. We'll look at just one
of them.

    Then he wanted a spreadsheet of 2 raised to nth power.

    I put it together and the numbers just looked weird. I then
    realized that
    when you type a number that contains more than 15 digits in a
    cell,
    Microsoft Excel changes any digits past the fifteenth place to
    zeroes

    What I felt like saying is that Python has built in this
    concept of "long integers" which has unlimited precision and it automatically
    switches to
    them

One of the clods knew Python. Instead of writing a trivial loop in
Python, apparently, clod #1 proceeded to type numbers into a
spreadsheet. The clod didn't *compute* them -- with formulas or
software -- the clod *typed* the numbers. *Typed*. Have Python.
Elected to type. How did they do the calculations? On a pocket
calculator? Oh the shame.

Also, additional penalties for exhaustive enumeration. They sent me
the spreadsheet as if it was somehow important that they could
enumerate values between 2**0 and 2**135. No summary or rule. Just a
mountain of useless numbers.

Strike 3. Floating Point
------------------------

This is not news. Nor should it be. Indeed, this should be the first
set of questions on the certification exam. If you can't figure out
floating point, you can't write software. Period. Please find another
job in an industry where you won't waste time on this.

Floating point is not simple, and everyone should study it before
they are allowed to charge money for creating software. Running
random experiments and exhaustively enumerating values is not
studying. That's not even hobbyist stuff. Try actually reading.
Starting with the standard. And David Goldberg's "`What Every
Computer Scientist Should Know About Floating-Point
Arithmetic <http://www.validlab.com/goldberg/paper.pdf>`__".

..

    contains more than 15 digits in a cell,
    Microsoft Excel changes any digits past the fifteenth place to
    zeroes

This is not "news". The link provided in the email ("`Last digits are
changed to zeroes when you type long numbers in cells of
Excel <http://support.microsoft.com/?kbid=269370>`__") indicates a
profound lack of understanding.

They could not have noticed that this is near :math:`2^50`. They never
looked up the `IEEE floating
point <http://en.wikipedia.org/wiki/IEEE_754-2008>`__
representation that -- pretty clearly -- says that there are only
52 bits of useful information. Wikipedia reminds us that this is
about 15 decimal digits. Rather than look this up, they chose to
be astonished.

These clods were astonished that floating-point numbers have a
finite mantissa. Astonished that -- empirically -- they had
stumbled on the fact that the mantissa is about 50 bits.

How much time did they waste on this? More importantly, how can
they consider their activities to be "professional"? Unable to
count from zero? Using the wrong tools and exhaustively
enumerating the obvious? Not realizing the floating-point values
have limited precision?

I find it appalling. Their escapades sound like two home hobbyists
with their fist ever copy of C#. Not like professionals.



-----

Hi, Your rant reminds me of the possibly allied c...
-----------------------------------------------------

Paddy3118<noreply@blogger.com>

2010-09-29 00:59:33.785000-04:00

Hi,
Your rant\* reminds me of the possibly allied case of the state of maths
awareness in the UK, where it is quite acceptable to admit to bad maths
skills whatever your other skills may be. You could be paid six-figures
in some industry, but have trouble working-out 17.5% of a number.
I guess the problem in your examples is that presumably these people are
calling themselves programmers without base knowledge that you think is
important.

I see the problem, but am not sure that certification, like microsoft
certification, is what we should be looking for. If someone has a degree
in programming or a degree in an allied subject such as a science or
engineering and computing was part of that course, then maybe all of
what you have mentioned should be covered by the course, and employers
should pay more for the degree qualified programmer. But programming can
still be self-taught and if you employ a self-taught programmer then you
should expect a much wider range of capabilities.

\*I meant rant in that you seemed to be letting off steam on an issue
rather than being excessively abusive.


When I started my current job, the company soon hi...
-----------------------------------------------------

Power Baker<noreply@blogger.com>

2010-10-02 00:03:52.501000-04:00

When I started my current job, the company soon hired someone officially
as a systems administrator, but also as another PHP programmer. The guy
spent a full two weeks (between taking phone calls about his side job)
editing a set of CSV files exported from Access tables, replacing the
commas with pipe characters, removing the in-field newlines (thereby
destroying vital information), replacing the end-of row newlines with
bare carriage returns (because that's "the Unix convention" despite
being completely ignored by Subversion), and stripping the quotation
marks.

By hand.

Because regular expressions were out of his league, and he hadn't spent
enough time on Google to learn about fgetcsv().





