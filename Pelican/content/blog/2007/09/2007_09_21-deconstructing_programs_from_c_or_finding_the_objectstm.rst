Deconstructing Programs from C; or Finding The Objects™
=======================================================

:date: 2007-09-21 01:26
:tags: architecture,design,unit testing,tdre
:slug: 2007_09_21-deconstructing_programs_from_c_or_finding_the_objectstm
:category: Architecture & Design
:status: published







It's about 10,000 lines of C.  Much of the C is focused on "framework" issues -- logging, synchronization, parsing the parameters and that kind of thing.   In this case, it appears to be 30-50% of the original C code is stuff that is available in Java and can be removed.



So what's interesting?



What's interesting is a vague outline of **How to Deconstruct C**.  Further, it's a story of **Python to the Rescue**, even though the goal is to write Java.



There's a bottom-up view.  If the C program is reasonably well-written, each individual file will be a class-like module.  In some cases, the file will be more like a Python module or Java package: it will have a smattering of closely-related data structure and processing.



There's a front-to-back view.  However, you can't really begin at the beginning, because the setup and initialization is often badly uncoupled from the processing it initializes.  You can, however, start reading the program at the end and work out some of the preconditions that have to exist for each statement to make sense.  You can, if the program is not pathologically poorly-written, arrive at a pleasant overview that makes some sense.



You should eventually discover some essential data structure.  `Jackson Structured Programming <http://en.wikipedia.org/wiki/Jackson_Structured_Programming>`_  builds programs around the transformation of one data structure into another; this is the basic principle behind a well-designed set of XSL transformations.  It is also the heart of most batch programs -- transform the source records into output records.



The really hard part is locating the record types in a procedural program.



Finding the Central Loop
------------------------



In this case, the program had a very complex outline.  There was an "essential" loop, however, that was buried under the complexity.  I found it helpful to ask **"What's The Business Value?"**  when confronted with another hideous C function.



It turns out that the business records were aggregated into batches.  There was a long, complex preparation which created temporary tables and result tables.  A rather complex query-insert process populated the temporary tables.  Indexes were added, and the database's analysis procedures executed.  None of this created obvious business value. 



Eventually it became clear that there was a loop that did the relevant processing on rows within a batch.  Now we're getting somewhere.



Order N-Squared
----------------



It turned out that the central loop was actually two nested loops, created an O(n²) kind of process.  Yes, there was a sort, but each row was compared to each row after it in the collection.  So row 1 was compared to all rows 2 through *n*.



In the long run, this can't be optimal.  I suspect that what this program really does can be transformed into an order *n*  log(*n*) operation that uses two passes.  The first pass builds a few useful hashmaps, the second pass then does the final, interesting algorithm.  However, at this point, it's hard to prove that.



Once we'd uncovered the two inner loops, we had a picture of the overall structure.  However, we weren't really close to anything useful yet.  We haven't uncovered any fundamental objects or classes, just some algorithms.



Cryptic Class Definitions: Parallel Arrays
------------------------------------------



Clearly, the things being processed in these two loops are the central objects of the application.  In a reasonable C program, you'd expect the objects to be part of a proper C-language type or structure declaration.



However, because of the batch-processing overheads, this program used `Oracle array fetches <http://download.oracle.com/docs/cd/B28359_01/appdev.111/b28395/oci05bnd.htm#insertedID5>`_ .  It didn't have a proper record structure.  It did, however, have dozens of parallel arrays.  This was -- in effect -- a kind of ``List<BusinessRecord>`` structure.  With a bunch of assumptions, we could construct the effective class definition for these central objects.



The original array fetches can be replaced some simpler processing to load POJO's rather than dozen of parallel arrays.  The various layers of batch management overhead can be stripped away and the program pared down to the single function which does the real work.  Once we knew what we were looking at, we found the function did the array fetch and executed two nested loops to process all of the objects in the array.



At this point, we could put our first unit tests together.  That's real progress.



Python To The Rescue
---------------------



Our target was Java.  However, that still leaves a need for tools.  Specifically, we had a pile of SQL which implied some table structures.  The customer had some idea what those tables looked like, but didn't have the actual DDL to create the tables.  (They never seem to keep this or put it under configuration control.  Why not?)



