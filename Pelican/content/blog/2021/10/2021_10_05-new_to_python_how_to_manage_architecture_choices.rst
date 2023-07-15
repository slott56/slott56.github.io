New to Python -- How to manage architecture choices
###################################################

:date: 2021-10-05 10:00
:tags: #python,architecture,community,management
:slug: 2021_10_05-new_to_python_how_to_manage_architecture_choices
:category: Technologies
:status: published

This is a problem folks new to Python have, and sometimes can't
articulate that they have it.

They don't know which package is the "right" one to use. Tox vs. Nox.
Click vs. Argparse vs. getopts? What's the "best" choice?

-  **Response 1**. The whole Python ecosystem is chaos and the language
   is just a "toy". You don't have this many choices with (pick your
   language: e.g., Go or Rust or Scala).

-  **Response 2**. We need a way to make architectural choices that the
   team understands and can use.

Response 1 is remarkably common. It's hard to argue against. If someone
thinks innovation is chaos, they -- perhaps -- shouldn't be in
technology to begin with. **Innovation IS chaos**. That's the essential
definition!

However, they may be a project owner (or the manager of an old-school
waterfall-style project) or -- worse -- someone responsible for
architecture, and complain about chaos. If so, they're not really cut
out for managing rapid technological change, and they need to be
bypassed.

Yes. Bypassed. Ignore them. Go to their meetings. Nod politely when they
rant about chaos. Then build working software. Eventually, they'll grow
to understand that a large ecosystem is NOT chaos. Rapid innovation is
not chaos. They may come to understand that filters are required to
reject some of the noise that comes from innovation.

Response 2 -- How do we make choices?
=====================================

Glad you asked.

I have seen four common approaches.

#. **HiPPO**: The Highest-Paid Person's Opinion.
#. **Tech Oracle**.
#. **HashTAG**: Hyperconnected And Socially Helpful Tech Advisory Group.
#. **Peer Pressure**.

Let's look at each of these.

HiPPO
-----

The Highest-Paid Person's Opinion isn't easy to dismiss. They're an
executive or the product owner and they think their position in the
company gives them a magical ability to somehow predict the technical
shortcomings of a component or a framework or a language.

Once upon a time, when all components were licensed, someone negotiated
contracts for support and training. The contracts (and negotiations)
were a Big Sweaty Deal (BSD™). The HiPPO needed to justify all the time
and money spent with the vendor. Okay. Sure. Then their opinion on
continuing to invest in a losing proposition makes a lot of sense. Since
they've already spent money with the vendor, they'd like us to continue
to spend money with the vendor, even if the vendor's product isn't
really very good.

Those times are past. Most everything is open source nowadays, and we
pay for support reluctantly. We often have POC's to chose among
alternatives. We can fire a vendor quickly. We don't invest heavily in
inking a deal. (In the olden days, I got lots of plane rides and hotels
from vendors. Getting to a deal was fun back then.)

The HiPPO needs to be informed that their opinion isn't helpful unless
they can back it up with a POC. If they can't supply the POC, then the
technical folks will keep arguing until they have competing POC's to
help make a technical choice.

With good languages (like Python) and large ecosystems, POC's are cheap
insurance to back up an opinion.

Tech Oracle
-----------

The Tech Oracle is expected to provide an opinion on everything. In many
cases, this can work.

If the architecture is reasonably well known to the Oracle, then picking
open-source projects to help build a solution isn't too difficult.
Filters like "date of last update" and "volume of changes on GitHub" can
be useful ways for the Oracle to locate better components and
frameworks.

The Oracle should be producing POC's. This makes it hard for them also
to produce production code. Not impossible, but hard. Their role isn't
quite the same as other devs, since they have to provide up-front
justification before too much real work is invested.

If the Oracle can't provide POC's, that's a bit of a problem. I've met
architects who don't code. I couldn't find a way to trust them. Yes,
they may know a lot. They're wonderfully articulate. Great slide decks.
Good choices of lunch places where they try to influence you. But... I
don't trust architects who don't code. Sorry. Personal weakness.

Architecture diagrams are an essential work product in addition to
POC's. Usually, they're focused on a specific project, rather than
providing general-purpose guidance. Generally, the overall ecosystem
moves so quickly that the idea of a general-purpose, one-size-fits-all
architecture isn't a good idea.

HashTAG
-------

The Hyperconnected And Socially Helpful Tech Advisory Group is often a
really good thing. It's best when there are multiple teams who need to
coordinate. It can be slow-ish, however, and time needs to be invested
in this. TAG meetings deserve stories on the storyboard. TAG time needs
to be prioritized above individual team needs.

