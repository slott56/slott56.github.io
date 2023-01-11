Configuration Files -- Again
============================

:date: 2008-12-09 02:29
:tags: architecture,design,data structure,algorithm
:slug: 2008_12_09-configuration_files_again
:category: Architecture & Design
:status: published







See `Configuration Options in Code or INI Files? <http://www.heikkitoivonen.net/blog/2008/12/07/configuration-options-in-code-or-ini-files/>`_ .  Also, see `Python as Configuration Language <{filename}/blog/2008/03/2008_03_28-python_as_configuration_language_more_good_ideas.rst>`_ .



Here's some of the argument.



-   **Editing**.  Which is easier?  Which is more expressive?  Some say that Text (INI format especially) is easier -- but I don't see what.  Python is just as easy as INI, and has more expressive power.  Advantage Python.

-   **Reloading**.  It is easier to reload configuration options from a regular text file than a Python import.  I'm not sure what we're reloading or why, but I do depend on Apache reloading it's configuration.  However, I've never written a program that reloaded anything.

-   **Configuration Control**.  This statement makes approximately no sense: "Code files should be read only"  What distinguishes code in .INI format from code in .PY format?  Both are code; one is relatively stable "source" and the other is relatively "dymamic" configuration.  But they're both code, subject to slightly different rules of use.  This usage difference doesn't have anything to do with syntax.

-   **Debugging**.  Somehow, .INI errors are purported to be easier to debug.  I don't get this.  I suppose it's true if you don't use **try**  blocks.  If, on the other hand, you use ordinary **try**  blocks, you can produce easy-to-live-with error messages from importing a Python config module.

-   **"Security"**.  I put "security" in quotes because it's not at all clear what we're securing against.



So Python has better syntax, and non-Python is slightly easier to reload.  At this point, we've got no good reason for anything other than Python.



**The Security Specter**



It's not clear why "security" keeps surfacing.  I can't determine the threat scenario.  Since the config files are under tight permission control, only a sys admin can change them.



So, the security threat is a sys admin who knows Python and is using the configuration files to subvert something in the organization.



And -- bonus -- there can be no other corporate controls over the system being subverted.  



Wait -- what?



No controls.  The security thing only makes sense when you have programming sysadmins and no controls.  Python syntax vs. .INI syntax has nothing to do with this.



The security argument makes no sense.  There is no point in .INI configuration files.




