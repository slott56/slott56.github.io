Learning Styles -- The Astonishment Response
============================================

:date: 2010-04-12 08:00
:tags: software process improvement,learning,architecture
:slug: 2010_04_12-learning_styles_the_astonishment_response
:category: Technologies
:status: published

We're not really talking about "`Learning
Styles <http://www.ldpride.net/learningstyles.MI.htm#Learning%20Styles%20Explained>`__"
as much as "Denial Styles". This is a list of responses to
"Astonishment" I've seen.

We're not talking about the Kübler-Ross model of grief, although this
is similar.

However, the response to astonishment isn't a "progression" toward
acceptance. Some folks simply don't like to learn and are perfectly
capable of arguing down the facts because they don't fit with
assumptions and preconceived notions.

When faced with new information, some folks seem to have a consistent
response to astonishment. Other folks seem to jump around among a few
preferred responses. Additionally there are people who seem to prefer
to escalate things to a crisis level because learning seems to
require adrenaline.

**Oh**. Classic acceptance. Many folks start here; which is pleasant.
It saves a lot of email traffic. When astonished, they assimilate the
information without really fighting against it.

**That Can't Be True**. Classic denial. It's surprising how often
this happens. Even when confronted with facts *supplied by the
learner themself*.

Example. The DBA says stored procedures are a maintenance problem.
You say, "Correct, perhaps they shouldn't be used to heavily".

The DBA asks "Why reduce dependence on stored procedures?" You say
that, amongst other things, "they're a maintenance nightmare."

And the DBA says, "That can't be true; it's just a management
problem." WTF -- Wasn't That Funny -- the DBA is going to deny their
own facts in order to avoid learning something knew.

**I Wasn't Told.** This is a kind of grudging, negotiated acceptance.
"What you say about bubble sort being inefficient may be true, but I
wasn't told." Okay. You weren't told. Does that mean that I have to
email all of Don Knuth to you so that you will have been "told"?

**I'll have to see it**. This is really just a basic denial wrapped
in the terms of settlement. In short, the learner is saying, "I still
disagree with all your facts." I'm not sure what "I'll have to see
it" means when we have working implementations of something "new" or
"different".

Example. A: "RESTful web services are simpler." B: "No." A: "No SOAP,
no WSDL; seems simpler." B: "Perhaps, but I'll have to see it." See
what? How can you "see" the absence of complex WSDL?

**This project is out of control**. This is a somewhere near grudging
acceptance. It might also be a form of reneging or repudiation of
acceptance. It's hard to say.

Example. Manager: "The Ontology has thousands of objects with dozens
of properties and the SPARQL processing is slow." Architect. "Replace
it with a relational database derived from the ontology." Manager:
"Okay".

Four Weeks Later. Manager: "This Project is Out of Control."

Right. We're making a disruptive change to the architecture. What did
you expect? Non-disruptive change? How is it change if it doesn't
disrupt *something*?

**Does Everyone Know This?** This is a form of "I wasn't told". It's
my favorite because it projects one's own knowledge-gathering onto a
mysterious "everyone". I'm not sure why some folks say this. To me,
it seems a pretty bold statement about the mental states of other
folks on the team.

**That's Non-Standard**. More properly this should be "That's
atypical" or "That's unconventional". This is another negotiated,
grudging acceptance. But it's a pretty complex deal. The first part
is to establish a convention. Sometimes a legacy usage needs to be
elevated to "typical" or "conventional"; other times legacy usage
already is conventional. The second part is to realize that the new
thing is different from the convention. The third part -- which is
subtle -- is to deprecate something new because it is unconventional.

Example. Architect: "You should use a HashMap for those dimensional
conformance lookups." Programmer: "Not everyone understands those
fancy collection classes, so we use primitive arrays." Architect:
"That's amazingly slow. It's less code to build and lookup a HashMap,
and it runs faster."

Programmer: "That would be non-standard". Architect: "There's no
applicable ISO standard. Perhaps you mean 'unconventional'."
Programmer: "Right, unconventional. And we can't change now because
it would disrupt the established code base."

Architect: "It will be less code and run faster." Programmer: "I'll
have to see it."

**Doesn't That Contradict Something?** This is best nit-picky form of
denial ever. Step one is to analyze each word of the suggested
change; in some cases, using the level of care appropriate to
studying the
`Talmud <http://www.myjewishlearning.com/texts/Rabbinics/Talmud/Talmud/Studying_Talmud.shtml>`__.
Step two is to locate something that could be construed as
contradictory. The third step is to deprecate the new thing because
it can be linked to something that can be seen as contradictory.

Architect: "Can we add some formal assert statements in the tricky
actuarial scoring algorithm. It involves non-obvious assumptions
about NULL's and ranges of values." Programmer: "No. That contradicts
your earlier advice to unit test all those corner and edge cases."

Architect: "Contradict? Perhaps you mean it's redundant." Programmer:
"No, it's clearly contradictory; one never needs both assertions and
unit tests. You demanded unit tests, that means that assertions are a
contradiction."

Summary
-------

Other than patience, it's hard to provide any other advice on how to
work through these things. Mostly, these are fact-free positions. In
some cases, even facts don't help the learning process.

I think the only way to cope with a fundamental refusal to learn is
to ask what it takes to convince them. In many cases, the answer
amounts to "Do the entire implementation two ways and then
micro-examine each nuance of performance, maintainability,
adaptability and cost to the organization over a period of a decade
before I'll consider your worthless opinion."

I remember once being asked -- seriously -- how I can possibly claim
one implementation is higher performance than another. The question
was asked as if "measurement" didn't apply to software performance.
At the time, I couldn't figure out why "measurement" wasn't the
obvious fact gathering technique. Now I realize that they were simply
refusing to learn and didn't care about evidence; they simply didn't
want to change to a more efficient implementation.





