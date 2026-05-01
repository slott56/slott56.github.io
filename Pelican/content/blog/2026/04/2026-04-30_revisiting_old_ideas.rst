Revisiting Old Ideas
################################################

:date: 2026-04-30 17:37
:tags: OpenD6,#python
:slug: 2026-04-30_revisting_old_ideas
:category: TTRPG
:status: published

See `Writing Project -- perhaps a bad idea <{filename}/blog/2026/04/2026-04-23_writing_project.rst>`_.
I'm trying to dig around in my old notes to pull together a "World Book" with a fantasy setting I think has a lot of good gaming opportunities. More important, I've got a pile of details for a fairly lengthy campaign.

This isn't easy.

As I've noted earlier, a lot of my notes were written in the late 90's using ClarisWorks.
I carefully saved the files, but -- of course -- the software to read those files no longer exists in a handy, useful form.
I've found that `LibreOffice <https://www.libreoffice.org>`_ reads ClarisWorks files.

Generally.

But not universally.

In a few cases, sadly, I have files with some feature that confuses LibreOffice.
The result wasn't wonderfully meaningful content. Nothing I could rewrite into my TTRPG Campaign Book.

What started as a kind of lark has turned into real work.

ClarisWorks Struggles
=====================

The underlying library that LibreOffice uses to read ClarisWorks is **libmwaw**. See https://sourceforge.net/p/libmwaw/wiki/Home/.
(I imagine it starts as MacWorks/AppleWorks, and grew from there to encompass many other formats.)

The **libmwaw** approach isn't easy to understand for three reasons.
First, it handles a vast number of file formats, leading to a source directory with 382 files.
Second, it has to support a narrow interface that converts a source document into a LibreOffice data structure.
Finally, it's focused on the old, pre-XML, pre-Protobuf file formats, where everything's just a pile of bytes.

My scope is narrow:

- I'm only interested in the ClarisWorks features, which is a tiny subset what **libmwaw** can decode.

- Further, I'm looking at identifying what -- precisely -- is making **libmwaw**  choke on a few specific files.

- And. Bonus. I'd rather not relearn techniques for debugging C++ code.

(I was told to try using Anthropic's Claude for this kind of problem.
Really. For understanding 300,000 lines of C++.
To locate a place where the code isn't properly parsing the graphics primitives.
Ahem. I may be chasing after my childhood TTRPG toys, but let's be realistic about LLM's.)

What I did was rewrite parts of the **libmwaw** into Python, using the ``struct`` module to try and extract meaningful bits of the file.
The resulting code is very, very ugly.
(I won't share it. It's that bad.)
It's a lot of ``struct.unpack()`` and ``print()`` function calls.

Ideally, it would be something like this.

::

    thing = SomeClass(
        *struct.unpack(
            SomeClass.format,
            buffer[start:start+SomeClass.size]
        )
    )
    start += SomeClass.size

This has some encapsulation problems, but it's easier to debug.

In the long run, a really tidy form like this is ideal.

::

    thing = SomeClass.parse_bytes(buffer, start)
    start += SomeClass.size

Pragmatically, I never quite bashed the design into this pattern.
I was exploring the bytes, not creating a final library.
Each step forward was a lot of experimental code that failed in very obscure ways.

After all, bytes are bytes.
You can overlook some C++ obscurity that skips 4 bytes of the file.
You have no way to know until some seemingly unrelated data structure has unholy attribute values.
And it's hard to be **sure** they're unholy.

During my exploration, I found a sequence of graphic primitives (I think they were supposed to be polygons) that could not be parsed.
The format of the bytes had some unexpected feature; the **libmwaw** C++ code simply skipped the whole structure, moving on to something that could be parsed.
I poked around for a while, unsuccessfully, trying to understand the bytes.
And failed.

What I **did** find were the base rectangles that contained the various graphic items.
In many cases, the objects were simple lines and rectangles and regions with text.
There were a few arcs.
Some of the polygons could be recovered, until the "oopsie" point, where the file was uninterpretable.

This sequence of rectangles was -- actually -- good enough for my purpose.

What Did I Mean By That?
========================

I was trying to recover some maps from my old ClarisWorks files.
I had the text descriptions that explained the maps, but, those notes about traps, secret doors, and hidden altars made precious little sense.
They were terse bits of text to back up a diagram that LibreOffice couldn't parse.
Without the diagram, the text wasn't helpful.

With my Python hacking around, the recovered images looked like this:

..  figure:: {static}/media/Xorn%20Cave%201.png
    :alt: Sketch extracted from Clarisworks as a collection of colored rectangles.
    :height: 8cm

The picture is hideous, but, the clumps of rectangles and the room numbers helped me
understand the text notes that went with the map.

(Note the axes have two sets of numbers: integers from 0 to 160,000, and float from 1.0 down to 0.0.
The C++ converts everything to float.
This doesn't seem necessary when tools like **matplotlib** will gracefully work with any units,
so some of the object coordinates are unconverted, and a few are converted.
The picture was useful enough without resolving this inconsistency.)

My text notes were terse. Just hints for myself, really.
This campaign was for a standing TTRPG group that I hung around with for years and years.
We played frequently (often weekly) from maybe 1990-ish to about 1995.

Because of this, I could get away with a very sketchy design.
After all, I knew the players.
The players knew the world the campaign existed in.
The details were a mythos that was evolving as part of our shared story-telling.

(Also. No campaign design survives contact with players.
I didn't dwell on details that would clearly evaporate on day one when Dave would have his character really push the envelope on the world, the other players, and me.)

Now, thirty years down the road, I'm trying to reconstruct that group's collective understanding and collaborative discovery of this campaign.
I can now see my intent.
And 2026 me can see some weak design 1996 me had included.

Status
======

Uncovering the lost maps took many weeks. (Maybe as much as two months. It was very hard work.)

Redrawing the maps in `Worldographer <https://worldographer.com>`_ took another few weeks.

Now, I can address the sketchy notes.

This is the fun part: capturing enough detail that a GM can spin a good yarn from my campaign notes.
