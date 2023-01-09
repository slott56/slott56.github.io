Paranoid Schizophrenic Programming (Revised)
============================================

:date: 2011-12-12 14:31
:tags: #python,architecture,OO design,defensive programming,assert statement
:slug: 2011_12_12-paranoid_schizophrenic_programming_revised
:category: Architecture & Design
:status: published

Some folks love the twin ideas that (1) "someone" might break the API
rules and (2) they must write lots of bonus code to "prevent" problems.

Sigh.

There are three distinct things here.

-  API definition - something we do all the time.

-  "Defensive Programming" - something that may or may not actually exist.

-  Paranoid Schizophrenic programming - a symptom of larger problems; this exists far too often.

It's not that complicated, there's a simple 3-element
checklist for API design.  Unless "someone" is out to break
your API.   Whatever that means.

A related topic is this kind of thing on Stack Overflow:
`How Do I Protect Python Code <http://stackoverflow.com/questions/261638/how-do-i-protect-python-code>`__?
and `Secure Plugin System For Python
Application <http://stackoverflow.com/questions/908285/secure-plugin-system-for-python-application>`__.

Following the Rules

When we define an API for a module, we define some rules.
Failure to follow the rules is -- simply -- bad behavior.
And, just as simply, when someone breaks the API rules, the
module can't work.  Calling the API improperly is the as
same as trying to install and execute a binary on the wrong
platform.

It's the obligation of the designer to specify what will
happen when the rules are followed.  While it might be nice
to specify what will happen if the rules are not followed,
it is not an obligation.

Here's my canonical example.

::

    def sqrt( n ):
        """sqrt(n) -> x such that x**2 == n, where n >= 0."""

The definition of what will happen is stated.  The
definition of what happens when you attempt sqrt(-1) is not
defined.  It would be nice if sqrt(-1) raises an exception,
and it would be nice to include that in the documentation,
but it isn't an obligation of the designer.  It's entirely
possible that sqrt(-1) could return 0.  Or (0+1j).  Or nan.

Item one on the checklist: define what the function will do.

And note that there's a world of difference between failing,
and being used improperly.  We're talking about improper use
here; failure is unrelated.

Complete Specification
-----------------------

When I remind people that they are only obligated to specify
the correct behavior, some folks say "That's just wrong!  An
API document should specify every behavior!  You can't omit
the most important behavior -- the edge cases!"

Ummm... That position makes no sense.

There are lots and lots of situations unspecified in the API
documentation.  What about sqrt(2) when the underlying math
libraries are mis-installed?  What about sqrt(2) when the OS
has been corrupted by a virus in the math libraries?  What
about sqrt(2) when the floating-point processor has been
partially fried?  What about sqrt(2) when the floating-point
processor has been replaced by a nearly-equivalent
experimental chipset that doesn't raise exceptions properly?

Indeed, there are an infinite number of situations not
specified in the API documentation.  For the most part,
there is only one situation defined in the API
documentation: the proper use.  All other situations may as
well be left unspecified.    Sometimes, a few additional
behaviors are specified, but only when those behaviors
provide value in diagnosing problems.

Diagnosing Problems
-------------------

An API with thoughtful documentation will at least list the
exceptions that are most likely to be raised.  What's
important is that it does not include an exhaustive list of
exceptions.  Again, that's an absurd position -- why list
MemoryError on every single function definition?

What's important about things like exceptions and error
conditions is the diagnostic value of this information.  A
good designer will provide some diagnostic hints instead of
lots of words covering every "possible" case.

If there's no helpful diagnostic value, don't specify it.
For example, there's little good to be done by adding a
"Could raise MemoryError" on every method function
description.  It's true, but it isn't helpful.  Except in a
rare case of an API function that -- if used wrong -- will
raise a MemoryError; in this rare case you're providing
diagnostic information that can be helpful.  You are
overwriting the API, but you're being helpful.

Item two on the checklist: provide diagnostic hints where
they're actually meaningful and helpful.

Error Checking
---------------

How much error checking should our ``sqrt()`` function do?

-  None?  Just fail to produce an answer, or perhaps throw an exception?

-  Minimal.  This is easy to define, but many folks are unhappy with minimal.

-  More than minimal but not everything.  This is troubling.

-  Everything.  This is equally troubling.

No error checking is easiest.  And it fits with our
philosophy.  If our sqrt function is used improperly --
i.e., someone broke the rule and provided a negative
number -- then any exception (or nan value) will
propagate to the caller and we're in good shape.  We
didn't overspecify -- we provided a wrong answer when
someone asked a wrong question.

Again, we're not talking about some failure to process
the data.  We're talking about being called in a
senseless way by a client that's not following the rules.

There's a subtlety to this, however.

A Non-Math Example
-------------------

Yesterday, I tried to use a postal scale to measure the
temperature in my oven.  The scale read 2.5 oz.

What does that mean?

I asked an ill-formed question.  I got something back.
It isn't an answer -- the question was ill-formed -- but
it looks like an answer.  It's a number where I expected
a number.

