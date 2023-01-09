Code Kata : Merge Changes
=========================

:date: 2009-09-23 20:36
:tags: code-kata
:slug: 2009_09_23-code_kata_merge_changes
:category: Technologies
:status: published

**The Situation**

A co-worker has mistakenly cloned a directory tree rather than link
to it. Then they made some number of changes to files in that
directory.

**Your Job**

Your job is to compute a directory-level difference between an
official copy and the changes they made. Sadly, you can't trivially
rely on using Subversion for this. You're going to have to write your
own differ.

The difference report should show the following kinds of information.

1. Baseline files unchanged in the clone.

2. Cloned files which are new and don't exist in the baseline.

3. Cloned files which are changed and newer than the baseline.

You'll need to skip certain directories. They're either working files
or are ignored for other reason.

You'll need to skip certain file extensions. Things like ``.pyc`` or
``.class`` files have date-stamps that don't indicate a real difference.

Ultimately, you'll produce two things.

1.  A report to show what was changed.

2.  A script that will copy the changes from the clone back into the
    master directory.

**Some Notes**

Python has several modules that help with doing directory and file
comparison.

In non-Python environments, you may have to rely on system utilities
like **diff** or **cmp**.

This is best built incrementally, creating the report first. Then
handle exceptions. Then do the copy.





