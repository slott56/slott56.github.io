SOA, Web Services, and Other Religious Experiences
==================================================

:date: 2007-08-17 21:53
:tags: architecture,software design,complexity,SOA
:slug: 2007_08_17-soa_web_services_and_other_religious_experiences
:category: Architecture & Design
:status: published







TC writes:


    I’m sitting in the corner, considering SOA from various perspectives:

    -   What sized company?

    -   When you sell/license the tech, what are you actually
        trying to sell? The initial implementation, individual services, ???

    -   Chicken vs. egg – implement first or align the culture first?

    What is *our company's*  approach?

    Has anyone generated succinct flyers or white papers? 
    I’m lost in a Google-lanche of info, and I dearly want to narrow the
    focus a bit before I have to explain it to *VP's*  and others. 




What Sized Company?
--------------------






TC's an architect, so he's asking about selling something that we'll develop, install and support.







SOA is for every size of company.  Developing applications with an SOA is cheaper and
simpler than traditional "wholistic" apps that don’t have
clearly defined services.








Why?  Simplicty.  Services force you to think about agility and
simplicity.  The result can be software which is simpler, cheaper and more effective.   










To achieve the required agility requires you to pare things down to their essence and then build that essential service.  The more traditional approach is to gatther a bunch of requirements and design a bunch of software.  At no point in the process does anyone ask you to simplify those requirements or the resulting software.











What Are You Trying to Sell?
-----------------------------











Actually, there are two parts to this, because there are two things you can sell.









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.


2. You can use the technology as a means to an end.  This, I think, is where you are coming from.   The customer
wants an app -- a solution to a business problem -- and you are going to use an SOA framework to save yourself considerable agony.   Much of
the glue that takes time to specify, build and test is now part of
most SOA frameworks.  Generally, the customer could care less
whether it comes from a vendor or you.  









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.


Consider applications for which we have extensive proprietary source.  We could convert our code to a SOA framework (for example `Sun's JCAPS <http://www.sun.com/software/javaenterprisesystem/javacaps/index.jsp>`_ ).  Our apps would work
the same, but the overall installation is MUCH smaller and simpler.









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.


Culture (a/k/a Governance)
---------------------------









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.



The culture of
the developers must precede the implementation.  If they don't get the SOA viewpoint, then you can't build an SOA application.  What's important is separating the final "to the user" presentation, the composite workflows and the underlying services.  In many cases -- particularly where schedules are golden -- managers will undermine the SOA work by insisting that some piece of user interface be completed RIGHT NOW, irrespective of how it devastates the architecture.  Serious, essential business functionality cut and pasted into several JSP pages leaps to mind.









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.



Some places are brain-dead.  I blogged a specific quote in "`SOA is DOA <{filename}/blog/2006/09/2006_09_30-why_soa_is_doa_in_some_organizations.rst>`_ ".









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.



Culture of the customer is a “don’t
care” item if you are using SOA to build a solution.  If the customer is clueless and you’ve built a working solution, the orientation of the architecture doesn't matter.  It could be service oriented, object oriented or aspect oriented.  









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.



However, if you're trying to
teach them SOA, it had best be strategic for them.  Otherwise, the mentoring will be immediately trumped by management.  "It's taking too long to write the use cases," for example, will subvert everything by undoing the training and coaching you've done for the first few weeks of the program.









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.



Lost in the Google-lanche
---------------------------









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.




Read up on the `Sun Java Composite Application
Suite <http://www.sun.com/software/javaenterprisesystem/javacaps/index.jsp>`_  (JCAPS).  The presentations are focused on what matters: lowering TCO by making it easy to manage the composite application as a whole.  Look at the eGate Integrator as the lynchpin -- everything else is an add-on.









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.




Also, for the leading-edge folks, there's a lot of SOA goodness in the Python community.  The Python folks exploit the dynamic language to create a proper Don't Repeat Yourself (DRY) technology that's considerably simpler than the Java worldview.









1. You can sell the technology as an end in itself.  For example, when the customer wants
to use it and you’re the expert.  We're doing some of this for customers who want to build in-house skills.








