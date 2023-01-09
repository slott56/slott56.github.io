Implementation
==============

:date: 2005-10-11 11:02
:tags: architecture,design,methodology,process,agile
:slug: 2005_10_11-implementation
:category: Architecture & Design
:status: published





An implementation document is prepared along with
the software to present the packaging and component structure, including visible
interfaces of components.  This shows the structure of the final deliverables,
and describes the files, databases and other persitent features of the system. 
This document will also identify all third-party components
used.



The implementation depends on the
design, the architecture and the
requirements.



This process summarizes
implementation, omitting the difficult problems of testing and
integration.



**Content** 



Final
software.  Typically source, plus executable form.  This of course, varies with
language.



UML diagrams for packages and
components.



Either UML diagrams or
narratives describing the packaging and installation
procedures.



**Process** 



For
each architectural component, create a detailed design of all classes required
to implement the component.

1.  Define the overall responsibilities and
    constraints.  Write a clear statement of the component.

#.  Determine the entities, associations,
    operations and attributes in the statement of the component.  Noun and verb
    analysis of the statement is a good starting point.

#.  Select appropriate design patterns for the
    overall structure and relationships among the classes.  This will help select
    design for associations, state and collections.

#.  Select appropriate data structures and
    algorithms.

#.  Construct diagrams.

#.  Validate the design via a "walkthrough." 
    Follow each relevant use case's execution through the classes and methods in the
    design.  Confirm the responsibility
    assignments.



Construct the source. 
Stick to widely used standards.  Read open source projects for examples. 
Consider the use of literate programming tools to merge design and source into a
single
document.



**Standards** 



Trace
back to architectural components and requirements.  Every class belongs to a
package, every package has one or more classes.  Each component is built from
packages of classes.  Each package contributes to one or more
components.














