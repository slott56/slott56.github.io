Learning about Python from Pharo
================================

:date: 2019-06-20 13:36
:tags: pharo,#python
:slug: 2019_06_20-learning_about_python_from_pharo
:category: Technologies
:status: draft


See https://blog.usejournal.com/python-vs-pharo-2c2c1a3b1afe for a
language description with a bunch of interesting anecdotes. The
context is comparing Pharo with Python. I'm not interested in which
language is **better**. I'm interested in the points used to describe
a language. Starting with these two:

-  **Simplicity, Conciseness, and Elegance**. This has an example with a
   number of syntax elements that fits on a postcard when rendered in a
   reasonable font. It's an interesting approach to asking people to
   read code and understand legibility.

-  **One-Liners**. While Code Golf is a game everyone loses at, the
   anecdotal value of one-liners may be important to some. A few of them
   seem interestingly difficult, and might serve as handy tutorials more
   than comparisons.

I'll return to these two topics below. I think they're interesting
and insightful ways to talk about a programming language.

The other points seem to fall into three major categories. I don't
want to sound like I'm debating these in any depth. Rather, I want to
look at them as ways to teach (and not teach) a programming language.

One point is commonly repeated and misleading. This doesn't seem
helpful.

-  "Off-side Rule" -- really a side-bar on how whitespace is called
   "controversial." Having helped a lot of people debug languages like C
   and C++, I can say people get whitespace correct more often than they
   get ;'s and {}'s correct. I'm going to ignore this complaint. It
   doesn't reflect the experienced reality of programming in Python.


A number of points labels an aspect of Python as bad. I'd rather
focus on what Pharo does right. While some of these are strawmen --
Python non-problems -- the topics seem potentially interesting. These
are things to be covered when teaching a language.

-  Object-oriented Programming. One detail (encapsulation) is lifted up
   as an indictment of the Python language. Setting that aside, the OOP
   features are important.

-  Functional Programming. Python's use of generators and immutable
   namedtuples makes this partially achievable. The itertools library
   covers a lot of territory.

-  IDE (integrated development environment). Not sure this is even part
   of the language, but Python has many IDE's.

-  Productivity and Ease of Development. This seems part of the previous
   point.

-  Multithreading. One detail is described as a problem for Python when
   -- in practice -- it isn't. Setting this aside, the covering
   something like the Dining Philosophers is always an important part of
   maximizing resource use through concurrency.


Also, an aspect of Python is identified good. That's cool.

-  Ecosystem.


