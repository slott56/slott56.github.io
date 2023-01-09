The Swift Programming Language
==============================

:date: 2014-06-19 08:00
:tags: iOS,swift,#python
:slug: 2014_06_19-the_swift_programming_language
:category: Technologies
:status: published

https://developer.apple.com/swift/
This lowers the bar for entry to the iOS market.
Does it also lower the bar for Mac OS X?
Can it be used to write command-line command-line applications
("scripts")? It has a REPL, which means it can do a kind of
"just-in-time" compile and run. This is how Python works, so perhaps
this is a viable mode for using Swift.
Via the Objective-C and C compatibility, it has full access to the POSIX
libraries, as well as Cocoa, so it can clearly be used to build
command-line apps. It might lack the flexibility of Python, since it's
compiled. But C (C++, Objective-C) with automated memory management is
still a gigantic victory for writing fast and reliable programs.
Can it be plugged into Apache to write backend applications? It's
compiled, and compatible with C and Objective-C. So, one can imagine
that a mod-swift component in Apache might be possible. It might be
better to work through existing FCGI interfaces and write stand-alone
Swift back-ends. This would require a bunch of libraries for database
API's, template rendering, request and response processing, and the
various bits and pieces that make up a rich web development environment.
But this is largely available for C and C++, making it available to
Swift-based backends.
Is one language even a desirable goal?
The idea of having one official version of the class definitions seems
very helpful for capturing knowledge and managing the intellectual
property that is embodied in application logic.





