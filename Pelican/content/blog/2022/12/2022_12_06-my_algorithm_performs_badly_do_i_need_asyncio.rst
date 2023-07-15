My algorithm performs badly, do I need asyncio?
===============================================

:date: 2022-12-06 11:00
:tags: algorithm,software design,analysis,asyncio,concurrency
:slug: 2022_12_06-my_algorithm_performs_badly_do_i_need_asyncio
:category: Technologies
:status: published

Real Question (somewhat abbreviated): "My algorithm performs badly, do I
need asyncio?"

Short answer: No.

Long answer: Sigh. No. Do you need a slap upside the head?

Here's how it plays out:

Q: "We figured that if we 'parallelize' it, then we can apply multiple
cores, and it will run 4x as fast."

Me: "What kind of I/O are you doing?"

Q: "None, really. It's compute-intensive."

Me: "Async is for I/O. A function can be computing while other functions
are waiting for I/O to complete."

Q: "Right. We can have lots of them, so they each get a core."

Me: "Listen, please. A function can be computing. That's "A". Singular.
One. Take a step back from the asyncio package. What are you trying to
do?"

Q: "Make things faster."

Me: "Take a breath. Make *what* faster?"

Q: "A slow algorithm."

Me:

Q: "Do you want to know what we're trying do?"

Me:

Q: "First, we query the database to get categories. Then we query the
database to get details for the categories. Then we query the database
to organize the categories into a hierarchy. Except for certain
categories which are special. So we have if-statements to handle the
special cases."

Me: "That's I/O intensive."

Q: "That's not the part that's slow."

Me:

Q: "Context is important. I feel the need to describe all of the
background."

Me: "That's trivia. It's as important as your mother's maiden name.
What's the problem?"

Q: "The problem is we don't know how to use asyncio to use multiple
cores."

Me: "Do you know how to divide by zero?"

Q: "No. It's absurd."

Me: "We already talked about asyncio for compute-intensive processing.
Same level of absurd as dividing by zero. What are you trying to do?"

Q: "We have some for loops that compute a result slowly. We want to
parallelize them."

Me: "Every for statement that computes a collection is a generator
expression. Every generator expression can be made into a list, set, or
dictionary comprehension. Start there."

Q: "But what if the for statement has a super-complex body with lots of
conditions?"

Me: "Then you might have to take a step back and redesign the algorithm.
What does it do?"

Q: <code> "See all these for statements and if-statements?"

Me: "What does it do? What's the final condition?"

Q: "A set of valid answers."

Me: "Define valid."

Q: "What do you mean? 'Define valid?' It's a set that's valid!"

Me: "Write a condition that defines whether or not a result set is
valid. Don't hand-wave, write the condition."

Q: "That's impossible. The algorithm is too complex."

Me: "How do you test this process? How do you create test data? How do
you know an answer it produces is correct?"

Q:

Me: "That's the fundamental problem. You need to have a well-defined
post-condition. Logic. An ``assert`` statement that defines all correct
answers. From that you can work backwards into an algorithm. You may not
need parallelism; you may simply have a wrong data structure somewhere
in <code>."

Q: "Can you point out the wrong data structure?"

Me:

Q: "What? Why won't you? You read the code, you can point out the
problems."

Me:

Q: "Do I have to do all the work?"

Me:





