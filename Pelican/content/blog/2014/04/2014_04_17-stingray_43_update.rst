Stingray 4.3 Update
===================

:date: 2014-04-17 08:00
:tags: stingray reader,#python,COBOL
:slug: 2014_04_17-stingray_43_update
:category: Technologies
:status: published

| See https://sourceforge.net/projects/stingrayreader/

-  Some small improvements to the COBOL DDE parsing.
-  A sensible demo program that shows how to read COBOL files.
-  A complete rewrite to Python3.3.
-  Support for more COBOL syntax.
-  Support for Occurs Depending On
-  Support for RECFM=F, RECFM=V and RECFM=VB legacy files.

| 
| The support for Occurs Depending On is a Big Sweaty Deal (BSD™). It
  breaks the essential structure for calculating offset and size of data
  items in a fixed file schema. It breaks it badly. We wind up with a
  fairly complex recursive calculation in the general case of variably
  located items.
| We'll address ODS and Numbers spreadsheets with a somewhat cleaner
  implementation, also. I figured out how ElementTree QNames work. I
  regret the ignorant misuse of namespaces in previously posted code.
  This will be part of release 4.4 or later.





