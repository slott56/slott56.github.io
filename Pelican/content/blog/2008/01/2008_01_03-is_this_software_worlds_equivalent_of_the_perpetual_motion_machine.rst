Is This Software World's Equivalent of The Perpetual Motion Machine?
====================================================================

:date: 2008-01-03 11:01
:tags: architecture,software design,data structure,algorithm
:slug: 2008_01_03-is_this_software_worlds_equivalent_of_the_perpetual_motion_machine
:category: Architecture & Design
:status: published







See Spolsky's `Talks at Yale, Part 1 of 3 <http://www.joelonsoftware.com/items/2007/12/03.html>`_  for a fairly typical summary of formal methods in software development.  Here's the part RL liked: "Now, if the spec does define everything about how the program is going to behave, then, lo and behold, it contains all the information necessary to generate the program!"



RL sent me this link, and tried to create a "perpetual motion" metaphor for Joel's comments.  The thermodynamics parallel seems to stem from thinking that a suitable spec must be of the same level of detail and sophistication as the resulting program.  Joel certainly makes it seem that way with his horror story of an all-day affair to prove simple assertions about simple assignment statements.



This is essentially a "formal methods can't work -- it's logically impossible to use logic" argument.  In Joel's case, there are two points.  First, since you need to both know and prove everything about a program, the formal post-condition is so complex that it essentially *is*  the program.  His other argument is that the proof is just as likely to contain errors as the resulting program.  Compounding this, RL has an inappropriate metaphor.



Complexity and Abstraction
---------------------------



Generally, Joel's position on complexity is false.  In some special cases, it might be true.  But those are special cases where you have no trustworthy (proven) compiler, no trustworthy (proven) libraries, and no previous results on which we can rely.  This is often true in an academic setting, but it is far from true in the "real world".



As a practical matter we have two ways to use formal methods that make practical, useful sense.  Fundamentally, these are simply abstraction techniques; we apply one to the specification and one to our languages, libraries and tools.



Additionally, Joel's point on "everything about how the program is supposed to behave" is misleading.  We don't -- ever -- write down "everything".  If we did, we'd have specifications that explain digital logic, power distribution, memory access, sequential programming, interrupt management, direct memory access input/output devices, and how a simple integrated circuit can flip on and off a billion times each second.  Think of having to specify how data is encoded on the surface of a disk, just to be sure "everything" was in the specification.



So Joel's "everything" doesn't really mean "everything".  He seems to mean "everything relevant at the level of abstraction at which I'm proving things."  The problem arises with the mismatch in abstraction between his proof technique and the problems he wants to solve.  This arises partly from textbook examples that are necessarily simple enough to make sense.  These don't scale in an obvious way to a large, complex program.



Read Dijkstra (`A Discipline of Programming <http://www.amazon.com/Discipline-Programming-Prentice-Hall-Automatic-Computation/dp/013215871X>`_ ) and Gries (`The Science of Programming <http://www.amazon.com/Science-Programming-Monographs-Computer/dp/0387964800/ref=pd_bxgy_b_img_b>`_ ).  These were life-altering books for me.  Gries, in particular, provides a wonderful text-book approach that builds a thorough foundation in logic, propositions and proof techniques before diving into a simple language, and ways to develop programs.



There are some exercises which hit on the "prior results" issue as a subtext.  For example, one exercise in Gries asks you to prove that swapping two elements of an array leaves the rest of the array intact.  This is -- to an extent -- a duh proposition.  "Of course swapping two elements leaves the array intact," is the standard response.  However, what's the *proof*  of that glib assertion?  Once you have this, you don't ever need to prove it again.  Indeed, you can -- without too many problems -- omit this trivial detail from a post-condition.  In short, your prior results serve to abstract details away from the real problem.



In The Real World
-----------------



The examples in Gries and Dijkstra are pleasantly focused, bounded, and -- in some cases -- intentionally gnarly.  Real world problems tend to be vague, sprawly and rarely have gnarly parts.  For example, if we're matching financial documents (invoices with receipts) we have some common attributes, and some "business rules" that allow customers to partially pay, overpay, split invoices or combine invoices.  There's nothing gnarly about this.  Mostly, there's just vagueness and odd special cases, exceptions, and unstated assumptions.



Proof techniques are appropriate for the complex nested loops of this application.  Partitioning the input into "batches" of documents which are likely to be related is an algorithm with a fairly easy to define post-condition, and a relatively low level of gnarl.  



The :math:`\textbf{O}(n^2)` comparison of documents within a batch of likely matches, similarly, has a relatively simple post-condition, and a moderate level of gnarl.  It's the insertion of all the special cases that becomes tedious.  Except, of course, for abstraction.  All the special cases are subclass of a common "Condition" or "DocCombo" superclass.  We have to prove that our abstract superclasses have the right properties.  Once we have that, we simply prove that each subclass satisfies the superclass assertions.



Did we specify "everything?"  Actually, no.  We omitted specifying the OS, the RDBMS, or the JVM.  We omitted specifying how the logger works; we just used it, with a blind level of trust that it was reasonably rigorously proven.



