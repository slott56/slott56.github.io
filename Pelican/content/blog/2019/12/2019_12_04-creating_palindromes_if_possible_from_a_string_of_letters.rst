Creating Palindromes -- if possible -- from a string of letters.
================================================================

:date: 2019-12-04 19:07
:tags: #python
:slug: 2019_12_04-creating_palindromes_if_possible_from_a_string_of_letters
:category: Technologies
:status: published


This can be an interesting exercise. I think it is something that can
help people learn to code well. I found this in the LinkedIn Python
community:  https://www.linkedin.com/groups/25827/.





The Palindrome Problem:

   Make a function that makes a palindrome out of the letters in a
   string and
   returns -1 if this is not possible.
   Convert a list of strings with the function.


   Some test cases:


    ::

        >>> palify('eedd')
        'edde' (or 'deed')
        >>> palify('wgerar')
        >>> palify('uiuiqii')
        'uiiqiiu' or several similar variants.


Let's not get too carried away. I like \*some\* of this problem.

I don't like the idea of Union[str, int] as a return type from this
function. Yes, it's valid Python, but it seems like a code smell.
Since the intent is to build lists, a None would be more sensible than
a number; we'd have Optional[str] which seems better overall.

The solution that was posted was interesting. It did way too much
work, but it was acceptable-looking Python. (It started with a big
block comment with "#" on each line instead of a docstring, so...
there were minor style problems, but otherwise, it was not bad.)

Here's what popped into my head, to act as a concrete response to the
request for comments.

::

   """
   Make a function that makes a palindrome out of the letters in a string and
   returns -1 if this is not possible.
   Convert a list of strings with the function.
   Some test cases:

   >>> palify('eedd')
   'edde'
   >>> palify('wgerar')
   >>> palify('uiuiqii')
   'uiiqiiu'
   """
   from typing import Optional, Set


   def palify(source: str) -> Optional[str]:
       """Core palindromic conversion."""
       singletons: Set[str] = set()
       pairs = list()
       for c in source:
           if c in singletons:
               pairs.append(c)
               singletons.remove(c)
           else:
               singletons.add(c)

       if pairs and len(singletons) <= 1:
           # presuming a single letter can't be palindromic.
           return ''.join(pairs+list(singletons)+pairs[::-1])
       return None

   if __name__ == "__main__":
       s =  ['eedd', 'wgerar', 'uiuiqii']
       p = list(map(palify, s))
       print(f"from {s=}, we get {p=}")




The core problem statement is interesting. And the ancillary
requirement is almost as interesting as the problem.

The simple-seeming "Make a palindrome out of the letters of the
string" has two parts. First, there's the question of "can it even
become a palindrome"? Which implies validating the source data against
some set of rules. After that, we have to emit one of the many
possible palindromes from the source material.

The original post had a complicated survey of the data. This was
followed by an elegant way of creating a palindrome from the survey
data. Since we're looking for a bunch of pairs and a singleton, I
elided the more complex survey and opted to collect pairs and
singletons into two separate collections.

When we've consumed the input, we will have partitioned the characters
into their two pools and we can decide if the pools have the right
sizes to proceed. The emission of the palindrome is a lazy assembly of
the resulting data, first as a list, and then transformed to a single
string.

The ancillary requirement is interesting in its own right. When a
bundle of letters can't form a palindrome, that seems like a
ValueError exception to me. Doing bulk transformations in the presence
of ValueErrors seems wrong-ish. I already griefed about the -1
response above: it seems very bad. A None is less bad than -1. An
Exception, however, seems like a more right thing to do.

Code Review Response
--------------------


I think my response to the original code should be follow-up questions
on why a defaultdict(int) was used to survey the data in the first
place. A Counter() is a better idea, and requires less code.

The survey involved trying to locate singletons -- a laudable goal.
There may have been a better approach to looking for the presence of a
singleton letter in the Counter values.

More fundamentally, there are few states for each letter. There are
two stark algorithmic choices: a structure keyed by letter or
collections of letters. I've shown the collections, and hinted at the
collection. The student response used a collection.

I think this problem serves as a good discussion for algorithmic
alternatives. The core problem of detecting the possibility of
palindromicity for a bunch of letters is cool. There are two choices.
The handling of the exceptional case (-1, None or ValueError) is
another bundle of choices.





