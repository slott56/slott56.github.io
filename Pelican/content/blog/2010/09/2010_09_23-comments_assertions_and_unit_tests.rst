Comments, Assertions and Unit Tests
===================================

:date: 2010-09-23 08:00
:tags: unit testing,sphinx,#python
:slug: 2010_09_23-comments_assertions_and_unit_tests
:category: Technologies
:status: published

See "`Commenting the
Code <http://wrongsideofmemphis.wordpress.com/2010/09/15/commenting-the-code/>`__".

This posting tickled my fancy because it addressed the central issue of
"what requires comments outside Python docstrings". All functions,
classes, modules and packages require docstrings. That's clear. But
which lines of code require additional documentation?

We use Sphinx, so we make extensive use of docstrings. This posting
forced me to think about non-docstring commentary. The post makes
things a bit more complex than necessary. It enumerated some cases,
which is helpful, but didn't see the commonality between them.

The posting lists five cases for comments in the code.

#.  Summarizing the code blocks. Semi-agree. However, many code
    blocks indicates too few functions or methods. I rarely write a
    function long enough to have "code blocks". And the few times I
    did, it became regrettable. We're unwinding a terrible mistake
    I made regarding an actuarial calculation. It seemed so logical
    to make it four steps. It's untestable as a 4-step calculation.

#.  Describe every "non-trivial" operation. Hmmm... Hard t0 discern
    what's trivial and what's non-trivial. The examples on the
    original post seems to be a repeat of #1. However, it seems
    more like this is a repeat of #5.

#.  TODO's. I don't use comments for these. These have to be
    official ".. todo::" notations that will be picked up by
    Sphinx. So these have to be in docstrings, not comments.

#.  Structures with more than a couple of elements. The example is
    a tuple of tuples. I'd prefer to use a
    `namedtuple <http://docs.python.org/library/collections.html#collections.namedtuple>`__,
    since that includes documentation.

#.  Any "doubtful" code. This is -- actually -- pretty clear. When
    in doubt, write it out. This seems to repeat #2.

One of the other cases in the the post was really just a
suggestion that comments be "clear as well as short". That's
helpful, but not a separate use case for code comments.

So, of the five situations for comments described in the post, I
can't distinguish two of them and don't agree with two more.

This leaves me with two use cases for Python code commentary
(distinct from docstrings).

-   A "summary" of the blocks in a long-ish method (or function)

-   Any doubtful or "non-trivial" code. I think this is code where
    the semantics aren't obvious; or code that requires some kind
    of review of explanation of what the semantics are.

The other situations are better handled through docstrings or
named tuples.

Assertions
----------

Comments are interesting and useful, but they aren't real quality
assurance.

A slightly stronger form of commentary is the assert statement.
Including an assertion formalizes the code into a clear predicate
that's actually executable. If the predicate fails, the program
was mis-designed or mis-constructed.

Some folks argue that assertions are a lot of overhead. While they
are overhead, they aren't a lot of overhead. Assertions in the
body of the inner-most, inner-most loops may be expensive. But
must of the really important assertions are in the edge and corner
cases which (a) occur rarely and (b) are difficult to design and
(c) difficult to test.

Since the obscure, oddball cases are rare, cover these with the
assert statement in addition to a comment.

That's Fine, But My Colleagues are Imbeciles
--------------------------------------------

There are numerous questions on Stack Overflow that amount to
"comments don't work". Look at at the hundreds of question that
include the keywords `public, protected and
private <http://stackoverflow.com/search?q=public+protected+private>`__.

Here's a particularly bad
`question <http://www.blogger.com/Access%20Modifiers%20%E2%80%A6%20Why?>`__
with a very common answer.


    Because you might not be the only developer in your project and
    the other developers might not know that they shouldn't change
    it. ...

This seems silly. "other developers might not know" sounds like
"other developers won't read the comments" or "other developers will
ignore the comments." In short "comments don't work."

I disagree in general. Comments **can** work. They work particularly
well in languages like Python where the source is always available.

For languages like C++ and Java, where the source can be separated
and kept secret, comments don't work. In this case, you have to
resort to something even stronger.

