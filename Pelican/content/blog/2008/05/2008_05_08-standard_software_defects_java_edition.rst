Standard Software Defects - Java Edition
========================================

:date: 2008-05-08 12:58
:tags: architecture,software design,data structure,algorithm,defects
:slug: 2008_05_08-standard_software_defects_java_edition
:category: Architecture & Design
:status: published







**NUT**.  No Unit Test Cases.  Need I say more?  If there are not unit tests, this isn't real programming. 



**MCF**  and **NCF**.  Minimal/No Use of Collections Framework.  The **MCF**  defect occurs when someone uses only the Array or Vector classes.  The **NCF**  defect occurs when someone uses only primitive arrays, often with fixed sizes.



**NCF** defects also occur when someone creates a linked list, but insists on traversing it with the horrifying:

::

    for( int i=0; i != aList.size(); ++i ) {
        SomeClass x= (SomeClass)aList.get(i);
    }





I find the above deeply disturbing because of the intentionally incomplete understanding of the linked list structure.



**Deprecated Feature**.  This is a big, big warning.  Anyone who insists on using deprecated features needs to find a new job in which learning is not valued.  Deprecated features must be removed from application programs.  There's no room for the moronic "it isn't actually broken yet."



Also, if you read the Java API Docs, you find nuggets of goodness like the following, in Enumeration.

    NOTE: The functionality of this interface is duplicated by the Iterator interface. In addition, Iterator adds an optional remove operation, and has shorter method names. New implementations should consider using Iterator in preference to Enumeration.





This seems simple enough to me: Enumeration is not something you should use.  Yes, it is used in a few places in the collection framework.



**EIM**  - **BOD**.  **EIM**  is the Everything In Main defect.  Generally, this is accompanied by the **BOD** (Bad Object Design) defect.  These are closely related, and both stem from a failure to grasp OO design, and a failure to allocate responsibility through the class structure.  Instead of doing some kind of class responsibility assignments, a massive method was written to do all the work.  Often this method is public static void main( string[] args ).



The Everything In Main defect occurs depressingly often.  There are several good reasons why **EIM**  programs are defective.  *Adaptability and Reusability*: the public main method is the operating system's interface to our application, and is quite hard to repackage and reuse.  *Testability*.  It's also very difficult to construct a meaningful unit test for an **EIM**  program.  *Maintainability*.  Making simple, controlled changes can be hard:  an **EIM**  program is often a house of cards.  Plus, *auditability*  and *understandability*  suffer.



There are two arguments the get raised here.



1.  Some folks argue that it's good to have "everything in one place".  They don't like class design because they have to "look at something else" to understand an algorithm.  The "everything in one place" folks often are big-brained people who feel it important to keep all details in the forefront of their thinking; they tend to distrust summaries.  For the rest of us little-brained people, a pithy, accurate summary is essential to understanding.  We little-brained people are able to summarize a lot of software with terms like "OS" and "RDBMS".  I don't know why similar summaries can't be used by big-brained people when doing object design.



2.  Some folks argue that reuse of an EIM program can be handled through shell scripts and what-not.  This adds another element into our application, an element that reflects procedural design where the only way to bind data and processing was in an application main program.  In C, your libraries where essentially just method functions, not reusable class definitions.  Object design doesn't have this limitation, and isn't helped by writing some functionality in shell scripts and other functionality in Java.



Remediation



Remediation of these standard defects is hard.   If you have the **NUT**  case, you have to write test cases.  Since you're writing them after the fact, they'll be incomplete.  Warning: Hard Work Required.



If you have **MCF**  programs you can sometimes rewrite them incrementally to replace dumb old Arrays and Vectors with more efficient Linked Lists, Sets and Maps.  Sometimes.  



If you have **NCF**  programs, you often have to throw them away and begin again from the beginning to write something that leverages the collection framework.  Further, you have a large education problem to solve.  Warning: Coaching and Training Required.



When you have **BOD**  programs, you have an even larger object-design education problem.  Folks who come to OO programming from non-OO environments (VB, particularly) are often baffled by the basic concept of responsibility allocation and emergent behavior from object interaction.  



It turns out that **EIM**  programs are often a good way to learn better object design.



Remediating EIM
---------------



EIM programs involve a big procedure full of details that could have been summarized into other class definitions.  They also involve the obscurity of the OS's interface to a "program" and force us to write some of our application's functionality in the shell script language, diluting the value of Java.



It's important to draw some lessons from the design of Ant's Task class or Maven's MOJO interface. We'll use the Ant Task definition, it's simpler.



Every "step" in a program can be defined as some kind of Task. Each Task has some configurable properties: you set those and cut the task lose to do it's job. When a Task finishes, it may have some resulting properties that you can check.



EIM programs have to be recast using the **Command**  design pattern.  See (`Command Design Pattern <http://exciton.cs.rice.edu/javaresources/DesignPatterns/command.htm>`_  for details.)  You can define a simple abstract superclass for all of the various kinds of Tasks.  You can also define a simple Macro Task that contains a List of subtasks.



