Letter to Mom -- What Is This "Computer Programming" Thing?
===========================================================

:date: 2021-07-04 14:31
:tags: architecture,C4model,Programming Languages,API Design,os
:slug: 2021_07_04-letter_to_mom_what_is_this_computer_programming_thing
:category: Technologies
:status: published

Happy birthday, mom. Glad to see you're still doing well, avoiding the
complications of COVID-19.

You asked what it was I did for a living. Emphasis on the past tense,
now that we're both fully retired old people.

I have to confess that it's not easy describing high-tech work. There's
a lot of jargon. Your varied range of careers included many things, one
of which was being a school librarian. The world has had libraries and
librarians for millennia. The job title is pretty well understood. The
world hasn't had electronic computers for very long, making the job of
programming them a relative novelty.

Aids to computation include slide rules and other mechanical devices.
The idea of a mechanical computer dates from the 1830's. You can read
about the first computer programmer, Ada Lovelace, here:
https://www.computerhistory.org/babbage/adalovelace/. Proper electronic
digital computes didn't arise until the 40's, when you were a child.
ENIAC, for example dates from 1945.

While a lot has changed since the ENIAC, there are a few universal
truths. I'm going to beat one of those truths like a dead horse because
it's both essential and obscured by layers of technology.

This first and most fundamental truth is that a computer -- even
something as sophisticated as a laptop with a dozen open browser tabs,
zoom, and two different solitaire games -- is really a small device that
is patiently waiting for you to type or click; the software works out
some response and this is displayed on the screen or burbles out the
speakers (or both.)

We can say that a general-purpose computer is "applied" to a specific
problem. We shorthand this into creating "Application Software;" the
software that applies the computer's hardware to a problem. And we
shorthand this into "Apps" or "Applications" that do useful things on a
general-purpose device.

The distinction between software (things you download and change) and
hardware (the box on your desk) has become pretty common-place. The
details of the software are what we need to put under the magnifying
glass to look at closely.

To make your computer more useful, clever engineers have worked out a
way to interleave activities from a variety of applications, all of
which are using your computer concurrently. There's a set of rules to
determine which application is in the "foreground"; this is the
application software that has access to keyboard, mouse, display, and
speakers. When you click on another window, you bring another
application to the foreground. Access to the hardware switches and the
display updates. It's very slick. They provide a number of visual cues
to show you which application's "window" is in the foreground; all the
others have different cues to show you they're in the background.

What's important about this foreground/background concept is that each
application is -- from one point of view -- free to behave as if it is
in total control of the entire computer. In reality, an application
emphatically does not have unfettered control over the computing
resources; there are a large number of gates and fences forcing
applications into an orderly, and disciplined sharing and cooperation.

You taught at a nursery school. You know how important an orderly set of
rules is. Applications are no different than unruly three- and four-year
olds: they try to grab snacks out of order. They forget how pants work
when they try to use the toilet. They need lessons in how to put their
coats on to go outside in the winter.

These rules -- the set of policies and procedures that constrain
applications -- is collectively called the "Operating System." (Don't
ask why, the computer folks borrow terms from other disciplines and
imbue them with new meanings. There's rarely a sensible etymology, just
conventional usage.) The idea of a "system" of components is essential.
There are a lot of layers of engineering in the OS.

The presence of an operating system lets multiple apps cooperate. But,
it doesn't change the fundamental truth that originated with Babbage and
Lovelace and continued on through Turing and Von Neumann and others and
was handed down to me.

The general-purpose computer is applied ("programmed") to a problem;
it's set up to respond to inputs by displaying outputs.

So that was boring. What did you do?
------------------------------------

Good point. That was boring. But necessary, I think, to bracket the
nuanced difference between "computer" as a collection and an individual
application. The computer-as-collection includes a lot of software: an
OS plus applications. This is distinct from each individual application
that's part of the collection. It's all software, but the context shifts
from everything the computer is doing to one specific solitaire game.

Above, I mentioned that the OS has layers. In a way it's like a quilt,
there's a backing, batting in the middle, and a complex quilt top made
from pieces. Most important is the quilting that holds the layers
together.

In a way, it's also like a library. There's the foundational problem of
storing and loaning books. But there's a secondary problem of finding
the damn things; leading to Dewey or LC codes for topics so we can keep
related books together. And there's a third layer problem of having an
accurate index or catalog of all the books. Using small cards (the card
catalog) gives the library flexibility to make sure the catalog matches
the stacks. And there are related problems of loaning them out with some
reasonable promise to return them.

I might even be able to work out an analogy with the Apple Orchard or
the Arboretum or the Summer Camp. But, I think you get my drift here,
that there are foundational elements that we can't really change, and we
build on those foundations to make the whole slightly easier for people
to use.

I get it, you built application software. What did you do?
----------------------------------------------------------

What's important about concept of layers is how pervasive the layering
idea is in all of computing.

Because of the potential complexity of a solution to a problem, we take
the "layering" idea one step further than simply decreeing there should
be layers.

What we found, starting in the 70's, was that the operating system
tended to conceal many details of the underlying hardware. A modern
programming language also divorced us from details of the hardware.
Admiral Grace Murray Hopper's idea was to have an application that would
transform a program written in some neutral language into the language
of whatever hardware we had on hand. She pioneered the COBOL programming
language; the language was utterly unlike any specific piece of
hardware, and required a "compiler" application to translate COBOL
statements into a form that the OS could run as an application.

We liked this idea: the underlying hardware became a kind of hazy
abstraction. We knew it was there, but between our languages, libraries
of pre-written software, our compilers, and the OS, we didn't really see
the underlying hardware. This lets us decompose a complex problem into a
number of smaller problems; giving us a lot of leverage.

