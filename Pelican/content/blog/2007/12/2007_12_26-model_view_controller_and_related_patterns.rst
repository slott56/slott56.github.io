Model - View - Controller, and Related Patterns
===============================================

:date: 2007-12-26 03:08
:tags: architecture,design,UX,UI,GUI,TUI
:slug: 2007_12_26-model_view_controller_and_related_patterns
:category: Architecture & Design
:status: published







TP sent me this great link on MVC and related patterns.  It's Ctrl-Shift-B's posting, `Interactive Application Architecture Patterns <http://ctrl-shift-b.blogspot.com/2007/08/interactive-application-architecture.html>`_ .  It is helpful at disentangling the distinctions between various kinds of model-view-controller, and model-view-presenter alternatives.



This is important because the terminology gets borrowed and adulterated sometimes.  When we look at `Struts <http://struts.apache.org/>`_ , we see one interpretation of the pattern.  Sun provides a lot of useful detail in their Developing Enterprise Applications with the J2EE Platform book, specifically, the `Web-Tier Application Framework Design <http://java.sun.com/blueprints/guidelines/designing_enterprise_applications_2e/web-tier/web-tier5.html>`_  section.  When we look at `Django <http://www.djangoproject.com/>`_ , we see another implementation of MVC.



In the world of fat-client SWING applications, control is a pretty big deal.  In many cases, the GUI is stateful: GUI controls are enabled and disabled to guide the user through a complex set of actions.  Handling input and reflecting this in the state of the controls are important responsibilities of the control elements of the design pattern.



There are many ways to finely chop the responsibilities, leading to various MVP variations on the basic theme.



:strong:`Web Interaction` 



In the "pure" HTTP world, where the GUI is somewhat simpler, there's less event-by-event processing, just big POST and GET actions.  This is where Struts and Django provide different versions of MVC.  Struts -- consistent with other Java-isms -- rubs your nose in the control element.  I must admit that I find the web.xml specification of interactions to be a largely tedious exercise in repeating myself.



There's a theoretical use case for maintenance and adaptation where someone rearranges the web transaction by updating the definitions in the web.xml file.  However, I've never actually seen this exercised.  Indeed, I've never seen a design that would tolerate this kind of change.  [And yes, I realize I'm throwing down the gauntlet for a good example of using this "flexibility".]



There seem to be two kinds of transactions: a few obvious pages (form for search, list of many objects, form for a single object, confirmation) or a multi-step transaction where each step is a piece of a complex object, and the sequence of operations is essentially hard-wired by a binding between business process and information needs.  Neither seems to benefit very much from the overhead of the web.xml configuration for a struts application.



Django seems to skin this cat with reasonable elegance.  Learning Django after learning Struts can be confusing at first.  Clearly, the model is the Django DB API.  They call it that -- you can't miss the implementation.  However, it isn't as clear that control is the parsing of the request and the mapping from URL to "view" function.  When you start looking at JSP as the view, it is odd to think of the Django templates as being just another part of the view element.  



Any flexibility required from a multi-step transaction can be put into the URL mapping with relative ease, since that's the entire control element of the pattern.  If you want a Struts-style parameter for the "do-this-next" URL, you can easily provide this in the URL mapping, passing it as an argument to the view function.  With a little care you can make all of the view functions independent of any specific URL.



It also means that presentation changes are often split across two parts of the view layer.  This is more manageable than it appears, since the template language of Django is (intentionally) limited to simple iteration and decision.  The Python objects used by the template have to be pretty simple; this helps steer the allocation of responsibility between these sub-layers.



:strong:`The AJAX Factor` 



When you throw AJAX into this mix, the boundaries seem blurry.  Since AJAX happens in the browser, it's part of the view implementation.  But it's also another MVC.  The Model is some XML document and it's Javascript objects, the View is the browser's world, and the Control is all that Javascript making things happen.



The net is that you have this two-part architecture with the HTTP MVC and the AJAX MVC.  You can, in principle, have a single conceptual model with Java, Javascript, XML and ORM implementations.  It sounds to be an icky level of complexity; if we use tools to create the mappings (e.g. JAXB) we can probably keep it all straight.  Or, if use just one compact, expressive language (Python/`JSON <http://www.json.org/>`_ ) we could manage this nicely.



The essential feature is that Model elements of an AJAX MVC are accessed via a formal, secure public web-service API.  See `JSON for Ajax Web Services <http://www.theserverside.com/news/thread.tss?thread_id=42722>`_ .  [As an aside, this API seems to be the weakest part of AJAX implementations.  Some developers don't design the AJAX-related services with the kind of respect that ordinary web services are given.]



:strong:`Care and Feeding` 



While Ctrl-Shift-B's posting dwells on Smalltalk, it's still useful.  It shows how an architecture can be documented.  It shows a clear, thoughtful presentation on how the architecture implements common design patterns.  It has some compare-and-contrast elements that can help developers (and maintainers) understand the general design principles and the strategy for allocating responsibility.