Here's another one.  "Which is heavier, the number 7 or
the color green?"  Any answer ("7", "green" or "splice
the main brace") is valid when confronted with a question
like that.

Perhaps I should have run a calibration (or "unit") test
first.

The Termination Question
------------------------

In the case of a function like square root, there is an
additional subtlety.  If we're using logarithms to
compute square root, our log function may raise an
exception for sqrt(-1) or it may return nan; either of
which work out well - an ill-formed question gets an
improper answer.

However, we might be using a search algorithm that will
fail to terminate (a bisection algorithm, or Newton's
method, for example.) Failure to terminate is a much,
much worse thing.  In this case -- and this case only --
we have to actually do some validation on the range of
inputs.

Termination is undecidable by automated means.  It's a
design feature that we -- as programmers -- must assert
independently of any lint, compiler or testing
discipline.

Note that this is not "defensive programming".  This is
ordinary algorithm design.  Every loop structure must
terminate.  If we're trying a simple bisection algorithm
and we have not bracketed a root properly (because, for
example, it's a complex number), the bisection won't
terminate.  A root-finding bisection algorithm must
actually do two two things to assure termination:  check
the range of the inputs and limit the number of
iterations.

This isn't defensive programming because we're not
checking that a mysterious "someone" is abusing the API.
We're asserting that our loop terminates.

Item 3 on the checklist: reject values that would lead
loops to not terminate properly.

::

        def sqrt( n ):
            """sqrt(n) -> x; such that x**2 == n; where n >= 0"""
            assert n >= 0

Incorrect Error Checking
------------------------

Once we start checking for loop termination, folks say
that "we're on a slippery slope" and ask where's that
"fine line" between the minimal level of error checking
(loops will terminate) and the
paranoid schizophrenic level of error checking.

It isn't a slope.  It's a cliff.  Beyond loop
termination, there's (almost) nothing more that's
relevant.

By "almost", I mean that languages like Python have a
tiny realm where an additional assertion about the
arguments is appropriate.

Because of duck typing, many algorithms in Python can be
written very generically.  Very generically.  Sorting,
for example, can be applied to lists of -- almost --
anything.  Except, of course, it isn't meaningful for
things with no useful \__cmp_\_ function.  And in the
case of things like a dictionary, what's the basis for
comparison?

In the case of `dynamic
languages <http://en.wikipedia.org/wiki/Dynamic_programming_language>`__
and `duck
typing <http://en.wikipedia.org/wiki/Duck_typing>`__,
it's possible that an algorithm will terminate, producing
a wrong answer.  (BTW, this one reason why Python has /
and // as distinct division operators -- to assure that
ints and floats can be used interchangeably and the
algorithm still works.)

Item 4 on the checklist: When you have a known problem
with a type, reject only those types that are a problem.

This is very rare, BTW.  Mostly it occurs with
overlapping types (lists and tuples, floats and ints.)
Most well-designed algorithms work with a wide variety
of types.  Except in the overlapping types situation,
Python will raise exceptions for types that don't work;
make use of this.

What About "Business Rules"?
----------------------------

By "business rules" most people mean value ranges or
codes that are defined by some externality.  As in "the
claim value must be a number between the co-pay and the
life-time limit".

This is not a "Defensive Programming" issue.  This is
just a policy statement written into the code.  Your API
won't break if the claim value is less than the co-pay.
Your users will be pissed off, but that's a separate
problem.

Also, you rarely raise an exception for business rules.
Usually, you'll collect business rule violations into a
formal error report or log.  For example, Django's
`Forms <http://docs.djangoproject.com/en/dev/ref/forms/validation/#ref-forms-validation>`__
will collection a dictionary of validation errors.  Each
element in the dictionary has a list of problems with a
particular field on the form.

What About "Someone" Who Can't Use The API?
-------------------------------------------

Here's where the conversation goes awry.

First, if this is a hypothetical "someone", you need to
relax.  Consider these use cases. Are you worried that
"someone" will download your software, install it,
configures it, start to use it, and refuse to follow the
documented API?  Are you worried that they will send you
angry emails saying that they insist on doing the wrong
thing and your software doesn't work?  You don't need
"defensive programming", you need to either add the
features they want or steer them to a package that does
what they're expecting.

Here's another version of a hypothetical someone: you're
working as part of a larger team, and you provide a
package with an API.  Are you worried that a team member
will refuse to follow the documented API?  Are you
worried that they will send you angry emails saying that
they insist on doing the wrong thing and your software
doesn't work?  This isn't a call for "defensive
programming," this is a call for a conversation.  Perhaps
you built the wrong thing.  Perhaps you API documentation
isn't as crystal-clear as you thought.

Someone Really Is Using It Wrong
--------------------------------

A common situation is someone who's actually using the
API wrong.  The conversation didn't help, they refuse to
change their software.  Or you can't easily call them out
on it because -- for example -- your boss wrote detailed
specs for you, which you followed, but someone else isn't
following.  What can you do?  The specification
contradicts the actual code that uses the API.

Is this a place where we can apply "Defensive
Programming"?

Still no.

This is a call for some diagnostic support.  You need
error messages and logs that help you diagnose the
problem and locate the root cause.

Root Causes
------------

The issue with "Defensive Programming" is that it
conflates two unrelated use cases.

-  API Design.

-  Unwilling (or unable) to Follow Instructions. (UFI™)

API design has four simple rules.

#.  Document what it does.

#.  For diagnostic aid, in common edge cases, document
    other things it might do.  Specifically, describe
    conditions that are root causes of exceptions or weird
    answers.  Sometimes a subclass of exception is handy
    for handling this.

#.  Be sure that it terminates.  If necessary, validate
    arguments to determine if termination can't happen and
    raise exceptions.

#.  In rare cases, check the data types to be sure the
    algorithm will actually work.  Most of the time, wrong
    data types will simply throw exceptions; leverage that
    built-in behavior.

If (1) someone refuses to follow the rules and (2)
complains that it's your API and (3) you elect to make
changes, then...

First, you can't prevent this.  There's no "defensive
programming" to head this off.

Second, know that what you're doing is wrong.   Making
changes when someone else refuses to follow the rules
and blames you is enabling someone else's bad
behavior.  But, we'll assume you have to make changes
for external political reasons.

Third -- and most important -- you're relaxing the API
to tolerate ordinarily invalid data.

Expanding What's "Allowed"
--------------------------

When someone refuses to follow the API -- and demands you
make a change -- you're having this conversion.

Them: "I need you to 'handle' sqrt(-1)."

You: "Square Root is undefined for negative numbers."

Them: "I know that, but you need to 'handle' it."

You: "There's no answer, you have to stop requesting sqrt(-1)."

Them: "Can't change it.  I'm going to make sqrt(-1) requests for external political reasons.  I can't stop it, prevent it or even detect it."

You: "What does 'handle' mean?"

At this point, they usually want you to do something that
lets them limp along.  Whatever they ask you to do is
crazy.  But you've elected to cover their erroneous code
in your module.  You're writing diagnostic code for their
problem, and you're burying it inside your code.

If you're going to do this, you're not doing "defensive
programming", you're writing some unnecessary code that
diagnoses a problem elsewhere.  Label it this way and
make it stand out.  It isn't "defensive" programming.
It's "dysfunctional co-dependent relationship"
programming.



-----

"Errors should never pass silently." -Zen of Pytho...
-----------------------------------------------------

Benjamin<noreply@blogger.com>

2009-06-02 12:44:53.415000-04:00

"Errors should never pass silently." -Zen of Python
sqrt(-1) returning 0 is failing silently.

While you may not like it, verifying inputs leads to much, much
friendlier APIs. And while you may not feel it's an obligation, you'll
make users of your API much happier if you do so. And sometimes, it is
an obligation: http://xkcd.com/327/


When you first mention rule 4 you state:

"Item 4 ...
-----------------------------------------------------

Paddy3118<noreply@blogger.com>

2009-06-01 04:36:38.306000-04:00

When you first mention rule 4 you state:

"Item 4 on the check-list: check types; reject only those types that are
a problem."

When you mention it in the main list later, it becomes:
"In rare cases, check the data types to be sure the algorithm will
actually work. Most of the time, wrong data types will simply throw
exceptions; leverage that built-in behavior."

You need t modify the first mention to something like
"Don't check argument types! (Except where you know a particular
data-type leads to a problem, where that data-type should then be
excluded rather than checking for a data-type that you know works
correctly)"

