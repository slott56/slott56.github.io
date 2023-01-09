The No Code Approach to Software and Why It Might Be Bad
========================================================

:date: 2017-09-12 08:00
:tags: knowledge capture,Design Principles
:slug: 2017_09_12-the_no_code_approach_to_software_and_why_it_might_be_bad
:category: Technologies
:status: published

Start
here: https://www.forbes.com/sites/jasonbloomberg/2017/07/20/the-low-codeno-code-movement-more-disruptive-than-you-realize/#98cfc4a722a3


I'm not impressed. I have been not impressed for 40 years and many
previous incarnations of this idea of replacing code with UX.


Of course, I'm biased. I create code. Tools that remove the need to
create code reflect a threat.


Not really, but my comments can be seen that way.


Here's why no code is bad.


   **Software Captures Knowledge**


If we're going to represent knowledge in the form of software, then,
we need to have some transparency so that we can see the entire stack
of abstractions. Yes, it's turtles all the way down, but some of
those abstractions are important, and other abstractions can be taken
as "well known" and "details don't matter."


The C libraries that support the CPython implementation, for example,
is where the turtles cease to matter (for many people.) Many of us
have built a degree of trust and don't need to know how the libraries
are implemented or how the hardware works, or what a transistor is,
or what electricity is, or why electrons even have a mass or how mass
is imparted by the Higgs boson.


A clever UI that removes (or reduces) code makes the abstractions
opaque. We can't see past the UI. The software is no longer capturing
useful knowledge. Instead, the software is some kind of interpreter,
working on a data structure that represents the state of the UI
buttons.


Instead of software describing the problem and the problem's state
changes, the software is describing a user experience and those state
changes.


I need the data structure, the current values as selected by the
user, and the software to understand the captured knowledge.


Perhaps the depiction of the UI will help.


Perhaps it won't.


In general, a picture of the UI is useless. It can't answer the
question "Why click that?" We can't (and aren't expected) to provide
essay answers on a UI. We're expected to click and move on.


If we are forced to provide a essay answers, then the UI could come
closer to capturing knowledge. Imagine having a "Reason:" text box
next to every clickable button.


We all know what the essay answers will look like. They'll look like
bad comments in code. And bad commit comments in Git. And bad
documentation.


..  csv-table::

   Some Option:, ☑️,Reason:,*Required*
   Other Option:,☐,Reason:,*Not sure if its needed*


The problem with fancy UI's and low-code/no-code software is
low-information/no-information software. Maintenance becomes
difficult, perhaps impossible, because it's difficult understand
what's going on.





