The Anti-IF Campaign
====================

:date: 2010-12-27 11:48
:tags: anti-if,#python
:slug: 2010_12_27-the_anti_if_campaign
:category: Technologies
:status: published

Check this out: http://www.antiifcampaign.com/.

I'm totally in favor of reducing complexity. I've seen too many
places where a **Strategy** or some other kind of **Delegation**
design pattern should have been used. Instead a cluster of
if-statements was used. Sometimes these if-statements suffer
copy-and-paste repetition because someone didn't recognize the design
pattern.

What's important is the the **if** statement -- in general -- isn't
the issue. The anti-if folks are simply demanding that folks don't
use **if** as a stand-in for proper polymorphism.

Related Issues
--------------

Related to abuse of the **if** statement is abuse of the **else**
clause.

My pet-peeve is code like this.

::

  if condition1:
     work
  elif condition2:
     work
  elif condition3:
     work
  else:
     what condition applies here?

When the various conditions share common variables it can be very
difficult to deduce the condition that applies for the **else**
clause.

My suggestion is to **Avoid Else**.

Write it like this.

::

  if condition1:
     work
  elif condition2:
     work
  elif condition3:
     work
  elif not (condition1 or condition2 or condition3)
     work
  else:
     raise AssertionError( "Oops.  Design Error.  Sorry" )

Then you'll know when you've screwed up.

[**Update**]

  Using an **assert** coupled with an **else** clause is a kind of
  code-golf optimization that doesn't seem to help much. An **elif**
  will have the same conditional expression as the **assert** would
  have. But the comment did lead to rewriting this to use
  AssertionError instead of vague, generic Exception.



-----

How do you feel about an assert in the else, e.g. ...
-----------------------------------------------------

Fred<noreply@blogger.com>

2010-12-23 18:47:19.280000-05:00

How do you feel about an assert in the else, e.g. assert not (condition1
or condition2 or condition3)? Failed asserts usually mean some kind of
design or logic error (they mean that exactly to me, but opinions vary),
which you indicated in your last mock up.


Um... I thought everyone whom took CS101 was taugh...
-----------------------------------------------------

Doug Napoleone<noreply@blogger.com>

2010-12-25 05:07:08.052000-05:00

Um... I thought everyone whom took CS101 was taught this when the case
statement was covered.


To be clear:

Rules for the proper use of the case...
-----------------------------------------------------

Doug Napoleone<noreply@blogger.com>

2010-12-25 05:12:46.968000-05:00

To be clear:
Rules for the proper use of the case statement:
1. always have a 'default:'

2a. if the work in the case statement changes the score state (i.e.
later code is expecting it to have set state to a valid value) then
raise an exception unconditionally as the only work in the default
target. That exception should not be treated as a normal error, but a
development internal error.

2b. if not, then use an assert in the default target.

3. In either case of 2, have the error or assert contain descriptive
text.

(Taken from our coding standards document)


I didn&#39;t mean the assert as code golf. The ass...
-----------------------------------------------------

Fred<noreply@blogger.com>

2010-12-28 19:24:26.852000-05:00

I didn't mean the assert as code golf. The assert has an indication of
"we shouldn't really have to check this, as it's supposed to be
guaranteed true already, but we will anyway", which isn't as obvious (at
least to me) the other way.
I do find it useful, moreso in early prototyping, to include the failed
expression as the exception message by default. A generic "internal
error, exiting" message can be shown to the user at a higher level where
AssertionError is caught, rather than coming up with a meaningful
message for each of these explicit raises.
However, both are very close in any case. (You seemed to acknowledge
this by saying the only difference is in golf.)



Fred<noreply@blogger.com>

2010-12-28 19:24:38.279000-05:00

This comment has been removed by the author.





