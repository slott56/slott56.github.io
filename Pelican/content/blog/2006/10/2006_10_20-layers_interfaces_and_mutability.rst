Layers, Interfaces and Mutability
=================================

:date: 2006-10-20 18:50
:tags: architecture,software design,UX,UI,GUI,TUI
:slug: 2006_10_20-layers_interfaces_and_mutability
:category: Architecture & Design
:status: published





Here's the full, minimally-edited
question:



    "We are having a debate about
    the basic way the UI, Business Logic, and Data Access layers
    communicate.

    My experience has been
    that the UI talks to the BizLogic, and the BizLogic maps between itself and the
    Data Access layer.. like
    this:

    ::
        UI -> BizLogic -> Data Access -> DB

    The debate is whether the UI should
    see both the Data Access and the BizLogic, and the Data Access object references
    the Biz Object.

    So instead of

    ::

        myBizObject.Save()

    you have

    ::

        DataAccess.Save(myBizObject)

    In my view
    there are a few flaws with this approach, not the least being that the business
    object cannot ask for another business object required for processing, since the
    business layer does not know of the existence of the data
    access."



What's the real problem?
------------------------



We could look at this as
"how do the layer communicate?" but that's can become too broad.  It doesn't
focus on intent, but folds in technology choices, and allows us to wring our
hands over kinds of side issues.



We
should look at much of what has been written about the `Model-View-Controller <http://java.sun.com/blueprints/patterns/MVC.html>`_  (MVC) design pattern.
We'll return to this after looking at layers in general.



I think that it's helpful to
reframe the question as “What are the appropriate bindings between
layers?”  This allows us to focus on cohesive design within a layer
and bindings between layers.  For basics on this topic, see `On the Criteria
To Be Used in Decomposing Systems into Modules <http://www.acm.org/classics/may96/>`_ , by D. L. Parnas.
Additional terms, Coupling and Cohesion were introduced by Constantine and
Yourdon in Structured Design: Fundamentals of a Discipline of Computer Program
and Systems Design.  I like Binding instead of Coupling.



As we go forward, we’ll
have to further reframe the question again into “What is an appropriate
interface design, and how is it separated from the implementation?” 
However, for now, we'll just look at the binding between layers.



Architectural Bindings
----------------------



Usage is bound to
UI.  We know that, and we want that.  We want the users to think of the
application as the UI and nothing more.  The supporting implementation is none
of their business.



Ultimately, the only
thing that matters is the data.  This is an important point; there's additional
supporting material and links in "`Absurdity? Consistent Code and Inconsistent Data
Structures <{filename}/blog/2006/10/2006_10_11-absurdity_consistent_code_and_inconsistent_data_structures.rst>`_ ".



Between the UI
and the Data, there' s a lot of software.  We have “what”,
“how” and “where” (logical data model, processing and
network locations).  We want to strike a balanced solution to the binding
problem.  We want an appropriate level of binding: tight enough to assure
things work without tying up too many resources in endless layers of
meta-programming; loose enough that we can make changes without breaking too
much.



I'm a fan of `Mutability Analysis <{filename}/blog/2005/09/2005_09_18-essay_14_mutability_analysis.rst>`_ ;
let’s look at what
the potential mutations are:

1.  UI changes should be isolated from the
    processing.  There’s the essential processing and UI which guides a
    human being through that processing.  We know those are independent. 
    However, there’s a lot of potential bleed-through here.  We’ll
    return to this.

2.  Processing changes should be isolated from the
    UI.  When we add details as part of a next release, there are some parts of
    the UI where we want stability.

3.  Processing changes should be isolated from the
    model.  Clearly, a change in process is pretty normal.  A change in
    the data model, however, is less common.  Indeed, the principle reason we
    make software changes is because the users need flexibility to handle their odd,
    special cases.  However, a reasonably good data model may cover many
    variations in processing needs.

4.  Data Model changes must be isolated from the
    processing.  This is less common, but we will often add features to the
    data model, but want the processing (and the UI on top of it) to remain
    stable.  SQL, in fact, encourages this by allowing us to alter tables to
    add features, and to alter indexes without breaking the processing (or the
    UI).



In short, isolation is essential
to allowing flexibility.  We define an interface so that the implementation
is free to change.  We must explicitly separate interface from
implementation.  



Really, we're binding
one layer's implementation to another layer's interface.  This is the secret
sauce that allows our bindings to remain
flexible.



Technology Implications
-----------------------



Generally, we want
some immunity from technology changes, as well as data or processing
changes.  That’s why we often add a Data Access layer.  Its
purpose is to make the business logic immune to changes in the technology that
implements the data model.  Sadly, the interface to the data storage layer
isn’t completely standardized, so we create a Façade (a data access
layer) to wrap the variability up and isolate it.  It creates a relatively
fixed interface in spite of product variability.



If we use X-windows (or
Mac OS `Cocoa <http://developer.apple.com/cocoa/>`_ , or Java `SWING <http://java.sun.com/products/jfc/>`_ ,
or a browser), we can have immunity from the software which implements our
UI.  Folks don’t often pursue this as hotly as they pursue the data
access independence.  I’m not sure why, but many people are willing
to marry the MS-Windows proprietary UI but not marry SQL/Server. The
interface between UI and Processing isn’t treated with the same respect as
the interface between Processing and Data.



