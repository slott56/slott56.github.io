Fiction Writers and Query Letters
=================================

:date: 2019-05-07 08:00
:tags: #python
:slug: 2019_05_07-fiction_writers_and_query_letters
:category: Technologies
:status: published


See http://flstevens.itmaybeahack.com/writing-world-building-and/ for
some back-story on F. L. Stevens and the need to write a \*lot\* of
query letters to agents for fiction. (The non-fiction industry is
entirely different; there are acquisition editors who look for
technical contributors.)

There's a tiny possibility of a Query Manager Tool (of some kind) on a
writer's desktop.

Inputs include:

-  Template letter.

-  A table of customizations per Agent. The intent is to allow more than
   simple name and pronoun changes. This includes Agent-specific content
   requirements. These vary, and can include the synopsis, first
   chapter, first 10 pages, first 50 pages. They're not email
   attachments; they have to be part of the main body of the email, so
   they're easy to prepare.

-  Another table of variant pitches to plug into the template. There are
   a lot of common variations on this theme. Sizes vary from as few as
   50 words to almost 300 words. Summaries of published works seem to
   have a median size of 140 words. A writer may have several (or
   several dozen) variants to try out.


This can't become a spam engine (agents don't like the idea of an
impersonal letter.)


Also. A stateful list of agents, queries, and responses is important.
Some Agents don't necessarily respond to each query; they often offer
a blanket apology along the lines of "if you haven't heard back in
sixty days, consider it a rejection." So. You want to try again.
Eventually. Without being rude. And if you requery, you have to send
a different variant on the basic pitch.


Some Agents give a crisp "nope" and you can update your list to avoid
requerying.


For new authors (like F. L. Stevens,) there's a kind of manual query
tracking mess. It's not really horrible. But it is annoying. Keeping
the database up-to-date with responses is about as hard as a tracking
spreadsheet, so, there's little value to a lot of fancy Python
software.


The csv, string.Template, email and smtplib components of Python make
this really easy to do.  While I think it would be fun to write,
creating this would be work avoidance.





