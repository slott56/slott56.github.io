Essay 7 - Application Design
============================

:date: 2005-09-09 15:27
:tags: architecture,design
:slug: 2005_09_09-essay_7_application_design
:category: Architecture & Design
:status: published





Architecture is the first step in creating
software to meet the requirements.  This is followed by the design effort to
transform the high-level picture into components that can be realized in
software.  This line between assemblies of components, and the internal
construction of components is a good dividing line between architecture and
design.



It is generally best to use
well-known and widely used design patterns when developing a design.  This
creates a design with elements that are reasonably well understood, and lead to
early confidence that the design will meet the
requirements.



A common component is a
stand-alone application.  This may be a fat-client application that runs on a
desktop, or a web application accessed through the browser.  An application
typicall has five layers or tiers:

-   **View** .  The presentation of data to the users,
    or other interfaces.

-   **Control** .  The sequence of activities or state
    changes to manage interaction.

-   **Model** .  The underlying data model that the
    application manipulates.  This is optimized for interaction, and may differ from
    the persistent data structure.

-   **Access** .  The mechanism for acquiring
    persistent data.  This may be CORBA, JDBC or other access
    mechanism.

-   **Persistence** .  The mechanism of persistence. 
    This may be the file system or the
    RDBMS.



Each of these has more narrowly
defined responsibilities.  The overall functionality of the application can then
be partitioned according to these layers.  Once the larger problem is
decomposed, each can be tackled and built
separately.



Generally, it is best to
proceed up the hierarchy.  The first phase of effort moves from persistent data,
through access, to the model.  This creates a simple framework for the
following:

-   Validating the persistent data model. 
    The initial design may have ommitted classes or attributes, or mis-communicated
    those.

-   Assuring that the access methods meet
    requirements.  The initial design may have omitted useful navigation paths or
    other physical access mechanisms.

-   Developing a usable application data
    model.  The matching between the working model and the persistent model must be
    resolved and tested.



Once the
Model-Access-Persistence is in place, then the View and Control can be added. 
It is critical that the model's methods be completely tested before attempting
to add view and control features.  If the model is incomplete, inconsistent or
incorrect, and these problems are fixed in View and Control, then reuse is
compromised, and the essential functionality is spread across the
application.



Since the essential
feature of object-oriented design is correct assignment of responsibility,
spreading application features through multiple layers defeats basic good
design.  For this reason, the essential functions must be completely developed
and tested in the lower layer of the application design.  Then the GUI can be
fastened onto a working structure.
















