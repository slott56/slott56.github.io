TCP/IP Mysteries and user support
=================================

:date: 2014-02-13 08:00
:tags: user stories
:slug: 2014_02_13-tcpip_mysteries_and_user_support
:category: Technologies
:status: published

| It's not clear, actually, if this involves a TCP/IP "Mystery". What it
  may involve is a simple lack of ability to communicate. Or something.
| I got this question:

   "Request help w/ finding a reference or you can post a blog about how
   you can you have 2 oracle servers or for that matter any 2 servers
   listening in on different sockets on the same unix box."

| And this background. Such as it is.

   "They are going to ask, how can this work? My lame explanation is
   that on a unix box you can have multiple servers listening in on
   different ports. I tried Googling around but couldn’t find anything
   good."

| It appears that the DBA provided a TNSNAMES.ORA. And some desktop tool
  user was not happy with the TNSNAMES.ORA that was provided.
| The saga is long and sad.
| It amounts to something like this.
| DBA: Here's the TNSNAMES.ORA.
| User: That didn't work.
| DBA: Yes, it did.
| User: No, it didn't. You're an idiot.
| DBA: I know you are but what am I?
| And it devolved from there into a request to help use Google to locate
  a tutorial on TCP/IP address and port numbers.
| I'll repeat that: a request to help use Google.
| Apparently, the desktop user had done something in database A and
  couldn't find the results in database B. And didn't understand what
  was going on.
| And this lead to the DBA asking me to help with Google to prove that
  the DBA's TNSNAMES.ORA worked.
| How does that help the user?