Okay, did we specify "everything at this level of abstraction?"  Again, no.  We specified the core algorithms for batching and matching.  The post-processing involves an API call that has a loop through the batch.  Does this loop require a full, formal proof?  Or can we inspect it, determine that it fits a proven template, and leave it at that?



Buggy Proofs Replace Buggy Programs
------------------------------------


Yep.  Can't argue with the argument that a buggy proof is the same as a buggy program.



Here's the clincher.  You don't have tools for testing or validating your proof: you can't easily find "bugs" in your proof.  Instead, you have to rely on manual inspection of the proof.



    [*Irony*] Yep.  That makes the whole technique completely worthless.  How stupid of me to be mislead by charlatans like Gries or Dijkstra. [*End Irony* ]



Rather than lying in wait to attack the technique, we can ask what -- if any -- practical value a proof might create.  Of course, it's easier to indict than it is to consider what value lies hidden with the weakest precondition predicate transformer.  What value is created by attempting a proof?



First, defining a post-condition, and trying to write a formal assertion, is perhaps the single most valuable step that can ever be performed.  If you can't define "done" or "success", you know something important.  Without a definition of done, you know that you'll never finish writing your program.  Without a definition of done, someone will always be able to say "It doesn't do [X]" and you can't prove whether it does or doesn't do [X].  Worse, you probably can't say if [X] is in scope or out of scope.  Worse still, you may not be able to define [X] clearly.



Second, a proof is developed side-by-side with the program.  Joel's example of trying to prove something about a program is specious.  The more productive approach is to locate a statement that has the right post condition, and who's weakest precondition is something that you stand a reasonable chance of implementing.  Then you -- recursively -- start to prove that precondition by locating a statement and it's precondition.  The net is that a buggy proof will grow in parallel with the buggy program.  A tiny bit of test engineering will reveal the program bug -- and the proof bug.



Third, a proof requires that you work at a level of abstraction that makes the program explainable.  One goal is to arrive at a "hands in the pocket" explanation of the program.  Ideally, you want an explanation so pithy, accurate and compelling that it's "obvious" that the associated program has to work.  And it doesn't require pages of UML.  When you're able to abstract/summarize a program in this way, you can deeply understand what it does, why it does it, what the limitations are, and how it fits into it's overall information processing context.



[*Nothing -- nothing! -- is worse than programs which must be carefully reverse engineered into word processing documents.  Think what this means.  Software is a form of knowledge capture.  Yet, we have programs that are so opaque, confusing and dysfunctional that we must read the source to determine  what they might have meant.  When we reach this impasse, we also tend to find that the programs cannot be summarized.  They are a morass of exceptions and special cases, and there is rarely a way to accurately characterize what they* mean *.*]



Perpetual Motion
----------------


The perpetual motion metaphor for formal techniques has one further problem.  Programs and their proofs live in different worlds.  The proof system is a "higher order" logic, distinct from the logic system in which software is implemented.  Proof systems contain a number of concepts that aren't actually part of the software system.



Our computer system relies on a simple Boolean world of True/False and the NAND operator.  Our proof system, however, introduces predicate qualification like "For All" (∀) and "There Exists" (∃).  In order to prove that a loop "makes progress" in each iteration, we may have to introduce propositions that aren't part of the final condition, but are features of our chosen algorithm.  



Our "spec [defines] everything" isn't like perpetual motion at all.  The specification lives in "proof world" where we have abstraction and higher-order predicates.  The program lives in "hardware world" where we have approximations and limitations.



Since our spec is in a "larger" language, we don't have a situation where we need all the details of the finished program in order to write the specification.  The laws of thermodynamics don't apply.  In thermodynamics you can't win, you can't break even and you can't even get out of the game.  In software, your proof system is precisely how you "get out of the game".  This is how you win: you transform a set of well-chosen conditions and proof techniques into a fully-detailed, working program.



[*And no, the fact that you didn't prove verything doesn't indict the technique as worthless.  That wasn't the goal.  Formal methods are a tool that use with version control, automated testing, databases, operating systems, interpreters and IDE's.*]



The Process
-----------



What gets omitted in Joel's notes (and RL's inappropriate thermodynamics metaphor) is the highly directed nature of the process.  The basic theory of formal methods says that we "somehow" derive a final post-condition from the requirements.  Then we prove some "arbitrary" program as satisfying the post condition.



As a practical matter, we aren't stupid.  We have a sense of what works and what doesn't.  We know what we've already proven to work.  We have an idea of what kind of algorithm is required.  We don't write a random post-condition based on the requirements.  When we're doing reading the requirements, we write a post-condition with a hidden agenda.  It isn't a random mapping of requirements words onto post-condition formalisms.  We write the post-condition for the program we intend to develop.  One that we intend to satisfy the mushy English-language requirements.



Then we develop the program, using the post-condition as a formal statement of the goal.  It's hard to emphasize that textbook formal methods demonstrate that we can do *anything*.  Practically, we have some pretty specific requirements that constrain the space in which we're working.  We're not going to flail at random; we're going to take the minimal number of steps to eke out our victory.




