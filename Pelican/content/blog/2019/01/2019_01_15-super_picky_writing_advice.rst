Super-picky Writing Advice
==========================

:date: 2019-01-15 08:00
:tags: writing,pycon,#python
:slug: 2019_01_15-super_picky_writing_advice
:category: Technologies
:status: published


There are patterns to bad writing. I'll give some examples based on a
blog post I was sent. It's also based -- indirectly -- on some of
proposals I saw for PyCon and PyDataDC.

For the conference calls for papers, I can ask a few questions of the
author, but that's about it.

For the blog post, I suggested a bunch of changes.

They balked.

Why ask for advice and then refuse to do anything?  (We can conjecture
they wanted a "good job" pat on the head. They didn't want to actually
have me give them a list of errors to fix.)

One of the points of contention was "Not everyone has your depth of
expertise."

Sigh.

The blog post was on Ubuntu admin: something I know approximately
nothing about. Let me step away from being an expert, while sticking
closely with being able to write. I work with editors who -- similarly
-- can write without being deep technology experts. I'm trying to
learn what and how they do it.

In this case, my editing was based on general patterns of weak
writing.

#. Contradictions
#. Redundancy.
#. Waffling.
#. Special-Casing.




Any blog post on Ubuntu admin that starts with "This is not just
another blog post..." has started off with a flat-out contradiction.
It emphatically **is** another blog post. You can't rise above the
background noise of blog posts by writing a blog post that claims it's
not a blog post. Sheesh. Find a better hook.

Any blog post on Ubuntu admin that includes "This blog post assumes
the reader is familiar with linux sys administration." As if --
somehow -- a reader interested in Ubuntu admin could be confused by
the required skills. It's clearly redundant. Cut it.

(This led to an immense back-and-forth with repeated insistence that
\*somehow\* someone once got confused and \*something\* bad happened
to someone. Once. My response was adamant. "It's redundant. The title
says Ubuntu. That covered it. More repetition is an insult to the
reader.")

Anything that has "this may nor may not work depending on your
filesystem" is flat-out confusing: it covers both bases. Does it work
or does it not work? Which is it? Clearly, there's some kind of
precondition -- "must be this file system" or "most not be this file
system" -- buried under "may or may not work." It's not that I know
anything about Ubuntu file systems. But I can spot waffling.

Indeed, when you look at it, this is a "hook" to make the blog post
useful and interesting. Some advice doesn't work. This advice always
works. Simple statements of fact are better than contradictions and
waffling.

Finally, there was a cautionary note that replacing "/swapfile" with
"/ swapfile" would brick your OS. Which. Was. Crazy. It's really
difficult to arbitrarily introduce spaces into shell commands and
still have proper syntax. Sometimes a shell command with rando spaces
may have proper syntax and may work. Most commands won't work at all
with a rando space added. Try some and see.

What's more important is only one random punctuation error was listed.
The special-case nature of this was a tip-off that something was not
right with this advice.

What about a random ">" in the command? Or a random "|"? Not covered.
A single space was considered worthy of mention. The rest. Meh.

(If you want details, it's was \`dd -of=/swapfile ...\`. If asked, I'd
guess \`dd -of=/ swapfile\` is a syntax error because \`swapfile\`
isn't a valid operand to \`dd`. Not an expert. I didn't check. AFAIK,
the author didn't actually check, either.)

None of this editing was based on any vast expertise. It was simple
editorial work looking for some common problems with hasty writing.

#. Avoid clear contradictions.

#. Avoid redundancy.

#. Don't waffle.

#. Special cases are instances of a more general pattern. The pattern is
   more important than the case.




One of the contentious back-and-forth issues was "I'm not writing a
book, it's only a blog post."

Wait. What? Blog posts are often **more** widely-read than books. Look
at Stack Overflow. If one of my books had the kind of readership my
Stack Overflow answers have, I'd be living on royalty payments alone.

A blog post requires the same depth of care as a book.

This applies to proposed talks at conferences, also. The proposal
needs to be carefully edited to reflect the final presentation's care
and quality.

Thank goodness, most of the 100's of proposals I've looked at rarely
have the four obvious problems listed above.

The problems I see in conference proposals are minor.

#. Incompleteness. A 45 minute talk boiled down to 4 bullet points
   doesn't give us any confidence. It's hard to imagine filling the
   whole time with useful content when looking at a four-sentence
   outline. Will it be rambling digressions? Or will we have disgruntled
   attendees who had hoped for more?

#. Weirdly cute style. Things like "This is where I jokingly outline
   something something and the real fun begins." We assume everyone is
   witty and charming, you don't need to tell us. We assume all talks
   will be fun. Can we move on to the Python (or PyData) topics you'll
   cover?

#. Sales Pitches. "[Speaker's name] is a respected industry expert who
   delivers exciting and transformative keynote addresses and will
   dynamically cover the state-of-the-art blah blah blah..." Please.
   What Python topic is this? We like to review the outlines without
   speaker information; we need to focus on the content. Subverting this
   by including the speaker's name in the description or outline is
   irritating.


I'm really pleased we see very few `PyCon
Code-of-Conduct <https://github.com/python/pycon-code-of-conduct>`__
problems in the calls for proposals. That is a delight.
Editing is hard work. I'm sorry to report that editing means making
changes. If you ask for editorial advice, it helps to listen.





