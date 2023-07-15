Python as Configuration Language -- More Good Ideas
===================================================

:date: 2008-03-28 21:27
:tags: architecture,software design,data structure,algorithm,python
:slug: 2008_03_28-python_as_configuration_language_more_good_ideas
:category: Architecture & Design
:status: published







Some recent thoughts on using Python, directly, as configuration file syntax.  In a way, a configuration is a highly-specialized Domain Specific Language focused on the application's problem domain.  The point is to leverage syntax we already have to create meaningful configuration files.



"Python is sometimes a good use for a configuration language -- such as in Django."



While it's true that Django does this elegantly, I'd been doing something more complex than Django's relatively clear and simple approach.  My example in `Two Python Config-File Design Patterns <{filename}/blog/2008/01/2008_01_19-two_python_config_file_design_patterns.rst>`_  was a structural definition that was difficult to express in any other language.



The structural configuration file was more like Django's Model definitions than a simple "configuration" file.  However, in a very real sense, it is the model which configures Django to have the data elements we want to display and persist.



I've used the **Structural Declaration**  pattern a number of times.  I cribbed it from the packages like urllib2 where you build up a fairly complex object from component parts.



Malicious Code
--------------



"It's a security vulnerability."  While technically true that you might get "malicious" configuration from a support forum, this is an easy vulnerability to prevent.  It's configuration.  It should be obvious what it is doing. 



If the configuration starts to look like code -- i.e., it is no longer a strictly declarative construction -- then an architectural design expectation has been violated.  Any doubt about the content of a configuration file is a red-alert, class 1, fatal defect.  Epic Fail.



The Apache configuration, for example, has code-like pattern-matching and decision-making rules.  This is a compromise because Apache needs speed, and also needs flexibility.  For this kind of thing, I would prefer a Plain-Old Python extension as a proper subclass that extends the framework.  Subclasses and extensions can preserve the distinction between "a few constants that are reused heavily and likely to change" and "more code to handle special cases."



Syntax Woes
-----------



"By using Python as your configuration syntax, you force your users to learn the idiosyncrasies of Python syntax when configuring."



Interesting point.  I'll counter with the observation that XML syntax is opaque and .INI syntax is more obscure that Python syntax.



The point of a configuration file is specifically not to write code.  The lowest level of configuration is a Django-style sequence of simple assignment statements (which is almost precisely the same syntax as an .INI file.)  The higher level is a more complex structural declaration that is more clear in Python than any .INI file.  (I know, I had to struggle with an .INI file that was a total mystery.)



Also, "Configuration files cease to work whenever Python changes."  I'm not sure how to interpret this.  Since the application is in Python, the whole house of cards collapses when Python changes.  The configuration is the least of my worries.  If I had a program in C that merely imported the Python interpreter to parse a configuration file, perhaps there's something to this consideration.



Diagnostics
------------



"Errors in configuration files can be hard to diagnose for users, as it may not be clear whether the error arose from the configuration or the app itself."



This is an interesting point.  There is a handy trick for this, however.  

::

    try:
        execfile('config.py')
    except Exception, e:
        logging.exception("Configuration Syntax:", str(e))
        sys.exit(2)






We could, additionally, check for Python SyntaxError specifically.  We could also manipulate the traceback to produce more meaningful error messages.




Preventing Problems
-------------------




The "malicious code injection" problem is good way to talk about good design and bad design.  A reasonably careful design and a little bit of looking at the configuration file will prevent problems.  




[Additionally, if someone is in the habit of simply installing files they got from a support forum, then perhaps they should consider a different line of work.]




This malice consideration says that we need a design that makes it trivial for anyone to vet a configuration file for malicious code.  This vet-ability (a kind of maintainability) is central to any good configuration file design, irrespective of syntax.




The "syntax" consideration is one of the strengths of Python.  Python syntax (for assignment statements) is as simple as .INI files, and more flexible.  The idea that the core syntax of the assignment statement could change -- while remotely possible -- isn't on the horizon any time soon.  I'm perfectly confident.




Finally, the diagnostics issue gives us another direction for good design.  Any configuration file can have serious problems with improper data.  I've seen very sophisticated modules to read, parse and report problems in .INI files.  Personally, I'd like to leave out the reading and parsing part and focus on the problem detection and reporting.




Rules
-----




I've found a few moderately complex problems where .INI files are too simple.  The amount of crapola that has to be done to describe the configuration exceeds the capabilities of .INI files.  That's when Python really pays out handsome rewards.




First, make the application robust enough that the configuration file is simple and can be inspected by someone other than the application's author.  The meaning should be manifest.




Second, make the configuration simple enough that it doesn't use too much Python syntax.




Third, make is easy to diagnose syntax problems; leverage what Python already does for us.  We can then concentrate on the semantics of the configuration file.  It's all about the meaning.











