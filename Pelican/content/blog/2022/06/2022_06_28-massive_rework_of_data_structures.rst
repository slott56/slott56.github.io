Massive Rework of Data Structures
=================================

:date: 2022-06-28 08:00
:tags: Test-Driven Development,#python,pyWeb
:slug: 2022_06_28-massive_rework_of_data_structures
:category: literate programming
:status: published

As noted in `My Shifting Understanding and A Terrible Design
Mistake <{filename}/blog/2022/06/2022_06_21-my_shifting_understanding_and_a_terrible_design_mistake.rst>`__,
I had a design that focused on serialization instead of proper modeling
of the objects in question.

Specifically, I didn't start with a suitable abstract syntax tree (AST)
structure. I started with an algorithmic view of "weaving" and
"tangling" to transform a WEB of definitions into documentation and
code. The weaving and tangling are two of the three distinct
serializations of a common AST.

The third serialization is the common source format that underpins the
WEB of definitions. Here's an example that contains a number of
definitions and a tangled output file.

::

   Fast Exponentiation
   ===================

   A classic divide-and-conquer algorithm.

   @d fast exp @{
   def fast_exp(n: int, p: int) -> int:
       match p:
           case 0: 
               return 1
           case _ if p % 2 == 0:
               t = fast_exp(n, p // 2)
               return t * t
           case _ if p % 1 == 0:
               return n * fast_exp(n, p - 1)
   @| fast_exp
   @}

   With a test case.

   @d test case @{
   >>> fast_exp(2, 30)
   1073741824
   @}

   @o example.py @{
   @< fast exp @>

   __test__ = {
       "test 1": '''
   @< test case @>
       '''
   }
   @| __test__
   @}

   Use ``python -m doctest`` to test.

   Macros
   ------

   @m

   Names
   -----

   @u

This example uses RST as the markup language for the woven document. A
tool can turn this simplified document into complete RST with
appropriate wrappers around the code blocks. The tool can also weave the
``example.py`` file from the source document.

The author can focus on exposition, explaining the algorithm. The reader
gets the key points without the clutter of programming language
overheads and complications.

The compiler gets a tangled source.

The key point is to have a tool that's (mostly) agnostic with respect to
programming language and markup language. Being fully agnostic isn't
possible, of course. The ``@d name @{code@}`` constructs are transformed
into markup blocks of some sophistication. The ``@<name@>`` becomes a
hyperlink, with suitable markup. Similarly, the cross
reference-generating commands, ``@m`` and ``@u``, generate a fair amount
of markup content.

I now have Jinja templates to do this in RST. I'll also have to provide
LaTeX and HTML. Further, I need to provide generic LaTeX along with
LaTeX I can use with PacktPub's LaTeX publishing pipeline. But let's not
look too far down the road. First things first.

TL;DR
-----

Here's today's progress measurement.

::

   ==================== 67 failed, 13 passed, 1 error in 1.53s ====================

This comforts me a great deal. Some elements of the original structure
still work. There are two kinds of failures: new test fixtures that
require ``TestCase.setUp()`` methods, and tests for features that are no
longer part of the design.

In order to get the refactoring to a place where it would even run, I
had to incorporate some legacy methods that -- it appears -- will
*eventually* become dead code. It's not totally dead, yet, because I'm
still mid-way through the refactoring.

But. I'm no longer beating back and forth trying to see if I've got a
better design. I'm now on the downwind broad reach of finding and fixing
the 67 test cases that are broken.





