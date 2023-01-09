Too Much of the Wrong Kind of Fun or The Object Model To The Rescue
===================================================================

:date: 2007-12-03 03:04
:tags: architecture,design,data structure,algorithm
:slug: 2007_12_03-too_much_of_the_wrong_kind_of_fun_or_the_object_model_to_the_rescue
:category: Architecture & Design
:status: published







In `Lenses That Distort Our Software <{filename}/blog/2007/11/2007_11_03-lenses_that_distort_our_software_flat_files_relational_databases_batch_processing.rst>`_ , I noted that the relational model of data can distort our view of the underlying reality that software models.  In that posting I was whining about how meaningful structure is sacrificed to force fit information into the rows and columns of the relational world.



I think I have some ways to test an implementation to see if it's the reasonably good, or it's the :strong:`Wrong Kind of Fun`\ ™.  An implementation is Fun when things fit together, and it seems to work.  It's the Wrong  Kind of Fun when you can't implement something, performance is abysmal, or you have maintainability or adaptability problems.



One indicator, BTW, seems to be the Paralysis of Analysis.  If you have a lot of open issues, and have invest a lot of time in very detailed plans, you may be having the :strong:`Wrong Kind of Fun`.  Your technology choices don't fit your problem very well.



I've been working with customers who are trying to renovate old applications and bring the technology up to date.  These are riddled with examples of the Wrong Kind of Fun.  The technology choices in the project planning are more examples of :strong:`WKoF`.  But they're boring.  Here's a much more colorful example.  And yes, it's a :strong:`Python To The Rescue`\ ™ story.



:strong:`The RPG Example`



Recently, I started a big time-waster.  As part of moving away from my old PPC-based Mac, I've got to release myself from two Hypercard applications that I still actually use once in a while.  One is my resume (a database, not a document), which I update constantly.  The other is -- well -- harder to explain.



For those of you old enough to remember Paper and Pencil Role-Playing Games, one of those RPG's is the `Hero Game System <http://www.herogames.com/home.htm>`_ .  I found it to be a pile of fun.  My Fourth Edition Champions book is falling apart from the use.  I haven't actually played in years, but my little nephews have heard about this thing that old people did, called P&amp;P RPG's.  From my sister's prodding, I've been dusting things off.



Hero uses an elegant accounting system for describing characters.  Very elegant.  The fifth edition rules, indeed, are supported by a handy piece of software, Hero Designer, that appears to run everywhere and handle this accounting very nicely.  Very tempting.



While elegant, it does require some care and a calculator.  Indeed, the math for some of this accounting can be baffling.  For basic features, it isn't so bad.  For Powers, however, the advantages, limitations and active points require a bunch of number crunching.



Back in the olden days, we fourth-edition Hero players were left to our own devices for doing the number crunching.  And in my case, my own device was a Hypercard stack that helped me concoct Hero characters, powers, spells, gadgets, devices and what-not with relative ease.



:strong:`The Underlying Data Model`



The Hero data model is full of ad-hoc special-cases.  It's a paper and pencil game, mediated by people, so ad-hoc rules aren't too intimidating.  Indeed, the appeal of P&amp;P RPG's is the human mediation.  This isn't :strong:`World of Warcraft`; it can be more subtle.  Of course, if your Game Master/Story Teller isn't very good, it's no better than WoW.  Indeed, some GM's are worse than playing WoW.



The Hero rules started out with the express goal of being relatively simple.  There were several kinds of generalization-specialization relationships that were plainly in the minds of the original writers.



I don't want to specify the whole game, but I do need to note that there are both deep symmetries and casual ad-hoceries that break those symmetries.  Everything in Hero has a collection of features.  For characters, these features include a complete set of Characteristics, plus instances of all the various kinds of "Powers": Skills, Talents, Perks and proper Powers.  Gadgets, Bases, Vehicles and what-not are generally just containers for Powers, but may also have a few Characterstics of their own.  



