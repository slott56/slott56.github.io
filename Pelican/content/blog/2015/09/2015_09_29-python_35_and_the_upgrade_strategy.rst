Python 3.5 and the Upgrade Strategy
===================================

:date: 2015-09-29 08:00
:tags: #python
:slug: 2015_09_29-python_35_and_the_upgrade_strategy
:category: Technologies
:status: published

Start here: https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-484

While new syntax is important, remember your audience in pitching the
upgrade from Python 2.7. You may need to pander to people who aren't
programmers or don't really know Python.

When selling the upgrade, it can help to focus on the objective
measures.

#. **Performance**. When anyone asks why we should disturb our precious
   Python 2 ecosystem, point out the performance improvements. Begin
   with Python 3.2, 3.3, 3.4, and then 3.5 improvements. The union of
   these is an impressive list. Faster is better, right?

#. **New Libraries**. For some folks who don't know Python well, it
   helps to give them a concrete list of features you absolutely
   require. Seriously. Enumerate **all** the new libraries from Python
   3.2, ..., 3.5. It's a big list. Some of them have been backported, so
   this list isn't a a complete win. You may not really need all of
   them, but use them to bolster your case.

#. **Other Cleanups**. These are important for folks who use Python
   daily, but aren't too impressive to manager types who aren't deeply
   into the language details.

   #. The fact that Python 3 handles class/type better than Python 2
      isn't impressive to anyone who hasn't dealt with it.
   #. The fact that Python 3 handles Unicode better than Python 2 isn't
      going to impress too many people, either.
   #. The **print** statement issue will cause some managers to claim
      that the upgrade is "risky".
   #. The division issue is a complete win. Weirdly, nay-sayers will
      claim (a) just use float() a lot, (b) just add +0.0 a lot, or (c)
      just add from \__future_\_ import division a lot.  How is this
      workaround better? No clue. Be prepared to make the case that the
      dumb workarounds are... well... dumb.

You can lift up the type definition and
`http://mypy-lang.org <http://mypy-lang.org/>`__. If you do, be
prepared for snark from the Java/Scala crowd. These folks will
(wrongly) claim that a partial type proof is useless, and static type
checking is mandatory. This is a difficult discussion to have because
the "type safety is important" crowd don't seem to recognize the
awful gyrations they're forced into so they can write generic code
that's type-agnostic. All Python code is type-agnostic; the type
checking just confirms some design constraints. The presence of
differing strategies -- type-specific code vs. generic type-agnostic
code -- means that neither is right, and the argument is moot.

Don't focus on async/await. Yes, it's first on the Python web site,
but, it can be a tough sell.

.. rubric:: Performance
      :name: performance

The easy sell is this impressive list of optimizations.

3.2

   -  Peephole optimizer improvements

   -  Serializing and unserializing data using the pickle module is now
      several times faster.

   -  The Timsort algorithm used in list.sort() and sorted() now runs
      faster and uses less memory when called with a key function.

   -  JSON decoding performance is improved and memory consumption is
      reduced whenever the same string is repeated for multiple keys.

   -  Recursive locks (created with the threading.RLock() API) now
      benefit from a C implementation which makes them as fast as
      regular locks, and between 10x and 15x faster than their previous
      pure Python implementation.

   -  The fast-search algorithm in stringlib is now used by the split(),
      splitlines() and replace() methods on bytes, bytearray and str
      objects. Likewise, the algorithm is also used by rfind(),
      rindex(), rsplit() and rpartition().

   -  Integer to string conversions now work two “digits” at a time,
      reducing the number of division and modulo operations.

   -  Several other minor optimizations.

      -  Set differencing now runs faster when one operand is much
         larger than the other
      -  The array.repeat() method has a faster implementation
      -  The BaseHTTPRequestHandler has more efficient buffering
      -  The operator.attrgetter() function has been sped-up
      -  ConfigParser loads multi-line arguments a bit faster

3.3

   -  Some operations on Unicode strings have been optimized
   -  UTF-8 is now 2x to 4x faster. UTF-16 encoding is now up to 10x
      faster.


