Chapter 12 Alternate Example - Normalization and Decorators
===========================================================

:date: 2015-01-15 08:00
:tags: packtpub,#python,functional programming
:slug: 2015_01_15-chapter_12_alternate_example_normalization_and_decorators
:category: Technologies
:status: published


In the forthcoming *Functional Python Programming*
(https://www.packtpub.com/application-development/functional-python-programming) I
was pressured by one of the technical reviewers to create a better
example of composite function creation with decorators.

This was a difficult request. First, of course, "better" is poorly
defined. More importantly, the example in the book is extensive and
includes the edge-of-the-envelope "don't do this in real code" parts,
too. It's important to be thorough. Finally, it's real-world data
cleansing code. It's important to be pragmatic, but, it's kind of
boring. I really do beat it into submission showing simple decorators,
parameterized decorators, and crazy obscurely bad decorators.

In this case, "better" might simply mean "less thorough."

But, perhaps "better" means "less focused on cleansing and more
focused on something else."

**On Decoration**

The essence of the chapter -- and the extensive example -- is that we
can use decorators as higher-order functions to build composite
functions.

Here's an alternative example. This will combine z-score normalization
with another reduction function. Let's say we're doing calculations
that require us to normalize a set of data points before using them in
some reduction.

Normalizing is the process of scaling a value by the mean and standard
deviation of the collection. Chapter 4 covers this in some detail.
Reductions like creating a sum are the subject of Chapter 6. I won't
rehash the details of these topics in this blog post.

Here's another use of decorators to create a composite function.

::

    def normalize( mean, stdev ):
       normalize = lambda x: (x-mean)/stdev
       def concrete_decorator( function ):
           @wraps(function)
           def wrapped( data_arg ):
               z = map( normalize, data_arg )
               return function( z )
           return wrapped
       return concrete_decorator




The essential feature of the @normalize(mean, stdev) decorator is to
apply the normalization to the vector of argument values to the
original function. We can use it like this.

::

    >>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
    >>> from Chapter_4.ch04_ex4 import mean, stdev
    >>> m_d, s_d =  mean(d), stdev(d)
    >>> @normalize(m_d, s_d)
    >>> def norm_list(d):
    ...     return list(d)
    >>>
    >>> norm_list(d)
    [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]




W've create a norm_list() function which applies a normalization to
the given values. This function is a composite of normalization plus
list().

Clearly, parts of this are deranged. We can't even define the
norm_list() function until we have mean and standard deviation
parameters for the samples. This doesn't seem appropriate.

Here's a slightly more interesting composite function. This combines
normalization with sum().

::

    >>> @normalize(m_d, s_d)
    >>> def norm_sum(d):
    ...     return sum(d)
    >>>
    >>> norm_sum(d)
    0.0




We've defined the normalized sum function and applied it to a vector
of values. The normalization has parameters applied. Those parameters
are relatively static compared with the parameters given to the
composite function.

It's still a bit creepy because we can't define norm_sum() until we
have the mean and standard deviation.

It's not clear to me that a more mathematical example is going to be
better. Indeed, the limitation on decorators seems to be this:

-   The original (decorated) function can have lots of parameters;

-   The functions being composed by the decorator must either have no
    parameters, or have very static "configuration" parameters.

If we try to compose functions in a more general way -- all of the
functions have parameters -- we're in for problems. That's why the
data cleansing pipeline seems to be the ideal use for decorators.






