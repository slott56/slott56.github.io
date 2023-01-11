Python and the "Syntactic Whitespace Problem"
=============================================

:date: 2021-09-27 16:04
:tags: #python
:slug: 2021_09_27-python_and_the_syntactic_whitespace_problem
:category: Technologies
:status: published

Check out this list of questions on Stack Overflow:

http://stackoverflow.com/search?q=%5Bpython%5D+whitespace+syntax

About 10% of these are really just complaints about Python's syntax.
Almost every Stack Overflow question on Python's use of syntactic
whitespace is really just a complaint.

Here's today's example: "`Python without whitespace requirements <http://stackoverflow.com/questions/3994765/python-without-whitespace-requirements>`__".

Here's the money quote: "I could potentially be interested in
learning Python but the whitespace restrictions are an absolute no-go
for me."

Here's the reality.

    **Everyone Indents Correctly All The Time In All Languages.**

Everyone. All the time. Always.

It's amazing how well, and how carefully people indent code. Not
Python code.

All Code. XML. HTML. CSS. Java. C++. SQL. All Code.

Everyone indents. And they always indent **correctly**. It's truly
amazing how well people indent. In particular, when the syntax
doesn't require any indentation, they still indent beautifully.

Consider this snippet of C code.

::

  if( a == 0 )
     printf( "a is zero" );
     r = 1;
  else
     printf( "a is non-zero" );
     r = a % 2;

Over the last few decades, I've probably spent a complete man-year
reading code like that and trying to figure out why it doesn't work.
It's not easy to debug.

The indentation completely and accurately reflects the programmer's
intention. Everyone gets the indentation right. All the time. In
every language.

And people still complain about Python, even when they indent
beautifully in other languages.



-----

When first learning python I found the use of whit...
-----------------------------------------------------

Mark<noreply@blogger.com>

2010-10-26 08:53:12.128000-04:00

When first learning python I found the use of whitespace for defining
blocks odd too. What was especially troublesome was the notion of tabs
vs. spaces for the whitespace. Once you get a decent python aware editor
that problem is no longer a problem and you are left with a language
that helps enforce readability. Maybe "get a good python aware editor"
should be the first step to every tutorial.


"Every[one] Indents Correctly All The Time In...
-----------------------------------------------------

Robin Norwood<noreply@blogger.com>

2010-10-26 11:45:18.435000-04:00

"Every[one] Indents Correctly All The Time In All Languages."
Oh, if only that were true. Look at pretty much any Javascript code that
isn't part of a framework. For some reason, JS coders seem to treat
mis-indentation as an obfuscation technique.


Attempting to do templating with django templating...
-----------------------------------------------------

Travis<noreply@blogger.com>

2010-10-26 13:00:24.648000-04:00

Attempting to do templating with django templating language can be ugly
and horrifying, but jinja2 fixes most of those problems.

What I find fascinating is that HAML, a syntax for HTML and XML that
represents structure using indentation and a syntax similar to CSS, is
written in ruby. It's also an extremely popular ruby library. There's no
popular alternative for python.

The same is true for its' whitespace significant CSS syntax, SASS, but
that's understandable... since it's a product that has no barrier to
using it standalone other than a zealotry for having everything in your
language of choice.

I miss HAML working with python. :/


s/not and error free/not as error free/ 
sorry
----------------------------------------------

matt harrison<noreply@blogger.com>

2010-10-26 12:04:22.431000-04:00

s/not and error free/not as error free/
sorry


Whenever you respond to complaints, you should ask...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-10-26 19:33:59.273000-04:00

Whenever you respond to complaints, you should ask yourself whether the
complaint is worth answering.

I think people who make a reflexive judgement based on whitespace (or
even any syntax, so long as the syntax is internally reflective) are
likely to either be zealots for some other technology, irrational, or -
most likely - very inexperienced with real-world development. In other
words, they are people whose acceptance the Python community (or any
community) does not need.

Python's whitespace requirement is a trade-off like any other. I find it
easy to work with and aesthetically pleasing. It does have some pitfalls
(tabs vs. spaces when working with poorly configured editors; pasting a
block at a different level of statement nesting than the level it was
copied from), but those are just different trade-offs to other languages
where e.g. you may have more superfluous syntax or less consistency in
code layout (which makes debugging other people's code and co-operation
harder).
Martin


There are a couple of times the whitespace bites y...
-----------------------------------------------------

matt harrison<noreply@blogger.com>

2010-10-26 12:02:40.573000-04:00

There are a couple of times the whitespace bites you in Python (and not
in non-whitespace aware languages).

One is pasting code. If you are at different levels of the block or the
pasted code contains tabs instead of spaces it's annoying. Other
languages don't have this.

