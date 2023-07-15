Essay 19 - Disentangling Use Cases and GUI Design (Revised)
===========================================================

:date: 2005-09-24 11:40
:tags: architecture,software design
:slug: 2005_09_24-essay_19_disentangling_use_cases_and_gui_design_revised
:category: Architecture & Design
:status: published





There are two layers of use case authoring and
minimal consensus on which level is "right" for any particular
purpose.

1.  Business Level use cases - ignore the presence
    or absence of a GUI, and pursue the business problem. This leaves designers free
    to create any GUI, perhaps one that is not so easy to use.

#.  Interaction Level use cases - dwell on
    detailed interactions with GUI elements, presuming an overall business context
    in which these interactions create value. This can ignore larger Business Issues
    in favor of simple productivity.



There
are more and less detailed levels, also. There is less confusion about these
additional levels.  At the highest level, people sometimes write
application-level use cases that involve interactions among enterprise
applications. These are focused on Enterprise Application Integration (EAI)
issues.  At the lowest level of detail we see use cases that specify the
interaction among individual objects.  Typically, each layer involves "5
plus-or-minus 2" more detailed interactions at the next lower level of
detail.



**Use Cases** .  The definition of a use case (An Actor
interacting with a System to create business value) tells me that a use case is
**business** 
focused, and anything more detailed is more of an operating scenario. This
leaves us with two levels of operating scenarios: business-level and
user-interaction-level. However, the context is now much more clear. Business
Use Cases focus on value creation, not on the software technology of how that
business value is created. User Interaction Scenarios implement use cases by
showing the steps a person performs to create that
value.



There can be a proper tree from
one use case to a few variant business scenarios to a number of of user
interaction scenarios. This makes requirements traceability simple. However, it
is not strictly necessary; often, a clever application scenario may address
multiple use cases.



**User Interaction** .  There appears to be a tangled
hierarchy between use cases and GUI design. We know that use cases should come
first, and GUI design should be based on use cases. However, it often appears
that the use cases need to presuppose some GUI in order to step through the
user's interactions with the system.  How do we draw the GUI when we don't have
use cases?  How do we document the use cases when we don't have a GUI? 
Something has to come first.



This
situation often indicates that the use cases aren't business focused in the
first place, but technology focused. People who can't write their use cases
without sketching the GUI have conflated business value and software
implementation. They need to step back and define the value creation first. Then
(and only then) can they propose a GUI and work through interaction scenarios
that implement the business-value use cases.




Writing the use case without a GUI
often seems like a pointless exercise.  Analysts (or users) complain that until
they know the details of how a person will execute their job, they can't specify
what the job accomplishes.  Worse, when you reflect that back, they're
comfortable saying that the goal comes from the detailed steps.  This means that
they aren't comfortable articulating the business goal.  Perhaps the goal is
vague, or perhaps there are political considerations that make it difficult to
expose the real business purpose. 




Generally, however, the reason people
can't articulate the business goal is because they are focused on developing a
specific technical solution.  Business analysts working for IT are often guilty
of channeling the user's business needs into technologies.  Business users with
a technology background or hobby are just as bad at "translating" the business
need into IT terminology to "help" the business analyst.  Both are steering the
use case analysis into GUI interaction design, and neither will successfully
articulate the actual purpose behind the interactions.










