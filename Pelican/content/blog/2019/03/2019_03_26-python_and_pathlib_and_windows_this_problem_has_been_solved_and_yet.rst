Python and pathlib and Windows -- this problem has been solved -- and yet...
============================================================================

:date: 2019-03-26 08:00
:tags: windows,#python
:slug: 2019_03_26-python_and_pathlib_and_windows_this_problem_has_been_solved_and_yet
:category: Technologies
:status: published

| The Passive-Aggressive Programmer strikes again. A sad story of
  sadness.
| I tell everyone to stop using os.path and use pathlib. Everyone.
  Here's the link: https://docs.python.org/3/library/pathlib.html
| It's essential to realize the semantic richness of OS filesystem
  paths. They're not simply strings. They have a string representation,
  but there's quite a bit going on there that is not captured trivially
  by strings and string parsing.  "path/basename.extension" is more than
  just slashes and dots.
| Windows users, of course, have a nightmarish problem. Actually many
  nightmarish problems, one of which is pathnames.
| I tell Windows developers to use pathlib, it will make their life
  somewhat more bearable.
| And Yet. The Passive-Aggressive Programmer insists on using Windows as
  if it doesn't have a problem with \\ in path strings.
| Line 110 has a literal r"C:\\windows\\is\\xtreme\\evil" Note the \\x
  in the path. Without the r"" string, this literal raises a
  SyntaxError.
| Line 50 had subprocess.run(r"C:\\path\\to\\xectuable -option" + " " +
  options + " " + filename). Note the r"" string. Note the Linux-style
  -option, too. They're wrapping an open source app in a Python shell.
| You're with me so far? They're Windows devs. They've managed to use
  raw strings in two places. Right?
| But. They're Passive-Aggressive. They don't like PR comments of any
  kind. They'll "agree" to a change, but then... This...
| Line 50 should change. It's needs to use a list.
| The Passive Aggressive Programmer can't make a list work.

::

   list_of_arguments = ["C:\path\to\xectuable -option"] + options_list + ["C:\windows\is\xtreme\evil"]

| 
| See what they did there? They didn't want to change from string to
  list. (We had to go over it more than once.) They wanted to leave it
  alone. Grudgingly, they agreed to change from string to list.
| But.
| SyntaxError. See? The list just doesn't work. Python is weird. It's an
  undocumented WAT.
| *[Yes, some of us know the r's vanished. They author couldn't figure
  that out, though.]*
| And the pathlib suggestion?
| Since the strings are now a SyntaxError, they need me to fix that for
  them. I made them change to a list, therefore, I caused the
  SyntaxError. It would be a distraction to spend tome researching
  pathlib. "I need to Google and think about how to handle the Unicode
  error" was the response.
| Using Path("C:/path/to/xecutable") to avoid any Window-ism of any kind
  is an impossible burden. Impossible. It requires them to Google.
  Instead, the SyntxError is all my fault.
| The previous examples of the use of raw strings?  Don't know why
  they're not helpful, but I'm not the one who's struggling to implement
  a change.



-----

If you&#39;re having hard times looking for a team...
-----------------------------------------------------

PoL<noreply@blogger.com>

2019-03-26 19:21:22.087000-04:00

If you're having hard times looking for a team overseas, this article
will help you `find offshore dev
team <https://youteam.io/blog/how-to-build-an-offshore-development-team-in-ukraine/>`__.


The advice that I would give to people is to just ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2019-03-27 14:50:38.770000-04:00

The advice that I would give to people is to just always use the forward
slash "/" and let Python handle the rest.
I would then give them the following example to think about and analyze
>>> p = Path('C:/Program Files/7-Zip')
>>> p.parts
('C:\\\\', 'Program Files', '7-Zip')


&quot;\windows\is\xtreme\evil&quot; - hilarious
-----------------------------------------------

Robert Lucente<noreply@blogger.com>

2019-03-27 14:38:40.857000-04:00

"\\windows\\is\\xtreme\\evil" - hilarious


In <a href="https://gtm-plus.com/" rel="nofollow">...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2019-08-29 08:32:14.012000-04:00

In `GTMplus <https://gtm-plus.com/>`__ best architectors in Ukraine