So I spent a pleasant half-hour typing up a version of the DDL.  Rather than simply make a script, however, I made some small SQLAlchemy programs to create the database, load some randomly generated test data, and do some basic reporting.  This is all too painful in Java, but trivial in state-of-the-art tools. 



Business Rules
---------------



The program's parameter files were used to build two sophisticated ancillary data structures.  In effect, the parameters encoded two sets of business rules.  Half of the "parameter parsing" section of the program merely built these structures out of the INI files.  Somehow, the rules where used in the main loops to do the processing.



The program did three separate things, each of which had an INI file.  These INI files, in turn included some general INI parameter settings.  We could partition the INI material into two parts: standard property-setting, and business rule definitions.  The property-setting stuff is garden-variety Java property processing; the associated C code to parse properties is no longer needed.



After peeling them out of the INI files, the business rule definitions formed a kind of declarative language.  This little declarative language built two families of rules, each of which had distinct sets of keywords, options and parameters.



The rules had first-class C type definitions.  The attributes of the class could be identified.  What about the methods?



Business rules are -- universally -- examples of the **Strategy**  design pattern.  That means that each rule embodies some unique processing.  While each rule in the C program was a simple structure with a half-dozen fields, it also had some method buried inside it.



A little grepping of the source turned up a series of functions with similar names, each of which had a pointer to a rule field as an argument.  We found this kind of parallelism.

::

    someFuncA( ruleFieldA *arg, other args )
    someFuncB( ruleFieldB *arg, other args )


This clarified things considerably.  It told us that a rule was merely a **Façade**  or **Container**  for a set of individual Strategy objects.  Each "field" of the original rule definition was really a **Strategy**  object, and the rule was just a container.



This unveiled dozens of strategy class definitions which were knit together in these rule containers.  This, also, lead to a cool Pythonic design.



Pythonic Initialization
-----------------------



One of the cooler Python techniques is to use basic Python class and object definitions to create a Domain Specific Language (DSL) using Python syntax.  Projects like Django's data model and SQLAlchemy show elegant ways to use Python syntax to create a DSL.



While our goal was Java, it's so much quicker and easier to prototype the design in Python.  In a few minutes -- seriously, minutes -- I had enough Python class definitions to demonstrate that we could trivially transform the INI files into Python or Java object definitions.



The best part was replacing INI files and the associated parsing with first-class Java (or Python) as the source language.  The user-facing initialization file would have things like "[section]" replaced with "rules= {", plus a few extra commas.  Except for a little required boilerplate code at the beginning and end, it would be identical.  



Thanks, Pythonistas, for inventing such a cool declaratory style of Python programming.



More Unit Testing
------------------



Once we decoded the rules as a bunch of largely static initialization, we could turn to the method hidden down inside each individual rule.  We examined each of the someFuncA and someFuncB rule-specific processing.



At this point, we were nearing the heart of what was going on in this program.  There were about half a dozen of these rule-specific methods that had to be unwound into a forest of **Strategy**  class hierarchies.  Each **Strategy**  class hierarchy needed a proper set of unit tests to validate the precise business rule that it implemented.



Flags and Classes
------------------



Flag settings have lots of interpretations.  They might be dynamic **States**  or they might be static **Strategies**.  Either way, a flag -- even a boolean flag -- is often a class definition; it is rarely a simple boolean value.  A flag with enumerated values usually identifies a family of related subclasses.



If-statements to test flags have to be looked at as potentially polymorphic methods of the implied subclasses.  In our case, there were parallel function names that made the polymorphism more obvious.  However, rotten choice of function names can conceal the relationship.



Often we get to do **If-Statement Hoisting**.  Once we've elected to transform a flag into a class, we'll find if-statements which are now needless class membership tests.  For example, down deep within someFuncA will be an if-statement that asks if the rule has the ruleFlavorA flag set.  Once we make the rule flavors into classes, each class has a unique implementation of someFunc, and a test for class membership go away.



In effect, the if statement is hoisted out of the function and moved forward in the algorithm.  The test becomes part of initial rule object construction.  This is an optimization that is very elegant.  Rather than execute the if statement for every one of the *n*\ ² record processing steps, we execute the if statement one during initialization.



Globals and Integration
------------------------



