XML/XSLT - A Response
=====================

:date: 2003-12-24 20:37
:tags: technologies,xml
:slug: 2003_12_24-xmlxslt_a_response
:category: Technologies
:status: published





The idea of "universal" processing via
XSLT is moderately appealing.  There's a big issue with poorly defined
semantics, which always breaks a meta-data driven approache.  The holy grail is
perfect metadata from which all application software can be derived in a trivial
way.  I'm not sure this is ever achievable - it requires a perfect metadata
description language and perfect metadata for the problem domain. 




However, more pragmatically,
I'm deeply suspicious of introducing
**Yet Another Programming Language**  into the world.  XSLT as a
simple-minded tool to transform notations is fair, but once you start to usurp
real computation, the value of yet another broadly focused language seems to
diminish.  We already have ecmas/javascript that can be packaged up with the
XSLT, effectively splitting it into two languages; but when javascript is too
simple for some problems, we have step outside javascript into another language.
Why not just start with the other language (Java, C#, Python) and skip the XSLT
step.  Keep XSLT focused on the one thing is does well, and do the other things
in existing general-purpose programming languages. 