So, the Data Access layer is
really there to isolate processing from database technology.  It’s
not really part of our essential “who”, “what”,
“how” and “where” set of questions.  We feel the
need to define a relatively fixed interface because RDBMS implementations differ
in often significant ways; we don't want to suffer from differences among
proprietary interfaces.



Further, we may
also have an Object-Relational mapping layer.  This sublayer is above the
data access layer, but below the rest of the processing layer.  It provides
the mappings between RDBMS and actual objects as used by the application. 
This, too, is best looked at as a sublayer on part processing and not part of
the persistent RDBMS storage model.



The Struts Example
------------------



A good example of the
UI-Processing-Persistence separation is the implementation of `Struts <http://struts.apache.org/>`_ .  In
Struts, there is a separation among the layers, and a pleasant test to assure
that the separation has been implemented properly.



The Struts UI layer is built
with simple JSP's (read ASP if you don't know Java.)  The UI displays Java Beans
that may have been created by an Object-Relational mapper (and really live in
the database) or they may be containers of validation errors that were created
by the processing layer.  The UI doesn’t know and can't know; they're all
just beans.  It displays beans and produces beans from filled-in forms.



The Struts UI will have
considerable programming logic, but this is merely presentation gloss, not
substantial processing.  For example, pluralizing words, formatting dates and
numbers, handling variant form layouts or optional fields are all appropriate
ways to improve presentation without bleeding through into providing real processing.



The Django Example
-------------------



As a second example, we
can look at `Django <http://www.djangoproject.com/>`_  framework.  They distinguish between a
number of layers.  The low-level RDBMS is wrapped with an access layer (the
Python DB-API) and a Django Object-Relational layer to define the "Model".  A
web request and response is handled by a "View" which implements the processing.
Most views will use Django templates to present the final web content.  




The template doesn't have access to
any real functionality, by design.  Unlike Java JSP's (and ASP's), Django
templates use a special-purpose template language, not the full Python (or Java
or VB) programming language.  By limiting the templates to just simple
alternatives, iteration and object navigation, any "real" processing has to be
put into the view layer.  Since the UI can't "do" anything, the whole question
of layering is moot.



Just to complete
the picture, Django implement the "Control" of MVC in the URL dispatcher.  It's
a very elegant solution.  Struts has to coexist with the Servlet API's.  Django,
on the other hand, doesn't need to make this legacy interface visible.




Recommendation
--------------

                                                                                                                                                

So, what should the UI bind to?  Should it bind to Processing, or can it bind
to Data Access?



