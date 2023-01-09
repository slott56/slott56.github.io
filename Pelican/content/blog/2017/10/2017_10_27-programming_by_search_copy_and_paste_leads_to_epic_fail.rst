Programming by Search, Copy, and Paste Leads to Epic Fail
=========================================================

:date: 2017-10-27 18:08
:tags: Design Principles,#python,architecture
:slug: 2017_10_27-programming_by_search_copy_and_paste_leads_to_epic_fail
:category: Technologies
:status: published


In a way, this is about an epic fail attempting copy-and-paste coding.
But really, this is about thinking outside the box. The issue -- to me
-- comes from failing to see the box. Here's the body of the email,
edited slightly.

   "...how determine when a file has completed downloading. It would be
   helpful if code snippets in a unix shell and Python.

   "I did Google but none seemed to address the fundamental race
   conditions. They all involve a variant of try, sleep and try again.
   This is problematic for my particular case because the file sizes
   very significantly."


I'll ignore the grammar problems and focus on the intent of the "I did
Google..." part. Based on some personal knowledge, I doubt there was
more than a single search string tried. And I doubt that more than a
single page of the response was looked at. Those are not important
concerns.

The important concern is the shocking vagueness of the problem
statement. These words are almost entirely meaningless:

   "a file has completed downloading"


Imagine the variety of possible file transfer protocols that could be
involved, and how many of them can be properly scripted. Take all the
time you want. It can help to make a list of all the protocols that
make this is a non-problem.

No protocol was named. Therefore, a protocol was assumed. And the
presence of this kind of tacit assumption forms an implicit box
restricting what they're doing. The restriction is so unyielding to
them than they don't even need to mention it. It's as essential to
them as air. They need it, but cannot see it, and refused to
acknowledge it.

At this point, all we can do is make random guesses.

  ("Why didn't you ask them for clarification?" you ask.  Good point.
  It's a personal failure in this case. The back-and-forth would take
  days. Eventually, they would send me useless explanations of deep
  ineptitude or a need to engage in corporate politics. Or both. I'll
  admit that I'm a jerk about requiring folks to take a first step and
  make a stab at code. Without code, I find it largely impossible to
  determine what they're **really** talking about. The above question is
  a prime example of a disconnection from reality that's too
  exasperating to deal with except superficially.)

Identifying the Box
-------------------

Guess #1. This may be about FTP (or SFTP) file transfers. Further, it
may involve FTP file uploads to a server, where the client doesn't
disclose a size. Yes, the word "downloading" seems to preclude this
guess, but almost all other choices aren't even possible.

If it really was a client side **download**, this is trivially
automated using any of the available FTP client programs, include
wget, curl, sftp, etc. The Python ftplib seems to be a fully automated
client for FTP. The documentation is packed with examples. It seems
unlikely that the question is actually client-side.

It's also possible that a single search failed to reveal all these
automatable FTP clients.

Guess #2. "determine when"? Who actually cares when the upload
finishes? An upload matters to the next client doing a download, or --
perhaps -- to a process that's supposed to consume the uploaded file.
Is that what this is about?

Is the real question "how to trigger processing of an uploaded file
when using FTP?"

In this case, we're left with stacks of follow-up questions.
Primarily: "Why are you using FTP?"

If they replace their silly FTP (or SFTP) server with a RESTful API,
they won't have these problems. It takes a few days to write a secure
file-upload Flask container. With a swagger spec. And unit tests. And
Gherkin feature definitions, and a behave test suite to be sure it
\*really\* works.  It doesn't need very many routes. On completion of
upload, it can fork off subprocesses to process the uploaded files.
This is not hard. Really. Flask + Celery will do this.

Understanding the problem seems to require stepping outside of some
box. It appears this is a struggle because of a poorly-defined box: a
box assumed without being stated.

Working With the Box
--------------------


At this point, we can only pretend the problem is about triggering
processing after an upload. Let's further pretend the FTP is a legal
requirement. Or we can pretend that SFTP is imposed by an inept IT
department who also loves living inside some poorly-defined box. We're
stuck with FTP for inexplicable reasons.

What can we do to game an FTP server to trigger processing of files of
unknown sizes?

-  Write our own FTP server. This isn't very hard. It is, however, far
   simpler to write a RESTful Flask service that handles the file upload
   as a POST request via curl or wget. Writing an FTP server's a pain in
   the ass because the FTP protocol is surprisingly complex. Even
   writing an FTP subset that serves very specific client needs can be
   painful.

-  Poll the upload directory. This implies a race condition. Polling
   (and the race condition) have no practical consequences. If you want
   "real-time", write a RESTful API and don't use FTP. Since you're
   insisting on FTP, a delay is going to be part of the solution.


I'm more than a little shocked that search was considered as a viable
design strategy to solving this problem. It doesn't seem like
searching for solutions is required at all. I'm probably overstating
this, but it seems sort of trivial and obvious that either a second
file is required or a better file protocol is required. This seems to
be simple "thinking" not "googling."

There are bunches of ways to approach this. Here are a few ways to use
a second file and some kind of naming convention to show that two
files are part of one transfer.

-  Send a file with the size of the target file \*before\* the target
   file. When the target file matches the stated size, initiate
   processing.

-  Send a file with the size and MD5 checksum of the target file. etc.

-  Send a file \*after\* the target file with the size and checksum.
   When this file shows up, simply confirm that the first file is all
   there.


Yes, polling is required. However, there's no race condition: there
are two separate conditions which must both be met. The files are
provided serially, the conditions are met serially.


Here are a two approaches that use a file format that properly
handles completeness.


-   Gzip the file. The file receipt polling loop repeatedly tries to
    unzip it. If the unzip fails, the file is incomplete.

    Don't want to spend too much CPU time? Wait until the size has
    been stable for two polling intervals and then try to unzip
    then.

-   Tar the file. Yes. A tar archive of a single file can be checked
    for integrity. When the archive can be checked and shown to be
    valid, the target element can be extracted and processed.

    Don't want to spend CPU time validating? Again. Wait for a
    stable size for a few polling intervals.


And, of course, it's possible to invent an entirely home-brewed
file-wrapping protocol. Here's an approach.

   
-   Wrap the content in MIME-style headers. These can provide a
    size or a terminator string to help identify the end of the
    transfer.


The point here is that googling for code isn't part of solving
this problem. Indeed, it can't solve this problem. Merely
thinking about the nature of the problem ("triggering
processing", "knowing the size") seemed necessary and
sufficient to frame a solution.

What's Essential
----------------


Here's what didn't happen:

-   State the actual problem.

-   Identify the boxes constraining the solution. Write them down. In words. There may be more
    than one.

-   Locate code to work with the boxes. Find the libraries or
    packages. Install them. Write a hello world. example to be sure
    that the code is understood.


Then -- and only then -- can we start to imagine solutions and ask
questions about the boxes or the code that might manage the boxes.


   It's impossible to state this strongly enough: We can't think outside
   the box if we refuse to acknowledge the box.








