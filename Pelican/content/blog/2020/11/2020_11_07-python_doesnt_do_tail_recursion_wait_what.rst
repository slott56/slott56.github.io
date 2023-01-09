"Python doesn’t do tail recursion" -- wait, what?
=================================================

:date: 2020-11-07 15:36
:tags: #python,functional python programming
:slug: 2020_11_07-python_doesnt_do_tail_recursion_wait_what
:category: Technologies
:status: published

Yes, that's what the email said.

I was -- well -- shocked. Too shocked to be polite. Content Warning:
much snark follows.

BLUF: Tail Recursion is not Tail Recursion Optimization.
--------------------------------------------------------

Eventually, it became clear they were worried about tail recursion
**optimization**. Maybe I'm too focused on words, but I think words
matter. The initial claim was so clearly wrong, I had to challenge it.
It took three \*more\* emails to get to the optimization point.

Hence my overload of snark. Three emails to discover they didn't see the
word "optimization."

Tail Recursion
--------------

Here's an example. (I wish questions included example code instead of
weird assertions that are clearly false.)

::

   def f(x: int) -> int:
       if x == 0: return 1
       return x*f(x-1)

This function demonstrates tail recursion. The "tail" of the function
involves a recursive reference to the function. An optimizing compiler
can optimize the recursion to make it not recursive.

If Python doesn't do tail recursion, this function would not work.

Since it works, Python does tail recursion.

Python limits recursion so that you crash cleanly before you're out of
memory.

This is important. Older languages would run out of memory for stack
frames. Instead of reporting a recursion problem, they'd just crash.
Out-of-memory. Sorry. No drop to \`pdb`. Nothing. This is bad.

In the old Mac OS (≤9) the stack and heap memory grew from opposite ends
of the available RAM. If they collided, it was a stack overflow, and the
running app was crashed.

Here's how the stack limitation plays out in practice:

::

   Python 3.9.0 | packaged by conda-forge | (default, Oct 10 2020, 20:36:05) 
   [Clang 10.0.1 ] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>> def f(x: int) -> int:
   ...     if x == 0: return 1
   ...     return x*f(x-1)
   ... 
   >>> f(999)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 3, in f
     File "<stdin>", line 3, in f
     File "<stdin>", line 3, in f
     [Previous line repeated 995 more times]
     File "<stdin>", line 2, in f
   RecursionError: maximum recursion depth exceeded in comparison
   >>> f(997)
   403597244616453902342926527652907402110903352461393891430307973735196631901068423726375883385358710213700663198466197719394411318126551961682447808198924968051643330792790545975658652366984953410102994729193397927862707860663312211428139657339199210288839829245965893084586772188847949801354437616450752245066665598898009417557796737695167521343249479413631414534202184726421479392615730781173164526393982880263279118925406206180689438683308644696334133955184235540077242451165903811018277198321800315958279899941381566151490917379981054549852483223292752438981198080270888254399197574536460570473430371595872403169486757166154294941258045311241382930836862005052391967478429035362983199050663230586866257612402804942403442331663944341683350732204123565349869446216232111598995678724462182568501131746383857706790400107507266739002631612931124112227909672935742104968533278074796000335855930432060517447195226436187301231195091058916141500005034486568847599649004940677693185232218378659444854645703908824934015144550035704605317977378620311855095356769488892217130200011250491151641531090120083765159221969755314437880209281708574493693840125338722070514029362985801732618715060934298236579096167095859504053310608725711198457200226544350445941157734863407428532431126485686678788466148681975019174010453297639004006819520704463840773528691224455265229985489764356909675383800245969276679872407757924211918488179598530382266647547907226165479802976547896939656888813256826539067915695278878516257396920983511389029563101112325372395464739783143361362879872578550147571168136083391354242735142803988735616917749898060073075542403509536490539404444972668319521415425667918323473675966566332390993259591959049424070380861864682206986463729281557338747466546627859206287571996491606797979064142819469589200812679026561288124087136359830959867034513441434850212864818601504529520195828528045600869420646442863720485414968365312690523835026508545772659712105161137693595262919371358840019473383802028344531181679417716563013501242477291139042422814166369601152223293596957527530934652046662174154235850073391729650007182794396630407081318880947107940245036774649857429379220776637356890211596540009349092255988047909417594778375705723841918167663026277009033939654785671715045122185315730249393616044737902170116980736000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
   >>> 

This shows how a large number of operations (around 1,000) exceeds an
internal limit. The exception is not out-of-memory, it's too much
recursion.

A slightly smaller number (997 in this example) worked.  999 didn't work
because it exceeded the threshold.

Manual Tail Recursion Optimization
----------------------------------

New word: Optimization. New concept.

If the tail recursion were optimized into a loop, we'd see code that
behaves as if we wrote this:

::

   >>> from math import prod
   >>> def f1(x: int) -> int:
   ...     return prod(range(1, x+1))
       

This unwinds the tail recursion into a loop. A generator,
``range(1, x+1)``, creates a sequence of values, which are reduced into
a product. This doesn't involve recursion or stack frames. Indeed,
because it's a generator, it involves very little memory.

And it works for  numbers well over 1,000. Evidence (if any were needed)
that tail recursion optimization is \*not\* being done in Python.

We'll repeat this for those who feel the need to send me crazy-sounding
emails.

Automatic Tail Recursion Optimization
-------------------------------------

There is no automatic transformation from tail recursion to loop in
Python.

I'll repeat that for the folks who send me emails claiming tail
recursion isn't supported. (Everyone else probably has a pretty good
grip on this.)

There is no **automatic** transformation from tail recursion to loop.

Tail recursion works. It has a limit.

Manually optimized tail recursion (to create a loop) also works. It
doesn't have the same limit.

Stated yet another way: unlike some languages, Python does **not**
optimize for you. You must do the rewrite yourself.

While I would have thought these ideas (tail recursion and tail
recursion **optimization**) were different. I was wrong. Hopefully, this
blog post will help folks read \*all\* the words.

I'm also pretty sure it's covered in
here: https://www.packtpub.com/product/functional-python-programming-second-edition/9781788627061.