A TAG needs to look at choices, and publish recommendations. That often
means reviewing POC's. And that means folks have to take POC's to the
TAG for them to weigh in on the difficult-to-quantify "better solution".

These are interesting demos. The TAG should be looking at the same (or
similar) functionality from competing POC's to render a final, binding
judgement. There needs to be an agenda, strict time-lines for the
presentation, and a final -- almost objective -- score-card to show the
elements of the final decision.

Decisions are an essential work product. Published. Socialized.
Well-known. Easy-to-find. A whole GitHub repo with decisions is
essential.

Architecture diagrams are also an essential work product. These should
provide general-purpose guidance. A team should be able to start with
one of these, eliminate the parts they don't need, plug in their product
name, and move forward quickly.

Peer Pressure
-------------

This is the HashTAG reduced to a single team. Given a choice, the
members of the team need to look at filters the way the Tech Oracle
should. They need to weigh things like More stars in GitHub? Fewer bug
reports? Documentation? And they need to capture the decision in
something more than a conversation.

If it's hard to reach consensus, this means the team has to commit to
dueling POC's. This needs to be time-boxed work. It's enough of a POC to
show how competing libraries or frameworks \*could\* be used in the
implementation. It's important not to run down the road to a candidate
implementation. The POC should point the implementers in the right
direction.

(A candidate implementation becomes a kind of *fait accompli*: "I've
already built it, we might as well use it. This dilutes consensus in
favor of fast coding.)

Ideally, the POC shows what code could look like. It might include
benchmarks. Test cases. Concrete things that can be compared -- line by
line if necessary -- to show some measurable aspect of "better."

The decision and the diagram are part of the team's legacy. It has to
live with the code. The number of decisions that get redebated after a
few sprints needs to be minimal. It's never zero, but the team needs to
put stories on the board for finalizing tech documentation with
architectural decisions, reasons, and links to the POC that backs up the
decision.

Wait. What about Python?
========================

This, clearly, has nothing to do with Python.

The vastness and rapidity of change in the Python ecosystem surfaces a
need for some kind of formal decision-making process.

But Python isn't the cause of the problem. All open source software
moves quickly. A popular language like Python has more potential sources
of confusion than a more specialized language/framework like R.

Embrace the community nature of decision-making. Python is about
community building and collective solutions to difficult problems.

But. All those Proofs of Concept...
===================================

Yes, there will be POC's. In the case of a HashTAG or TechOracle, these
need to be preserved and maintained and upgraded all the time. It's real
work. It's a lot of real work.

Remember, the Python ecosystem moves rapidly. There's a lot of
innovation, and it needs to be actively tracked. (Unlike the olden days
where a C compiler update was an annual affair buried in an annual OS
upgrade.)

This leads to defining projects via project templates.
See https://cookiecutter.readthedocs.io/en/1.7.2/ for a good approach to
this. You want to create cookie cutters that include enough skeleton
code that you can run a complete 100% code coverage unit test.

You can then use `tox <https://tox.readthedocs.io/en/latest/>`__ (or
`nox <https://nox.thea.codes/en/stable/>`__) to define your component
and framework versions as variant virtual environments. As components
evolve, you update the versions and rerun your test suite. You can
publish internal update trackers for project teams to make sure they're
testing with the latest-and-greatest environments.

You'll also have to watch Python version changes. These can creep up on
organizations. The PEP's and the schedules need to be central to folks
using Python. See https://endoflife.date/python for a handy
visualization.

The Billboard
-------------

Enterprise developers all discover that there's no way to share code
**easily** within an enterprise. Everyone is isolated in their teams,
and each team winds up reinventing some wheel or other. It's been an
ongoing problem since IT organizations grew beyond a single team.

Python is no different. Teams solving related problems don't talk
enough. If you have lots of meetings to share things, no real work gets
done.

Python uses a Package Index to track popular useful packages. Visit
https://pypi.org if you haven't seen it yet. You have two paths forward
in an enterprise.

-   Your own PyPI. This is easy and fun. You can have the internal PyPI
    shadow the global PyPI.

-   Use JFrog Artifactory. https://jfrog.com/artifact-management/ This
    involves spending money to track in-house artifacts as well as global
    PyPI artifacts.

-   A GitHub Billboard organization. This is an organization that serves
    as a place to post links to other repos. It needs a little bit of
    curation. As an implementation, the organization's repositories are a
    lot of small project advertisements. The degenerate case is a README.md.
    A better case is the POC repo showing how to use the real project. In
    the middle is a cookie cutter. This is your in-house advertising. It's
    relatively easy to search because you're looking at one organization's
    list of repositories. Each is a pithy, focused summary of another
    project. Choose names that reflect why someone wants to look more deeply
    at the project.

The point here is to embrace the chaos that stems from innovation and
make it visible.





