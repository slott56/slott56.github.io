Literate Programming and GitHub
===============================

:date: 2015-06-23 08:00
:tags: sphinx,#python,literate programming,PyLit,github
:slug: 2015_06_23-literate_programming_and_github
:category: Technologies
:status: published


I remain captivated by the ideals of `Literate
Programming <http://www.literateprogramming.com/>`__. My fork of PyLit
(https://github.com/slott56/PyLit-3) coupled with
`Sphinx <http://sphinx-doc.org/>`__ seems to handle LP programming in
a very elegant way.

It works like this.

#. Write RST files describing the problem and the solution. This
   includes the actual implementation code. And everything else that's
   relevant.

#. Run PyLit3 to build final Python code from the RST documentation.
   This should include the setup.py so that it can be installed
   properly.

#. Run Sphinx to build pretty HTML pages (and LaTeX) from the RST
   documentation.


I often include the unit tests along with the sphinx build so that I'm
sure that things are working.

The challenge is final presentation of the whole package.

The HTML can be easy to publish, but it can't (trivially) be used to
recover the code. We have to upload two separate and distinct things.
(We could use BeautifulSoup to recover RST from HTML and then PyLit to
rebuild the code. But that sounds crazy.)

The RST is easy to publish, but hard to read and it requires a pass
with PyLit to emit the code and then another pass with Sphinx to
produce the HTML. A single upload doesn't work well.

If we publish only the Python code we've defeated the point of
literate programming. Even if we focus on the Python, we need to do a
separate upload of HTML to providing the supporting documentation.

After working with this for a while, I've found that it's simplest to
have one source and several targets. I use RST ⇒ (.py, .html, .tex).
This encourages me to write documentation first. I often fail, and
have blocks of code with tiny summaries and non-existent explanations.

PyLit allows one to use .py ⇒ .rst ⇒ .html, .tex. I've messed with
this a bit and don't like it as much. Code first leaves the
documentation as a kind of afterthought.

How can we publish simply and cleanly: without separate uploads?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Enter GitHub and `gh-pages <https://pages.github.com/>`__.

See the
"`sphinxdoc-test <http://daler.github.io/sphinxdoc-test/index.html>`__"
project for an example. Also this
https://github.com/daler/sphinxdoc-test. The bulk of this is useful
advice on a way to create the gh-pages branch from your RST source via
Sphinx and some GitHub commands.

Following this line of thinking, we almost have the case for three
branches in a LP project.

#. The "master" branch with the RST source. And nothing more.
#. The "code" branch with the generated Python code created by PyLit.
#. The "gh-pages" branch with the generated HTML created by Sphinx.


I think I like this.

We need three top-level directories. One has RST source. A build
script would run PyLit to populate the (separate) directory for the
code branch. The build script would also run Sphinx to populate a
third top-level directory for the gh-pages branch.

The downside of this shows up when you need to create a branch for a
separate effort. You have a "some-major-change" branch to master.
Where's the code? Where's the doco? You don't want to commit either of
those derived work products until you merge the "some-major-change"
back into master.

GitHub Literate Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~


There are many LP projects on GitHub. There are perhaps a dozen which
focus on publishing with the Github-flavored Markdown as the source
language. Because Markdown is about as easy to parse as RST, the
tooling is simple. Because Markdown lacks semantic richness, I'm not
switching.

I've found that semantically rich markup is essential. This is a key
feature of RST. It's carried forward by Sphinx to create very
sophisticated markup. Think ``:code:`sample``` vs. ``:py:func:`sample``` vs.
``:py:mod:`sample``` vs. ``:py:exc:`sample```. The final typesetting may be
similar, but they are clearly semantically distinct and create
separate index entries.

A focus on Markdown seems to be a limitation. It's encouraging to see
folks experiment with literate programming using Markdown and GitHub.
Perhaps other folks will look at more sophisticated markup languages
like RST.

Previous Exercises
~~~~~~~~~~~~~~~~~~~~~~


See https://sourceforge.net/projects/stingrayreader/ for a seriously
large literate programming effort. The HTML is also hosted at
SourceForge: http://stingrayreader.sourceforge.net/index.html.

This project is awkward because -- well -- I have to do a separate FTP
upload of the finished pages after a change. It's done with a script,
not a simple "git push." SourceForge has a GitHub
repository. https://sourceforge.net/p/stingrayreader/code/ci/master/tree/.
But. SourceForge doesn't use  GitHub.com's UI, so it's not clear if it
supports the gh-pages feature. I assume it doesn't, but, maybe it
does. (I can't even login to SourceForge with Safari... I should
really stop using SourceForge and switch to GitHub.)

See https://github.com/slott56/HamCalc-2.1 for another complex, LP
effort. This predates my dim understanding of the gh-pages branch, so
it's got HTML (in doc/build/html), but it doesn't show it elegantly.

I'm still not sure this three-branch Literate Programming approach is
sensible. My first step should probably be to rearrange the
`PyLit3 <https://github.com/slott56/PyLit-3>`__ project into this
three-branch structure.





