How to Write Crummy Requirements
================================

:date: 2012-06-28 08:00
:tags: requirements,use case,LaTeX,user stories
:slug: 2012_06_28-how_to_write_crummy_requirements
:category: Architecture & Design
:status: published

Here's an object lesson in bad requirements writing.

    "Good" is defined as a nice simple and intuitive GUI interface. I
    would be able to just pick symbol from a pallette and put it
    somewhere and the software would automatically adjust the spacing.

Some problems.


#.  **Noise words**.  Phrases like "'Good' is defined as" don't
    provide any meaning.  The word "just" and "automatically" are
    approximately useless.  Here is the two-step test for noise words.

    1.  Remove the word and see if the meaning changed.

    2.  Put the opposite and see if the meaning changed.  If you can't find a
        simple opposite, it's noise of some kind.  Often it's an empty
        tautology, but sometimes it's platitudinous buzzwords.

#.  **Untestable requirements**.  "nice, simple and intuitive" are
    unqualified and possible untestable.  If it's untestable, then
    everything meets the criteria (or nothing does.)  Elegant.  State
    of the art.  Again, apply the reverse test:  try "horrid, complex
    and counter-intuitive" and see if you can find that component.
    No?  Then it's untestable and has no place.

#.  **Silliness**.  "GUI".  It's 2012.  What non-GUI interfaces are
    left?  Oh right.  The GNU/Linux command line.  Apply the reverse
    test: try "non-GUI" and see if you can even locate a product.
    Can't find the opposite?  Don't waste time writing it down.


What's left?

  pick symbol from a palette ... the software would ... adjust the
  spacing.

That's it.  That's the requirement.  35 words that mean "Drag-n-Drop
equation editing".

I have other issues with requirements this poorly done.  One of my
standard complaints is that no one has actually talked to actual
users about their actual use cases.  In this case, I happen to know
that the user did provide input.

Which brings up another important suggestion.

-  Don't listen to the users.

By that I mean "Don't **passively** listen to the users **and
blindly write down all the words they use**.  They're often
uninformed."  It's important to **understand** what they're
talking about.  The best way to do this is to actually do their
job briefly.  It's also important to provide demos, samples,
mock-ups, prototypes or concrete examples.  It's 2012.  These
things are inexpensive nowadays.


In the olden days we used to carefully write down all the users
words because it would take months to locate a module, negotiate a
contract, take delivery, install, customize, integrate, configure
and debug.  With that kind of overhead, all we could do was write
down the words and hope we had a mutual understanding of the use
case.  [That's a big reason for Agile methods, BTW:  writing down
all the user's words and hoping just doesn't work.]


In 2012, you should be able to download, install and play with
candidate modules in *less* time than it takes to write down all
the user's words.  Often *much less* time.  In some cases, you can
install something that works before you can get the users to
schedule a meeting.


And that leads to another important suggestion.

-  Don't fantasize.


Some "Drag-n-Drop" requirements are simple fantasies that
ignore the underlying (and complex) semantic issues.  In this
specific example, equations aren't random piles of mathematical
symbols.  They're fairly complex and have an important semantic
structure.  Dragging a ∑ or a √ from a palette will be
unsatisfying because the symbol's semantics are *essential* to
how it's placed in the final typeset equation.


I've worked recently with some folks that are starting to look at
`Hypervideo <http://en.wikipedia.org/wiki/Hypervideo>`__.  This is
often unpleasantly difficult to write requirements around because
it *seems* like simple graphic tools would be all that's required.
A lesson learned from Hypertext editors (even good ones like
`XXE <http://www.xmlmind.com/xmleditor/>`__) is that "WYSIWYG"
doesn't apply to semantically rich markup.  There are nesting and
association relationships that are no fun to attempt to show
visually.  At some point, you just want to edit the XML and be
done with it.


Math typesetting is has deep semantics.
`LaTeX <ftp://ftp.ams.org/ams/doc/amsmath/short-math-guide.pdf>`__
captures that semantic richness.


It's often best to use something like
`LaTeXiT <http://pierre.chachatelier.fr/latexit/>`__ rather than
waste time struggling with finding a Drag-n-Drop tool that has
appropriate visual cues for the semantics.  The textual rules for
LaTeX are simple and—most importantly—fit the mathematical
meanings nicely.  It was invented by mathematicians for
mathematicians.



-----

"invented by mathematicians for mathematician...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-06-28 18:55:39.370000-04:00

"invented by mathematicians for mathematicians"
So what are non-mathematicians suppose to do?
"WYSIWYG doesn't apply to semantically rich markup"
Very well put!


&quot;So what are non-mathematicians suppose to do...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2012-07-04 22:44:18.925000-04:00

"So what are non-mathematicians suppose to do?" Either learn some math
or stop trying to write equations.





