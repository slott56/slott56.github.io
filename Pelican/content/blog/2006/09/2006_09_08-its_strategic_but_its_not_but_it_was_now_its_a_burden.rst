It's Strategic -- but it's not -- but it was -- now it's a burden
=================================================================

:date: 2006-09-08 13:06
:tags: strategic,Enterprise IT,technical debt
:slug: 2006_09_08-its_strategic_but_its_not_but_it_was_now_its_a_burden
:category: Management
:status: published





Here's the scenario I see:

1.  The customer bought something, and then
    customized it.  The customization -- by definition -- must have had significant
    strategic value.

#.  The customer set it aside, making no more
    changes of any kind.  Okay, there were bug fixes, but nothing significant.  The
    developers were re-assigned to something new.  Perhaps a maintainer was brought
    in.

#.  After a decade of neglect mixed with casual
    bug-fix and work-around maintenance, they call and want a significant change to
    the functionality.  The word "strategic" is used. 




The cost, of course, is astronomical. 
Our proposal gets thrown out because we're going to charge a fortune for someone
to reverse engineer the software.  The neglect appeared to have a minute cost,
setting up the appearance of a low-cost piece of application
software.



However, neglect is a cost
which accrues from year to year.  The total cost of a decade of neglect is now
owed.  The lost knowledge has to be rebuilt.  Then software designed based on
that new knowledge.  Then the old software reworked to the new
design.



What Happened?
--------------



It's hard to say why
software is Strategic when it's being acquired and customized, but non-strategic
for the rest of it's service life.  I've heard it described as **Executive ADD**\ ™:
an inability to focus.
This means that every shiny new idea wind up with the label "Strategic" so that it's
acceptable to pour resources into it. 




One consequence of Executive ADD is
`Turnover in IT <{filename}/blog/2006/07/2006_07_11-the_root_cause_of_turnover_in_it.rst>`_ .  Another consequence is poor
quality:  nothing is ever improved or refined.  Instead it is implemented, then
the ADD kicks in and everyone is assigned to the next shiny new
thing.



What causes this flip-flopping? 
I think there are several reasons, all of which stem from a feeling that
**Software is Omniscient**.  Once we install it, it will so
regulate and structure our work-life that nothing bad will ever happen.  Once
we've tested it, it cannot be misused, it's a **Thing of Beauty and A Joy Forever**.



Clearly, **Executive ADD**\ ™ is caused by the failure to see how
people abuse and mistreat software.  



I often see examples of the `Third Christmas Club Problem <{filename}/blog/2005/09/2005_09_17-essay_13_analysis_without_running_aground.rst>`_ : there's a field
that isn't currently in use, so we can put data in there.  Sometimes we'll find
that our business entity has multiple state changes, but only one status code,
so end users invent new status codes to reflect combinations of the various
states.



Invisible Abuse
---------------



Why don't managers and
executives see this envelope-pushing and mistreatment?  A couple of reasons
spring immediately to mind.

1.  The business process is already so complex
    that there are numerous manual operations; fudging things in the software is
    largely invisible against the background noise of manual
    processing.

#.  There are limited skills or interest in
    knowing what is really going on.  Who really wants to watch their staff doing
    customer account updates all day just to be sure nothing "funny" is going
    on?



What we wind up with is a perception that "Strategic" software is a **Fire and Forget**  proposition.
Once installed, it runs on autopilot forever.  The complexities are inherent in the business, and the
details are boring (or complex), so we'll never be 100% rock-solid sure that the
software is being used properly.



Choices
-------



We have really two choices: (1) treat strategic software like any other strategic
asset and work to improve it, or (2) don't call it strategic unless it really is
the centerpiece of the business for the next few years.



If it's a strategic asset, it's
someone's job to make sure it works, and to make enhancements and improvements. 
It isn't a maintenance (read "bug fix") job.  It's strategic, visionary, a
differentiator, a source of ongoing value creation.  This means that there will
be revisions, expansions, integration, new features and roll-outs.  This will
look more like a for-sale product than in-house, back-office information
technology.



If it's merely business-critical, it's something you install, and then assign a maintainer to
apply bug fixes.  It isn't a differentiator; indeed, all your competitors may
have the same thing.  The vendor-supplied upgrades will be dutifully installed
as necessary.



Customization
-------------



Where does customization fit into this stark dichotomy?  There is really only one
proper role for customization, and that's to transform commodity software into
strategic software.  If the customizations are strategic, then they are
visionary and a differentiator, a source of ongoing value creation.  Someone
owns those customizations, and their job is to leverage those customizations
throughout the business to maximize their
value.



I think this is the only way to
avoid the following Haiku, called "Please Replace it,"

*It's heavily customized,* 

*We can't install an upgrade,* 

*We don't dare touch it.* 














