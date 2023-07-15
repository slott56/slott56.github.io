State-Based Object Modeling
===========================

:date: 2007-06-25 13:29
:tags: architecture,object-oriented design,methodology,process,agile
:slug: 2007_06_25-state_based_object_modeling
:category: Architecture & Design
:status: published







In `Object Modeling <{filename}/blog/2005/10/2005_10_16-object_modeling_revised.rst>`_ , I repeated a procedure for object identification that comes from the classic `Object-Oriented Modeling and Design <http://www.amazon.com/Object-Oriented-Modeling-Design-James-Rumbaugh/dp/0136298419>`_  (Rumbaugh, et. al.)



Objects are characterized by their state change.  Therefore, to distinguish among classes of objects, we need to determine if two objects have the same states and state transitions.



States are defined by the object that undergoes the state change.  Therefore, we need to examine the object to distinguish among its states.  We need to know the object in order to know the states; we need to know the states in order to know the object.



How do we cut through this tangled hierarchy, and locate some place we can begin?



One of my `Mokeskines <http://www.moleskine.com/eng/default.htm>`_  and this Blog have many features in common.  They have very similar state transitions - writing, reviewing, editing, etc.  There are, however, some slight differences in state transition rules; based on those differences we can see that there may be a common superclass, but the individual subclasses are distinct.  In particular, my Moleskine has no "power off" state.



Can we start from object identification and then determine state?  Or do we have to begin with state and use this to inform object identification?



Procedure
---------



Try to begin with `noun analysis <{filename}/blog/2005/10/2005_10_16-object_modeling_revised.rst>`_ .  If, for some reason, you have only one noun, or cannot distinguish among the nouns, then you probably have very serious scope definition problems.  For example, if the only noun you can identify is "the system" or "the user" then your initial summary is deeply flawed.



Step 4 suggests that you bounce back and forth among categorizing, associating, defining attributes and defining operations.  An addition activity is defining states.



State definition can be tackled for a given noun using something like the following procedure.



#.  **Find examples**. To prevent fruitless hypothetical and counterfactual discussions it helps to have tangible examples of an object in each state.  For business documents, get print-outs.  For other kinds of objects, use notecards or sticky notes, or `Koosh Balls <http://www.kooshball.com/>`_ ; use something tangible.

#.  **Characterize Each State**. For each example of a given state, highlight (or circle or underline or write down) the attributes which define the state.  States are defined by the attributes; they are not "implied" or "obvious".  Expert judgement isn't part of this.  If things are implied, obvious or require judgement, you'll need to add attributes.  The best case is adding attributes to make the implied state into a manifest state.  A bad case is adding attributes that are going to be set by having an expert (i.e., a person) look at the other attributes and make their oracular pronouncement.  The worst case is where you cannot establish a finite, definite list of attributes that characterize the states.

#.  **Confirm**. At this point, you may have learned many things.  You may have, for example, found that your "object" was really a composite and you have multiple, parallel sets of states.  You may have found, for example, that your object has several associations, each of which has it's own set of states.  You may have found that some states are indistinguishable and other states have substates.  This is all good.  In some cases, you'll have to rework your object model, bounce around among categories, associations, attributes, operations, and begin this process again with a new object model.

#.  **Determine Transitions**.  We're not fully specifying things; we're only discovering.  It's important to set aside details for the moment, since many kinds of details only serve to muddy the waters.  In particular, processing details -- which are stateful -- can often confuse the identification of states.  To make it possible to see what's going on, the magic words "processing happens" have to be used when defining the transitions.

    Examine each state, saying the words "processing happens" and determine what update will move the object to the next state.  The point is to avoid the details of the processing and focus on the net effect of the processing.  Some processing is an object's internal response to arriving in a state; other processing is initiated from outside the object to force it to a particular state.  "Processing Happens" and now the object is in a new state; capture this relationship first, provide details later.

#.  **Elaborate**. You've learned a great deal, and can add a few details at this point.  First, check for orphan states.  If you've got an object state (you have an example, right?) but you don't have any transitions to or from this state, you've got more work to do.  You may be missing some transitions, but you may also be missing some states; states which are intermediate between states you've identified and this orphan state.  An orphan state can also be caused by examining a composite object; this may be a state of one component of the composite object.

    You should have identified inital and final states, also.  Objects begin their existence in initial states.  Some kind of objects will reach a final state, from which no more state transitions are possible.

#.  **Reconcile**.  You can now march an object through the various state transitions beginning from one of the initial states.  Generally, each "path" or sequence of transitions is a scenario for a potential life of this object.  It is essential that the tangible examples be compared against this model to be sure that all states are part of a scenario and all the scenarios make sense when compared with use cases or other source documentation.  If necessary, rework other elements of the model based on what has been learned so far.

#.  **Elaborate**.  Now, at long last, you can write detailed specifications.  The reason details are left for last is because people often confuse state ("static", "status") with processing.  It's inevitable to think of the sequence of steps in an object's processing, not the stages along that lifeline.  At this time, you can finally write state entry and exit processing; this is processing which sets attributes, but doesn't change the overall state being modeled.  Each transition can be annotated with events, guard conditions and processing.



At this point, you should have a state transition or activity model that helps define your object class.  You can select a diagram, either state diagram or activity diagram, depending on what features need to be emphasized in the state model.



Use a state diagram when there is relatively little processing or the entity is relatively active.  When there is relatively little processing, a quick summary on a transition line, or within the state's rectangle conveys everything that's required.



Use an activity diagram when there is rather complex processing or the entity is passive, and is acted on by other objects.  An activity diagram adds activity states or responsibility swimlanes to the basic state machine notation.  



In some cases, both diagrams are required.  The state diagram shows the states and their transitions for a given object class.  An activity diagram may show the ways this object collaborates with other objects to achieve those state transitions.