Automatic re-indent is not and error free as in other languages.
This also makes Python a bad language for (html) templating. Python
based template languages end up looking like ruby (with end statements).
But ... people don't mention these, they only say that it's hard to use
whitespace. Well the rule is easy (replace { with : and indent
consistently), not sure what the holdup is since no one seems to mention
what I've just said.


Ok, having a look at your post once more, I now d...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-10-27 06:24:54.731000-04:00

Ok, having a look at your post once more, I now \*do\* think that was
exactly your point (people getting indentation right when not getting
the braces right)...

Sorry about that stupid comment :-)


Is there a Python auto-formatter?

Because I don&#...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-10-26 12:50:22.324000-04:00

Is there a Python auto-formatter?
Because I don't format my code any more. I let tools format it. And I
don't fool with it. I used to spend a lot of time on indentation, but I
ended up letting it go and I'm a lot more productive now. (C#, SQL)


I loved the significant whitespace in Python from ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-10-26 13:23:48.083000-04:00

I loved the significant whitespace in Python from the first time I saw
it.

@matt harrison:
Cut and paste will mess up a program more ways than whitespace. I very
often regret doing it. If the same code is repeated often it should be
refactored into a function.

@cade:
Many editors/IDEs have Python formatters. emacs comes to mind.


I&#39;m not 100% whether this actually might be yo...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-10-27 06:19:52.348000-04:00

I'm not 100% whether this actually might be your point about the C
example, but: This C code will not compile.

The indentation hides the fact that the "if" only refers to the next
statement. The "else" therefore has no matching "if" and the compiler
will throw an error. In those archaic languages you need braces {...}
:-)


There are people who don&#39;t indent correctly. W...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-10-28 15:25:07.925000-04:00

There are people who don't indent correctly. When I was a TA for
Programming 101, there was a student in the class that indented Every.
Single. Line. Differently. I had to reformat his code to see what the
heck he was up to.

He was the only one who did this, though.


&quot;Everyone Indents&quot;

Oh man, you don&#39;...
-----------------------------------------------------

Herberth Amaral<noreply@blogger.com>

2010-10-27 10:38:01.125000-04:00

"Everyone Indents"

Oh man, you don't know non-experienced programmers. In the beginning,
make them indent their code is like make an turtle climb a mountain:
they don't do.

Python solves this problem in a very elegant way, by throwing syntax
errors when indentation aren't done right.

For me, at least, whitespace is a Python's killer feature.


I believe you meant &quot;Everyone indents ...&quo...
-----------------------------------------------------

André Roberge<noreply@blogger.com>

2010-10-26 21:45:30.073000-04:00

I believe you meant "Everyone indents ..." when you wrote "Every indents
...". Also, for the commenter who mentions missing HAML, lookup shpaml
...


Sorry, but you have no idea what you’re talking ab...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-10-05 06:00:12.819000-04:00

Sorry, but you have no idea what you’re talking about. When writing in
C#, I don’t indent correctly. I don’t bother, because I don’t have to.
Visual Studio fixes all indentation for me. If I did what you said, I
would end up with wrong programs, as demonstrated in your own example.
Instead I rely on Visual Studio’s formatting to tell me what I
\*actually\* wrote. Your example demonstrates how to end up with a wrong
program that doesn’t mean what you think it does. I get the feedback
that tells me that my code structure is \*actually\* what I mean it to
be.


So good topic really i like any post talking about...
-----------------------------------------------------

Smart Spanish Blogs<noreply@blogger.com>

2012-05-05 06:13:16.655000-04:00

So good topic really i like any post talking about `STD symptoms
pictures <javascript:void(0);>`__ and more , you shall search in Google
and Wikipedia about that .... thanks a gain ,,,


&quot;Consider this snippet of C code.&quot;

I do...
-----------------------------------------------------

Earth<noreply@blogger.com>

2013-03-26 08:12:00.003000-04:00

"Consider this snippet of C code."
I don't understand your example. Is it correctly indented or badly
indented? What does it do and what should it do?


Indeed.  No one in their right mind would write C ...
-----------------------------------------------------

drichardson<noreply@blogger.com>

2013-07-09 18:04:35.162000-04:00

Indeed. No one in their right mind would write C code (or code in any
language with C-like syntax) that looks like that.

This same example is repeated over and over on the web. It seems
Python's goofy syntactic whitespace solves only a single problem -- a
problem that no one has ever actually had.

The problems Python's syntactic whitespace causes, however, are varied
and numerous. The astonishing number of apologetic articles like this
are a testament to that.

I'm sure replies will follow with all the usual "rules" (PEP 8, only use
spaces, use a special editor) to solve the problems that Python
apologists refuse to acknowledge actually exist!