- Given half a chance, some people will want to code data-type checks.

- Paddy.


A good analogy is in the world of electric applian...
-----------------------------------------------------

nnis<noreply@blogger.com>

2009-06-01 15:07:12.399000-04:00

A good analogy is in the world of electric appliances. Electronic
components like resistors, capacitors, transistors blow up if they are
hooked up wrong or too much voltage is put into them, yet no electronic
engineer says: “Gosh, these components are junk, let’s ask the supplier
to send us protected versions that withstand any kind of abuse”. A
component built that way would cost 5 times as much. What is actually
done is to look at the spec sheets for the components used and put them
together in such a way that they won’t blow up when you operate the
appliance.


I&#39;m not convinced.   When I write defensive ch...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-06-15 16:40:51.110000-04:00

I'm not convinced. When I write defensive checks for, say, function
arguments, I'm guarding against someone (very probably me a few weeks
later) accidentally misusing an API. I'd rather know about that misuse
as soon as it happens, instead of later discovering that the numerical
results of all past year's calculations are suspect because somewhere we
took a square root of a negative number.

Then again expensive rockets have been brought down by excessive error
handling (Ariane 5 Flight 501). I don't know where the line lies
exactly; but as long as program crashes aren't prohibitively expensive
I'd rather see a crash than garbage output.





