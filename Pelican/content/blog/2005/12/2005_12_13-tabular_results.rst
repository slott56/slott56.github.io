Tabular Results
===============

:date: 2005-12-13 11:43
:tags: architecture,software design,data structure,algorithm,database design
:slug: 2005_12_13-tabular_results
:category: Architecture & Design
:status: published





The "correct" answer is to fully normalize the
design and get away from a mixed bag of columns and nulls.  The MESS is bad from
every perspective, except query performance.  A semi-normalized design that
separates the STATE CHANGES from the ESSENTIAL DEFINITION is an optimal design
in many respects.



Here are the tabular
results that show the cost of fragmentation in size and
time.



..  csv-table::

    " ","fragmented size","fragmented time"
    " ","min","max","min","max"
    "Denorm","1.58","2.67","1.11","1.13"
    "Semi-Norm","1.63","2.13","1.49","1.56"
    "Norm","1.73","2.23","1.46","2.04"


    


    













