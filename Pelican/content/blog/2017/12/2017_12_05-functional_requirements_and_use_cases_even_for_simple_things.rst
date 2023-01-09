Functional Requirements and Use Cases -- even for "simple" things
=================================================================

:date: 2017-12-05 08:00
:tags: requirements,use case,architecture
:slug: 2017_12_05-functional_requirements_and_use_cases_even_for_simple_things
:category: Architecture & Design
:status: published

In the mailbag I found this nonsense, doomed to inevitable failure:

   "As I get more serious about this data science stuff, it has become
   obvious that a windows machine is not the way to go. ...
   Q1: What other things should I think about and consider while
   shopping for a new computer?
   Q2: Are there issues w/ running VmWare and Windows 7 w/in VmWare on
   Ubuntu?
   "

I've omitted many, many words (400 or so.)

Here are all of the functional requirements I could discern:

-  I would like to have 1 machine. I don't want a desktop and a laptop

-  Install VmWare

-  Install Windows 7 using VmWare

This was **all** of the functional requirements. The other 400 words
involved specifications. Nothing that approaches a use case other
than singular, VMWare, and Windows under VMWare. The form factor of
laptop, which seems to go without saying, might be a user story, but
that's pushing it.

The "a windows machine is not the way to go" and "Install Windows 7"
indicate a fairly serious problem. It is not the way to go **and**
it's required. Both. This is doomed to inevitable failure.

This is not the way to make a decision.

Q1. What other things should I think about?
--------------------------------------------

Just about every other thing. Start with use cases and functional
requirements. Skip over specifications. (In general, never start with
specifications because that's where you end: a list of useless
numbers that don't bracket what you actually want to do.)

Use Cases Matter. Specifications Don't Matter.
Write down all the Mbs and Tbs you want. Without a use case, they're
irrelevant noisy details. Throw the numbers away until you have a
list of verbs. Things you will DO.

With so few actual functional requirements, almost *any* computer
(possibly including a Raspberry Pi 3) would pass the suite of
acceptance test cases.

✅ One Machine.

✅ VMWare.

✅ Windows.

After a lot more back-and-forth, I discerned one (or maybe two)
additional functional requirement(s).

-  I have `leo <http://leoeditor.com/>`__ w/ java to gen html.

I know what `Leo <http://leoeditor.com/>`__ is in this context. I'm
guessing the "java to gen html" is
`JRst <https://github.com/vorburger/JRst/blob/master/jrst/doc/en/index.rst>`__.
The lack of clarity is, of course, part of the problem here.

This requirement surfaced in the context of explaining to me why
Windows was so important. Really. Windows was required to run two
open-source apps. And. "a windows machine is not the way to go."
Doomed. To. Inevitable. Failure.

Here's the only relevant functional requirement(s): run Leo and Java.
And even then, there's a huge hole in this. Leo is Python-based.
Docutils RST2HTML is Python-based. Why not simply use Leo and Python?
What does Java have to do with anything?
Buy this: a Pi-top: https://www.sparkfun.com/products/13896

Q2. Are there issues w/ running...?
------------------------------------

Yes. Always. For everything you can possibly enumerate there are
"issues".

There. Are. Always. Issues.

Use Cases Matter.

Since you don't have any functional requirements or use cases, it's
impossible to filter the issues and see if any of the known issues
impact what you think you're going to do.

From what I was told, a Pi-top covers everything that's **required**.
It's hard to be sure, of course, when the functional requirements are
so vague. But there's no evidence that the Pi-top can't work to fill
**all** of the stated functional requirements.

What To Do Next
---------------

It seems obvious, but the next step is to create a test plan.
Actually, that was the first step. Since it wasn't done first, now
it's the next step.

Write down the things you want to **do**. Make a list. Ideally a long
list of things you will **DO**. Active voice. **Verbs**. **Actions**.
**Tasks**. **Activities**. It's hard to emphasize this enough.

Then, when considering a computer, see if it can actually do those
things. Test it against the requirements to see if it does what it's
supposed to do. Among all the machines that pass the tests, you can
then sort by price. (Or availability, or reputation, or cool
stickers, whatever non-functional requirements seem relevant.)

The questions of Tb and Mb and processor clock speed mean nothing.
Nothing. Find the cheapest (smallest) machine that does what you
want. Don't find the machine with xMb and yTb of whatever.

There there's this, "As I get more serious about this data science
stuff" which seems little more than context. But it's really
important. Indeed, it's **essential**.

If you're going to **do** machine learning, you don't really want to
**buy** the necessary computer. You want to rent it for the hour or
so each day you actually need it. It will be idle 23/24 hours each
day (96% of the time.) Why buy that much horsepower which you are
never going to use.

If you're going to login to a server you purchased from a cloud
computing vendor. Amazon AWS. Microsoft Azure, etc., then, you can
probably get by with a tablet that runs SSH and a browser. A tablet
with a cool keyboard and a little display rack can be very
nice. https://panic.com/prompt/ and `https://www.termius.com <https://www.termius.com/>`__
seem to be all that's required.

https://azure.microsoft.com/en-us/services/virtual-machines/

`https://www.brydgekeyboards.com <https://www.brydgekeyboards.com/>`__


Without Use Cases, however, it's impossible to select a computer.
Don't spend money without test cases.






