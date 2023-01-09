Needlessly Redundant Overcommunication and DevOps
=================================================

:date: 2015-11-03 08:00
:tags: DevOps
:slug: 2015_11_03-needlessly_redundant_overcommunication_and_devops
:category: Technologies
:status: published

| At the "day job" I use a Windows laptop. It was essential for a
  project I might have started, but didn't. So now I'm stuck with it
  until the budgetary gods deem that it's been paid for and I can
  request something more useful.  Mostly, however, Windows is fine. It
  doesn't behave too badly and most of the awful "features" are
  concealed by Python's libraries.
| This is context for a strange interaction today. It seems to exemplify
  DevOps and the cruddy laptop problem.
| The goofy Microsoft Office Communicator -- the one that's so often
  used instead of a good chat program like Slack or HipChat -- pinged.
   The message went something like this.

   **"I sent you an email just now. Can you read it and reply?"**

| 
| I was stunned. Too stunned to save the text.  This is either someone
  being aggressive almost to a point that hints at rudeness, or someone
  vague on how email works. Let's assume the second option. I can only
  reply, "I agree with you, that is how email works."
| The email was a kind of vague question about server provisioning.  It
  was something along the lines of

   "Do we provision our own server with Ansible or Chef? Or is there a
   team to provision servers for us? ..."

| 
| It went on to describe details of a fantasy world where someone would
  write Chef scripts for them.  The rest of the email mostly ignored the
  first question entirely.

The Real Question
-----------------

| If you're familiar with DevOps as a concept, then server provisioning
  is -- like most problems -- something that the developers need to
  solve. Technical Support folks may provide tools (Ansible, for
  example) to help build the server, but there aren't a room full of
  support people waiting for your story ("make me a server") to appear
  on their Kanban board.
| Indeed, there was *never* the kind of support implied in the email,
  even in non-DevOps organizations. In a "traditional"  Dev-vs.-Ops
  organization, the folks that built servers were (a) overbooked, (b)
  uninterested in the details of our particular problem, or (c) only
  grudgingly let us use an existing server that doesn't quite fit our
  requirements. They rarely built servers for us.
| Reason A, of course, is business as usual. Unless we're the Hippo
  (Highest Paid Person in the Organization,) there's always some other
  project that's somehow more important than whatever foolishness we're
  engaged in. How many times have we been told that "The STARS Project
  is tying up all our resources. It will be 90 days before..."? Gotcha.
  The bad part about this situation is when the person paying the bills
  says to me "You need to make them respond." How -- precisely -- do you
  propose that I change the internal reward system of the ops people?
| We could label this as a passive-aggressive approach. They're waiting
  for us establish a schedule so that they can shoot it down. Or maybe
  that's reading way too much into the situation. Maybe they're really
  just overbooked.
| Regarding reason B. Years ago, I had a hilarious interaction where we
  sent a stream of emails explaining our server requirements. The emails
  were not exactly *ignored*. But. When we asked about the status of our
  servers, the person responsible for the team brought a yellow pad and
  wrote down the requirements. I read the email to them. Without a trace
  of embarrassment, they wrote down what I was reading from an email.
   (It was long enough ago, that we didn't have laptops, and I had a
  hard-copy of the email. They refused the hard-copy. I had to read it.
  Really.)
| Were they clueless about how email works? Or. Was this a kind of
  passive-aggressive approach to architecture where our input was
  discounted to zero because it didn't count until they wrote it on a
  their yellow pad? The behavior was bizarre.
| Something similar happened with another organization. We made server
  recommendations. They didn't like the server recommendations. Not
  because the recommendations seemed wrong, but because we didn't have a
  formal sciency-seeming methodology for fantasizing about servers that
  were required to support the fantasy software which hadn't been
  written yet. They felt it necessary to complain. And when we talked
  with hardware vendors, they felt it necessary to customize the cheap
  commodity servers.

   [It got weirder. They were convinced that a server farm needed to be
   designed from the bottom up.  I endured a lecture on how a properly
   sciency-seeming methodology started by deciding on L1 and L2 cache
   sizing, bus timing, and worked through memory allocation and then I
   slowly grew to see that they had no clue what they were talking about
   when buying commodity servers by the rack-full for software that
   doesn't exist yet.]

| We all know about reason C. The reason for DevOps is to avoid being
  stuffed into a kind of random server where there are upgrades that we
  all have to agree on. Or -- worse -- a server that can't be upgraded
  because no one will agree. A single app team vetos all changes.
| "We can't install Anaconda 3 because we know that Python 3 is
  incompatible with Python 2"...
| What?
| I stopped understanding at that point. It seemed like the rest of the
  answer amounted to "having the second Anaconda on a separate path
  could lead to problems. It can't be **proven** that no problems will
  arise, so we'll assume that -- somehow -- PATH settings will get
  altered randomly and a Python 2 job will crash because it accidentally
  had the wrong PATH and accidentally ran with Python 3."
| It was impossible to explain that this is a non-problem. Their
  response was "But we can't be **sure**." That's the last resort of
  someone who refuses to change. And it's the *final* answer. Even if
  you do a proof-of-concept, they'll find reasons to doubt the POC's
  results because they can't be **sure** the POC mirrors production.

The Real Answer
---------------

| The answer to the original Ping and the Email was "You're going to do
  this yourself."  I included links to four or five corporate missives
  on Chef, Ansible, DevOps, and how to fill in the form for a cloud
  server.
| I have my doubts -- though -- that this would be seen as helpful.
| They may not be happy because they don't get to use Communicator and
  Email and someone else's Kanban board to get this done. They don't get
  to ask someone else what they're doing and why they're not getting it
  done on time. They don't get to second-guess their technical
  decisions. They actually have to do it. And that may not work out
  well.
| The truly passive-aggressive don't seem to do things by themselves. It
  appears to me that they spend a lot of time looking for reasons to
  stall. Either they need to get more information or get organized or
  they need to have some kind more official "permission" to proceed.
  Lacking any further information, I chalk it up to them only feeling
  successful when they've found the flaws in what someone else did.
| It's challenging sometimes to make it clear that a rambling email
  asking for someone else to help is going nowhere. A Communicator ping
  followed by an email isn't actually getting anything **done**. It's
  essentially stalling, waiting for more information, getting organized,
  or waiting for permission. Overcommunication can become a stalling
  tactic or maybe a way to avoid responsibility.
| I'm stuck with a cruddy laptop because the budget gods have laid down
  some laws that don't make a lick of technical sense. I think that the
  short-sighted "use it until it physically wears out" might be more
  costly than "find the right tool, we'll recycle the old one
  appropriately." In the same way, the shared server world view is
  clearly costly.  We shouldn't share a server "because it's there."
| The move to DevOps allows us to build a server rather than discuss
  building a server.
| I want a DevOps parallel for my developer workstation. I don't want
  permission or authorization. I don't want to overcommunicate with the
  budget gods. I want a workstation unencumbered by permission-seeking.





