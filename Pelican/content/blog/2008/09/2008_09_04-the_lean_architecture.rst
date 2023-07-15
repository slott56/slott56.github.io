The Lean Architecture
=====================

:date: 2008-09-04 10:15
:tags: architecture,software design,complexity,database design
:slug: 2008_09_04-the_lean_architecture
:category: Architecture & Design
:status: published







First, look at "`Protecting your MySQL database from SQL injection attacks with GreenSQL <http://www.linux.com/feature/145341>`_ ".  Okay, a longish article on the ins and outs of installing something that blah blah blah



Wait -- what?  `GreenSQL <http://sourceforge.net/projects/greensql/>`_  is a proxy for MySQL that checks the SQL for certain kinds of injection attacks!?!?!



Now read `Twisted Radix: This is a Rant <Twisted radix: this is a rant>`_ .  Oh.  I get it.  The comments in the original article *are*  a riot. Bottom Line: there's no point in adding a layer like GreenSQL.  You don't need to "check" for SQL injection attacks, since it's easier to simply prevent them.



Just use bind variables. 



Rather than layer on extra software, one should just read the `OWASP Top 10 Vulnerabilities <http://www.owasp.org/index.php/Top_10_2007>`_  and address them systematically.



A1 Cross Site Scripting.
    Assume all user inputs include hidden javascript, and do appropriate HTML encoding.  **Do HTML Encoding.**   That's it.



A2 Injection Flaws.
    Never build strings of anything, particularly SQL.  Use bind variables, or similar techniques like HTML encoding.  That's all.  Don't layer in extra junk.  **Use.  Bind.  Variables.**



A3 Malicious File Execution.
    Assume all user files are binaries that will cause problems.  Validate the contents and segregate them into "media" directories that can't be used for other purposes.  Django uses PIL to validate image files.  And Django never accepts a filename from the web -- it generates its own.  **Always Generate Filenames**.



A4 Insecure Direct Object Reference.
    This is subtle, since REST demands a direct object reference.  Providing a reference isn't a problem, as long as object dereferencing has appropriate authorization checks.



A5 Cross Site Request Forgery.
    This is complicated -- there are a lot of use cases for bookmarking and spoofing form data.  It's handled by Django in a pretty cool way -- a simple hidden field with a unique token that must come back as sent.  This is the "nonce" technique used in digest authentication.



A6 Information Leakage and Improper Error Handling.
    That's what logs are for.  HTML bletches are a big mistake.  When in doubt, show 500.html and keep quiet.  **Don't Debug via End-User HTML**.



A7 Broken Authentication and Session Management.
    Here's a tip: use a framework that does this -- **Don't Roll Your Own**\ ™.



A8 Insecure Cryptographic Storage.
    Like A5, this is tough: everyone wants to use crypto, but no one knows how to do key management.  A hard-coded key is useless.  Encrypted databases are only as secure as the keys, and the keys never seem to get handled properly.  Also, you have keep the database behind a firewall so only the web server itself has access.  Never store passwords, only digests of passwords.



A9 Insecure Communications.
    SSL is easy.  Use it.



A10 Failure to Restrict URL Access.
    Obscurity is not Security.  You can't say "no one will find the backdoor URL for debugging."  They will.  Plan on it.  Either secure it, or don't do it.



There's no room for after-the-fact glue like GreenSQL.  All of the OWASP vulnerabilities are solved in the basic design of the framework you chose and the application built on that framework.  



An application that assembles SQL on the fly is flawed to begin with, and no amount of patching will fix it.  It's an arms race between SQL injection tricks and software filtering.  Someone can always create SQL so confusingly complex that the tool is fooled.



Further, everything you add can add bugs and vulnerabilities.  Less software is better; no software is best.  Keep it lean, simple and secure.




