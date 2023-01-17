Code Kata : "Simple" Database Design
====================================

:date: 2011-05-26 08:00
:tags: design,code-kata
:slug: 2011_05_26-code_kata_simple_database_design
:category: Technologies
:status: published

Here's a pretty simple set of use cases for a code-kata database
application.

This is largely transactional, not analytical.

It's a simple inventory of ingredients, recipes and locations.

Context
-------

-  42' sailboat.
-  Lots of places to keep stuff. Lots.

Stuff gets lots or misplaced. It's helpful to marry recipes with
ingredients to use up the last of something before it goes bad and
stinks up the boat.

Actor is essentially the cook.

Use Cases
---------

-  Perishables to be eaten soon?
-  Shopping list for specific recipes.
-  Where did I put that?

Model
-----

|image1|

-   Ingredient. A generic description: "lime", "coconut". Not too
    much more is needed. A "food safety" notation (refrigeration
    required, etc.) is a helpful attribute. Maybe a "food group" or
    other nutrition information.

-   Location. A text description of where things can be stored.
    This shouldn't have too many attributes, because boats aren't
    big grids. Phrases like "port saloon upper cabinet", or "galley
    outer cooler" make sense to folks who live on the boat.

-   On Hand. This is simply ingredient, location and a measurement
    of some kind. Example: 3 limes in the starboard galley center
    cooler. There's a lot of magic around units and unit conversion
    that can be fun. But that strays outside the database domain.

-   Recipe. Example: "One of sour, two of sweet, three of strong,
    and four of weak.", lime, simple syrup, rum, water. Plain text
    using a lightweight markup is what's required here. Along with
    a many-to-many relationship with ingredients. This is not
    carefully defined above because it should be done as a "more
    advanced" exercise.

I think this has the right amount of complexity and isn't very
abstract. Since the use cases are pretty obvious to anyone who's
cooked or been to a grocery store, use case details aren't
essential.

.. |image1| image:: http://yuml.me/diagram/scruffy/class/%5BIngredient%5Dm-n%5BRecipe%5D,%20%5BIngredient%5D1-n%5BOn-Hand%5D,%20%5BOn-Hand%5Dn-1%5BLocation%5D.
    :target: http://yuml.me/diagram/scruffy/class/%5BIngredient%5Dm-n%5BRecipe%5D,%20%5BIngredient%5D1-n%5BOn-Hand%5D,%20%5BOn-Hand%5Dn-1%5BLocation%5D.



-----

What did you use to draw your schema? Looks cool.
-------------------------------------------------

Fred Janon<noreply@blogger.com>

2011-05-29 01:01:28.601000-04:00

What did you use to draw your schema? Looks cool.



mlee3680<noreply@blogger.com>

2020-11-07 15:35:35.681000-05:00

This comment has been removed by a blog administrator.


I wanted to thank you for this excellent read!! I ...
-----------------------------------------------------

liperk<noreply@blogger.com>

2021-11-15 08:11:01.943000-05:00

I wanted to thank you for this excellent read!! I definitely loved every
little bit of it. I have you bookmarked your site to check out the new
stuff you post. `Meridian Norstar <https://www.meridiannorstar.net/>`__





