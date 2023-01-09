Overcoming Incuriosity -- Sailing Over The Horizon
==================================================

:date: 2020-06-02 08:00
:tags: #python,architecture
:slug: 2020_06_02-overcoming_incuriosity_sailing_over_the_horizon
:category: Technologies
:status: published

I'm in regular contact with a few folks who seem remarkably incurious.
Seem.
Perhaps they're curious about something other than software. I don't
know.
But I do know they're remarkably incurious about software. And are
trying to write Python applications.
I know some people don't sail out of sight of their home port. I've
sailed over a few horizons. It's not courage. It's curiosity. And
patience. And preparation.
I find this frustrating. I refuse to write their code for them.
But any advice I give them devolves to "Do you have an example?" With
the implicit "Which I can copy and paste?"
Even the few who claim they don't want examples, suffer from a
paralyzing level of incuriosity. They can't seem to make search work
because they never read beyond the first few results on their first
attempt. A lot of people seem to be able to make search work; and the
incurious folks seem uniquely paralyzed by search.
And it's an attribute I don't understand.
Specific example.
They read through the multiprocessing module until they got to examples
with apply_async() and appear to have stopped reading.  They've asked
for code reviews on two separate module. Both based on apply_async().
One module was so hopelessly broken it was difficult to make the case
that it could never be made to work. There's a way the results of
apply_async() have to be consumed, and the code not only did not reflect
this, it seemed like they had decided specifically never to consider an
alternative. (Spoiler alert, it requires an explicit wait().)
The results were sometimes consumed -- by luck -- and the rest of the
time, the app was quirky. It wasn't quirky. It was deplorably wrong. And
"reread the apply_async()" advice fell on deaf ears. They couldn't have
failed to read the page in the standard library documentation, no, it
had to be Python or Windows or me or something.
The other module was a trivial map() application. But. Since
apply_async() has an incumbency, there was an amazingly elaborate
implementation that amounted to rebuilding ``apply()`` or ``map()`` with
globals and callbacks. This was wrapped by queue processing of Byzantine
complexity. The whole mess appeared to stem from an unwillingness to
read the documentation past the first example.
What to do?
My current suggestion is to exhaustively enumerate each of the methods
for putting work into the processing pool. Write an example of each and
every one.
In effect: "Learn the methods by building throw-away code."
I anticipate a series of objections. "Why write throw-away code?" and
this one: "That's not realistic, what do you do?"
What do I do?
I write throw-away code.
But that's no substitute for a lack of curiosity.



-----

Hi

Have you tried TDD with them. Maybe they want ...
-----------------------------------------------------

McSee<noreply@blogger.com>

2020-06-03 23:02:18.227000-04:00

Hi
Have you tried TDD with them. Maybe they want to start with a functional
approach instead of an implementative one.
With good guidance this might lead to a simpler implementation





