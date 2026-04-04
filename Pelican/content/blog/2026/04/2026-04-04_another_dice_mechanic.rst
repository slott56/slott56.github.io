Another D6 Dice Mechanic -- Equiprobable Choices
################################################

:date: 2026-04-04 15:37
:tags: DSL,OpenD6,#python,dice,mechanic
:slug: 2026-04-04_another_d6_mechanic
:category: TTRPG
:status: published


When playing a game using D6 -- and only D6 -- we're sometimes confronted with a need to
make a selection from equiprobable items.

For example, pick a random day of the week: 7 choices, but only 6 sides to a die.

What can we do?

How can we select fairly among 7 choices using only a handful of 6-sided dice?

See this extract from a Jupyter Notebook:
`Dice Mechanics: Equal Probability Outcomes from D6 <{filename}/pages/equiprob_d6.rst>`_.

For direct computation of the exact distribution of a handfull of dice, we need a lesson in multinomials.

See https://towardsdatascience.com/modelling-the-probability-distributions-of-dice-b6ecf87b24ea/.
From this we learn the following (amongst other things).
For :math:`n` dice of :math:`s` sides (6 in our case), the probability of getting the target value :math:`T` is this:

..  math::

    P(n, s, T) = \Bigl(\sum\limits_{k=0}^{\lfloor \frac{T-n}{s} \rfloor}\bigl(-1\bigr)^k \frac{n!}{(n-k)!k!} \frac{(T-sk-1)!}{(T-sk-n)!(n-1)!}\Bigr)\Bigl(\frac{1}{s}\Bigr)^n

Which has a lot of maths, but is very helpful.

TL;DR
=====


..  csv-table:: Mechanic Alternatives
    :widths: 1, 10
    :header-rows: 1

    Outcomes,D6 Mechanic
    "2","1D [1-3, 4-6]"
    "3","1D [1-2, 3-4, 5-6]"
    "4","1D with reroll {5, 6}
    or 2D with weights of 2, 1"
    "5","1D with reroll {6}
    or 4D [4-10, 11-12, 13-14, 15-16, 17-24]"
    "6","1D *Do we even need to include this?*"
    "7","Use 8 outcomes with a reroll {7}
    or 5D [5-12, 13-14, 15-16, 17, 18-19, 20-21, 22-30]"
    "8","4D [4-9, 10-11, 12, 13, 14, 15, 16-17, 18-24]
    or 3D with weights of 4, 2, 1"
    "9","5D [5-12, 13-14, 15, 16, 17, 18, 19, 20-21, 22-30]
    or 2D with weights of 3, 1"
    "10","3D [3-6, 7, 8, 9, 10, 11, 12, 13, 14, 15-18]
    or 5 outcomes combined with 2 outcomes"
    "11","Use 12 outcomes with reroll {11}
    or 5D [5-11, 12-13, 14, 15, 16, 17, 18, 19, 20, 21-22, 23-30]"
    "12","Use 6 outcomes, combined with 2 outcomes"
    "above 12","Decompose into 2 or more tables; use a chain of rolls"