3.4

      -  The UTF-32 decoder is now 3x to 4x faster.
      -  The cost of hash collisions for sets is now reduced.
      -  The interpreter starts about 30% faster.
      -  bz2.BZ2File is now as fast or faster than the Python2 version
         for most cases. lzma.LZMAFile has also been optimized.
      -  random.getrandbits() is 20%-40% faster for small integers.
      -  By taking advantage of the new storage format for strings,
         pickling of strings is now significantly faster.
      -  A performance issue in io.FileIO.readall() has been solved.
      -  html.escape() is now 10x faster.

3.5

   -  The os.walk() function has been sped up by 3 to 5 times on POSIX
      systems, and by 7 to 20 times on Windows.
   -  Construction of bytes(int) (filled by zero bytes) is faster and
      uses less memory for large objects.
   -  Some operations on ipaddress IPv4Network and IPv6Network have been
      massively sped up,
   -  Pickling of ipaddress objects was optimized to produce
      significantly smaller output.
   -  Many operations on io.BytesIO are now 50% to 100% faster.
   -  The marshal.dumps() function is now faster: 65-85% with versions 3
      and 4, 20-25% with versions 0 to 2 on typical data, and up to 5
      times in best cases.
   -  The UTF-32 encoder is now 3 to 7 times faster.
   -  Regular expressions are now parsed up to 10% faster.
   -  The json.dumps() function was optimized.
   -  The PyObject_IsInstance() and PyObject_IsSubclass() functions have
      been sped up.
   -  Method caching was slightly improved, yielding up to 5%
      performance improvement in some benchmarks.
   -  Objects from random module now use two times less memory on 64-bit
      builds.
   -  The property() getter calls are up to 25% faster.
   -  Instantiation of fractions.Fraction is now up to 30% faster.
   -  String methods find(), rfind(), split(), partition() and in string
      operator are now significantly faster for searching 1-character
      substrings.


I think this list can help move an organization away from Python 2
and toward Python 3. This list and a lot of lobbying from folks
who know what the improvements are.

.. rubric:: Library
   :name: library

Here's the library upgrade list, FWIW.

-  3.2: https://docs.python.org/3.2/whatsnew/3.2.html#new-improved-and-deprecated-modules.
   I count 51 modules.

-  3.3:

  -  `New
     Modules <https://docs.python.org/3.3/whatsnew/3.3.html#new-modules>`__

     -  `faulthandler <https://docs.python.org/3.3/whatsnew/3.3.html#faulthandler>`__
     -  `ipaddress <https://docs.python.org/3.3/whatsnew/3.3.html#ipaddress>`__
     -  `lzma <https://docs.python.org/3.3/whatsnew/3.3.html#lzma>`__

  -  https://docs.python.org/3.3/whatsnew/3.3.html#improved-modules.
     60 improved.

-  3.4:

  -  `New
     Modules <https://docs.python.org/3.4/whatsnew/3.4.html#new-modules>`__

     -  `asyncio <https://docs.python.org/3.4/whatsnew/3.4.html#asyncio>`__
     -  `ensurepip <https://docs.python.org/3.4/whatsnew/3.4.html#ensurepip>`__
     -  `enum <https://docs.python.org/3.4/whatsnew/3.4.html#enum>`__
     -  `pathlib <https://docs.python.org/3.4/whatsnew/3.4.html#pathlib>`__
     -  `selectors <https://docs.python.org/3.4/whatsnew/3.4.html#selectors>`__
     -  `statistics <https://docs.python.org/3.4/whatsnew/3.4.html#statistics>`__
     -  `tracemalloc <https://docs.python.org/3.4/whatsnew/3.4.html#tracemalloc>`__

  -  https://docs.python.org/3.4/whatsnew/3.4.html#improved-modules.
     62 improved.

-  3.5:

  -  `New
     Modules <https://docs.python.org/3.5/whatsnew/3.5.html#new-modules>`__

     -  `typing <https://docs.python.org/3.5/whatsnew/3.5.html#typing>`__
     -  `zipapp <https://docs.python.org/3.5/whatsnew/3.5.html#zipapp>`__

  -  https://docs.python.org/3.5/whatsnew/3.5.html#improved-modules.
     2 new. 75 improved.

The details of the improvements can be overwhelming.
The dozen new modules, however, might help overcome organizational
inertia to make progress on ditching Python2. I've been making heavy
use of statistics. I need to make better use of pathlib in future
projects.




