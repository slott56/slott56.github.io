couchdb on Mac OS X
===================

:date: 2012-03-06 08:00
:tags: xcode,mac os x,SQL,noSQL
:slug: 2012_03_06-couchdb_on_mac_os_x
:category: Technologies
:status: published


I've started to work with `couchdb <http://couchdb.apache.org/>`__.

I've blogged before about the problems of SQL schema in `Escaping the
Relational Schema
Trap <{filename}/blog/2011/02/2011_02_02-escaping_the_relational_schema_trap.rst>`__.

A SQL schema -- for many applications -- is too confining.  It creates
cost with relatively little value.  Once upon a time (when disks where
expensive and computers were slow) it was essential.

The funny part about using couchdb is the build process.

In the couchdb Wiki, they have a page for `Mac OS X
installation <http://wiki.apache.org/couchdb/Installing_on_OSX>`__.
The relevant part is the following line of shell script.

brew install couchdb

That's it?

Yes.  If--and only if--you follow the directions.

If you don't follow the directions, however, it can take all day.
   Here are the steps.

#.  Install Apple's Developer Tools.  I have Mac OS X 10.7.  `XCode 4.3 for Lion <https://developer.apple.com/xcode/>`__.

#.  Launch XTools and install the command-line utilities.  This is important because it includes things like **make**.

#.  Remove **fink** or **MacPorts** if you happened to have used them for
    anything.  For fink, you'll need to clean it out of your ~/.profile
    or ~/.bash_profile and rename the /sw directory.

#.  Install `Homebrew <https://github.com/mxcl/homebrew>`__.   Use the
    one-line ruby script from the
    `Installation <https://github.com/mxcl/homebrew/wiki/installation>`__
    page of the Homebrew wiki.  This: /usr/bin/ruby -e "$(curl -fsSL
    https://raw.github.com/gist/323731)" I tried several wrong ways
    before doing it the right way.

#.  Install **couchdb** using homebrew.  It takes a while.

There are numerous things which may go wrong.

A missing lib/crt.1.10.6.o, for example. This is just an out-of-date
Xcode. It took few hours of failed experiments to (a) realize it and
(b) get the right one.  There are several proposed solutions around
the web.  Most of them are clever, but ineffective.  Just get the
right Xcode.

A failure to build Erlang. This was just an improperly installed
version of Homebrew.  There were a lot of message.  A lot.  I messed
around with a lot of things until I finally crashed brew doctor. I
deleted and reinstalled Homebrew and everything built.  First try.





