Some Notes on Python
###########################

:date: 2026-01-08 10:44
:tags: python,math,object-oriented
:slug: 2026-01-08_some_notes_on_python
:category: Python
:status: draft

TL;DR
=====

Math and Programming overlap in strange ways.

Booleans
==========================

Boolean values are a small domain of :math:`\{\mathtt{True}, \mathtt{False}\}` and a few operators.
The usual operator culprits are ``and``, ``or``, and ``not``. We'll use the math symbols :math:`\wedge`, :math:`\vee`, and :math:`\neg` for these.
Other languages have added other operators, ``imp``, and ``xor`` are popular.

To compress the following chart, we'll abbreviate the boolean domain as three values. :math:`\{\mathtt{T}, \mathtt{F}\}`.

There are 16 possible logic operators. Let's designate these operators with :math:`p \circledast_n q`.
For each operator, the two operands come from :math:`p = [ \mathtt{F}, \mathtt{F}, \mathtt{T}, \mathtt{T} ]`, and :math:`q = [ \mathtt{F}, \mathtt{T}, \mathtt{F}, \mathtt{T} ]`.
This gives us four argument pairs, and therefore, there will be four possible results.

.. p = F F T T  q = F T F T

..  csv-table::
    :header: "operator", "logic", "notes", "Python"

    ":math:`p \circledast_{0} q = [\mathtt{F}, \mathtt{F}, \mathtt{F}, \mathtt{F}]`",:math:`\text{False}`,Kind of limited.,:code:`False`
    ":math:`p \circledast_{1} q = [\mathtt{F}, \mathtt{F}, \mathtt{F}, \mathtt{T}]`",:math:`p \wedge q`,The ``and`` operator.,:code:`p and q`
    ":math:`p \circledast_{2} q = [\mathtt{F}, \mathtt{F}, \mathtt{T}, \mathtt{F}]`",":math:`p \not\Rightarrow q`, or :math:`p \wedge \neg q`",,:code:`not (q or not p)`
    ":math:`p \circledast_{3} q = [\mathtt{F}, \mathtt{F}, \mathtt{T}, \mathtt{T}]`",:math:`p`,The value of :math:`q` is ignored.,:code:`p`
    ":math:`p \circledast_{4} q = [\mathtt{F}, \mathtt{T}, \mathtt{F}, \mathtt{F}]`",":math:`q \not\Rightarrow p`, or :math:`q \wedge \neg p`",,:code:`not (p or not q)`
    ":math:`p \circledast_{5} q = [\mathtt{F}, \mathtt{T}, \mathtt{F}, \mathtt{T}]`",:math:`q`,The value of :math:`p` is ignored.,:code:`q`
    ":math:`p \circledast_{6} q = [\mathtt{F}, \mathtt{T}, \mathtt{T}, \mathtt{F}]`",":math:`p \veebar q`, or :math:`\left(p \vee q\right) \wedge \left(\neg p \vee \neg q\right)`",The exclusive or operator.,:code:`(p or q) and (not p or not q)`
    ":math:`p \circledast_{7} q = [\mathtt{F}, \mathtt{T}, \mathtt{T}, \mathtt{T}]`",:math:`p \vee q`,The ``or`` operator.,:code:`p or q`
    ":math:`p \circledast_{8} q = [\mathtt{T}, \mathtt{F}, \mathtt{F}, \mathtt{F}]`",":math:`\neg \left(p \vee q\right)`, or :math:`\neg p \wedge \neg q`","The ""nor"" operator.",:code:`not (p or q)`
    ":math:`p \circledast_{9} q = [\mathtt{T}, \mathtt{F}, \mathtt{F}, \mathtt{T}]`",":math:`p \Leftrightarrow q`, or :math:`\left(p \vee \neg q\right) \wedge \left(q \vee \neg p\right)`","The ""biconditional"" or ""equivalent"" operator.",:code:`(p or not q) and (q or not p)`
    ":math:`p \circledast_{10} q = [\mathtt{T}, \mathtt{F}, \mathtt{T}, \mathtt{F}]`",:math:`\neg q`,The value of :math:`p` is ignored.,:code:`not q`
    ":math:`p \circledast_{11} q = [\mathtt{T}, \mathtt{F}, \mathtt{T}, \mathtt{T}]`",":math:`q \Rightarrow p`, or :math:`p \vee \neg q`",,:code:`p or not q`
    ":math:`p \circledast_{12} q = [\mathtt{T}, \mathtt{T}, \mathtt{F}, \mathtt{F}]`",:math:`\neg p`,The value of :math:`q` is ignored.,:code:`not p`
    ":math:`p \circledast_{13} q = [\mathtt{T}, \mathtt{T}, \mathtt{F}, \mathtt{T}]`",":math:`p \Rightarrow q`, or :math:`q \vee \neg p`","The ""conditional"" or ""implication"" operator.",:code:`q or not p`
    ":math:`p \circledast_{14} q = [\mathtt{T}, \mathtt{T}, \mathtt{T}, \mathtt{F}]`",":math:`\neg \left(p \wedge q\right)`, or :math:`\neg p \vee \neg q`","The ""nand"" operator.",:code:`not (p and q)`
    ":math:`p \circledast_{15} q = [\mathtt{T}, \mathtt{T}, \mathtt{T}, \mathtt{T}]`",:math:`\text{True}`,"The tautology, always true.",:code:`True`


The point of this table is to exhaustively enumerate all 16 *possible* logic operators.
A few of these are available directly. The rest can be implemented using ``and``, ``or``, and ``not``.

(This was not done by hand. I used ``sympy`` to help generate this table.)

Numbers
=======

Mathematics offers a variety of number domains.

- Integers (:math:`\mathbb{Z}`). Positive and negative counting numbers, as well as zero: {..., −3, −2, −1, 0, 1, 2, 3, ...}.
- Rational numbers (:math:`\mathbb{Q}`). Numbers that can be expressed as a ratio of an integer to a non-zero integer.
- Real numbers (:math:`\mathbb{R}`). Numbers that correspond to points along a line. They can be positive, negative, or zero. All rational numbers are real, but the converse is not true.
- Irrational numbers (:math:`\mathbb {R} \setminus \mathbb {Q}`). Real numbers that are not rational. These are solutions to polynomials like :math:`x^2-5=0`.
- Imaginary numbers: Numbers that equal the product of a real number and the imaginary unit :math:`j = \sqrt{-1}`, or :math:`j^2 = 1`.
- Complex numbers (:math:`\mathbb{C}`). Includes real numbers, imaginary numbers, and sums and differences of real and imaginary numbers.

Here are the Python equivalents.

..  csv-table::
    :header: Math, Python

    :math:`\mathbb{Z}`, ``int``
    :math:`\mathbb{Q}`, ``from fractions import Fraction``
    :math:`\mathbb{R}`, ``float`` is an approximation of real, it is not a perfect representation.
    :math:`\mathbb{C}`, ``complex``

The ``float`` type is actually a kind of rational number: :math:`f = \frac{m}{2^{53}}*2^e`.  The upper bound on the denominator leads to truncation.
The value of :math:`2^{53} \approx 10^{15}`, meaning there are about 15 digits of precision available.

Since the value of :math:`m`, the mantissa, is divided by a power of 2, there will be problems computing a representation that involves any of the prime numbers other than 2. Currency values often involve 0.1 and 0.01, which don't have exact values.

When working with currency, use the ``decimal`` module. Import the definition with ``from decimal import Decimal``.
The ``Decimal`` objects provide real number values that work in base 10.
They are slower, consume more memory, but, give precise answers for currency computations, avoiding the complications of binary representation of decimal fractions.