Unit Tests
----------

Unit tests are perhaps the best form of documentation. If someone
refuses to read the comments, abuses a variable that's supposed to be
private, and breaks things, then tests will fail. Done.

Further, the unit test source **must** be given to all the other
developers so they can see how the API is supposed to work. A unit
test is a living, breathing document that describes how a class,
method or function behaves.

Explanatory Power
-----------------

Docstrings are essential. Tools can process these.

Comments are important for describing what's supposed to happen.
There seem to be two situations that call for comments outside
docstrings.

Assertions can be comments which are executable. They aren't always
as descriptive and English prose, but they are formal and precise.

Unit tests are important for confirming what actually happens.
There's really no alternative to unit testing to supplement the
documentation.



-----

Wow, being commented (even to more or less disagre...
-----------------------------------------------------

Jaime<noreply@blogger.com>

2010-09-23 09:31:45.493000-04:00

Wow, being commented (even to more or less disagree on some things) on
this blog is a great honor ;-)

I've updated a little the post, and also what to remark that, those are
habits I have, not ready guidelines.

I also make use of assertions from time to time, probably not as much as
I should.

What is important to note, is that comments are actually useful (or
could be, at least). And, of course, any documentation, unit testing,
assertions, etc... I don't know why, but my impression is that recently
there is some "anti comment" movement (probably more on high level,
dynamic languages, as they are more descriptive), stating that comments
(not bad-quality comments, but all comments) are not only unnecessary,
but pointless/confusing.

And I found that quite dangerous.


I tend to comment sparingly, relying on clear code...
-----------------------------------------------------

casey<noreply@blogger.com>

2010-09-23 16:26:12.991000-04:00

I tend to comment sparingly, relying on clear code as much as possible,
however there are some cases where I feel comments are invaluable:

-   Where the code does not clearly convey intent. This can often be the
    case with tightly optimized code. Unfortunately many common and
    effective code optimization techniques can make code difficult to read.
    A comment describing the algorithm and optimization, can prevent later
    second-guessing.

-   When I start out writing something "the obvious way" and find out that
    isn't adequate for whatever reason. For example, the obvious way may not
    handle an important edge case or may be very inefficient in some cases.
    A comment to explain why the code is not done the obvious way can be
    very helpful to others or your future-self.

-   Similarly when refactoring "obvious" code to fix edge case bugs.
    Sometimes its really useful to say why. Long explanations can be left to
    checkin comments and bug reports, of course, but a short comment can be
    really handy.

-   Explaining what isn't there. Sometimes you need to highlight or
    describe things that are either highly implicit or deliberately omitted
    from the code. Since there is typically no explicit code for these
    things, a comment is needed. Sometimes an assertion is also good for
    this, but it isn't always practical.

-   Small things that have big consequences. Sometimes you might have a
    very finely tuned constant, or threshold that appears arbitrary. You
    might have to import things in a special order (ugh, I know) or use an
    unsavory hack because of reasons you don't control. These things are
    rarely self-explanatory.

-   Backward compatibility hacks or caveats. You may beautifully refactor
    your api for the latest version, but you still need to support the old
    gross api for a while. You may need some comments to separate the wheat
    from the chaff.

I could go on and on. But primarily they are needed when there are
factors and reasons outside of the code itself that make it not
self-explanatory. In general, any dogma such as "____\_ is bad" reveals
a lack of practical perspective. Ideally we wouldn't need comments, but
that is not the world we inhabit.


Check out &quot;Java Programming With Assertions&q...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-09-23 22:10:52.044000-04:00

Check out "Java Programming With Assertions"
http://download-llnw.oracle.com/javase/1.4.2/docs/guide/lang/assert.html


Efficiently written information. It will be profit...
-----------------------------------------------------

Saqib Khatri<noreply@blogger.com>

2019-05-19 02:43:22.222000-04:00

Efficiently written information. It will be profitable to anybody who
utilizes it, counting me. Keep up the good work. For certain I will
review out more posts day in and day out. `Free offline English learning
software <https://kissenglishcenter.com/phan-mem-hoc-tieng-anh-offline-mien-phi/>`__





