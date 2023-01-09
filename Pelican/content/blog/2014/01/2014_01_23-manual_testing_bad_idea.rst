Manual Testing -- Bad Idea
==========================

:date: 2014-01-23 08:00
:tags: unit testing,selenium
:slug: 2014_01_23-manual_testing_bad_idea
:category: Technologies
:status: published

The question of testing came up recently. The description of the process
sounded like manually "testing" some complex web application.
When trying to work out manual "testing", I find it necessary to use
scare quotes. I'm not sure there's a place for "manual testing" of any
software.

I know that some folks use Selenium to created automated test scripts
for interactive applications. That may be a helpful technology. I prefer
automated test scripts over manual testing. Consequently, I'm not too
interested in helping out with testing -- other than perhaps coaching
developers to write automated test scripts.


http://docs.seleniumhq.org <http://docs.seleniumhq.org/


To continue this rant.


I've seen the suggestion that having a person do some manual
"testing" will permit them to notice things that are "broken" but not
a formal requirement in a test script. This seems to require some
willing misuse of words. A person who's supposed to be noticing stuff
isn't testing: they're exploring or demonstrating or thinking.

They're not testing. Tests are -- by definition -- pass-fail. This is
a very narrow definition: if there's no failure mode, it's not a
test, it's something else. Lots of words are available, use any word
except "test." Please.


Reading about exploratory "testing" leads to profound questions about
the nature of failing an exploratory "test." When did the failure
mode become a requirement? During the exploration? Not prior to the
actual development?


When an explorer finds a use case that was never previously part of a
user story, then it's really an update to a user story. It's a new
requirement; a requirement defined by a test which fails. It's a
really high-quality requirement. More importantly, exploratory
"testing" is clearly design. It's product ownership.


This kind of exploration/thinking/playing/experiencing is valuable
stuff. It needs to be done. But it's not testing.


Developers create the test scripts: unit tests of various kinds.
Back-end tests. Front-end tests. Lots of testing. All automated. All.


Other experienced people -- e.g., a product owner -- can also play
with the released software and create informed, insightful user
stories and user story modifications that may lead to revisions to
test cases. They're not testing. They're exploring. They're writing
new requirements, updating user stories, and putting work into the
backlog.


**Putting work into the backlog**


An exploratory "test" should not be allowed to gum up a release. To
do that breaks the essential work cycle of picking a story with fixed
boundaries and getting it to work.  Or picking a story with nebulous
boundaries and grooming it to have fixed boundaries. Once you think
you're doing exploratory "testing" on a release that's in progress,
then the user stories no longer have a fixed boundary, and the idea
of a fixed release cycle is damaged. It becomes impossible to make
predictions, since the stories are no longer fixed.


For a startup development effort, the automated test scripts will
grow in complexity very quickly. In many cases, the test scripts will
grow considerably faster than the product code. This is good.


It's perfectly normal for a product owner to find behaviors that
aren't being tested properly by the initial set of automated test
scripts. This is good, too. As the product matures, the test scripts
expand. The product owner should have increasing difficulty locating
features which are untested.


**Management Support**


What I've found is that some developers object to writing test
scripts. One possible reason is because the test scripts don't seem
to be as much "fun" as playing with GUI development tools.


I think the more important reason is that developers in larger
organizations are not rewarded for software which is complete, but
are rewarded for new features no matter what level of quality they
achieve. This seems to happens when software development is
mismanaged using a faulty schedules and a faulty idea of the rate of
delivery of working software.


If the schedule -- not working features -- dominates management
thinking, then time spent writing tests to show precisely how well a
feature works is treated as waste. Managers will ask if a developer
is just "gold plating" or "polishing a BB" or some other way of
discrediting automated test case development.


If the features dominate the discussion, then test development should
be the management focus. A new feature without a sufficiently robust
suite of automated tests is just a technology spike, not something
which can be released.


Manual "testing" and exploratory "testing" seem to allow managers to
claim that they're testing without actually automating the tests. It
appears that some managers feel that reproducible, automated test
take longer and cost more than having someone play with the release
to see if it appears to work.

**But What About...**

The most common complaint about automated GUI testing isn't a proper
pass-fail test issue at all.

Folks will insist that somehow font choice, color, position or other
net effects of CSS properties must be "tested." Generally, they seem
to be conflating two related (but different) things.

1.  Design. This is the position/color/font issue. These are design
    features of a GUI page or JavaScript window or HTML document. Design.
    The design may need to be reviewed by a person. But no testing makes
    sense here. The design isn't a "pass-fail" item. Someone may say it's
    ugly, but that's a far cry from not working. CSS design (especially
    for people like me who don't really understand it) sure feels like
    hacking out code. That doesn't mean the design gets tested.

2.  Implementation. This is the "does every element use the correct
    CSS class or id?" question. This is automated testing. And it has
    nothing to do with looking at a page. It has everything to do with an
    automated test to be sure HTML tags are generated properly. It has
    nothing to do with the choice of packing algorithm in a widget, and
    everything to do with elements simply making the correct API calls to
    assure that they're properly packed.

For people like me who don't fully get CSS, lots of pages need to be
reviewed to make sure the CSS "worked". But that's a design review.
It's not a part of automated testing.

Here's the rule: Ugly and Not Working have nothing to do with each
other. You can automate tests for "works" -- that's objective. You
can't automated the test for "ugly" -- that's subjective.

Here's how some developers get confused.  A bug report that amounts
to "ugly" is fixed by making a  change to a GUI element. This is a
valid kind of bug-to-change. But how can the change have an automated
test? You **must** have a person confirm that the GUI is no longer
ugly. Right?

Wrong.

The confusion stems from conflating design (change to reduce the
ugliness) and implementation (some API change to the offending
element.) The design change isn't subject to automated testing.

Indeed, it passed the unit tests before and after because it worked.
No design can have automated testing. We don't test algorithm design,
either. We test algorithm implementations.

Compare it with class design vs. implementation. We don't check every
possible aspect of a class to be sure it follows a design. We check
some external-facing features. We don't retest the entire library,
compiler, OS and toolset, do we? We presume that design is
implemented more-or-less properly, and seek to **confirm** that the
edges and corners work.

Compare it with database design vs. implementation. We don't check
every bit on the database. We check that -- across the API -- the
application uses the database properly.

There's no reason to test every pixel of an implementation if the
design was reviewed and approved and the GUI elements use the design
properly.





