Why rewrite a shell script in Python?
=====================================

:date: 2016-06-07 08:00
:tags: #python,bash,ksh,shell
:slug: 2016_06_07-why_rewrite_a_shell_script_in_python
:category: Technologies
:status: published


Here's the actual quote:

    Why would you need to rewrite a working script in python ? Was there
    any business direction towards this ?


This was an unexpected response. And unwelcome. I guess I called their
baby ugly.

The short answer is that the shell script language is perhaps one of
the worst programming languages ever invented. Okay. I suppose it's
better than
`whitespace <https://en.wikipedia.org/wiki/Whitespace_(programming_language)>`__.
Okay it's better than many others.
See https://en.wikipedia.org/wiki/Esoteric_programming_language

The longer answer is this:

-   There are (at least) three ksh scripts involved, two of which are
    over 1,000 lines long. It's not perfectly clear precisely what's
    involved. It's ksh. Code could come from a variety of places through
    very obscure paths; e.g. the source command and it's synonym, ..

-   There are no comments other than #!/usr/bin/ksh and a few places
    where code is commented out.  Without explanation.

-   There is no other documentation. The author had sent a email
    describing the github repo. The repo lacked a README. It took two
    tries to get them to understand that any email describing a repo
    should have been the README **in** the repo. There is barely even a
    command-line synopsis. (Eventually, I found it in the parser for
    command-line options.)

-   No tests of any kind.


The last point is the one that I find shocking. And I find it shocking
on a regular basis.


Folks are able and willing to write 1,000's of lines of shell script
without a single unit test, integration test, system test,
performance test, anything test. How do they know if this works? Why
am I supposed to trust it?


More importantly, how can I meaningfully wrap this into a RESTful API
if I'm not even sure what the command-line interface **really** is?
It's the shell. It could use environment variables that are otherwise
undocumented. They would be discovered when they cause a crash at run
time. Crashes that become an HTTP 500 status code and a traceback
error message in the web log.


The "business direction" sounds like an attempt to trump the
technical discussion with a business consideration like "cost" or
"benefit". It should be pretty self-evident that 1,000's of lines of
shell script code is technical debt.


The minimally viable replacement will probably be a similarly-sized
of Python script that mindlessly mirrors the original shell script.
It's sometimes quite hard to tell what purpose a shell function
really serves. The endless use (and re-use) of global variables can
make state change hard to follow. Also, the use of temporary files
which are parsed (and reparsed) as a way to set state is a serious
problem.


What's important is that the various OS services used by the shell
script are mockable. Which means that each of the 100 or so
individual functions within the script can be tested in isolation.
Once that's out of the way, refactoring becomes plausible.

Let's savor those words for a moment: Tested. In. Isolation.

Ahhh.


The better replacement is (I think) about 250 lines of Python --
perhaps less -- that perform the real 8-step process that we're
automating.  Getting rid of bash language cruft is challenging, but
essential.





