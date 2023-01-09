Security Vulnerabilities
========================

:date: 2010-03-19 08:00
:tags: security
:slug: 2010_03_19-security_vulnerabilities
:category: Technologies
:status: published

I lean on the OWASP list heavily.
http://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project

This analysis is handy also:
http://www.cenzic.com/downloads/Cenzic_AppSecTrends_Q1-Q2-2009.pdf

The point is that most of the vulnerabilities are pretty clear.

#.  Injection flaws: SQL, OS, and LDAP injection. Pretty clear that
    building SQL, shell scripts or LDAP queries dynamically is simply
    wrong. Don't do it. Use SQL Binding, and proper
    escaping/quoting/filtering.

#.  Cross-site scripting. Again, proper escaping/quoting/filtering is
    essential.

#.  Authentication and session management. This is generally done well
    by most frameworks.

#.  Insecure object references. Files, directories, etc. A good
    framework prevents this by making all URL's into indirect
    references to underlying objects.

#.  Cross-site request forgeries, like session management, are
    generally handled by frameworks.

#.  Security misconfiguration. This is where actual skills shown up.
    This can be hard, and takes work.

#.  URL-level validation. I thought this went without saying: all
    URL's are available to users even if the link is not on a page
    anywhere; anyone can bookmark or forge a request. All requests
    must be validated even if "there's no way the user could see that
    link and click on it."

#.  Unvalidated redirects and forwards. This strikes me as weird
    because we use redirects in one (and only one) situation:
    redirect-after-post. However, if you synthesize a redirect from
    user input -- without filtering, validating or quoting properly --
    you'd be open to problems.

#.  Insecure crypto. Like security misconfiguration, this is very hard
    work on the part of architects and administrators. Key escrow
    systems are part of this, as is encrypted database fields and
    (possibly) encrypted physical storage. Sigh.

#.  Transport layer protection. SSL is part of any security framework.

Some of these are solved by using commonly-available open-source
frameworks.

Too many people reject these open-source solutions for dumb or
wrong reasons.

One of the biggest mistakes is to say that a framework is "too
heavyweight" for a small web application.

The rules are simple: **either reinvent the wheel properly, or use
an established open-source framework**.

Open Source? Yes, one that can be vetted for security
vulnerabilities.





