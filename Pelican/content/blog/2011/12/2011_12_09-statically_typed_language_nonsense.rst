Statically Typed Language Nonsense
==================================

:date: 2011-12-09 08:00
:tags: Programming Languages,#python,functional programming
:slug: 2011_12_09-statically_typed_language_nonsense
:category: Technologies
:status: published

| Read this: "`Here Comes Functional
  Programming <http://www.sdtimes.com/l/36103>`__" by Larry O'Brien in
  SD Times.

   people who should know better continue to assert that statically
   typed languages are "safer, because the compiler can catch errors
   that otherwise wouldn't show up until runtime." While it's true a
   statically typed language can detect that you've assigned a string to
   a double without running your code, no type system is so strict that
   it can substitute for a test suite, and if you have a test suite,
   type-assignment errors are discovered and precisely diagnosed with
   little difficulty.

| Thank you.   A language like Python, which lacks static type
  declarations for variables, is not evil or an accident waiting to
  happen.
| The article is about functional languages.  But the static declaration
  statement is universally true.



-----

I love Python myself, but I&#39;ve dabbled in Hask...
-----------------------------------------------------

Luke Plant<noreply@blogger.com>

2011-12-09 12:02:48.058000-05:00

I love Python myself, but I've dabbled in Haskell and this oft-repeated
argument only goes so far. You could equally say that no test suite is a
substitute for static typing!
For example, the following code has a type level bug (class Bar has a
method missing), despite a test suite with 100% coverage:
https://gist.github.com/1452367
The problem is that tests only test code works for one value - an
infinitesimal fraction of the possible number of values. Languages with
strong static typing systems can enforce checks for \*every\* value,
and, in the hands of someone skilled, can be used to make remarkable
guarantees about a program that would be extremely difficult/impossible
to do using a test suite.
For example, the guarantees made by STM code in Haskell - see
http://book.realworldhaskell.org/read/software-transactional-memory.html
section "STM and safety" - these checks are impossible to do using
tests.


Types Considered Harmful by Lamport

http://resear...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-12-26 15:38:19.907000-05:00

Types Considered Harmful by Lamport
http://research.microsoft.com/en-us/um/people/lamport/tla/notes.html


What criteria are being used to judge static versu...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-12-15 15:28:03.888000-05:00

What criteria are being used to judge static versus dynamic languages?
What is the context in which the criteria are being applied?
In my opinion, it is a design choice. What comes to mind is the quote
from spider man “with great power comes great responsibility”. The good
news is that dynamic languages allow for greater flexibility. The bad
news is that the greater flexibility allows you to get yourself into
more trouble.


&quot;but I&#39;ve dabbled in Haskell and this oft...
-----------------------------------------------------

mazelife<noreply@blogger.com>

2011-12-09 13:36:30.290000-05:00

"but I've dabbled in Haskell and this oft-repeated argument only goes so
far"
True, but Haskell is at the very far end of the scale in terms of what
its type system is capable of. When you make an assertion that a
statically typed language like, say, Java, is inherently safer, it's a
more problematic proposition.
Interestingly enough, Haskell's type system can actually aid you in
writing your test suite (see, for example QuickCheck, which can generate
test caes for you).


Should Your Specification Language Be Typed?  (wit...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-12-26 15:27:15.938000-05:00

Should Your Specification Language Be Typed? (with Larry Paulson)
ACM Transactions on Programming Languages and Systems 21, 3 (May 1999)
502-526. Also appeared as SRC Research Report 147.
http://research.microsoft.com/en-us/um/people/lamport/pubs/lamport-types.pdf


@Luke I&#39;d argue that it is not 100% coverage a...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-12-09 13:39:10.885000-05:00

@Luke I'd argue that it is not 100% coverage as it does not verify the
logic of what happens if val > 10.





