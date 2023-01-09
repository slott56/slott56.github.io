Idempotence, Hysteresis and Determinism
=======================================

:date: 2015-02-05 08:00
:tags: algorithm,#python,architecture
:slug: 2015_02_05-idempotence_hysteresis_and_determinism
:category: Technologies
:status: published

Three terms that seem to cause confusion: Idempotence, Hysteresis and
Deterministic. The subject came up during my webcast on the `Five Kinds
of Python Functions <http://www.oreilly.com/pub/e/3255>`__. We can use
all three terms to describe a function. Two of them are relevant to
common design questions in software. The third is a higher-order
architectural consideration, and not really part of writing a function
definition in Python.
**Idempotent** -- narrowly defined --  means that *f*\ (*f*\ (*x*)) =
*f*\ (*x*). In computer science, the meaning is stretched so that we can
distinguish functions like random number generators from other
functions. A random number generator (Python's random.random(), for
example) is **not** idempotent. It returns a different result each time
it's called. Many other functions are idempotent because they always
return the same result given the same arguments. The functions in
Python's os module are **not** idempotent. The results change based on
external events.
**Hysteresis** is memory of previous events. A random number generator
may have some hidden hysteresis so that it can return the next value in
it's random sequence. Note that os.random() is explicitly based on
/dev/random; it involves hysteresis where entropy is accumulated. A
function that has an internal memoization cache has hysteresis; it will
compute subsequent results more quickly after having memorized previous
results.
Most functions are simply idempotent and don't generally involve any
hysteresis. The result value is a  **fixed** mapping from the argument
values.
A memoization cache preserves idempotence while adding hysteresis. The
functools.lru_cache decorator, for example, adds hysteresis to an
otherwise idempotent function. The result value still reflects a fixed
mapping.
A random number generator cannot have idempotence; it will leverage
hysteresis. We should think of a random number generator as an iterator
through a sequence of numbers. Given a seed, the sequence is entirely
fixed. Between any two numbers, it's very difficult to predict one from
the other without also knowing the hidden seed value.
**Unrelated Concept**
**
**\ We use idempotence and hysteresis to describe programming language
features. These features are entirely **deterministic**.  There's no
room for arbitrary, undefined, unpredictable behavior. Any
non-determinism needs to be very tightly boxed in by otherwise
deterministic programming constructs.
When writing a Python function, we assume that the language is
deterministic. Without this assumption, it's hard to conceive of what
the language would be like. What if statements were executed out of the
order we wrote them?
External events -- interrupts and the like -- are **non-deterministic**.
They can happen at any time, with no relationship to what's going on
inside the software world. Inside the software world, however, we expect
that everything is deterministic. This means that a server must always
cope with non-deterministic request ordering. Once request processing
starts, however, we generally rely on essential non-deterministic
software to process the results perfectly consistently.
An important example of **bounded non-determinism** is in Dijksta's
hypothetical programming language described in `A Discipline of
Programming <http://www.amazon.com/Discipline-Programming-Edsger-W-Dijkstra/dp/013215871X>`__.
Here there is explicit non-determinism among the "elif" and "eldo"
clauses. The selection among true alternatives was specifically
non-deterministic. Indeed, an evil demon would always strive to select
the worst possible choice. There was no "first one that's true" kind of
silliness that would allow certain kind of logic errors to survive.
A multiprocessing application leverages the OS to keep all processes
separate. Each process can then operate deterministically. Any
non-determistic OS events are concealed from the process by the normal
OS libraries that generally queue up events into buffers.
A multithreaded application, however, has to use some kind of explicit
synchronization to handle the inherent non-determinism of thread
scheduling. Thread libraries make no guarantees about the exact sequence
of operations between threads; the execution is non-deterministic
between threads.
For real fun, read about the non-deterministic memory write orders. The
`Data
Race <https://software.intel.com/sites/products/documentation/doclib/iss/2013/inspector/lin/ug_docs/GUID-7202FDEF-0268-4966-A163-E9A08F734754.htm>`__
article from Intel is illuminating. Google "non-deterministic memory
write order" for interesting reading on how processors have gotten --
perhaps -- too complex to be completely trustworthy.
This is different, also, from "arbitrary." A word that describes how the
C language deals with constructs like a[i]= i++;. There are two
unrelated state changes that happen in this statement. The order of
those two things is best described as "arbitrary." It's
**deterministic**. But it's not well defined by the language. Depending
on the compiler and optimization settings, it will be entirely fixed. A
function that uses these constructs could be **idempotent**. However,
the outcome can vary from compiler to compiler and optimization setting
to optimization setting. This kind of thing is devoutly to be avoided.
It's presence is a less-than-ideal language design choice; writing
software around a bad language feature is simply inexcusable.





