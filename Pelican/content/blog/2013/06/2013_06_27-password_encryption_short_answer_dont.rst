Password Encryption -- Short Answer: Don't.
===========================================

:date: 2013-06-27 10:03
:tags: algorithm,software process improvement,encryption,security
:slug: 2013_06_27-password_encryption_short_answer_dont
:category: Architecture & Design
:status: published

| First, read this.    `Why passwords have never been weaker—and
  crackers have never been
  stronger <http://arstechnica.com/security/2012/08/passwords-under-assault/>`__.
| There are numerous important lessons in this article.
| One of the small lessons is that changing your password every sixty or
  ninety days is farcical.  The rainbow table algorithms can crack a
  badly-done password in minutes.  Every 60 days, the cracker has to
  spend a few minutes breaking your new password.  Why bother changing
  it?  It only annoys the haxorz; they'll be using your account within a
  few minutes.  However.  That practice is now so ingrained that it's
  difficult to dislodge from the heads of security consultants.
| The big lesson, however, is profound.
| **Work Experience**
| Recently, I got a request from a developer on how to encrypt a
  password.  We have a Python back-end and the developer was asking
  which crypto package to download and how to install it.
| "Crypto?" I asked.  "Why do we need crypto?"
| "To encrypt passwords," they replied.
| I spat coffee on my monitor.  I felt like hitting Caps Lock in the
  chat window so I could respond like this: "**NEVER ENCRYPT A PASSWORD,
  YOU DOLT**."
| I didn't, but I felt like it.
| **Much Confusion**
| The conversation took hours.  Chat can be slow that way.  Also, I can
  be slow because I need to understand what's going on before I reply.
   I'm a slow thinker.  But the developer also needed to try stuff and
  provide concrete code examples, which takes time.
| At the time, I knew that passwords must be hashed with salt.  I hadn't
  read the Ars Technica article cited above, so I didn't know why
  computationally intensive hash algorithms are best for this.
| We had to discuss hash algorithms.
| We had to discuss algorithms for generating unique salt.
| We had to discuss random number generators and how to use an entropy
  source for a seed.
| We had to discuss http://www.ietf.org/rfc/rfc2617.txt in some depth,
  since the algorithms in section 3.2.2. show some best practices in
  creating hash summaries of usernames, passwords, and realms.
| All of this was, of course, side topics before we got to the heart of
  the matter.
| **What's Been Going On**
| After several hours, my "why" questions started revealing things.  The
  specific user story, for example, was slow to surface.
| Why?
| Partly because I didn't demand it early enough.
| But also, many technology folks will conceive of a "solution" and
  pursue that technical concept no matter how difficult or bizarre.  In
  some cases, the concept doesn't really solve the problem.
| I call this the "`Rat Holes of Lost
  Time <http://www.itmaybeahack.com/homepage/iblog/architecture/C412398194/E20060223203608/index.html>`__"
  phenomena: we chase some concept through numerous little rat-holes
  before we realize there's a lot of activity but no tangible progress.
   There's a perceptual narrowing that occurs when we focus on the
  technology.  Often, we're not actually solving the problem.

   IT people leap past the problem into the solution as naturally as
   they breathe. It's a hard habit to break.

| It turned out that they were creating some additional RESTful web
  services.  They knew that the RESTful requests needed proper
  authentication.  But, they were vague on the details of how to secure
  the new RESTful services.
| So they were chasing down their concept: encrypt a password and
  provide this encrypted password with each request.  They were half
  right, here.  A secure "token" is required.  But an encrypted password
  is a terrible token.
| **Use The Framework, Luke**
| What's most disturbing about this is the developer's blind spot.
| For some reason, the existence of other web services didn't enter into
  this developer's head.  Why didn't they read the code for the services
  created on earlier sprints?
| We're using Django.  We already have a RESTful web services framework
  with a complete (and high quality) security implementation.
| Nothing more is required.  Use the RESTful authentication already part
  of Django.
| In most cases, HTTPS is used to encrypt at the socket layer.  This
  means that Basic Authentication is all that's required.  This is a
  huge simplification, since all the RESTful frameworks already offer
  this.
| The Django Rest Framework has a nice
  `authentication <http://django-rest-framework.org/library/authentication.html>`__
  module.
| When using
  `Piston <https://bitbucket.org/jespern/django-piston/wiki/Documentation#!authentication>`__,
  it's easy to work with their Authentication handler.
| It's possible to make RESTful requests with Digest Authentication, if
  SSL is not being used.  For
  example, `Akoha <https://bitbucket.org/akoha/django-digest/wiki/Home>`__ handles
  this.  It's easy to extend a framework to add Digest in addition to
  Basic authentication.
| For other customers, I created an authentication handler between
  Piston and `ForgeRock
  OpenAM <http://www.forgerock.com/openam.html>`__ so that OpenAM tokens
  were used with each RESTful request.  (This requires some care to
  create a solution that is testable.)
| **Bottom Lines**
| Don't encrypt passwords.  Ever.
| Don't write your own hash and salt algorithm.  Use a framework that
  offers this to you.
| Read the Ars Technica article before doing anything password-related.



-----

No.  &quot;Don&#39;t encrypt passwords.  Ever.&quo...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2012-08-30 07:18:19.719000-04:00

No. "Don't encrypt passwords. Ever." It seems clear.
Not in a database. Not anywhere. Never use a reversible encryption.
How many different ways would you like me to repeat it?


hello!
Not even in the database?
--------------------------------

cuby<noreply@blogger.com>

2012-08-29 06:36:40.972000-04:00

hello!
Not even in the database?


Fine, we get the message, &quot;Don&#39;t encrypt ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2013-01-03 03:11:22.404000-05:00

Fine, we get the message, "Don't encrypt passwords. Ever."
But I don't see why (or why not). This blog post doesn't seem to explain
anything.


&quot;In most cases, HTTPS is used to encrypt at t...
-----------------------------------------------------

Paul Anthony McGowan<noreply@blogger.com>

2013-03-19 19:34:23.846000-04:00

"In most cases, HTTPS is used to encrypt at the socket layer. This means
that Basic Authentication is all that's required"
seems pretty clear.





