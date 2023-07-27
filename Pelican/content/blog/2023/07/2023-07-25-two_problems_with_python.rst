Two Problems with Python
##############################################

:date: 2023-07-25 09:00
:tags: python,community
:slug: 2023-07-25-two_problems_with_python
:category: Python
:status: published

I want to call out two huge problems with Python.
I'm not the first to point these out, but they've been bothering me for a while.

1. `Surprising Changes`_

2. `Dependency Hell`_

I've provided them here to save folks from repeating these.
They're now officially "known" and there's no point in repeating this again.
Write your blog posts about something else, please.

Surprising Changes
==================

Every language and library has changes. That's part of normal innovation and
evolution of the language.

Some changes, however, were not communicated to me, personnally, and are therefore
suprising, which makes them bad. Really bad.

Let's focus on linter tools as an example. Here's the scenario.

1. I have a code base. It's good. 100% compliant.

2. I ugprade the linter.

3. A new error is flagged. This was not an error before but **somehow** (big eyeroll) it's an error now.

This is a surprising change. No one told me.

The code *is* sketchy. It could be seen as ambiguous. **Even though it passes all the unit tests.**

Someone else may have learned a lesson about sketchy code, and embodied that lesson in the linter.
But they didn't tell me.

Python had a surprise change, and the mere presence of a surprise means one thing:

**Python is useless**.

Dependency Hell
================

Every application has dependencies. That's part of building a language
in a rich ecosystem with a lot of useful packages.

Some changes to these packages, while well-intentioned, can break a dependency with another package.
Packages have inter-dependencies, which I find **impossible** to manage.

Here's the scenario.

1. I have a code base. It's good. 100% tests pass. Installs perfectly on all supported platforms.

2. Two packages, ``p==3.14`` and ``q==2.78`` both depend on ``x`` version 1.1

3. The authors of ``p`` updated to ``4.0`` and switched their dependency to to ``x`` version 2.0. The authors of ``q`` did not switch.

4. If I include ``p==4.0`` and ``x==2.0`` the ``q`` package breaks. I can't upgrade ``p``.

Dependency Hell.  Unresolvable Conflicts.

Any combination of packages will have numerous internal dependencies.
The mere presence of these dependencies means one thing:

**Python is useless**.

Summary
========

**Python is useless**.

I cannot tolerate innovation.

If someone learns something and changes a linter, that's innovation: it breaks my code; I don't want it.

If someone creates a new version of an open-source package, that's innovation: it breaks my code; I don't want it.

This isn't to say that innovation is **bad**.

Innovation is **good**. When it occurs very slowly, and I'm able to personally vet each individual change for impact on my project(s).

The idea that every single open source package is innovating and learning at their own unique tempo
is insanity. It makes Python **useless**.