I like this list as a jumping-off point for seven to nine key points
to cover. (I'd like to omit the two IDE-related considerations.)

Back to the first two kinds of examples: Simplicity (Syntax on a
Postcard) and One-Liners.

Postcard Syntax Summary
-----------------------


Here's the version from
GitHub: https://github.com/pavel-krivanek/pharoMaterials


This isn't precisely the version used in the Medium Post, but it will
do for our purposes.


   ::

       "A ""complete"" Pharo syntax"
       
       | y |

       true & false not & (nil isNil)
        ifFalse: [ self perform: #add: with: x ].

       y := thisContext stack size + super size.

       byteArray := #[2 2r100 8r20 16rFF].

       { -42 . #($a #a #'I''m' 'a' 1.0 1.23e2 3.14s2 1) } 
        do: [ :each |
         | var |
         var := Transcript 
          show: each class name;
          show: each printString ].

       ^ x < y


   The medium article presents this "You sure as hell can’t do that with
   Python!" which seems a little odd to me. The code and the example
   syntax for Python can be mashed onto a postcard. The details on the
   postcard itself indicate the syntax aren't really the complete Pharo
   language; a few features have been omitted. Omissions should be
   allowed for Python, also.

   This https://ci.inria.fr/pharo-contribution/job/UpdatedPharoByExample/lastSuccessfulBuild/artifact/book-result/SyntaxNutshell/SyntaxNutshell.html
   seems to be a useful syntax summary.

   If we take similar latitude with completeness for Python, we can fit
   a great deal of Python syntax onto a postcard. We can, for instance,
   translate this method definition. The notable gaps would be the
   ``import``, ``while`` and ``with`` statements. We'll get to those,
   later.

   ::

      def example_with_number(self, x):
          """A 'complete' Python Syntax"""
          if (not (True and False) and (None is None)):
              pass
          else:
              getattr(self, 'add')(with_=x)
          y = sys.getsizeof(traceback.extract_stack()) + sys.getsizeof(self)
          self.byte_array = bytes([2, 0b1100, 0o20, 0xff])
          for each in [-42, ('a', sys.intern('a'), sys.intern("I'm"), 'a', 1.23e2, Decimal('3.14'), 1)]:
              var = Transcript().show(each.__class__.__name__).show(str(each))
          return x < y

This covers the same, essential bases as the Pharo example.

-  method name
-  parameter
-  (There are no pragmas in Python, maybe a decorator would be the equivalent?)
-  comment
-  (Local variables aren't annotated in Python)
-  boolean literals
-  binary "message"
-  None literal
-  unary "message"
-  block
-  keyword "message"
-  "pseudo variables" (self, really, in Python)
-  assignment
-  instance variable
-  integer literals in various bases
-  array generated at runtime
-  (Characters aren't a distinct type in Python, so some of the example isn't helpful)
-  (Symbols are more-or-less interned strings in Python, and may not be relevant)
-  string
-  floating point
-  scaled decimal
-  iteration with a "block parameter"
-  global reference
-  (Python doesn't automatically cascade to create a fluent interface, but it's easy to implement.)
-  return


I think the point of the example is that Python does have more
language features than can be shown in a small example. Because
Pharo has fewer language features, the example has better
coverage. Whether some of the features (like symbols) are even
useful in Python is a separate question.


I do think this example is helps identify a focused subset of a
language for the first day of learning Python (or Pharo, or almost
any other OO language.)

I don't like the features shown, however. I think it's possible to
stick to 12 lines of code and cover a some more important points.

One Liners
----------


There are nine "one-liners" which show some strengths of Pharo. Most
of these are really interesting exercises. Let's begin.


Days Between Two Dates
-----------------------

   Here's the original:

::

   "Compute difference in days between two dates"
   ('2014-07-01' asDate - '2013/2/1' asDate) days


This is based in a string class which is aware of YMD format dates,
and is flexible with respect to punctuation.  Python datetime isn't
quite as clever as this string function.

We wind up with this, as a first pass.
::

      import datetime
      diff = (datetime.datetime.strptime('2014-07-01', '%Y-%m-%d') - datetime.datetime.strptime('2013/2/1', '%Y/%m/%d')).days
      print(f"days {diff}")

This is one line, but it misses some of the nuanced flexibility.

Really, we're talking about something more like this:

::

      import datetime
      import re
      strpymd = lambda text: datetime.datetime(*map(int, re.split(r'[/-]', text)))
      diff2 = (strpymd('2014-07-01') - strpymd('2013/2/1')).days
      print(f"days {diff2}")

This captures the essential simplicity by introducing a function to
Python that's effectively built-in to a Pharo class.

What we really want is this:
::

      import datetime
      import re

      class DateAwareStr(str):
          def asDate(self):
              return datetime.datetime(*map(int, re.split(r'[/-]', self)))

      diff3 = (DateAwareStr('2014-07-01').asDate() - DateAwareStr('2013/2/1').asDate()).days
      print(f"days {diff3}")


This captures the core simplicity of the Pharo string class. There's
an ``asDate()`` method we can use to parse certain common date
formats. We can imagine expanding ``asDate()`` to include more
flexibility in defining the punctuation rules.

      **Sidebar**.
      I'm not a fan of this implementation. The binding to the
      ``datetime.datetime`` class also needs to be exposed. The Pharo
      approach is elegantly succinct, but lacks needed flexibility. I
      suppose monkeypatching or perhaps traits might be useful here.

This problem is excellent as an introduction to the ``datetime``
module. I think I'm going to use this a lot for tutorials and
code-dojo examples.

Weekday of a date
-----------------

This is similar to the previous one-liner. Here's the original:
::

      "Return the weekday of a date"
      '2013/5/7' asDate dayOfWeekName

Pretty slick, right?

Here's one Python version:
::

      from calendar import day_name
      dow = datetime.datetime.strptime('2013/5/7', '%Y/%m/%d').weekday()
      print(f"weekday {dow} {day_name[dow]}")

Another Python version reuses the ``DateAwareStr`` class defined
above:

::

      dow2 = DateAwareStr('2013/5/7').asDate().weekday()
      print(f"weekday {dow2} {day_name[dow2]}")

The first example shows how Python can be exactly as one-liney as
Pharo, when the feature is part of the standard library.

The second example uses a subclass of ``str`` to provide a very
Pharo-like implementation. As noted above, there's a too-strong
binding between ``str`` and ``datetime`` in the ``DateAwareStr``
class.

Leap Years
----------

This is a little trickier than the previous date-processing examples.
What's trickier is knowing the standard library.

Here's the original:
::

      "Count the number of, or show the leap years between two years"
      (1914 to: 1945) count: [ :each Year isLeapYear: each ].
      (1895 to: 1915) select: [ :each Year isLeapYear: each ].

Here's a python version:
::

      from calendar import isleap
      c = sum(isleap(y) for y in range(1914, 1946))
      s = list(y for y in range(1895, 1916) if isleap(y))
      print(f"Leaps from 1914-1964 = {c}")
      print(f"Leaps from 1895-1916 = {s}")

It's very cool that Python's generator expressions are every bit as
powerful as Pharo. The syntax is different, but, not dramatically
more complex.

String Reformatting
--------------------

Here's the original:

::

   "Split a string on dashes, reverse the order of the elements and join them using slashes"
   $/ join: ($- split: '1969-07-20') reverse

This can be done in a very similar style in Python:

::

   r = '/'.join(reversed('1969-07-20'.split('-')))
   print(f"reversed {r}")


This example of parsing and rebuildinga  string is what made me think
  a collection of these "one-liners" is a helpful thing to give to
  students.

Unicode Encoding
~~~~~~~~~~~~~~~~

Here's the original:

::

   "Encode the same string using Latin1, UTF-8 and UTF-16"
   #(latin1 utf8 utf16) collect: [ :each 

     (ZnCharacterEncoder newForEncoding: each)
       encodeString: 'Les élèves Français' ]


The Python version is also very short:

::

   encoded = ('Les élèves Français'.encode(encoding) for encoding in ('latin1', 'utf8', 'utf16'))


Python seems simpler because we can encode the string as a whole
instead of encoding each individual character.

This is a generator expression. We can't simply ``print(encoded)``. We
need to use ``print(list(encoded))``.

Obscure Data Formats
~~~~~~~~~~~~~~~~~~~~

This seems to be an unusual example. Perhaps it seems unusual to me
because I've spent so long doing big data/data science work where
parsing blocks of bytes is a rarity.

This problem requires knowing some obscure corners of the Python
standard library.

Here's the original:

::

   "Extract a Unix format timestamp from the 5th to 8th byte of a byte array given in hex"
   DateAndTime fromUnixTime:
     ((ByteArray readHexFrom: 'CAFEBABE4422334400FF') 
         copyFrom: 5 to: 8) asInteger


Here's a Python version:

::

   import binascii
   import struct
   import datetime

   packed = struct.pack('10B', *binascii.unhexlify('CAFEBABE4422334400FF'))
   data = struct.unpack('4xI2x', packed)
   ts = datetime.datetime.fromtimestamp(data[0])
   print(f"timestamp {ts}")


I didn't cram the whole thing onto one line, but it certainly can be
done as a single, long expression. The liberal use of ()'s means line
breaks won't matter.

The presence of the ``binascii`` module in the standard library isn't
widely known. But. If we hand this out as a hint to new learners, it
can show how important it is to understand Python's standard library.

   **Sidebar**.
   The pack-unpack pattern is something that I have a weak objection to.
   It fits here, but I prefer doing this as an arithmetic operation on
   the byte values and ignore the details of how the bytes form a 32-bit
   integer.
   ``dt = (((b[7]*256)+b[6])*256+b[5])*256+b[4]``

HTTP Server
~~~~~~~~~~~

This example is the Pharo code to create a simple HTTP server.

::

   "Set up an HTTP server that returns the current timestamp"
   (ZnServer startDefaultOn: 8080) 
     onRequestRespond: [ :request
       ZnResponse ok: (ZnEntity with: DateAndTime now printString) ]


The Python code based on the standard library is not comparable at
all.

::

   import datetime
   import http.server
   from http import HTTPStatus
   class TimeHandler(http.server.SimpleHTTPRequestHandler):
       def do_GET(self):
           now_text = datetime.datetime.now().isoformat()
           self.send_response(HTTPStatus.OK)
           self.send_header('Content-Type', 'text/plain')
           self.end_headers()
           self.wfile.write(now_text.encode('utf-8'))

   server = http.server.HTTPServer(('localhost', 8080), TimeHandler)



This reveals the possibility of adding a pleasant wrapper to
http.server to permit Pharo-like simplicity. The step-by-step handling
of a simple response seems to be superficially more complex than the
Pharo example.

One choice is a method to write a textual response with any of the
common MIME types like ``text/plain``, ``text/html``,
``application/json``, ``application/yaml``, and ``application/csv``.

Another choice is to create a class similar to the Pharo ``ZnEntity``
class to contain status, headers, and body. Then, a subclass of
``SimpleHTTPRequestHandler`` can return this entity object using
step-by-step operations.

HTTP Client
~~~~~~~~~~~

This example is the Pharo code to create a simple HTTP client.


::

  "Save the HTML source of a web page to a file"
  'http://www.pharo.org' asUrl saveContentsToFile: 'page.html'


Here's the Python version of a simple HTTP client.


::

      import urllib.request
      import pathlib
      with urllib.request.urlopen('http://www.pharo.org') as source:
          with pathlib.Path('page.html').open('wb') as target:
              target.write(source.read())



This is not a one-liner. It relies on the ``with`` statements to be sure
the resources are properly closed and released when the operation
completes.

Here's another Python version of a simple HTTP client as a one-liner.


::

      import urllib.request
      import pathlib
      (open("page.html", "wb")
          .write(
              urllib.request.urlopen('http://www.pharo.org').read()
          )
      )


This is likely to close files when it's finished processing. However,
  an exception may leak an open network connection or an open file (or
  both.)

Prime Testing
~~~~~~~~~~~~~

The final example we'll look at is a Pharo example to sum primes.
Here's the Pharo version:

::

   "Sum of the primes up to 64"
   (Integer primesUpTo: 64) sum




The code relies on prime-testing features in Pharo integers. The
``primesUpTo:`` method does a lot of processing by default.

Here's one variation in Python with an extra function for prime
testing.

::

   import math
   from functools import lru_cache

   @lru_cache()
   def prime(x):
       if x >= 4 and x % 2 == 0: return False
       for p in range(3, int(1+math.sqrt(x)), 2):
           if x % p == 0: return False
       return True

   sp_64 = sum(p for p in range(2, 64) if prime(p))
   print(f"prime sum {sp_64}")




This combines an external function -- ``prime()`` -- into a generator
expression to emit primes. The ``prime()`` function is fairly complex,
not a one-liner at all.

Here's a slightly more sophisticated generator function.

::

   def primes_up_to(x):
       for i in range(2, x):
           if prime(i):
               yield i

   sp_64_b = sum(primes_up_to(64))
   print(f"prime sum {sp_64_b}")




This leads to a slightly simpler ``primes_up_to()`` generator
function. It's still outside any existing class. We can extend the
``int`` class like this.

::

   class PrimeAwareInt(int):

       def _check(self, n=3):
           if n * n > self: return True
           if self % n == 0: return False
           return self._check(n + 2)

       def prime(self):
           if self in (2, 3): return True
           if self % 2 == 0: return False
           return self._check()




The ``prime()`` method definition gives us a simple "is this prime?"
test. This isn't an ideal approach because we can't easily cache the
common prime values the way the stand-alone ``prime()`` function
worked.

Once we have a simple ``prime()`` method for an ``int`` object, we can
create a prime-aware function based on the ``range()`` object.

::

   PrimeAwareRange = lambda stop: (PrimeAwareInt(x) for x in range(2, stop))
   sp_64_c = sum(p for p in PrimeAwareRange(64) if p.prime())
   print(f"prime sum {sp_64_c}")




This ``PrimeAwareRange()`` object takes a "stop" value and emits prime
values up to the given limit. Because ranges in Python do \*not\*
include the given value, this isn't \*exactly\* like the Pharo
version.

In Python, the range() object is not a first-class part of the int
class, but is a separate class.

One-Liner Exercises
-------------------


Here's the short list, organized around some general principles I
  think I saw:

-  Date Processing
   -  "Compute difference in days between two dates"
   -  "Return the weekday of a date"
   -  "Count the number of, or show the leap years between two years"

-  String Wrangling
   -  "Split a string on dashes, reverse the order of the elements and join them using slashes"
   -  "Encode the same string using Latin1, UTF-8 and UTF-16"
   -  "Extract a Unix format timestamp from the 5th to 8th byte of a byte array given in hex"

-  HTTP/RESTful API
   -  "Set up an HTTP server that returns the current timestamp"
   -  "Save the HTML source of a web page to a file"

-  Basic Number Theory
   -  "Sum of the primes up to 64"


I think we need some one-liners related to the following topics:


-  float processing
-  list processing
-  dict processing
-  set processing


Once we get outside the built-in data structures, we get beyond
things that can be done as one-liners. But the philosophy of
leveraging the built-in data structures seems to be really
essential.