The answer was hinted
at above, when I mentioned “bleed-through”.  When the
processing details bleed up into the UI, this breaks the isolation rules. 
Here's the acid test:  we know the isolation rules are broken because we
can’t just change the implementation of the business processing without
also locating the bleed-through cases and fixing the UI.

 

For example, the business layer is supposed to validate some user inputs.
However, the UI developer wrote a JSP (or Ajax or ASP) thingy that did some of
the validation.  They were creating a “rich” user interface. 
When the business rule changes, however, we find that the JSP (or Ajax or ASP)
interface component isn’t doing the right validation any more. 
That’s **A Bad Thing**\ ™, and a direct consequence of
processing rules being implemented -- whole or in part -- in the UI
layer.



When too much processing bleeds
through into the UI, you have – in effect -- created a very complex
interface between the UI and the Processing layer.  The interface will
include the obvious Processing hooks used by the UI, but will also include the
Data Access hooks.  It’s much better to create a narrow interface of
the relevant Processing and nothing more.  Bundling the Data Access as part of
the Processing interface is adding complexity with no real
value.



You break your isolation rules
when the UI looks directly at the Data Access layer.  Specifically, a data
model change now leads directly to a UI change in addition to the expected
processing change.  This ripple effect of a data model change is
**A Bad Thing**\ ™, and it's the exact thing we were
trying to avoid when we broke things into layers in the first
place.

 

Consequences
------------

 

One of the consequences of this is the clear isolation of **all**
processing into a processing layer.  The UI becomes thinner, and the
database can also become thinner. 




The UI merely displays beans.  Any
“richness” to the interface involves close design cooperation
between the UI folks and the business layer folks to keep the UI pure and
simple.  This cooperation is a necessary part of designing good software. 
Too often, the UI folks work around this because the processing folks are slow
to respond to UI requests.



Similarly,
the data base becomes flat table storage, and all processing (triggers, stored
procedures, everything) moves into a processing layer where it is easier to
control and reuse.  The hard-core DBA's balk at this, and claim that their layer
is the ideal place for processing.  Sometimes they'll try to qualify this and
distinguish "stable" processing from "mutable" processing.  Generally,
processing in the database only serves to muddy the distinction between data and
processing.



The "stored procedures
involve less overhead" argument isn't often helpful, because it requires a
number of assumptions.  Specifically, a stored procedure in the database layer
is faster than the processing layer only when you demand all of your processing
be done with low-level SQL statements.  If, on the other hand, we rethink the
processing design to use objects in memory, we can often work out ways to do
much less SQL.  And, if we really want to push the envelope, we can resort to
ETL processing outside the
RDBMS.



Root Causes
-----------



It looks like there are two
causes for this question, both of which need to be addressed in order to keep
separation between layers.

1.  UI layer people want to provide richer
    functionality, but processing can't or won't provide the necessary
    API's.

2.  Processing layer people have pushed some
    processing into the RDBMS, blurring the line, and making it unclear where the
    processing is in the first place.



If UI layer developers want more API's, the processing layer folks should be ready,
willing and able to provide them.  This requires an adaptable style of work,
with fairly high levels of cooperation.  They need to be on the same team,
working for the same manager.  If it takes more than spinning around in your
chair to engage between teams, then the UI folks will bypass the processing
folks to get what they think they
need.



It's hard to foresee the entire
spectrum of UI needs.  In writing some processing logic, you may think you
instantiated all the relevant beans.  But during a review of the functionality,
someone (user or developer) realized that one more factoid would be helpful. 
When it isn't in the available beans, the UI developer has two choices: wait
around for the beans to be upgraded, or go straight to the database and do the
additional query.  What the UI developer does next is purely about
organizational culture.



If processing
is pushed into the RDBMS, then the horse is out, and locking the barn door seems
a bit silly.  You can insist that all UI requests go through the Processing
layer, but everyone knows that the Processing API simply calls an RDBMS
procedure through the Access layer.  It looks silly because it is.  However,
since the Processing was split up into multiple locations, a single, unified API
must be defined to preserve the intent of the Processing-Database interface and
allow implementation changes without breakage.














