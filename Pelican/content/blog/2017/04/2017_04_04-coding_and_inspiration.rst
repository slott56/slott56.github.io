Coding and "Inspiration"
========================

:date: 2017-04-04 08:00
:tags: Design Principles,architecture,literate programming
:slug: 2017_04_04-coding_and_inspiration
:category: Technologies
:status: published

Tweet:

    .. image:: https://pbs.twimg.com/profile_images/437332968768425984/hy1HDtPo_normal.jpeg
        :alt: Twitter Avater

    **Data Science Renee(**\ `@BecomingDataSci <https://twitter.com/becomingdatasci?refsrc=email&s=11>`__\ **)**

    `4/1/17, 3:53 PM <https://twitter.com/becomingdatasci/status/848262128050073601?refsrc=email&s=11>`__

Thread. Coding is inherently  frustrating. Expect that. But 
with puzzle-solving healthy  attitude, keep going. Don't give up on yourself!

`twitter.com/IsabellaGhemen… <https://t.co/8tXSQBXH7L>`__

This thread includes some interesting topics. What hit me was the
idea of "inspiration-driven coding."

  "Do you ever get frustrated when coding? Or is it all
  inspirational?"

  "go into obsessive mode until I fix the problem"

This is fascinating. I've been coding for -- well -- a looooong time.
I no longer recall a time when I struggled. These quotes provide some
insight into the barrier that some people find between them and a
finished project.

I think that "hard-part-do-later" is bad advice. I'm a big fan of
tackling the hard part first.

I find that I have to do several things to get software to work. And
I do these so often that I rarely think about doing them, so I might
be misstating what I'm **really** doing. But I think this is right:

-   **Understand the problem**. It helps to understand the problem
    being solved. It's not essential to understand **all** of the
    problem. In a lot of cases, the problem is a larger-scale
    "business" issue which stems from a regulatory or competitive
    climate that has a very huge context including human aspirations
    and the very nature of what it means to be human. In these cases,
    narrowing the focus of the problem helps. Stating the problem
    clearly really helps. Clarifying the context can help; but it may
    involve erecting random-seeming boundaries to keep the problem
    from involving too many imponderables.

-   **Understand the solution**. This is easy to turn into glib
    useless advice. But I think that one thing that really helps is to
    really carefully detail what "success" means. For small things
    (like functions or classes) it should be a dry, formal assertion
    about the state of the variables. Without a mathematical
    formalism, it's easy to get confused and write a function that
    doesn't do the right thing. For larger-scale features, the
    solutions pieces need pretty complete, formal descriptions of how
    we know that they worked. File formats. Messages. Swagger
    specifications for an API.

-   **Understand the technology**. This can be hard. For simple
    programming, the technology is the set of language constructs. For
    more sophisticated programming, the technologies are the libraries
    and packages available. When it comes to big data, these can be
    very large and complex packages (like pandas and numpy) with lots
    and lots of features. It's very easy to overlook features when
    searching through documentation. For integration of components,
    it's an understanding of what the various tools really do.
    (Example: I'm trying to get a grip on Docker, and there are a lot
    of commands that do a lot of things, and I have to be careful to
    understand the difference between "run" and "start".)


But how? How do we "understand" these things?


I'm a big fan of writing down everything. I really like the idea
of "literate programming:" write down the problem. Write down the
overview of the solution. Write down the technologies that will be
used. Detail the coding assertions and outcomes. Detail the
components being used. Write. Write. Write.


The first drafts will be all natural language. Summaries.
Overviews. Hand-wringing over alternatives and tradeoffs and
possibilities. That's okay. Writing helps. Write. Write. Write.


Describe how simple it "should" be. Describe how the inputs get
transmogrified to the outputs. Fantasize.


Then elaborate on the details of "how" this will get done. Confirm
the fantasy statements of how the various bits and pieces fit
together. Revise. Revise. Revise.


At some point, parts will start to map to code in obvious ways.
and there will be a break from natural language to more formal
code. This may happen gradually. Or it may happen all at once.


One of the best pieces of coding advice was something I saw many
years go.


"Write all the comments first."


The example that followed showed a "wire frame" program that had
some declarations, but was mostly blocks of comments describing --
in vague, general ways -- what would go here eventually. I like
this approach because it allows space to think at a high level
about how things fit together as well as space to think about
details of how each individual little thing works.


There's a kind of progressive filling-in-the-blanks as code
evolves into the frame.

Then A Miracle Occurs
---------------------


Perhaps most important is this. Starting with wire-frame comments
and natural language narratives can lead to identification of gaps
in understanding the problem, the solution, or the technology. I
think that these conceptual gaps are where the frustration grows.


This is why I think that the big problem is caused by
"hard-part-do-later" thinking. It can turn out that the "hard
part" required a miracle.


      
         There's a famous S. Harris cartoon
         (visit http://www.sciencecartoonsplus.com/pages/gallery.php)
         which has the "then a miracle occurs" step in the middle of a
         process.


A wire frame for code is a low-cost, low-investment,
low-emotional-content product. As code fills in, it may become
clear that the wire frame wasn't right. It's easier to discard a
hundred lines of comments once we realize that they're not quite
right. There's less emotional investment. It's easy to throw it
away and start again.


Indeed, we may have to go through a few wireframes to be really
clear on where we think the miracle will occur. This gives us a
chance to identify the hard part of the problem.


Once we've got the hard part identified, we can tackle that. It
may involve one of three kinds of deeper understanding:


-  Understanding the problem better,
-  Understanding the solution in more detail, or
-  Understanding the technology more completely.


Any combination of these may be the reason why some part is
hard. We'll have to fix our understanding before we can finish.
We may as well tackle it first, since we're going to have to do
it anyway.


It's best to look for alternatives before we've written too much
code. There's an emotional commitment to code, even if it doesn't
work right. It's hard to throw code away. Therefore, stall as long
as possible. Solve the hard parts. Commit to code last.






