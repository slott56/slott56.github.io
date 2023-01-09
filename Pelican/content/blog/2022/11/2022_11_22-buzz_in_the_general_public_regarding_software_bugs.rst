Buzz in the general public regarding software bugs
==================================================

:date: 2022-11-22 10:17
:tags: software process improvement,API Design,defensive programming
:slug: 2022_11_22-buzz_in_the_general_public_regarding_software_bugs
:category: Technologies
:status: published

I got this the other day: "there seems to be a lot of buzz out in the
general public regarding software bugs".


Attached to this was an article from The Economist in 2003 plus one
from 2010. To me, this doesn't seem to be a "lot" of buzz. But what
do I know?


Further, it did *not* come from someone outside the software/IT
industry. It came from a DBA. I guess the presence of this email in
my inbox must mean some DBA's are surprised that there are bugs. I
guess they were surprised to see "bug" in a general-interest
magazine.


They also forwarded a link to http://www.glitchthebook.com/. This
looks more interesting than a writer for The Economist
(http://www.economist.com/) providing information to a general
audience that every professional should already know.


I guess it could be interesting when someone notices "bug" in a
general-interest magazine.


Hidden Cost Hogwash
-------------------

I object, however to this "hidden cost" hogwash. Bugs have an
explicit, obvious, direct cost. There may be "hidden costs" but they
are largely irrelevant and pale in comparison to direct costs.


What we need are articles not on the "hidden cost", but on actual
bugs. In particular, there are two kinds of actual costs that we need
to look at: "hidden bugs" and "compound bugs".


-   **Hidden Bugs.**
    These are things simply below the user interface
    level. They're present and they're often worked-around by UI
    hacks. Hidden Bugs are more costly than visible bugs. Complex
    multi-layered and multi-component architectures are packed with
    hidden bugs.

-   **Compound Bugs.**
    These are hidden bugs where the workaround also
    has a bug. The interface file has an intermittent glitch, so the
    web services are cluttered with **try:** statements. The **try:**
    statements, themselves, harbor bugs, so we have to then add
    **assert** statements and declare it "defensive programming". The
    net effect is to simply log something that was provided to the
    interface incorrectly. Sigh.


We shouldn't waste time talking about "hidden costs" of glitches
when we aren't even sure what the actual up-front costs are. If we
knew the costs, we'd spend a bit more on the software to prevent
the bugs in the first place.

We also shouldn't be surprised to see "bug" in a general-interest
magazine.



