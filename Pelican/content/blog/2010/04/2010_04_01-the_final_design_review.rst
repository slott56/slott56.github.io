The Final Design Review
=======================

:date: 2010-04-01 08:00
:tags: architecture,design,humor,software process improvement
:slug: 2010_04_01-the_final_design_review
:category: Technologies
:status: published

Today, we're reviewing the final and only code in the application. It's
just that simple. We'll start with the data model.

::

    CREATE TABLE STUFF(
        COLUMN1 TEXT,
        COLUMN2 TEXT,
        COLUMN3 TEXT
        );

As you can see from the enclosed table design, we have generalized
the general triple-store to make it more general by removing all type
restrictions on the RDF triple.

This can be used to construct any relations by the convention of
having COLUMN1 be the database, schema and table, separated with
dots. COLUMN2 is the column or attribute name. COLUMN3 is -- again,
by convention only -- the target data type (integer, string, date,
etc.) and the quoted value.

Any Questions?

The stunned silence is -- I'm sure -- due to the glittering
brilliance of this design. Why this hasn't been more widely used, I
have no idea.

The code is equally simple. We don't need to get into the details,
but we have

    "a function called do_stuff. ... not to worry because the
    method does more than one thing. ... don't worry because the
    method is overloaded many different ways."

Great. That ends this design review. With this kind of obvious
simplification, we don't need any more design reviews, this one
covers all possible bases.

**Seriously**

I've seen the first discussed seriously in the context of "why
don't we simply...". The answer ("it doesn't perform well") is
always a surprise to people who pitch the triple-store solution to
a problem they've managed to get wrong.

I recently received an email bemoaning a real code review in which
someone seriously tried to put a function into production named
"do_stuff".

Equally bad is this "question" on Stack Overflow. "`Using
table-of-contents in
code? <http://stackoverflow.com/questions/2438841/using-table-of-contents-in-code>`__".
(It's not really a question, it's a blog post in the rhetorical
form of a question.) The money quote: "I know that alternative to
that kind of listing would be to split up big files into smaller
classes/files, so that their class declaration would be
self-explanatory enough.. but some complex tasks require a lot of
code".

It appears that there are programmers who have done too little
maintenance and adaptation.





