Literate Programming
====================

:date: 2010-03-14 12:02
:tags: open source,#python,literate programming
:slug: 2010_03_14-literate_programming
:category: Technologies
:status: published

About a decade ago, I discovered the concept of Literate Programming.
It's seductive. The idea is to write elegant documentation that embeds
the actual working code.

For tricky, complex, high-visibility components, a literate
programming approach can give people confidence that the software
actually works as advertised.

I actually wrote my own Literate Programming tool. Amazingly, someone
actually cared deeply enough to send me a patch to fix some
long-standing errors in the LaTeX output. What do I do with a patch
kit?

**Forward and Reverse LP**

There are two schools of literate programming: Forward and Reverse.
Forward literate programming starts with a source text and generates
the documentation plus the source code files required by the
compilers or interpreters.

Reverse literate programming generates documentation from the source
files. Tools like `Sphinx <http://sphinx.pocoo.org/>`__ do this very
nicely. With a little bit of work, one can create a documentation
tree with uses Sphinx's
`autodoc <http://sphinx.pocoo.org/ext/autodoc.html>`__ extension to
create great documentation from the source.

Reverse LP, however, tends to focus on the API's of the code *as
written*. Sometimes it's hard to figure out why it's written that way
without further, deeper explanation. And keeping a separate
documentation tree in Sphinx means that the code and the
documentation can disagree.

**My pyWeb Tool**

The gold standard in Literate Programming is Knuth's Web. This is
available as
`CWEB <http://www.literateprogramming.com/cweb_download.html>`__
which generates TeX output. It's quite sophisticated, allowing very
rich markup and formatting of the code.

There are numerous imitators, each less and less sophisticated. When
you get to `nuweb <http://nuweb.sourceforge.net/>`__ and
`noweb <http://www.cs.tufts.edu/~nr/noweb/>`__, you're getting down
to the bare bones of what the core use cases are.

For reasons I can't recall, I wrote one, too. I wrote (and used)
pyWeb for a few small projects. I posted some code as an experiment
on the Zope site, since I was a Zope user for a while. I went to move
it and got emails from a couple of folks who are serious Literate
Programmers and where concerned when their links broke. Cool.

I moved the code to my own personal site, where it sat between 2002
and today. It was hard-to-find; but there are some hard-core Literate
Programmers who are willing to chase down tools and play with them to
see how they work at producing elegant, readable code. Way cool.

**Patch Kit**

Recently, I received a patch kit for pyWeb. This says several things.

#.  It's at least good enough that folks can use it and find the
    errors in the LaTeX markup it produced

#.  Some folks care enough about good software to help correct the
    errors.

#.  Hosting it on my personal web site is a bad idea.

So, I created a SourceForge project, `pyWeb Literate Programming
Tool <https://sourceforge.net/projects/pywebtool/>`__, to make it
easier for folks to find and correct any problems.

I expect the number of downloads to hover right around zero
forever. But at least it's now fixable by someone other than me.



-----

Regarding Leo - it has advanced by leaps and bound...
-----------------------------------------------------

Ville<noreply@blogger.com>

2010-03-14 16:24:11.895000-04:00

Regarding Leo - it has advanced by leaps and bounds lately, including a
new fast (and good-looking!) Qt ui, simplified reST authoring, Python 3
support...

It's actually quite an exciting project, even if you were not into LP at
all.


Do you know Leo ?
-----------------------------------------------------

luigi_scarso<noreply@blogger.com>

2010-03-04 14:03:27.855000-05:00

Do you know Leo ?
http://webpages.charter.net/edreamleo/front.html


Hi Steven,

I've sent you a patch to pyWeb 2.1...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-06-18 02:59:21.054000-04:00

Hi Steven,

I've sent you a patch to pyWeb 2.1 related to RST generation yesterday
to s_lott at yahoo.com

Duplicating this info here to make sure it wouldn't lost.

Best regards,
Egor


Hi Steven,

Another patch for pyWeb 2.1 related to...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-08-02 12:17:54.267000-04:00

Hi Steven,

Another patch for pyWeb 2.1 related to RST generation was sent to s_lott
at yahoo.com

Best regards,

Egor