The core idea of "abstraction" leads to the idea of layers of
abstraction. Within our application software we can can also use this
idea of layers to decompose our solution to a problem. An application
layer can be quilted to a library layer that we bought or downloaded.
The library is -- independently -- quilted to an OS layer. And the whole
stack of layers is carefully stitched down to the underlying silicon
chip. Maybe it was a Motorola chip, or an Intel chip, or an AMD chip. We
didn't much know or care.

Well. We cared a little. Some of the AMD chips were faster than some of
the Intel chips. So we would prefer to have our OS and our language
focused on those chips because things were faster. Until Intel jumped
ahead of AMD. The concept was to remain divorced from gritty details of
how the little fleck of silicon with its millions of transistors
actually worked.

Recap
-----

Application software configures the general-purpose computer to a
specific task. Applications coexist via an operating system and reusable
libraries.

Software (application, operating system, libraries) is created in layers
and provide abstractions to hide the details of underlying layers.

My job?

Design the layers. Get other programmers to understand the design for
the layers. Help them to create statements ("code") using the language
of choice. (I'm a big fan of Python, but I've used many, many other
languages.)

Note that I didn't (generally) design the visible quilt top in any
detail. My job was to help the visual designers and the user experience
(UX) designers create a top that delighted people using the software. I
made sure that the top and the layers underneath it all fit together
reasonably well for a sensible budget. Cutting and stitching all the
blocks was a specialized skill that I tried to avoid.

I did more than design, however. When I say design of the structure, you
can imagine an architect or civil engineer looking over drawings of
girders and beams and making sure the floor would hold the weight of all
those books in the new wing of the library.

While many software designers and architects do pour over drawings, I --
personally -- didn't like to leave it at the drawing stage. This was
probably a career-limiting choice, but I liked to get my hands dirty
actually digging holes and standing up cinderblocks in the foundation.
The idea of swinging a hammer to build components told me -- directly --
how good (or bad) my design was.

There's a fork in the career path for programmers. Some software
architects work best with Keynote presentations to developers and
executives. They build understanding and consensus. They're trusted with
larger projects and larger budgets. If things didn't work out, they
could deflect blame to the folks writing the software. This distinction
between design and realization can be used to avoid culpability. It
worried me.

Other architects (me, specifically) work best with code. I still needed
to build understanding and consensus. But I also built software so I
could be \*sure\* things worked. I liked to provide concrete, tangible,
"do it like this" code.

To higher-level executives -- people with budget authority -- I was only
a low-level programmer.

For decades, this meant a project would wind down after completion, and
I would leave the customer's location, and move on to a new project.
That's why I traveled a LOT.

A few clients would come to realize that I did offer significant value
by being able to design the layers and abstractions while also helping
folks actually build the software. This recognition was a rarity, which
is why I call it a career-limiting choice. It happened a few times.
There's a particularly memorable offer from a client in the 90's that --
in retrospect -- I should have taken. But, generally, I moved from work
site to work site, designing, and building the application software for
very, very large computers.

So, you went to meetings a lot?
-------------------------------

Precisely.

At first, I needed to talk about the problem. What they want software to
do. Why do they think new, custom-built, unique software will solve the
problem they have? This means meeting with people to understand the
problem in the first place. "What can't you do?" "Why can't you do it?"
There's a lot of "Why?" questions that need to be asked to locate the
obstacle that's easiest to remove. (Or the lowest-hanging fruit we can
pick.)

Then, we need to talk about the solution. How will we solve the problem
with computers and software? In some cases, they have departments that
aren't talking. Or they have legal obstacles. Or they have a half-wit
vice president in charge of being the owner's brother. Eventually, we
wind up at "aha. They have software that acts as a kind of 'custodian'
for their cloud-based resources, but the language of the rules for that
custodian are opaque."

(Seriously. A real problem. Very, very removed from reality: governance
of rented "cloud" resources. Enterprise policies for use of cloud
resources. Concrete rules for cleaning up the computers rented from a
cloud vendor. Mathematical foundations for those rules. Very. Abstract.
https://github.com/cloud-custodian/cel-python)

Once we've got the preferred solution, we need to decompose it into
things we can download, and things we have to build. Ideally, we can
download most (or all) of it and move on. Realistically, the problem
domain is unique or something about the overall context and organization
is unique, and means leads to customized software to reflect the unique
situation.

Before too long, we have meetings to review some pictures: some
contexts, some containers for application software, some components (or
I've called them "layers" above). This will lead to people writing some
code. (The 4 C's: Context, Container, Component, Code.)

(Side-bar. The "container" is a generalization of the idea of a
computer. The OS lets multiple applications cooperate; what if we have
multiple OS's cooperating? This idea of layers of abstraction is so
compelling, we can apply it in a variety of places. This lets us to talk
about abstract containers instead of concrete computers.)

We'll have daily meetings while we're building the code that populates
the components that gets installed into the containers that fills out
the context. These last 10 minutes. What we've done. What we're doing.

We'll have meetings every two weeks to look at components and containers
and be sure they work. People will demo what they've done. It will be
fun. We'll have donuts.

We'll have impromptu meetings to talk about how to write tests and do
quality assurance on our code and components. The testing and quality
checking became my obsession during the last five years of my career.
Answering the question "Did you test **everything**?"

We'll have meetings to talk about managing the containers to be sure
they're working. And how to integrate and deploy the components into the
containers.

In and among the meetings, I wrote code. For the last ten years, it was
always in Python. Before that it was in other languages.

So, that's what I did for a living. I went to meetings. I wrote code.





