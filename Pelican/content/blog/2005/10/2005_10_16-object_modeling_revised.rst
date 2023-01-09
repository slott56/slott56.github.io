Object Modeling (Revised)
=========================

:date: 2005-10-16 18:16
:tags: architecture,design,methodology,process,agile
:slug: 2005_10_16-object_modeling_revised
:category: Architecture & Design
:status: published







**Objectives** 




To write software, we need to understand what we're doing. We need to have a well-defined universe of discourse. This understanding must be documented. The documentation proceeds through increasingly refined levels of documentation. 





1.  English prose.

#.  Diagrams and other semi-formal notations.

#.  Formal notations (BNF, IDL, Java, etc.)

#.  










Sometimes, the first or second level of formality (prose or diagrams) is skipped, reducing this approach to two levels: informal and formal.







The documents often iterate between the various levels because the increasing formalism often uncovers problems in the less formal representations. We rethink the less formal version, and identify a simplification or a missing feature; this begins the cycle again.








Various steps in this process will often benefit from prototyping. For example, when trying to capture the english prose version, an initial UML diagram helps clarify. This prototype is then discarded and the more refined UML model used to generate final Java code.









Mistake.









It is common to correct problems in the more refined levels, but not go back to the less refined levels and reconcile all the various descriptions.  Be sure to go back and reconcile all of the descriptions.










**Procedure** 











A formal procedure constrains free thinking. In this case, that's the point: object modeling is not expressionist painting. It is science (not engineering); it is an attempt to fully describe something in formal terms. As a science, object modeling forms a testable hypothesis based on observation, experimentation and measurement.












Experimentation can be done via prototyping - building something to see if it fits the theory or refutes the theory. The information gained may then modify the theory, leading another lap around the iterative track. However, prototyping in the early phases can be harmful; it tends to narrow the thought process.













#.  **Write a short summary of the problem at hand.** 

#.   If you have requirements, project scope documents, text book examples, or other references you can try to take a high-lighter to this text; however, it's hard to internalize that way. It's easier to internalize by rewriting from scratch, aiming for succinct explanations without background or justification. Many documents have to explain and justify much.  When modeling, you have to capture the entities and associations, but the why's and wherefore's aren't part of the object model.

#.  


#.  **Identify the entities (nouns).** 

#.   This is part of internalizing the model; without positive identification of the nouns, you don't have a universe of discourse. I don't know what you have, but when my clients try to rush past this step, their incomplete understanding is a train-wreck waiting to happen. Do not try too hard to assign attributes or associations. Some will surface, so collect them at this time.  Your goal is to identify nouns in a way that you can write a definition, give the definition to a non-expert and have them be able to distinguish among real-world examples based on the definitions.

#.  


#.  **List the nouns.** 

#.   Confirm that the nouns are truly independent entities. Sometimes they are aliases, sometimes they are attributes of each other. Sometimes they are prepositional phrases (associations). Sometimes they are verbs that have been nounized; these are operations of a noun, and can be collapsed into the relevant noun.  Sometimes they are states of a noun; in this case, also, they can be collapsed into the noun's definition.

#.  


#.  The following steps will occur in a non-deterministic back-and forth fashion.  You may also need to look at `State-Based Object Modeling <{filename}/blog/2007/06/2007_06_25-state_based_object_modeling.rst>`_  to see if a dynamic view of the object will help create a definition.

#.  


#.  -   **Categorize the nouns.** 

#.  -    Some nouns are generalizations, others are specializations.

#.  -   


#.  -   **Associate the nouns.** 

#.  -    Put in the prepositional phrases, labeled approximately correctly. Don't burn calories on optionality and cardinality. Don't waste time normalizing. We're only internalizing someone else's description.  You're not designing a database. 

#.  -   


#.  -   **Assign attributes to the nouns.** 

#.  -    Don't waste time on primary keys or foreign keys or surrogate keys. An association will eventually require an implementation, which may be a foreign key; at this time it does not have to be identified.

#.  -   


#.  -   **Assign operations to the nouns.** 

#.  -    Some nouns will be "active" and will be the center of action. Other nouns are "passive" and simply contain attributes and participate in associations.  Some nouns will have state changes, some nouns will be immutable objects that are created and destroyed without any transformations.

#.  -   


#.  -   






#.  



#.  **Write the semi-formal diagram of the objects under consideration.** 

#.   UML or ERD's will do. Don't burn too many calories on details that will be handled in implementation. Don't decide what kind of collection will implement a container, or what kind of foreign key will be used to implement an association.

#.  


#.  **Reconcile.** 

#.  Fix up or revise the original narrative to match the diagram. Fix the diagram to match the new narrative.  If necessary, revisit the external documents (project scope statements, plans, budgets, justifications, etc.) and be sure they match your current understanding; often, they will be seen in a new light and changes must be made.  These changes can be characterized as "scope creep" and labeled as "bad."  Or they can be characterized as lessons learned, management of ignorance, or similar and labeled as "good."

#.  


#.  **Test.** 

#.  Construct object instances to be sure that the general classes of objects describe the specific instances correctly and completely.

#.  


#.  






















At this point, you have an object model that you can use for design and eventually develop into fully formal notation (like Java or Python).


