Do not go insane and define **Commands**  to reflect every shell-script construct (loop, conditions, switches, etc.)  Java already has all the looping and condition testing statements you'll ever need.  Feel free to invent Commands that include sensible, easy-to-summarize ordinary Java programming.



Atomicity
---------



Ideally, you can break main into a series of atomic "steps".  These are the big picture, summary-level small-brain steps.  If, for some reason, you can't break a 150-line pile of gibberish into some kind of summarized set of steps, find a job in a different industry.  Seriously.  If you can't summarize, you shouldn't be programming.



Arriving at a summary isn't easy.  The brain's limit on comprehensibility is the `Magical Number Seven Plus or Minus Two <http://www.musanim.com/miller1956/>`_ .  You have to get the overall plan down to 7±2 high-level steps.  Some of those steps can have sub-steps.  Nesting is a good thing -- just keep everything into sensible, meaningful, easy-to-describe chunks.



Each step will be largely independent.  There will be some small amount of information passed from step to step; there will also be a certain amount of shared configuration information.  Each candidate step has global properties, input from previous steps, and output to subsequent steps.  Given a 150-line morass, it may be hard to distinguish the global inputs, local inputs and outputs of each "step".  We'll return to some specific issues below.



Define a subclass of Task for each step.  Some will be concrete classes -- with detailed implementations.  Some will be Macro Tasks which have constructors to create a List of subtasks.



Each concrete Task has an execute method which is pulled directly from the original, long main method.  Each Task will also have a number of properties -- the variables required to execute the step and the results of the step.



Replacing Main
--------------



Once main has been broken into Tasks, a new overall "What Was Formerly Main" Macro Task can be defined.  This will construct the 7±2 tasks that comprise the revised main sequence of steps, set their properties, and then use the ordinary Macro execute method to step through the sequence of Tasks.



Now the overall main method is a simple constructor for a Macro Task and an execute of that Macro Task.  Ideally, two lines of code, based on a highly reusable Task/Macro Task structure.



State Change and Shared State
------------------------------



As our sequence of tasks execute, the output from one task is input to the next.  Universally, state change means that an object's setter methods were used.  Sometimes, an object which gets updated (or created) must be shared by two or more Tasks.  A shared object is usually the responsibility of the overall Macro Task, and that object is a property of each subtask which shares the object.



Failure to identify the objects which undergo state changes is the leading cause of **EIM**.  It's also one of the root causes of **BOD**.



Often, this shared state must be persisted in some form.  (Other times, it is a report that written to some output stream.)  When we're dealing with persistent shared state, we might be using a database directly.  More often, we're using Hibernate or iBatis, and we may need to configure iBatis or Hibernate and potentially fetch some initial objects from the database.



Configuration and Global Properties
-----------------------------------



The public static void main method has three responsibilities.  The third and final is to create and initiate the overall Task.  The first is to gather the overall configuration as a complete set of Properties.  The java.lang.System has a base set of properties which come from Java defaults and command-line parameters.  In the middle is the management of any global objects.



Your application should create it's own Properties object.  Use application-wide or system-wide properties files for default values.  Merge in properties from System and any property files named on the command-line.  This complete set of properties can then be given to the overall Task to support any needed configuration.



In some cases, you may want to create shared objects outside the Task (in main), and assign these objects to specific Tasks.



Example



Your goal is to get to something like the following.

::

    Logger theLog= Logger.getLogger( "com.xyzzy.division.app.Main" );
    Properties p= mergeAllProperties();
    theLog.config( p );
    SomeObject theFocus= new SomeObject();
    try {
        Task t0= new MainTaskV3();
        t0.init(p);
        t0.setTheFocus( theFocus );
        t0.execute();
    } catch... {...}
    theLog.info( "Finished" )





Now, my main program is purely the administrative overhead of gathering property values, creating the shared state object(s), and executing the task that updates that object's state.



Note that we're creating MainTaskV3.  When we move to version 4, we can add the new class definition and update main to use the new class definition.  This simplifies change management to be mostly adding new class definitions and changing relatively little established, tested code.



Mutability Analysis
--------------------


What if we want to add a task?  In an **EIM**  program, this is hard -- sometimes impossible.  In a Task-based program, we're adding a Task definition, and adding an initialization into some Macro Task.



Note that this is inherently testable.  We can easily test the new task in complete isolation.  Further, we can easily back the change out by removing a single constructor from a Macro Task.  (We don't need to remove the unused class definition.)



What if we want to remove a Task?  Again, this is often hard in an EIM program because the various task dependencies are murky or non-existent.  In a Task-based program, we're simply removing a single constructor from a Macro Task.  



What if we want to reorder the Tasks?  We're just changing the order of SubTask construction within a Macro Task's initialization.



What if we want to dramatically restructure two formerly distinct programs and combine them into one new program?  What if we want to split a long program into two shorter programs?  Both cases are simply a re-organization of the MacroTasks to adjust the mix of tasks the create in their initialization.



Solutions
---------



Standard defects lead to standard solutions.  Each program is not a unique, special snowflake.  Each program just one of many, and should be evaluated using a standardized set of defects.




