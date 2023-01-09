Code Kata : Analyze A Hard Drive
================================

:date: 2009-10-05 07:01
:tags: code-kata
:slug: 2009_10_05-code_kata_analyze_a_hard_drive
:category: Technologies
:status: published

This isn't computer forensics; it's something much simpler.

A colleague has been struck down with a disease (or won the lottery)
and won't be back to work any time soon. Worse, they did not use SVN
to do daily check-ins. Their laptop has the latest and greatest. As
well as all experiments, spike solutions, and failed dead-ends.

You have their hard drive mounted in an enclosure and available as
/Volumes/Fredslaptop or F: if you're a windows programmer.

There are, of course, thousands of directories. Not all of which are
terribly useful.

Step 1 - find the source. Write a small utility to locate all
directories which contain "source". Pick a language you commonly work
in. For C programmers, you might be looking for .c, .cpp, .h, and
.hpp files. For Python programmers, you're looking for .py files. For
Java programmers, you're looking for .java, and .class files.

Step 2 - get information. For each directory that appears to have
source, we want to know the number of source files, the total number
of lines in all those source files, and the most recent modification
time for those files. This is a combination of the output from wc and
ls -t.

Step 3 - produce a useful report. To keep your team informed, create
a .CSV file, which can be loaded into a spreadsheet that summarizes
your findings.





