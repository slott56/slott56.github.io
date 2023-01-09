Amazing how Windows is “special.”
=================================

:date: 2016-12-13 08:00
:tags: #python,windows,POSIX,linux
:slug: 2016_12_13-amazing_how_windows_is_special
:category: Technologies
:status: published


Here's the quote:

   ...it is amazing how Windows is “special.” Back when ..., special
   things had to be done for Windows. Python continues the tradition w/
   an entire section in its doco titled “3. Using Python on Windows”


I wasn't sure what to make of this.

It appeared that they want Windows to be the norm and Linux/Mac
OS/POSIX to be treated as an exception.

I find that baffling. POSIX is a standard. Mac OS X is
POSIX-compliant. Linux distros are generally POSIX-compliant. There's
a nice list: https://en.wikipedia.org/wiki/POSIX

Windows is not POSIX-compliant. It seems to me that non-standard ==
special shouldn't be "amazing." It should be "tiresome" or "annoying."

Windows tools are uniquely awful. Or, perhaps, "special". Windows is
so "special" that the IDE concept appears to have evolved as a
solution to the awfulness. Using a Windows IDE (like Visual Studio)
insulated one from the vagaries of Windows. It appears this is
particularly important when trying to create a binary that will work
in multiple incarnations of Windows.

In Linux (and POSIX-compliant OS's in general) the OS **is** the IDE.
Start
here: https://sanctum.geek.nz/arabesque/unix-as-ide-introduction/.
This seems so much simpler and more rational. Perhaps I'm just biased
because I've used so many OS's that aren't Windows.

Worth considering: http://www.psychocats.net/ubuntu/virtualbox

When asked about IDE's for Python, I tell people that I've used a
number of text editors to write Python code:

-  vi
-  BBEdit
-  Atom
-  Komodo Edit
-  Notepad++
-  PyCharm
-  IDLE
-  Jupyter Notebook


They all work nicely. It's difficult to recommend one because they
all have distinct features. I always wind up with a lot of
command-line interaction. The "run-a-command-from-the-IDE" has
complex dialog boxes and sometimes confusing limitations. It's easier
to simply write a script than discern the nuances of the IDE
configuration rules.

These are (mostly) platform-independent. They can minimize a few of
the Windows "features." They don't eliminate all of the Windows
issues.

In all cases -- except using IDLE -- I also have a Python ``>>>``
prompt open in a terminal window.


I strongly encourage everyone to work this way. The terminal window
interaction can be copied and pasted into doctest strings. You've
written a unit test without really trying. It's extremely productive.
It gets away from IDE wrappers. It does expose some Windows-isms, but
as long as you can limit the number of times you find Windows
"amazing," that's not a problem.