The base Characteristics are relatively simple features: Strength for example is something you buy for your character.  A Character's Skills, Talents and Perks are slightly more complex features with more complex costs and effects.  The whole text of each effect is the content in the rule books; it doesn't really belong in a database.  What belongs in the database is the bewildering cost and effect calculations.



As an aside, it's the Skills, Talents and Perks that separate a P&amp;P RPG from Multiplayer On-Line Role Playing Game (MORPG).  These require intelligent mediation by the GM, and clever use by the players.  Nothing beats those :strong:`Clever Use of Skills`\ ™ moments in a well-played game.



A Power is a collection of more detailed features, generally including a large number of Advantage and Limitation modifiers.  Here's where the math kicks into overdrive.  The power has a basic cost.  Folding in the advantages leads to an "active cost" -- how effective the power really is.  Folding in the limitations derives the final cost.  There are endless special cases and exceptions.



:strong:`The Hypercard Implementation`



My old Hypercard implementation viewed this data model through the Hypercard lens.  In Hypercard, your application is a database built from a collection of Cards.  Each card has active controls, including data fields and unique blocks of code.  Additionally, each Card belongs to a Background that includes data fields and blocks of code.  The presentation is a union of the background controls (a type or classifier for cards) and instance controls on the card itself.  



Given this Card-Background model, each background could have controls that are generic to Powers or Skills, and a card would have controls that are unique to a specific Power or that Skill.  Each card is effectively a class definition; the data filled into the fields create the instance.  Each background, then, becomes a kind of superclass.



This doesn't work out well.  It's the :strong:`Wrong Kind of Fun`\ ™.  Yes, it has a handy built-in zero-pain, zero-cost GUI.  However, the object model is really flat.  You have background and card, and that's it.  Having a single background for Powers isn't good enough because standard Movement Powers are radically different from the ad-hoc heavy Special Powers.



Ever since I wrote this -- back in the '90's -- I've been struggling with ways to make use of a proper object-oriented data model.  Okay, it's a very casual hobby, so I haven't spent a lot of time on it.  When I played RPG's with my kids, I revisited the problem with no real resolution.  I knew that Hypercard was the :strong:`Wrong Kind of Fun`, but I didn't have an alternative.



:strong:`Tool and Platform Bias`



Given a gnarly, complex data model, what do you do?  The data model seems pretty easy to normalize, until you start considering the exceptions.  Compounding the data modeling problem are the presentation and use case issues.



On the one hand, a relational database tugs at the corners of my mind.  A tidy table-row-column data model, a few simple SQL scripts, and we have the rules in neat buckets.  Then, another tidy data model for characters and gadgets, and we can do simple joins between the character and the base data and -- voila -- character sheets and GM notes.  Sadly, it can't be this simple.  The number of ad-hoc special cases is almost unlimited.  While it's possible to create a generic cost function, it would be simpler to have variant cost functions for each special case.



On the other hand, an OO database tugs in the other direction.  A tidy class model defines all of the features of a character or gadget.  An instance of the class model is the specific character or gadget.  Further, characters and gadgets can be treated as features, allowing recursive build-up of complex characters that make us of the Multiform power or even more complex Power Framework rules.



Neither has a built-in GUI.  So, we're really looking at a whole platform, not just a data model.  Further, the C++ and Java toolsets that I've had at my disposal in the past weren't ideal for this.  Java would require an object model, a persistence framework, a GUI framework, and lead to a mountain of programming.



:strong:`Use Cases`



What are the use cases?  There are a few, but they all amount to the following.  I create a character, gadget, vehicle, base, magical spell, artifact, whatever.  I want a standardized description, in the style of the Hero Rules.  I want correct cost and effect calculations done automatically.



Do I need drag-and-drop?  Checkboxes?  Radio buttons?  Sure, they'd be nice.  But there are some features which are more central than a flashy GUI presentation.



First, I want persistence.  A simple directory of stuff in easy-to-edit flat files will do nicely.  In short, the standard XML or Domain Specific Language (DSL) use case applies here.  I want structured content in a human-readable form.  I want some schema validation, and I have some transformations.



