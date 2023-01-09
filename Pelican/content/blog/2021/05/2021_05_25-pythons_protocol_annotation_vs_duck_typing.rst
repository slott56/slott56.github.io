Python's Protocol Annotation vs. Duck Typing
============================================

:date: 2021-05-25 08:00
:tags: #python,duck typing,protocols,annotations,type hints
:slug: 2021_05_25-pythons_protocol_annotation_vs_duck_typing
:category: Technologies
:status: published

Let's talk about profound confusion.

I got an email with a subject of this, "Python's Protocol Reduces
Reliance on Duck Typing". The resulting conversation led to this nugget:
"... my current project could use protocols in Python, and thus I didn't
need to rely on duck typing and instead could use that as my type."

I'm unclear on what "reliance" really meant here.

Python depends (heavily) on duck typing. Because type annotations are
optional, this cannot change. It's unlikely to ever change.

Here's the bottom line: Duck Typing Won't Go Away.

Indeed, there's more: Duck Typing Isn't Bad.

Python doesn't "rely" on the type annotations. They're a bonus feature
to make sure you aren't lying about the types and how they're used.

Protocols are how duck typing works. When we leverage duck typing among
classes, we're implicitly relying on the classes all supporting a common
protocol. Numbers, for example, implement a ton of methods; this
collection of common methods (e.g., ``__add__()``, etc.) define a
protocol.

With mypy, we can create our own distinct protocols as named types.

I don't get the "reducing reliance" business when protocols make duck
typing work. And. Sadly. I couldn't figure out where the confusion
arose.

Follow-up
---------

I asked for clarification and got nothing useful in response. The person
sending the email seemed to be working from a summary of another
conversation, or something. I couldn't figure it out.

I can try to assume they used to have this.

::

   class Something:
       def useful_method(self, x: str) -> int:
           # whatever
           
   class CloselyRelated:
       def useful_method(self, x: str) -> int:
           # another polymorphic thing
           
   Polymorphic = Union[Something, CloselyRelated]

   # many classes and functions relying on Polymorphic

And they've realized that there may be a better way.

But. I haven't really got much to go on.

The better approach often involves something like this:

::

   class Polymorphic(Protocol): 
       def useful_method(self, x: str) -> int:
           ...

We can define a protocol to help locate the essential features of a
parameter or a result type.

But. I don't really know what was going on.

And I couldn't figure out why the word "Reliance" was used.





