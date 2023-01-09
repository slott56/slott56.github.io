HamCalc and Quirks
==================

:date: 2013-06-13 08:00
:tags: HamCalc,preservation,GW-Basic,modernization,software process improvement,test-driven reverse engineering
:slug: 2013_06_13-hamcalc_and_quirks
:category: Technologies
:status: published

Careful study of the HamCalc shows a number of quirks. Some are funny,
some are just examples of the need for unit test frameworks.
The Wikispaces for the modernization project
is here: http://hamcalc.wikispaces.com/home


For example, the following line of code, in GW-Basic, will (usually) set
Y to zero.

::

    Y = O

Yes. That's the variable "O", not the number 0.

Why does this work? Why can we use "O" instead of 0?

Most programmers avoid using the variable "O", since it's hard to read.

W-Basic provides default values of 0 for almost all variables.
So,``Y=O`` works as well as ``Y=0`` most of the time. The only time is doesn't
work is if the program happens to have "O" used as a variable.

This is one of the examples where people start shouting that a compiled
language is so obviously superior that the rest of us must be
brain-damaged to use a dynamic language like Python.

This isn't a **very** compelling argument for the overhead of a
compiler. It's a more compelling argument for avoiding languages with
default values. Python, for example, would throw an exception if the
variable "O" had no value.

This isn't common (so far, I've only found one example) but it's
amusing.

Another amusing quirk is the occasional tangle of GOTO/GOSUB logic that
defies analysis. There are several examples of GOSUB/RETURN logic that
is totally circumvented by a GOTO that circumvents the return. This
should (eventually) lead to some kind of stack overflow. But GW-Basic
doesn't really handle recursion well, so it would probably just be
ignored.

One of my favorites is this.

::

    730 FOR N=A TO T STEP B
    750 IF T/N=INT(T/N)THEN X=X+1:PN(X)=N:T=T/N:GOTO 730
    760 A=3:B=2
    770 NEXT N




What does the GOTO on line 750 **mean**? Since GW-Basic doesn't use a
stack of any kind, it doesn't create recursion or stack overflow. It
appears to "restart" the loop with a new value of T. I think.





