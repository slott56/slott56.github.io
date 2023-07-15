Preconceived Notions, Perceptual Narrowing, The Einstellung Effect 
===================================================================

:date: 2014-03-27 08:00
:tags: design,object-oriented design,Einstellung Effect
:slug: 2014_03_27-preconceived_notions_perceptual_narrowing_the_einstellung_effect
:category: Technologies
:status: published

Read this http://en.wikipedia.org/wiki/Einstellung_effect
Great
`article <http://www.scientificamerican.com/article/einstellung-how-psychologists-study-einstellung-effect-chess/>`__
in Scientific American on this.

I didn't realize that sometimes I do spend time trying to defeat the
Einstellung effect. Not a lot of time. But some time.

When confronted with gnarly design problems, I have the same bad habits
as many other programmers. I reach for algorithms or data structures
that I'm familiar with, even if they're not optimal. Sometimes I'll use
algorithms that are not even appropriate to the problem domain.

However.

In working on a book on Advanced Object-Oriented Python, I realized that
one habit I have is -- perhaps -- actually helpful.  It's this.
I can -- if I'm careful -- enumerate the alternatives. It's challenging
to exhaustively enumerate design choices. It seems to help to have a
list of things that clearly aren't optimal or aren't workable or aren't
elegant. After pruning away the bad ideas, sometimes a good idea
remains.

I'm not often good at this. Sometimes I dive in early, make choices,
learn from my failures, and am forced to refactor.

The "enumeration" isn't literally **every** possibility. Sometimes, it's
the **types** of possibilities or the strategies involved. Sometimes
it's the patterns that the possibilities fulfill.

Example 1. When looking at Python data structures, the ABC's of
Sequence, Mapping and Set provide a big-picture way to identify places
to look. Once we've narrowed the field of view, we can look at kinds of
sequences of kinds of mappings. We can also look at the generator
expression alternative to a sequence object.

Example 2. There are often three design strategies: inheritance,
composition (or wrapping) and invent-from-scratch. It's sometimes
helpful to actually put together a technical spike of a subclass, a
wrapper class and the outline of a *de novo* class definition. Bad ideas
usually surface quickly when actual code is involved.

I thought I was being fussy. Or I was just stalling to avoid starting to
write bad code too early. Or I was wasting time obsessing over
performance issues.

No. I was preventing Einstellung. Avoiding Perceptual Narrowing.
Avoiding "Calling a problems nails because I'm wielding the hammer."

**The Relational Database as Hammer**

I feel obligated to note that the relational database often becomes the
hammer and all problems are then reduced to RDBMS/SQL nails. No matter
what the problem is.

One of the most amazing of these problems was an inquiry about "the top
*n* rows query". It was the DBA's sense that getting the "top *n* rows"
using some selection and ordering criteria was a really standard problem
that everyone had confronted. The problem was so common there just
**had** to be a standard, widely-adopted high-performance solution.

When getting the top 100 rows out of 40,000, there will be performance
issues. The filtering and sorting (and any joins) will take time and DB
resources. My question was "why?"

The answer was appalling. The database was being used as a message
queue. The top 100 rows out of 40,000 was being doing to pick the next
few items out of the queue for processing. The non-top-100 rows were
merely lower priority items in the queue.

Wouldn't a proper message queue have been cheaper and simpler?'
Apparently not. Einstellung had set in. They had data. They had a
database. What more is there?