One of the biggest problems with converting C programs is the reliance on global variables.  The global variables make the scope of every function suddenly murky.  In a reasonably well-written program, there will be few globals.  



The parameters and properties, clearly, need to be global.  Often, a static class can be used to implement a kind of **Singleton**  for this.  In other cases, we can provide the parameter object to various objects within the program, eliminating the little bit of semantic confusion that purely static classes can raise.



However, we uncovered one bothersome situation where a deeply-buried business rule method made an appeal to a global variable.  A little reflection, however, made this less bothersome.  A business rule executes in a "context" of global parameter settings.  In this case, the context included some alternative business rules.



An open issue is whether this context was an attribute of the object, or a parameter to the business rule's method.  This is almost a matter of preference.  Method function parameters can always be turned into object properties.  However, there's usually some semantic behind the attributes.  We have to return to our initial question, **"What's the Business Value?"** for guidance in the parameter vs. attribute question.



It didn't take too much refactoring to provide the necessary context to the rules.  Since we were building unit tests, it was easy to move things around and rerun the tests.



Allocating Responsibility
--------------------------



Now we arrive at the actual heart of the matter.  What is each class responsible for?  The original C functions have several dispositions.  Either they're junk and get removed, or they're available in Java and get replaced.  What's left has to become a method of some class.  Where do we place the C functions?



The classes we've identified to this point will fall into two groups: passive classes, which are dominated by attributes, getters and setters; and active classes, which are dominated by complex methods.  The distinction is a little subjective and it will change as the deconstruction proceeds.    



These more passive classes will become Java Beans.  Often this is clear because the class is persisted, or is merely an item in a collection.  The more active classes will usually become the new application program.



Most C functions have a mixture of arguments and global variables as inputs and outputs.  It helps to make an attempt to characterize the implied inputs and outputs of each C function.  The assignment statements define the state changes.  In some cases, this will lead to an obvious partitioning of C functions around their effects.



In some cases, it is clear that a function is a method of a class because it updates attributes of that class.  However, a C function can have so many effects and side effects that the fog is nearly impenetrable.



One indicator is the parameters to the function.  For example, a function which uses one of our **Strategy**  classes as an argument is probably a method of that strategy class.  Similarly, when we deconstructed dynamic flags into a **State**  design pattern, all of the functions with if-statements based on the state settings are likely methods of the state subclasses.



In many cases, a strategy method will imply methods in one of the "passive" bean classes.  We may see several functions do similar processing on a bean class.  The similarity should be noted with a //TODO comment.  Later, the to do list can be examined for opportunities to refactor the similar-looking processing out of the strategy and into the bean.



Things to Look For
------------------



Here's the start of **Finding The Objects**  (FTO™) in C Programs.




-   Proper structures are the usual suspects for finding class definitions.

-   A union defines peer classes with a common superclass.

-   A C source file may be a class definition.  Does it provide operations for a common set of attributes?

-   A parallel set of arrays may hide a class definition.  Are the arrays indexed by the same value?  Functions with apply to one or more parallel arrays may be methods of the implied class.

-   A flag (either boolean or with an enumerated set of values) may be a peer subclass discriminator.  The various if-statements to test this flag may be replaced by polymorphic methods of a family of subclasses.

-   Globals merely serve to muddy the water.  In some cases, a variable is global out of pure laziness; it has a narrow scope.  In other cases, a global is used in enough different scopes that it is clearly an implied attribute of some objects, or is an implied parameter to method functions.

-   State changes -- assignment statements -- provide some hint on where responsibility belongs.  In many cases, a C function will do too much and must be decomposed into methods of distinct classes.


Conclusion
-----------




Python helps.




First, it's easier to create test data and mess around in the database using SQLAlchemy.  It leaves a processing trail.  With Python helper programs and scripts we can reload the test database, do performance testing and do integration testing.




Second, the Pythonic world-view gives us hints as to how we can eliminate programming in favor of declaration.  Rather than parse INI syntax, just write a readable object or class definition.




Third, we can dry-run object designs in Python far more quickly and simply than we can in Java.  Once it seems to work, we can add the necessary Java overheads to make it statically correct.




No, we're not done.  I don't have final metrics yet for a C-to-Java transformation.  Indeed, we're still waiting on the client.  However, we think we'll cut the program down to a third of it's original size.




