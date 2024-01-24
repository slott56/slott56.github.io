Essay 22 - Predictability, Hysteresis and Idempotency
=====================================================

:date: 2005-09-19 23:50
:tags: architecture,software design
:slug: 2005_09_19-essay_22_predictability_hysteresis_and_idempotency
:category: Architecture & Design
:status: published





It can be said that software is 'non-linear and
time variant. ... The output is definitely not just a function of the current
input.'



Whilepossibly true in one sense, the described understanding has to conflate a number of
things into "software". The conflation makes it very difficult to take action to improve
predictability.



Hysteresis and Idempotency
--------------------------



Software does not wear
out or change behavior.  If you want to talk about physical damage to media, you
are conflating software with the computer system, including hardware and
entropy.  Or, if you are talking about unintentional overwriting of software
files (the Windows "corrupted DLL" problem) you are conflating application
software plus buggy OS
software.



Software is idempotent: the
outputs reflect the inputs every single time.  To say otherwise is to conflate
the software with the running application plus persistent data.  Or, worse, to
conflate the running application plus persistent data plus user inputs.  While
the software is idempotent, your scenario may exploit a timing dependency,
making it difficult to predict the
results.



The hysteresis question is "do
you know all of the inputs?"  You may have hidden inputs.  There may be inputs
which are outside the declared variables, class definitions, packages and
dependencies.  There may be inputs which are buried as defects or ambiguities in
the programming language  formal specification or its implementation.  In the
case of Java, it could be either in the Java Language Specification or your
particular JVM.   In languages like C, you'd have a hard time pinning down all
of the hidden inputs in language and implementation.  They can be enumerated --
it's all just software -- but it can be challenging because it is a lot of
software.



There are two sources of
"Unpredictability" in software:

-   The presence of bugs makes behavior hard to predict. 

-   The sheer size of the software that makes
    it unpleasantly difficult to predict. 




One oft-cited issue is timing
dependencies: are these bugs or are we just overwhelmed by complexity?  They're
bugs.  A race condition means that timing matters: when timing matters, this is
a bug.  Period.



Software (Ideal) vs. Computer System (real)
-------------------------------------------



We can make a distinction
between software "as designed -- in the realm of ideas" and software "as
implemented -- in the realm of hardware".  This gives us two senses of
predictability.  One a mathematical absolute, with idempotency.  The other is a
stochastic process where things wear out and
break.



We can also separate what we
mean by correct behvior: the "as designed" behavior vs. the "meets requirements"
behavior.  There are two senses of what our basis for comparison is: "Designed
Behavior" vs. "Desired Behavior".  The desired behavior is notoriously slippery:
users lie, fail to tell the whole truth and change their mind.  The designed
behavior, again, is a mathematical
absolute.



Consequently there's this
little grid.  (But iBlog doesn't handle HTML formatting well, so we'll unwind it
into a hierarchy)



Ideal Software
--------------


-   **Designed Behavior**

    Software -- the formal language --
    matches the designed behavior perfectly.  Any failure in predictability here is
    failure to understand the formal language.

-   **Desired Behavior**

    Software matches what is required or
    intended; the extent to which it fails can be called
    **Design Noise** .

Real Software
-------------

-   **•Designed Behavior**

    A computer system (hardware+software)
    matches the designed behavior to the extent that the implementation of hardware
    and operating system is correct.  It also matches to the extent that language
    and run-time environment work correctly.  The extent to which this fails can be
    called **Implementation Noise** .

-   **Desired Behavior**

    A computer system (hardware+software)
    match against the required or intended behavior depends on both
    **Design Noise**  and **Implementation Noise**.


**Design Noise**  is all about process.  A good process
gives you an acceptable level of noise.  Having no process at all, of course,
produces noise so huge you may never get a chance to finish the project.  It
gets cancelled because of "scope creep" or other goofy management fiats.  If you
have no process, you cannot hope to control design noise.  Indeed, the very
reason for defining a process at all is to identify sources of design noise by
having a repeatable work effort and
deliverable.


**Implementation Noise**  is all about tools.  You can, with
appropriate tool use, reduce this noise to very, very low levels.  Can you
eliminate it?  My argument is "yes".  A simple-enough language, a simple-enough
OS, and a simple-enough design approach makes this very doable.  Most popular
tools fail the simple-enough test.  However, this is a noise source that is
controllable and measurable because it doesn't involve people and process; it
involves relatively static hardware and software.  Experiments are easy to run
and rerun.  Statistics aren't involved; this is basic cause and
effect.



Controls
--------


Control Design Noise with process and reviews of work products.


Control Implementation Noise with tools to automate testing.


















