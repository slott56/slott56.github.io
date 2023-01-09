Functional Python, Literate Programming & Trello Board Analysis
===============================================================

:date: 2017-05-02 08:00
:tags: #python,literate programming,functional python programming
:slug: 2017_05_02-functional_python_literate_programming_trello_board_analysis
:category: Technologies
:status: published

| The general advice to people using Kanban/Agile Project boards of
  various kinds is this:
| **Stop Starting -- Start Finishing**

-  http://www.agilebuddha.com/agile/agile-thinking-stop-starting-start-finishing/
-  http://www.allaboutagile.com/stop-starting-start-finishing-unfinished-work-is-debt/
-  http://www.leanagiletraining.com/key-problems/stop-starting-start-finishing/

| 
| *etc*.
| There's a lot of this advice. Some of it is helpful.
| Many tools have various dashboards and metrics computations.
| However.
| The basic velocity calculations -- starts v. finishes -- is pretty
  straight-forward. The rules to classify a Trello action as "start" or
  "finish" are actually nice examples of simple functions or lambdas.
  Which also means that the basic pipeline required to gather the data
  can be written as a lazy, functional process.
| Which leads to writing a Literate Programming version of a small
  program that gathers data from a Trello board.
| https://github.com/slott56/Trello-Action-Counts
| It's a kind of deep-dive into some aspects of Python functional-style
  programming. It's also a dive into Literate Programming via a longish
  example. And it has a fair number of type hints. It's not perfectly
  clean from MyPy-'s analysis. So there's some more to do on that front.





