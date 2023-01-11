Web Services and Architecture
#############################

:date: 2007-05-22 23:11
:tags: books,building skills,#python
:slug: 2007_05_22-web_services_and_architecture
:category: Books
:status: published







Thanks to everyone who attended.  See `Designing Web Services with the J2EE(TM) 1.4 Platform : JAX-RPC, SOAP, and XML Technologies <http://java.sun.com/blueprints/guidelines/designing_webservices/>`_  for more information.
Also, check out Dr. Dobb's `SOA, Web Services and XML <http://www.ddj.com/dept/webservices/>`_  department.



Here's the Micro$oft PPT file:  `Web Services 8.ppt <{static}/media/Web%20Services%208.ppt>`_



Here's the Open-Office file:  `Web Services 8.odp <{static}/media/Web%20Services%208.odp>`_



Also, here's a more useful thing: the actual contents.  


----------

Web Services
============



8 – Architecture



Steven F. Lott



Agenda
======


Nuclei around which architecture crystallizes



Architecture Design Patterns



Decision Nucleus
================


Interface-Driven Decisions



- External Interactions are typically web services



Several Implementations



- Heavyweight, SOAP document services



- Lightweight, RPC services



- Informal CGI and other HTTP services



Decision Nucleus
================


Data Model- or Processing- Driven Decisions



- Complex or Core data



  - Can be accessed directly (through JDBC)



  - Or indirectly through a web service



- Complex Processing



  - Can be accessed through a web service as needed



  - Or built as a batch job and run periodically



Business Focus is essential



Decision Nucleus
=================


Mutability-Driven Decisions



- If the implementation will change,



  - wrap it in an interface that won't change.



Special cases are often mutable



- So wrap them in a web service



Interim Solutions



- Best to wrap them in a service



- Replace the interim implementation with the final



Poor Choices for Web Services
==============================


Individual Data Entity Access



- Entity-Level services are too fine-grained



- Each CRUD operation has to be exposed



- It basically wraps the SQL, adding overhead



  - With no measurable value



Technical Processes (ETL, for example)



- Moving "Customer" from system to system isn't what a service does



  - No Business Focus – just data massaging



Service Design Questions



- Where's the system of record?  Who's the keeper of the master data?



- What do other systems need this system to DO for them?



- The system of record may publish useful services



Data Movement/ETL
==================



Single sources for Master Data?



- Then a single Service for this data



Duplicate sources – overlapping Master Data?



- System X source copied to System Y where extra attributes were added



- Coalesce into a single source, if possible



- Make multiple applications share a single, central service for the data – where possible



Multiple sources – multiple parts to the Master Data?



- System X has some records, System Y has other records



  - Union of these two systems is the master data



- Hard to coalesce, but a Single Service can wrap multiple sources for consistency



The Java Blueprints Reference Application: Adventure Builder
============================================================


See https://www.oracle.com/java/technologies/java-blueprints-guidelines.html


Adventure Builder
=================


A J2EE application that presents an application to end-users 



Consumes Web Services for a number of Back-end Operations



Suppliers and Finance are external interfaces



CRM is a shared data structure



Workflow is Process-driven



Order Receiver is a mixed bag



The Granularity Issue
======================


Services which are too small ("chatty")



- Endless back-and-forth



- Too much SOAP overhead for the real value



Services which are too large



- Giant XML messages



- Long-running web services



In the middle is a balance



- This is more art than science



Business focus is key



Business Focus
===============


It's all about Agility



It's all about Master Data



- One source for the data



- One source for the processing



It's all about **Assignment of Responsibility**



Important Questions:



- What is really happening?



- Is that business-related or is that a dumb technology work-around because of rubbish legacy software?



- MUCH of what passes for "business analysis" is really IT reverse engineering




