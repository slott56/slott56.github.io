Using SCons
===========

:date: 2010-09-01 08:00
:tags: RST,scons,#python,docutils,continuous integration
:slug: 2010_09_01-using_scons
:category: Technologies
:status: published

In looking at Application Lifecycle Management (see "`ALM
Tools <{filename}/blog/2010/02/2010_02_04-alm_tools.rst>`__"),
I had found that `SCons <http://www.scons.org/>`__ appears to be pretty
popular. It's not as famous as all the make variants, or Apache Ant or
Apache Maven, but it seems to have a niche in the forest of `Build
Automation
Software <http://en.wikipedia.org/wiki/List_of_build_automation_software>`__.

While it looks nice, parts of SCons are confusing. I struggled until
I found a simple use case.

More: `Empirical Comparison of SCons and GNU
Make <http://www.genode-labs.com/publications/scons-vs-make-2008.pdf>`__.

    "SCons proved to be more accurate, mostly due to its stateful,
    content-based signature model.

    On the other hand, GNU Make proved to be more resource
    friendly, especially regard- ing the memory footprint. SCons
    needs to address this problem to be a viable alternative to
    Make when building large software projects."

[Also, it appears that a lot of build and test automation have
been reframed as "Continuous Integration". Which isn't really a
bad thing. But it can be confusing because there are too many
categories into which general-purpose tools can be fit.]

While SCons looks cool, I haven't had a huge need for it at work.
Working in Python, there's no real "build". Instead our continuous
integration boils down to unit testing. Our "build" is an SVN
checkin. Our deployment is an SVN checkout and \`python setup.py
install`.

At some point, I would like to create an SConstruct file that runs
our integration test suite. But it's trapped at a low priority.

**SCons and Sphinx**

I did find an SConscript example that automated a document build
using Sphinx. This

`sphinx-scons <http://bitbucket.org/zondo/sphinx-scons/>`__ was
quite cool. However, it was challenging to customize. The SCons
documentation requires real work to understand. I could see the
value, but it was a lot of work.

I'm hoping that `No Starch Press <http://nostarch.com/>`__ finds
someone to write a tidy introduction to SCons.

**SCons and RST and LaTeX (oh, my!)**

Sphinx has made me a total fanboi of `ReStructured
Text <http://docutils.sourceforge.net/rst.html>`__. While I know
MS Word and iWorks Pages quite well, I have no patience with all
the pointing and clicking. Getting consistency is requires
consistent pointing and clicking; some people can do it, but some
of us find that manual pointing and clicking is sometimes
irreproducible. Semantic markup is a huge pain in the neck because
we have to stop typing to click on the proper style hint for the
various words.

I also know DocBook XML and LaTeX quite well. I've used very cool
XML editors including `XML Mind XML
Editor <http://www.xmlmind.com/xmleditor/>`__ (which is very
nice.) I no longer have any patience with any of these tools
because there's too much GUI.

RST is fun because you write in plain text. There are a few
directives and a few bits of inline roles for semantic markup. But
your work can focus on the content, leaving presentation aside. A
command-line tool (with templates) emits HTML or LaTeX or
whatever. The style considerations can be (a) secondary and (b)
completely consistent.

RST will easily produce complex LaTeX from plain text. What a joy.
LaTeX, of course, isn't the goal, it's just an intermediate result
that leads to DVI which leads -- eventually -- to a PDF.

Because of the Unicode and font selection on the Mac, I'm a user
of XeTeX and XeLaTeX. I have some problems with getting my copy of
`Blackadder
ITC <http://www.fonts.com/FindFonts/detail.htm?pid=204105>`__ to
work, but generally I'm able to write without much fussing around.

SCons has a great deal of the TeX/DVI/PDF tool chain already
installed. However, it doesn't have either the rst2latex script or
the XeTeX tools.

**An SConscript**

While my first attempts to understand SCons didn't work out well,
looking at RST and XeLaTex was a much better use case.

I wound up with this.

::


    rst2latex = Builder( action="rst2latex.py $SOURCES >$TARGET",
        suffix='.tex', src_suffix='.rst',
    )
    xelatex = Builder( action=["xelatex $SOURCES", "xelatex $SOURCES"],
        suffix='.pdf', src_suffix='.tex',
    )
    env = Environment(ENV=os.environ,
        BUILDERS = { 'rst2latex' : rst2latex, 'xelatex':xelatex }
    )
    env.rst2latex('someDoc')
    env.xelatex('someDoc' )
    env.rst2latex('anotherDoc')
    env.xelatex('anotherDoc')

Getting this to work was quite pleasant. I can see how I could
further optimize the document production pipeline by combining the
two Builders.

[And yes, the xelatex step is run twice to guarantee that the
references are correct.]

Now, I can get away with write, run \`scons\` and review the
resulting PDF. It's fast and it produces a nice-looking PDF with very
little work and no irreproducible pointing and clicking.

Given this baseline, I can now dig into SCons for ways to make this
slightly simpler.





