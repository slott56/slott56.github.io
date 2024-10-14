The Enterprise COBOL Conundrum
==============================

:date: 2022-07-12 08:00
:tags: #python,COBOL,stingray reader
:slug: 2022_07_12-the_enterprise_cobol_conundrum
:category: Technologies
:status: published

Enterprise COBOL is both a liability and an asset. There's tangible
value hidden in the code.

See https://github.com/slott56/looking-at-cobol

I've tweaked the presentation a little.

The essential ingredients in coping with COBOL are these:

-  Use something like `Stingray
   Reader <https://github.com/slott56/Stingray-Reader>`__ to parse COBOL
   DDE's and process the data in the native format.
-  Analyze the Job Control Language (JCL) to work out the directed
   acyclic graph (DAG) that leads to file and database updates. These
   "master" files and databases are the data artifacts that matter most.
   This is the value-creating processing. There aren't many of these
   files.
-  Create a process to clone those files, and write Python data access
   modules to process the data. This is a two-way process. You'll be
   shipping files from your Z/OS world to another server running Python.
   In some cases, files will need to come back to Z/OS to permit legacy
   processing to continue.
-  Work backwards through the DAG to understand the COBOL apps that
   update the master files. These can be rewritten as Python apps that
   consume transactions and update master files/databases. Transfer
   transaction files out of Z/OS to a server doing the Python
   processing. Either update a shared database or send updated master
   files back to Z/OS if there's further processing that needs an
   updated master.
-  Continue working backwards through the DAG, replacing COBOL with
   Python until you've found source files for the transactions. Expect
   to find transaction validation programs as well as transaction
   analytics or reporting. The validations are useful; the analytics and
   reporting can be replaced with simpler, more modern tools.
-  When there's no more legacy processing that depends on a given master
   file or database, then the Z/OS can be formally decommissioned. Have
   a party.

This is relatively low risk work. It's high value. The COBOL code
encodes enterprise knowledge. Preserving this knowledge in a more modern
language is a value-maintaining exercise. Indeed, the improved clarity
may be a value-creating exercise.





