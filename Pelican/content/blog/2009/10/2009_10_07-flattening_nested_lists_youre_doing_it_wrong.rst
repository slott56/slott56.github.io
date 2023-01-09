Flattening Nested Lists -- You're Doing It Wrong
================================================

:date: 2009-10-07 10:19
:tags: #python
:slug: 2009_10_07-flattening_nested_lists_youre_doing_it_wrong
:category: Technologies
:status: published

On StackOverflow you can read numerous questions on "flattening" nested
lists in Python.

They all have a similar form.

"How do I flatten this list ``[ [ 1, 2, 3 ], [ 4, 5, 6 ], ... , [ 98, 99, 100 ] ]``?"

The answers include list comprehensions, itertools, and other clever
variants.

[STRIKEOUT:All] Much of which is [STRIKEOUT:simply wrong]
inappropriate.

**You're Doing it Wrong**

The only way to create a nested list is to append a list to a list.

::

    theList.append( aSubList )

You can trivially replace this with the following

::

    theList.extend( aSubList )

Now, your list is created flat. If it's created flat, you never need
to flatten it.

**Obscure Edge Cases**

Sometimes it may be necessary to have both a flattened and an
unflattened list. I'm unclear on when or how this situation arises,
but this may be edge case that makes some of itertools handy.

For the past 3 decades, I've never seen the "both nested and not
nested" use case, so I can't fathom why or how this would arise.

**Visiting a Tree**

Interestingly, a tree visitor has a net effect somewhat like
"flattening". However, it does not actually create an intermediate
flat structure. It simply walks the structure as it exists. This
isn't a proper use case for transforming a nested list structure to a
flat structure. Indeed, this is a great example of why nested
structures and flat structures are quite separate use cases.



-----

I think we can safely remove itertools altogether ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-10-06 11:20:30.210000-04:00

I think we can safely remove itertools altogether after this.


Bit of an odd statement that you&#39;ve never seen...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-10-06 17:07:40.628000-04:00

Bit of an odd statement that you've never seen "both nested and not
nested" use cases. Consider a simple tree built via lists- walking the
tree depth/breadth is "flattening the list" (more so visitation, but I
digress).

The usage scenario where nested/not nested is extremely common...


This is pretty naive.  The times I&#39;ve needed t...
-----------------------------------------------------

Michael<noreply@blogger.com>

2009-10-06 10:20:04.707000-04:00

This is pretty naive. The times I've needed to flatten a list were
because I needed the non-flattened form for one thing, and the flattened
form for another thing. It's not like we just don't know about extend
versus append.


so, remove itertools.chain() from the standard lib ?
----------------------------------------------------

mike bayer<noreply@blogger.com>

2009-10-06 11:05:36.985000-04:00

so, remove itertools.chain() from the standard lib ?


List.append is not even close to the only way to c...
-----------------------------------------------------

John<noreply@blogger.com>

2009-10-06 14:58:00.388000-04:00

List.append is not even close to the only way to create nested lists.
The first counterexample that springs to mind is when you map a function
over a list where the result of the function is a list.


&gt; The only way to create a nested list is to ap...
-----------------------------------------------------

Jason<noreply@blogger.com>

2009-10-07 12:31:22.159000-04:00

> The only way to create a nested list is to append a list to a list.
Note quite true. One case I had the other day was like:
# got input data like this:

::

    >>> row = ["Apples", "100", "40 +- 10", "50 +- 4"]
    >>> row = [c.Split("+-") for c in row]
    >>> row
    [['Apples'], ['100'], ['40 ', ' 10'], ['50 ', ' 4']]
    Where I wanted to flatten "row" to:
    ['Apples', '100', '40 ', ' 10', '50 ', ' 4']

(Later stripping whitespace and converting everything where applicable
to float.)

I ended up naming each column explicitly, something like this:

::

    >>> a,b,c,d = row
    >>> c1, c2 = c.Split("+-")
    ...
    ...

which is in the real code pretty verbose and ugly. Wish Python had a
list.flatten(optional_depth) method...


(Reposted with slightly better formatting. I&#39;v...
-----------------------------------------------------

Chris Leary<noreply@blogger.com>

2009-10-08 18:14:43.601000-04:00

(Reposted with slightly better formatting. I've made a mental note that
typing
reStructuredText into arbitrary text boxes doesn't usually end well.)
People were extremely defensive about this post for some reason. I think
it's an excellent point -- if you don't need the nested structure for
something else, you should be creating a flat sequence to begin with.
As a corollary, you may prefer a for-loop to a list comprehension if you
use a transform function that creates a list, but want a flattened
result at the end. For example,

::

    flat = []
    for item in seq:
        flat += transform(item)

As preferable to:

::

    nested = (transform(item) for item in seq)
    flat = itertools.chain.from_iterable(nested)

The former certainly gets the point across with less jargon, if
\``nested`\` is created by you (as opposed to being passed in from
elsewhere).


Naive indeed.  Besides the nested version being us...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-10-06 12:04:53.652000-04:00

Naive indeed. Besides the nested version being useful as well, what
about working with data structures that one didn't create. :/
Uninspired.


I often have lists of objects each of which has an...
-----------------------------------------------------

Noufal<noreply@blogger.com>

2009-10-06 13:43:13.736000-04:00

I often have lists of objects each of which has an attribute which holds
a list of different objects. This is nested list like situation which I
can flatten using minor alterations to the solutions provided on Stack
Overflow. I don't think your suggestion would apply here.
OTOH, I've generally noticed that extend is used a lot lesser than
append.


@Michael: Are you sure it creates intermediate lis...
-----------------------------------------------------

Theran Cochran<noreply@blogger.com>

2009-10-07 02:44:38.313000-04:00

@Michael: Are you sure it creates intermediate lists? After testing in
Python 2.6.2, the += operator extends the existing list, and does not
create a new one. The id() of the list does not change at any point in
the loop. However, if you write 'L = L + newitems' you do indeed get a
bunch of new objects.


Putting nesting aside, I find myself using the fol...
-----------------------------------------------------

Michael Watkins<noreply@blogger.com>

2009-10-06 15:38:56.108000-04:00

Putting nesting aside, I find myself using the following rather than
[].extend([]):
>>> L = [1,2,3]
>>> L += [4,5,6]
>>> L
[1, 2, 3, 4, 5, 6]


@Nacho

Your list comprehension is, in effect, doi...
-----------------------------------------------------

Wyatt<noreply@blogger.com>

2009-10-11 15:44:43.690000-04:00

@Nacho
Your list comprehension is, in effect, doing an append. You should just
use a normal loop:
row = [...]
stuff = []
for item in row:
....stuff += item.split('+-')
Reusing the name row isn't saving you anything, and this version is
clearer, \*and\* it gets you what you want.



Chris Leary<noreply@blogger.com>

2009-10-08 18:12:08.065000-04:00

This comment has been removed by the author.


@Michael Watkins: I would be careful about getting...
-----------------------------------------------------

Michael<noreply@blogger.com>

2009-10-06 16:38:49.660000-04:00

@Michael Watkins: I would be careful about getting into that habit. If
you do that in a loop, you create a bunch of intermediate lists and
it'll get slow really fast.





