Why Isn't COBOL Dead? Or Why Didn't It Evolve?
==============================================

:date: 2020-04-07 21:07
:tags: COBOL,#python,fortran
:slug: 2020_04_07-why_isnt_cobol_dead_or_why_didnt_it_evolve
:category: Technologies
:status: published

| Here's part of the question:

   Why didn't COBOL evolve more successfully?

..

   FORTRAN, OTOH, has survived precisely because it--and more
   importantly, related tools, esp compilers--has evolved to
   solve/overcome many (certainly not all!) of the sorts of pain-points
   you describe, while retaining the significant performance edge that
   (IMHO, ICBW) prevents challengers (e.g., Python) from dislodging it
   for tasks like (e.g.) running dynamical models (esp weather
   forecasting).

| In short, why is FORTRAN still OK? Why is COBOL not still OK?
| Actually, I'd venture to say the stories of these languages are
  essentially identical. They're both used because they have significant
  legacy implementations.
| There's a distinction, that I think might be relevant to the
  "revulsion factor."
| Folks don't find Fortran quite so revolting because it's sequestered
  into libraries where we don't really have to look at it. It's often
  wrapped into SciPy. The GCC compiler system handles it and we're
  happy.
| COBOL, however, isn't sequestered into libraries with tidy Python
  wrappers and Conda installers. COBOL is the engine of enterprise
  applications.
| Also. COBOL is used by organizations that suffer from high amounts of
  technical inertia, which makes the language a kind of bellwether for
  the rest of the organization. The organization changes slowly (or not
  at all) and the language changes at an even more tectonic pace.
| This is a consequence of very large organizations with regulatory
  advantages. Governments, for example, regulate themselves into
  permanence. Other highly-regulated industries like banks and insurance
  companies can move slowly and tolerate the stickiness of COBOL.
| Also.
| For a FORTRAN library function that does something useful, it's not
  utterly mysterious. There's often a crisp mathematical definition, and
  a way to test the implementation. There are no quirks.
| For a COBOL program that does something required by law, there can
  still be absolutely opaque mysteries and combinations of features
  without acceptable unit test cases. This isn't for lack of trying.
  It's the nature of "application" vs. "subroutine."
| The special case and exceptions have to live somewhere. They live in
  the application.
| For FORTRAN, the exceptions are in the Python wrapper using numpy
  using FORTRAN.
| For COBOL, the exceptions are in the COBOL  Somewhere.



-----

&gt; COBOL is used by organizations that suffer fr...
-----------------------------------------------------

Tom Roche<noreply@blogger.com>

2020-04-08 00:15:25.622000-04:00

> COBOL is used by organizations that suffer from high amounts of
technical inertia, which makes the language a kind of bellwether for the
rest of the organization. [...] This is a consequence of very large
organizations with regulatory advantages.
I misspent the mid-noughties at a Giant Acronym for which banks are a
major [host](https://en.wikipedia.org/wiki/Host_(biology)) genus. While
there, I'm fairly sure I heard at least 3 different versions of [this
post's
predecessor](https://slott-softwarearchitect.blogspot.com/2020/04/the-cobol-problem.html),
all given by quasi-academic manager/mandarins sufficiently
up-the-food-chain that junior/grunt software engineers (like me) were
paid to Sit and Listen (and eat snacks :-) My group built IDEs designed
to make big bucks [^Hx14] help bankers wrap, refactor, and ultimately
replace their COBOL.
(I also once heard it said there--I have no idea if it's true, or who
has ever studied this sort of thing--that CICS is the single most
profitable piece of software ever written. And still earning.)
My impression (from a long spatiotemporal distance, and which again is
open to your empirical correction) is, banks \*did\* lotsa
better-engineered wraps and extensions. But when it came to getting
dirty with the COBOL base, banks just maintained, because offshoring
was--and, IIUC, remains--sooo much cheaper. Not just because Indians (et
al) cost less, but also because they were/are the only folks getting
trained in not just COBOL but the whole 370-390-Z ecosystem.
So my guess (YMMV) is, no change until boolean-OR (1) cheap labor gets
lots less cheap (2) governments/quangos (e.g., standards organizations)
with teeth start regulating software the way they currently do other
economically-significant products. But I'd be interested to read your
2030 followup on this topic ... presuming we all get there :-)


Just noting that this opinion piece was especially...
-----------------------------------------------------

crsevern<noreply@blogger.com>

2020-04-10 14:08:16.605000-04:00

Just noting that this opinion piece was especially topical for me as I
embark on trying to wrap a Medicare COBOL program in Python. No way I'm
touching the COBOL source.





