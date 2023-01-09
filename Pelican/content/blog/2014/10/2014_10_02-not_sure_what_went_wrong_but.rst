Not sure what went wrong, but...
================================

:date: 2014-10-02 08:00
:tags: #python,numpy,vispy
:slug: 2014_10_02-not_sure_what_went_wrong_but
:category: Technologies
:status: published

Read
this: http://quantlabs.net/blog/2014/09/here-is-why-i-gave-up-on-python-aka-dogs-breakfeast-of-a-so-called-programming-language/#sthash.Rp7pXObf.dpuf
Not sure what's going on here.
"Script I want to run" seemed
clear. http://vispy.org/examples/basics/scene/surface_plot.html#sthash.kIzbd33O.dpuf
The rest seemed like ill-advised trips down numerous ratholes. In
particular, anything that involved Python Tools for Visual Studio seems
like a waste of time and brain calories.
It's not clear at all what's not working. That's perhaps the most
frustrating thing about this kind of post.
The final note, "Decisions decisions..." pointed out a simple confusion
that befuddles the technically-minded. Too many details.
The decision between Python2 and 3 is trivial. There are a lot of
details, but they're irrelevant for making the decision.
What package are you trying to use? It's hard to tell, but it looks like
it's vispy. If so, that's all that matters. vispy works with Python3.3,
requires numpy, and a "backend." Install just that and nothing more. In
particular, avoid junk like Visual Studio.
The Dog's Breakfast seems to be the result of chasing down lots of
details that aren't too relevant. It's hard to tell. But a scatter-shot
post claiming "all this is broken" is a hint that the author wasn't
simply following the vispy installation instructions. It could be that
they turned something simple into a dog's breakfast by chasing
irrelevant technologies all around the garden.





