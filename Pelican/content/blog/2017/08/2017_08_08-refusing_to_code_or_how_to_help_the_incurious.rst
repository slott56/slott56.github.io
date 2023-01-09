Refusing to Code. Or. How to help the incurious?
================================================

:date: 2017-08-08 08:28
:tags: #python,learning
:slug: 2017_08_08-refusing_to_code_or_how_to_help_the_incurious
:category: Technologies
:status: published

The emphasis on code is important. Code defines the behavior of systems
-- for the most part Once upon a time, we used clever mechanical
designs, or discrete electronic components. The InternetofThings idea
exists because high-powered general-purposes CPU's are ubiquitous.


A DevOps mantra is "infrastructure as code". The entire deployment is
automated, from the allocation of processors and storage down to
pining the health-check endpoint to be sure it's live. Blue-Green
deployments, traffic switching, etc., and etc. These all require lots
of code and as little manual intervention as possible.


The gold standard is to use tools to visualize state, make a
decision, and use tools to take action. Lots of code.


When I meet the anti-code people, it's confusing.


Outside my narrow realm of tech, anti-code is fine. I have a
sailboat, I meet lots of non-tech people who can't code, won't code,
and aren't sure what code is.


But when I meet people who claim they want to be data science folks
but refuse to code, I'm baffled.


Step 1 was to "learn more" about data science or something like that.
I suggested some of the ML tutorials available for Python. Why? It
appears that Scikit Learn is the gold standard for ML
applications. http://scikit-learn.org/stable/tutorial/index.html


Because they didn't want to code, they insisted on doing things in
Excel. Really.


Step 2 was to figure out some simulated annealing process -- in
Excel. They had one of the central textbooks on ML algorithms. And
they had a spreadsheet. They had some question that can only arise
from avoiding open-source code. I suggested they use the open source
code available to everyone. Or perhaps find a more modern tutorial
like this: http://katrinaeg.com/simulated-annealing.html.


Because they don't want to code, they used the fact
that **scipy.optimize.anneal()** was deprecated to indict Python. I
almost wish I'd saved all the emails over why basin hopping was
unacceptable. The reasoning involved having an old textbook that
covered annealing in depth, and not wanting to actually read the code
for basin hopping. Or something.


Step 3 was to grab a Kaggle problem and start working on it. This is
too large for a spreadsheet. Indeed, the data sets push the envelope
on what can be done on a Windows laptop because the dataframes tend
to be quite large. It requires installing Scikit learn, which means
installing `Anaconda from
Continuum <https://www.continuum.io/downloads>`__. There's no
reasonable alternative.
The Kaggle exercise may also involve buying a new laptop or renting
time on a cloud-based server that's big enough to handle the data
set. ML processing takes time, and GPU acceleration can be a huge
help. All of this, however, presumes that there's code to run.


Because they don't want to code, this bled into an amazing number of
unproductive directions.  There's some kind of classic "do everything
except what you need to do" behavior. I'm sure it has a name. It's
more than "work avoidance." It's a kind of active negation of the
goals. It was impossible to discern what was actually going on or how
I was supposed to help.


I suggested a Trello board.


The Trello board devolved into dozens of individual lists, each list
had one card. Seriously. The card/list thing became a way of avoiding
progress. There were cards for considering the implications of
installing Anaconda. The cards turned into hand-wringing discussions
and weird status updates and memo-to-self notes, instead of actual
actions.


Bottom line?


No code.


In the middle of the Kaggle something-or-other board, a card appeared
asking for comments on some code. :yay2: Something I can actually
help with.

The code was bad. And precious. I blogged about this phenomenon
earlier. The code can't be changed because it was so hard to create.
It was really bad, and riddled with bizarre things that make it look
like they'd never seen code before.

Use pylint? This got a grudging kind of reluctant cleanup. But
``huge_variable_names_with_lots_of_useless_clauses`` aren't flagged
by Pylint. They're still bad, and reading other code would show how
atypical these names are. Unless, of course, you hate code; then
reading code is not going to happen.

My new model for their behavior? They **hate** code. So when they do
it, they do it badly. Intentionally badly. And because it was so
painful, it's precious. (I'm probably wrong, and there's probably a
lot more to this, but it seems to fit the observed behavior.)
It gets worse (or better, depending on your attitude.)

Another Trello card appears wondering what ``[a, b] * 2`` or some
such Pythonic thing might mean. Um. What?

It appears that they can't find the Standard Library description of
the built-in data types and their operators. As if chapter four was
deleted from their copy, or something.

The "can't find" seems unlikely. It's pretty prominent. I would think
that anyone aspiring to learn Python would see the "keep this under
your pillow" admonition on the standard library docs and perhaps
glance through the first five sections to see what the fuss was
about. Unless they hate code.

I'm left with "won't find."  Perhaps they're refusing to use the
documentation? Are they also refusing to use Python's internal help?
It's not great, but you can try a bunch of things and get steered
around from topic to topic, eventually, you have to find something
useful.

Apply my new model: they hate code and Python **help()** is code.
Do they really hate code that much? I now think they do. I think they
truly and deeply hate losing manual, personal. hands-on control over
things. If it's not a spreadsheet -- where they typed each cell
personally -- it's reviled. (Or feared? Let's not go too far here.)
Test the hypothesis. Ask if they used **help()**.

Answer: Yes. They had tried three things (exactly three) and none of
those three had a satisfactory explanation. The **help()** function
did not work. Indeed, two of the things they tried had the same
result, and the third reported a syntax error. So they stopped.
They tried three things and stopped.

Okay, then. They hate code. And -- Bonus! -- They refuse to explore.
Somehow they're also able to insist they must learn to code. Will the
self-beatings continue until the attitude improves?

It's difficult to offer meaningful help under these circumstances. I
don't see the value in being someone's personal Google, since that
only reinforces the two core refusals to use code or explore by
typing code to see what happened.

I like to think that coding is a core life skill. Like cooking. You
don't have to become a chef, but you have to know how to handle food.
You don't have to create elaborate, scalable meshes of microservices.
But you have to be able to find the data types and operators on your
own.

And I don't know how to coach someone who is so incurious that three
attempts with **help()** is the limit. Done at three. Count it as a
failure and stop trying. "Try something different" seems vague, but
it's all I've got. Anything more feels isomorphic to "Here's the
link, attached is an audio file of me reading the words out loud for
you."





