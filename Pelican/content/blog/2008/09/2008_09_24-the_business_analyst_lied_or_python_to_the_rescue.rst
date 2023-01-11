"The Business Analyst Lied" Or "Python To The Rescue"
=====================================================

:date: 2008-09-24 12:28
:tags: architecture,design,complexity
:slug: 2008_09_24-the_business_analyst_lied_or_python_to_the_rescue
:category: Architecture & Design
:status: published







This is a long, sordid story.  Maybe a the title should be "Seduced by Technology", rather than "The Business Analyst Lied."



Initially, it sounded like this:



"Our customer asks for a recommendation regarding an offering.  Based on the description of the offering, we use web services to get some scoring information from our vendors.  We combine that with our own proprietary models.  We reply with the recommendation."



There's a UML collaboration diagram that shows the vendor scoring web service requests front and center.



Got it.  Ready to code.



Not So Fast
-----------



Turns out, that this "get the vendor data" isn't actually what's going on.  It turns out that there are four parts to the recommendation.  Two of those parts involve vendor data and two of our proprietary models.  The other two parts involve two more proprietary models.



The web services turned everyone's heads.  It was "novel" and "confusing" so it got a lot of press.  The actual proprietary models were -- umm -- business as usual and hardly worth a page of documentation.



[**Note**. The business value is in the model.  But no one saw fit to document this.  And I'm not smart enough to ask.]



Okay.  So, the process is really this:  



"Our customer asks for a recommendation regarding an offering.  Based on the description of the offering, we evaluate our four-part proprietary model.  Two parts of the model happen to require some scoring information from our vendors; we use web services to get this.  We reply with the recommendation."



Revised requirements:  our model is front and center.  The vendor information and associated web service requests support part of our model.  Got it.



Still Not Right
---------------



After building a bunch of stuff, it turns out that I was still being lied to.



Here's what *really*  happens.



Part 1.  "The sales folks get our customer's entire catalog of offerings.  Our Deep Thinkers then get scoring information from our vendors on all of the offerings, and develop a four-part model."



Part 2.  "Our customer can ask for a recommendation regarding an offering.  Based on the description of the offering, we evaluate our four-part proprietary model.  Two parts of the model happen to require some scoring information from our vendors.  *Information we already have*.  We reply with the recommendation."



So, first they give us all the possible offerings.  Then we get **all**  the vendor information.  Then we build our proprietary four-part model using the vendor information.



Ummm... Where are the web services?  Where's the "on-the-fly" query to the vendor to get scoring information?  It turns out that we already have all of the necessary vendor information.  We had to have the all the vendor information in the first place so that could build the model!  Why would we go back to the vendor on a recommendation-by-recommendation basis when we already have all the data?



[**Note**.  A big performance improvement will result from this realization.]



Chickens and Eggs
------------------



The first draft made it look like there was no model -- only vendor data acquired through Web Services.  At the last instant.  All dynamic and state of the art.



Then it sounded like the model was central, supported by some vendor data acquired through Web Services.  Still pretty dynamic and state of the art.



But where did the model come from?



Oh That.  The model was built from giant sets of data.  It involved simple batch transfers from customer to us, us to our vendors, and our vendors back to us.  We load the database with customer data, vendor data and our model.  Not dynamic.  No web services.



The business value is in our proprietary model, and the folks that have experience, insight and skills to build that.  It's not in the fancy Web Services.



It's not that we get a query and do calculations on the fly.  We already know what we'll be asked.  We've already thought this through.  There's almost no 'on-the-fly' to this business.



Python to the Rescue
--------------------



Here's why I love Python.  I learned all this while building a working application in Django.



My summary of the Django world view is "Model first; default admin; evolve the presentation."



So, we started out with a data model, some web services, default admin, and a skinny little presentation of the working application.  That original model, BTW, remains largely unchanged.  The most significant changes to that have stemmed from the Django 0.97 to 1.0 evolution.



That was fine until I figured out that the our proprietary business model was central.  So, we rebuilt the data model to reflect the business.  The web services didn't change much.  The default admin is still fine.  The presentation had to expand to cover the additional parts of the model.



This Django model is in several parts.  In Django parlance we have many "applications".  Each application is a subset of the overall model with a specific subject-area focus.



That structure was fine until I figured out how our proprietary business model gets built in the first place.  Now we have to revise everything yet again to create a more sophisticated Django model that reflects how the business *actually*  operates.



Refactoring
-----------



It's all just Python, so the refactoring is very, very low cost.  If this was Java, we'd be paralyzed by the cost of rework.  For Java folks, redoing the database and the ORM layers would be a hellish cost that would lead to terrible workarounds.



In Django and Python, however, we fix the model, and the SQL takes care of itself.  The admin takes care of itself (for now).  We will have to rework the presentation, but that's only a few dozen template files that have to be adjusted to handle the new relationships.  



The hardest part will be reworking the various view functions.  But, because of the way Django works, there are only a few places to look for changes there.  The Django ORM layer allows us to ignore many of the model changes.




