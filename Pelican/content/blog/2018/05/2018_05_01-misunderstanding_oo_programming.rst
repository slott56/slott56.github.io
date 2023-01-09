Misunderstanding OO Programming
===============================

:date: 2018-05-01 08:00
:tags: OO design,#python,OO language
:slug: 2018_05_01-misunderstanding_oo_programming
:category: Technologies
:status: published

| Read this. `Goodbye, Object Oriented
  Programming <https://medium.com/@cscalfani/goodbye-object-oriented-programming-a59cda4c0e53?source=linkShare-879bf4230309-1524537370>`__
| I like this because parts of it are wrong, and parts are based on
  peculiarities of specific languages which aren’t problems in other
  languages.
| The “wrong” things are on a spectrum. At one end are things almost
  right. The other end is hoped-for things which — frankly — were never
  true.
| The most important piece of nonsense is class-level reuse across
  projects. Class-level reuse in a new project was not a thing in OO
  programming. The monkey-banana-jungle “problem” only exists in a
  strange world were someone made up the idea of single classes being
  reused in isolation. The rest of us knew the scope of reuse was within
  a project or a narrow family of projects aimed at a single problem
  domain.
| "Utility" classes that could be reused and generic data structures
  were always available as frameworks and libraries. Things built to
  solve a specific problem were going to be tailored to the problem.
  Most OO designers knew this and knew that making something generic
  would be hard. Making something reusable and installable by others was
  even harder. (Especially in compiled languages where you wanted to
  hide intellectual property by keeping the source secret.)
| The "OO promised me reuse and lied" is a misstatement. Please rephrase
  this is "I imagined there could be class-level reuse and discovered it
  was hard."
| Multiple inheritance does work in a number of languages, so I’ll skip
  the complaints centered on single inheritance.
| I don't fully understand the complained about encapsulation. There are
  lots of books on separating interface from implementation to more
  fully isolate implementation details. If references need to be treated
  more opaquely, there are lots of techniques for this. It’s not broken.
  Indeed, it’s really well understood. ("But I won't want to introduce
  wrapper classes to insulate the references." Sigh. That's how it's
  done.)
| I think the "references leak details about encapsulation" requires
  rephrasing as "I imagined some kind of perfectly isolated programming
  where references were not usable in spite of me making them usable."
  Or perhaps "I wish references had special treatment to make them not
  work as references except in a limited context which I get to
  imagine."
| The polymorphism complaint appears to be “okay, this actually works.”
   I guess. Or. “There are other ways to do this in other languages.”
  I'm sure it's an important point, but I can't quite discern what OO
  principle is allegedly broken here.

tl;dr
-----

| No one was lied to. If someone was "burned" by some OO hype, I’d like
  to see the actual quote of the actual hype. The “I was told there
  would be X”, requires some substantiation.
| And. Stop griping about encapsulation. When the source is available
  (as it is in many languages) there's no enforcement other than public
  shaming.
| Also. Use Python. Most of the original post seems to be complaints
  about C++ weirdness.





