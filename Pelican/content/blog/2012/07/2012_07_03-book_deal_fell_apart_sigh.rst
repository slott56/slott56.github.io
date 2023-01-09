Book Deal Fell Apart (sigh)
===========================

:date: 2012-07-03 08:00
:tags: #python,building skills books
:slug: 2012_07_03-book_deal_fell_apart_sigh
:category: Technologies
:status: published

 
After spending a couple of years (really) working with a publisher,
the deal has gone south.
 
The problem was—likely—all mine.  The book wasn't *really* what the
publisher wanted.  Perhaps it was close and they thought they could
edit it into shape.  And perhaps I wasn't responsive enough to
criticism.
 
I like to think that I was responsive, since I made almost all of the
suggested changes.
 
But the deal fell apart, so my subjective impression isn't too
relevant.
 
**What To Do?**
 
I have two essential choices here.

#. **Finish up**.  Simply press on with the heavily-edited version.  The
   path of least resistance.

#. **Roll back the content**.  This involves going back to a less
   heavily edited version and merging in the *relevant* changes and
   corrections from the writing process.

Option 2 is on the table because my editor was unhappy with
"digressive" material.  The editor had a vision of some kind of
narrative arc that exposed Python in one smooth story line.  My
attempted presentation was to expose language features and provide
supporting details.

Perhaps I'm too deeply invested in the details of computer science.
Or.  Perhaps I'm just a lousy writer.  But I felt that the
digressions were of some value because they could fill in some of the
gaps I observed while coaching and teaching programmers over the last
few decades.


In addition to the editorial challenge, there's technical challenge.
Do I step back from LaTeX?

-   **Use LaTeX**.  This means that I would have to create the non-PDF
    version with a LaTeX to HTML translator.  Read `Converting LaTeX
    to HTML in the Modern
    Age <http://river.styx.org/ww/2010/11/latex>`__.  See
    `Pandoc <http://johnmacfarlane.net/pandoc/>`__.  Or, it means that
    I don't offer an HTML version (a disservice, I think.)  Also, I
    need to unwind the publisher's LaTeX style libraries and revert to
    a plain LaTeX.  Since LaTeX is semantically poor, I need to rework
    a lot of RST markup.

-   **Revert to RST**.  While RST tools can make both LaTeX and HTML
    from a common source, it does mean that some of the fancier LaTeX
    formatting has to go.  Specifically, I really got to know the
    `algorithm and algorithmic
    packages <http://en.wikibooks.org/wiki/LaTeX/Algorithms_and_Pseudocode>`__.
    I hate to give those up.  But maybe I can work something out with
    Sphinx 1.1.3's various features.


The problem is that three of the four combinations of paths have
advantages.


-  Finish up using LaTeX is easiest.  Remove the publisher's document
   style.  Use HeVeA or Pandoc to make HTML.  Move on.

-  Finish up but revert to RST.  This means conversion from the
   publisher's LaTeX to RST followed by some editing to fix the
   missing RST semantic markup and then some debugging to get the
   LaTeX and HTML to look good.

-  Rollback the content using LaTeX.  This would be challenging
   because I would have to merge manually edited publisher-specific
   LaTeX from the heavily-edited version with the Sphinx-generated
   LaTeX from the less-heavily edited source.  Things like the
   publishers' style tags would complicate the merge.

-  Rollback the content and revert to RST. This means using Pandoc to
   convert the heavily-edited LaTeX to RST. Then merging the
   *relevant* edits into the RST original text.   This actually seems
   pretty clean, since the heavily-edited RST (converted from LaTeX)
   would be short.


Perhaps, if I was a better writer, I wouldn't have these problems.
It appears than the solution is MacFarlane's
`Pandoc <http://johnmacfarlane.net/pandoc/>`__.  This can reverse
LaTeX to RST, allowing easy side-by-side merging of texts from
various sources.  Or.  It can convert LaTeX to HTML, allowing easy
work with the heavily edited LaTeX version.



-----

I&#39;m glad you&#39;ve had good luck with HeVeA. ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2012-07-03 11:53:18.502000-04:00

I'm glad you've had good luck with HeVeA. I wanted to let you know that
I've been using plasTeX to convert latex to html and docbook in a
publishing setting. I had to write a few python classes for my own
customizations and I expect the algorigthm classes aren't supported out
of the box.
Still, it's a nice python package, imo.
[http://plastex.sourceforge.net/]


So the deal is definitely off the table? That&#39;...
-----------------------------------------------------

Knack<noreply@blogger.com>

2012-07-03 11:14:26.643000-04:00

So the deal is definitely off the table? That's unfortunate. Sorry to
hear that.
As the deal is gone (as I understood), the only person you need to
satisfiy is yourself. That's good news. I would finish the project as
fast as possible, as you've been happy with your style and content in
the first place. And then be proud of it!


What is your goal for writing this book? How would...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-07-07 06:03:24.632000-04:00

What is your goal for writing this book? How would having a publisher
help you achieve your goal?
"dinosaur publishing company"
Yes, the publishing industry is changing. However, publishers do still
add value. Just think O'Reilly.


As James says, self publish. Today it is the way t...
-----------------------------------------------------

Tucanae Services<noreply@blogger.com>

2012-07-03 12:54:05.902000-04:00

As James says, self publish. Today it is the way to go.
Get yourself a amazon publishers account set up. Retweek your content
for epub. Get an account with LuLu or Smartwords to support your hard
copy followers.


I just have to add a ditto. Why would any author t...
-----------------------------------------------------

Lee Daniel Crocker<noreply@blogger.com>

2012-07-03 13:18:19.967000-04:00

I just have to add a ditto. Why would any author today deal with a
dinosaur publishing company? Just publish it yourself and keep all the
money.


made almost all of the suggested changes ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-07-07 05:58:32.197000-04:00

... made almost all of the suggested changes ...
... unhappy with "digressive" material ...
... digressions were of some value because they could
fill in some of the gaps I observed while coaching and teaching
programmers over the last few decades ...
So, you cared enough about the reader not to get rid of the "digressive"
material.
... one smooth story line ...
How could anyone think that learning a language is one smooth and linear
process?
I am trying to work my way through your Python book and your writing is
cool.


Dude self publish. It&#39;s a real option.
------------------------------------------

James Thiele<noreply@blogger.com>

2012-07-03 11:06:09.293000-04:00

Dude self publish. It's a real option.


Choose the path that will result in a book that is...
-----------------------------------------------------

Lennart Regebro<noreply@blogger.com>

2012-07-09 04:13:50.730000-04:00

Choose the path that will result in a book that is good enough for you
to live with it, but involves the least amount of work.
Writing computer books in specialized topics (such as Python) is rarely
a profitable venture. You do it because it's fun, because the book is
needed or as a vanity project. Or, as in my case, all three.
But you are highly unlikely to ever get any significant amount of money,
so do whatever it takes to make a book that is good enough for you, but
no more.
Then self-publish it. If you live in the US or any country where they
can send you money via bank-transfer, Amazons self-publishing company
CreateSpace is a definite option.
I wrote a bit on the experience I had here:
http://regebro.wordpress.com/2011/10/24/self-publishing-a-book-part-1-why-and-how/
I'll write a bit on my experience with CreateSpace soonish.





