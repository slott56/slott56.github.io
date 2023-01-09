Pythonic vs. "Clean"
====================

:date: 2010-11-04 08:00
:tags: #python
:slug: 2010_11_04-pythonic_vs_clean
:category: Technologies
:status: published

This provokes thought:
"`Pythonic <http://nedbatchelder.com/blog/201011/pythonic.html>`__".

Why does Python have a "Pythonic" style? Why not "clean"?

Is it these lines from Tim Peters' "The Zen of Python" (a/k/a import
this)


       There should be one-- and preferably only one --obvious way to do it.

       Although that way may not be obvious at first unless you're Dutch.

Perhaps having a `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`__, a
`BDFL <http://en.wikipedia.org/wiki/Guido_van_Rossum>`__ (and
`FLUFL <http://www.python.org/dev/peps/pep-0401/>`__) means that
there's a certain "pressure" to conform?

Or do we have higher standards than other languages? Or less
intellectual diversity?

I think that "pythonic" is just a catchy phrase that rolls off the
tongue. I think a similar concept exists in all languages, but there
isn't a good phrase for it in most other languages. Although Ned
Batchelder has some really good suggestions. (Except for C++, which
should be "C-Posh-Posh" for really good coding style.)

**History**

When I was a COBOL programmer, there were two buzz-phrases used.
"Clean" and "Structured". Clean was poorly-defined and really just a
kind of cultural norm. In those days, each shop had a different
opinion of "clean" and the lack of widespread connectivity meant that
each shop had a more-or-less unique style. Indeed, as a traveling
consultant, I helped refine and adjust those standards because of the
wide variety of code I saw in my travels.

"Structured" is pretty much an absolute. Each GOTO-like thing had to
be reworked as properly nested IFs or PERFORMs. No real issue there.
Except from folks who argued that "Structured" was slower than
non-Structured. A load of malarkey, but one I heard remarkably often.

When I was a Fortran (and Ada) programmer, I worked for the military
in which there were simply absolute standards for every feature of
the source code. Boring. And no catchy buzz-word. Just "Compliant" or
"Wrong".

Since it was the early '90's (and we were sequestered) we didn't have
much Internet access. Once in a while we'd have internal discussions
on style where the details weren't covered by any standard. Not
surprisingly, they amounted to "`Code Golf <http://codegolf.com/>`__"
questions. Ada has to be perfectly clear, which can be verbose, and
some folks don't like clarity.

When I become a C programmer, I found a Thomas Plum's `Reliable Data Structures in C <http://www.amazon.com/Reliable-Data-Structures-Thomas-Plum/dp/091153704X>`__.
That provided a really good set of standards. The buzzword I used was
"Reliable".

The problem with C programming is that "Clean" and "Code Golf" get
conflated all the time. Folks write the craziest crap, claim it's
"clean" and ignore the resulting obscurity. Sigh. I wish folks with
stick with "Reliable" or "Maintainable" rather than "Clean".

While doing Perl programming I noticed that some folks didn't seem to
realize the golden rule.

  **No One Wins At Code Golf**

I don't know why. Other than to think that some folks felt that Perl
programs weren't "real" programs. They were just "scripts" and could
be treated with a casual contempt.

When I learned Java, I noted that an objective was to have a syntax
that was familiar. It was a stated goal to have the Java style
guidelines completely overlap with C and C++ style guidelines. Fair
enough. Doesn't solve the "Code Golf" vs. "Clean" problem. But it
doesn't confound it with another syntax, either.

**Python**

From this history, I think that "Pythonic" exists because we have a
BDFL with high standards.