Second, I want composition.  I want to be able to have standard libraries of things from which I can compose more complex stuff.  A magical spell, for example, is a kind of Gadget: it is a combination of Powers, Advantages and Limitations, with a name and some effects.  A collection of these spell definitions helps me  build characters quickly and simply.  



Third, I want standardized reports.  The Hero Rules have a long form and short form.  I want these two results as the result of a transformation.  Part of this will include the overall cost, allowing me to fine-tune a definition or a composite character to keep balance in the game.



I don't really need much of a GUI.  Take that off the table, and we're back to data model and processing tools.



:strong:`Python To The Rescue`



Here's two ways that Python helped me to tease my tools out of Hypercard, and create some significant improvements.



First, the GUI problem was solved by a blinding inspiration: :strong:`Text Files Work`.  A character, gadget, spell, vehicle or base can be a first-class piece of Python code.  We can encode the Hero rules as a set of class definitions.   These classes need a few methods which produce a tidy report, and not too much more.  Each character or gadget is an instance of a class. 



Python becomes a Domain Specific Language for describing Hero characters and gadgets.



What about the validation rules?  In some cases, a Power has options which are exclusive, or there are minima or maxima.  We can throw exceptions when attempting to construct an invalid object.  The use case is quite simple: we edit some text, execute the text, and read the messages.  The IDLE editor becomes our GUI.



All of the ad-hoc special cases are simply subclass definitions, in the most natural and obvious ways.  We don't need to force-fit our complex data into the relational mold.  Instead, we define the obvious attributes and the methods we're interested in.



:strong:`Duck Typing and the Development Cycle`



The usual hard part is coming up with a suitably general framework for Characteristics, Skills, Talents, Perks and Powers.  And we need the necessary collection framework for Characters, Gadgets, Vehicles and Bases. These have a pleasant recursive relationship: a Character can contain Characters as well as Gadgets, Vehicles and Bases.



But Python doesn't impose a sophisticated data model as a requirement.  We can develop in relative ignorance, adding features as necessary.  At some point, we need to refactor.  We can easily refactor without extensive breakage.  In particular, changing an attribute to a property (with the property built-in function) helps us evolve from a relatively simple model to a more sophisticated model.



Further, a basic set of Test Cases, built with :strong:`unittest`, helps us to evaluate our implementation directly.  As soon as we finish defining a class for a Power, we can write a simple test case to be sure that we've got a working implementation.  We can implement the examples from the Hero Rules to be absolutely sure that we're producing correct results.



:strong:`What?  No Database?  Where's the Persistence?`



This is the principle that is sometimes lost on my clients.  :strong:`Persistence`  does not mean :strong:`Database`.  While SQL has it's advantages, it isn't the final word in persistence.  XML is also a good, standardized persistence mechanism.  A DSL may even be better, even if it isn't standardized.



In this case, we have Python as object data base.  A file of Python source is the object model.  It is an executable persistent object.



We can, for instance, import the Python object definition, and query it, process it and report on it.  We change the data object "manually".  So it seems like we could "break the rules" or make changes that somehow bypass the "business rules" or "data validation rules".  However, since our constructors embody these validation rules, we can't execute ("instantiate") the model without the rules being satisfied.



Currently, the only capability I seem to be lacking is concurrent updates.  Wait, isn't that what Subversion does?



:strong:`A Quick Example`



Here's an example Gadget definition.  There's a lot of potential cleanup.  For now, I have long-winded names for the classes.  Since the DSL is Python code, classes can have aliases, giving us an easy way to provide better-looking names.


::

    import hero
    darkArmor= hero.Gadget(
      'Dark Armor',
      18,
      hero.Armor(
        armor=6,
        lim= ( hero.Focus_ObviousInaccessible(), )
      ),
      hero.Darkness(
         radius=2,
         lim= (
           hero.Focus_ObviousInaccessible(),
           hero.ActivationRoll_Activation12(),
         )
      ),
      hero.Superleap(
        distance=10,
        lim= ( hero.Focus_ObviousInaccessible(), )
      ),
    )
    darkArmor.longReport()




