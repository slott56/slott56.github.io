OpenD6 Deep Dive -- Area Effect Aspect
#########################################################

:date: 2026-03-05 16:20
:tags: #python,math
:slug: 2026-03-05_opend6_deep_dive
:category: TTRPG
:status: published

I went deep into OpenD6, chasing an idea through a maze of strange shapes.

See this extract from a Jupyter Notebook: `Area Effect Aspect Volume Computations <{static}/pages/area-effect-aspect-volume-computations.html>`_.

It was a lot of fun to uncover two errors in the rules, and work out what *could* have been used instead.

TL;DR
=====

Here are the revised shape rules.

..  csv-table::
    :header-rows: 1

    Shape,Measures,Equivalent Sphere R
    Hemisphere,radius :math:`r`,:math:`0.79 r`
    Cone,"height :math:`h`, base radius :math:`r`",:math:`0.63 \sqrt[3]{h r^{2}}`
    Cuboid,"height :math:`h`, width :math:`w`, depth :math:`d`",:math:`0.62 \sqrt[3]{d h w}`
    Cylinder,"height :math:`h`, radius :math:`r`",:math:`0.91 \sqrt[3]{h r^{2}}`
    Pyramid,"height :math:`h`, base width :math:`w`, base length :math:`l`",:math:`0.43 \sqrt[3]{h l w}`

The difficulty is :math:`5R`.

But Wait...
===========

There are two positions we can adopt on the Area Effect aspect options shown (in detail) in the attached article.

1. It's too complicated. Find a way to simplify the difficulty computation.

2. It's a necessary evil, and there aren't too many ways around it without a massive rethinking of that aspect.

Too Complicated
===============

Yes, the math involves a cube root. My phone's calculator has the needed :math:`\sqrt[3]X` button.

The problem is multi-dimensional objects. Take the "cuboid", with a height, width and depth.

Let's say some spell's space is going to be 3.5m by 3.5m by 3.5m (an actual cube.)
This is 42.875 cubic meters. What's the difficulty supposed to be? The (unpublished) *OpenD6 Magic Guide* rules don't actually say.
Is it 43? That seems absurdly high.
If we use the measure-to-value table, we get 8. That's a bit low.

A 33 cubic meter sphere has a difficulty of 10. A 43 cubic meter should be more than 10. How mich more?
It's 30% larger; does that mean 30% more difficulty?

Not when dealing with volumes, where the growth is cubic.

It's equivalent to a 2.17m radius sphere; difficulty 11.

(If 2.17m radius seems small, the diameter will be 4.34m, just slightly larger than the 3.5m cube.)

It's A Necessary Evil
=====================

A lot of these "classic" TTRPG rules assume calculators and computers are a rarity.

It is true that lots and lots of GM's and player don't have a strong math background.

It seems like those folks may be less likely to be designing new spells with complicated Area of Effect aspects.

Conclusion
==========

I don't know which is better. I like the explicit detail of this version as a way to help spell designers.

It has little impact on play; the difficulty, skills and dice rolls impact play more than this detail.
