Filesystem Deployment: Some Hand-Wringing
=========================================

:date: 2008-09-14 20:03
:tags: architecture,software design,data persistence
:slug: 2008_09_14-filesystem_deployment_some_hand_wringing
:category: Architecture & Design
:status: published







There are two candidate locations on the file system for application components.  What are the criteria for choosing among them?



The Python site-packages directory, IMO, is for packages that have two important criteria.  First, they have to be widely reusable.  Second, they have (or would benefit from) a setup.py.



A stand-alone /opt/someApp directory, on the other hand, is for finished applications.  



But, in the middle there's a lot of stuff.  What about sub-packages of an application?  How "reusable" do they have to be?  Finished or only potentially reusable?  What about multiple parts of an integrated system of applications?



Further, what about Django web applications which have relatively static application parts, plus relatively dynamic database and file uploads in the "media" directory?  What about command-line data management applications for bulk loads and transfers?



And -- relative to Django apps -- what is settings.py?  Technically, it's code.  But, practically, it's just configuration.  When you have multiple run-time environments (Training and Production) with the same code base, it's just the settings.py that discriminates between the two database instances.



Registering Intent
-------------------



The decision of where to put things often devolves to a matter of intent.



A package (or module) is an intellectual crutch.  We collocate class definitions in a module (or group modules into a package) to make a comprehensible intellectual chunks.  



The criteria for `decomposing systems into modules <http://sunnyday.mit.edu/16.355/parnas-criteria.html">`_  is pretty clear.  The essential module design is oriented around design decisions which can change.  But there is a taxonomy of design decisions.  Parnas provides some examples (Data Structures, Algorithms, API's, Performance.)



In my case, there are a few additional kinds of design decisions.  



1.  External WS APIs.  These are a separate package that can be installed in site-packages and distributed to clients.  Except, of course, that our application doesn't use them, so we don't need them in site-packages, only our customers do.  Still, the API rule should apply.



2.  "Irrelevant" data structures.  Many files and external interfaces impose data structures which are largely irrelevant to our application.  External XSD's, for example, are part of an interface, not part of our core application.  Also, interestingly, the endless complexity of spreadsheets that are used as data sources lead to irrelevant details.  We've used `XLRD <http://www.lexicon.net/sjmachin/xlrd.htm>`_  and `csv <http://docs.python.org/lib/module-csv.html>`_ .  Further, we're using a SAX parser for XML spreadsheets.  We can collect a lot of this in a "Workbook Library".  It isn't core to our application, it's a distraction.  But it isn't a package we'll polish up and put into an open-source repository.  But it isn't core, either.



3.  Tools.  For example, we generate Python classes from XSD's.  Clearly, this is separate.  But, just as clearly, it isn't very polished, and not usable as a stand-alone tool.  Do we leave this inside the main application directory under /opt/someApp?  Or do we register our intent to make it a stand-alone product and toss it into a separate /opt/someTool directory?



Strategy
---------



A web admin I respect said "It doesn't matter what you choose, someone will hate your decision."  Helpful advice.  In other words, "quit waffling -- it can't be perfect."  Indeed, what would "perfect" even mean?



What's important seem to be the following.



**Modularize Everything**.  
    The magic number is 7 ± 2 "concepts" in a module.  A few closely related classes go in a module.  More complex modules tend to be a problem.  When you're in a hurry and it isn't clear where the boundaries should fall, go for smaller.



**Think Packages**.  
    I'm starting to see that there's nothing wrong with a package that contains a single __init__.py file; this is a place-holder for future growth.  You can add to this structure easily.  I think this should be what you put down in the first sprint to get things started.  Later it can be refactored as the design matures.



    If, after a few months, the overall direction seems to have shifted, that package can be collapsed back into a module -- with no breakage.  I find it slightlly easier to refactor a single-module package into a module than to decompose a growing (and possibly bloated) module into a multi-file package.



**Written Justification**.  
    You need tidy, clear, documentation for your overall structure.  Be particularly focused on introducing newbies to your project.  It has to make compelling sense -- you have to know that your colleagues will do the right kind of design.  Few things are as challenging as the "you're right, it probably doesn't belong there" conversation surrounding some particularly egregious hand-waving.  It's most helpful with a n00b: they can see the irregularities more clearly than you can.



Our Stuff
----------



We've got a collection of /opt/this and /opt/that directories for the various "top-level" components.  Right now, we're using /opt/this/this-1.1 and /opt/that/that-2.1 kind of names.  These map to subversion tagged versions.  The idea is that we have version 1.1, 1.2 and 1.3 all side-by-side.  We try to avoid replacing a previous version so that we can fall-back -- if necessary -- during an attempted upgrade.  



For most of our "big" application systems we have /var/opt/this/prod and /var/opt/this/training for our "working" directory trees.  This allows us to more easily manage production, QA, training, staging and other parallel implementations of the same baseline application. 



Our small applications (and packages) have their own /opt directories.  Some don't have their own /var/opt working directories, since they're used by our big applications.  Many potentially reusable packages have setup.py scripts and are also installed into site-packages.



We're making an intentional effort to be absolutely sure that nothing in /home is ever used anywhere.   When your application is big (hundreds of files) it's easy to overlook something.  Sadly, I've looked at a fair amount of software where a poorly-chosen path to a module was snuck in somewhere and there were file conflicts that occurred rarely and made the software "flaky".




