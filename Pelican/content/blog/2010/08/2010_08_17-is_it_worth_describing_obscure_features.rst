Is It Worth Describing Obscure Features?
========================================

:date: 2010-08-17 08:00
:tags: #python,building skills books
:slug: 2010_08_17-is_it_worth_describing_obscure_features
:category: Technologies
:status: published

I'm rewriting *Building Skills in Python*. 2.7 is out. As more libraries
make the move, 3.1 is getting more and more viable.

I'm looking closely at the Decorators chapter (`Part 3, Chapter
6 <http://homepage.mac.com/s_lott/books/python/html/p03/p03c06_decorators.html>`__).

And I'm struggling with classmethod. It's a first-class part of
Python. And I'm sure there are folks who find it useful.

But I'm struggling to find a "simple" (i.e., under 12 lines of code)
example where it might be useful.

Indeed, I'm starting to suffer from a growing feeling that this is
one language feature that I can gracefully elide from in-depth to
mere mention.

There is a relevant Stack Overflow question: `What are Class methods
in Python
for? <http://stackoverflow.com/questions/38238/what-are-class-methods-in-python-for>`__
But the examples there aren't terribly compelling. Perhaps I have a
blind-spot here because I never seen a big need for writing
metaclasses. Or perhaps because I don't see a need for creating
alternate constructors -- the options in \__init__() seem to cover
almost all my needs.



-----

Just if it helps you as a real-world example, one ...
-----------------------------------------------------

Jaime<noreply@blogger.com>

2010-08-17 08:41:36.512000-04:00

Just if it helps you as a real-world example, one specific classmethod
that it's very useful it's when dealing with ORMs. Specifically with
SQLAlchey.

Your class it's something like

::

    class MyClass(Base):
        id = sa.Column(sa.type.Integer(), primary_key=true)
        name = sa.Column(sa.type.String())
        @classmethod
        def all(cls):
            ''' Get all the elements of this class '''
            return meta.Session.query(cls)

I don't know if it's a good example, as it relies on a particular module
(SQLAlchemy) and have some concepts of that module, like meta and query
it, etc... but, well, it's a real world example.

Other use I sometimes give to classmethods is, if for a particular
static function I want to associate it to a specific class, but it's not
using any object information, sometimes I will "attach" it to the Class.
For example, let's say we are describing vehicles

::

    class Vehicle():
        def __init__(self, type):
            self.type = type
        @classmethod
        def get_num_wheels(cls, type):
            ''' Return number of wheels for a particular type of vehicle '''
            matrix = {'CAR':4, 'BIKE':2, 'TRUCK':8}
            return matrix[type]

I could do the same with a static function outside the class, but I
found sometimes clearer to attach that inside the class, so the calling
will be Vehicle.get_num_wheels(type)
Maybe it's just a stupid example... ;-)


I use class methods often, but almost always as al...
-----------------------------------------------------

casey<noreply@blogger.com>

2010-08-17 12:38:47.211000-04:00

I use class methods often, but almost always as alternate constructors.
They really have nothing to do with metaclasses IMO, though they can be
useful with them. I've probably used classmethods 100 times for every 1
time I've created a metaclass (and more often then not, I wind up
refactoring it away later anyhow 8^).

Probably the best practical example is when an object can be constructed
with args of different meanings. I find it more explicit than sniffing
the arg types in \__init__. Also sometimes, the types of the input args
are the same type in both constructors. A simple, useful example I ran
into recently is a 2D vector class. It can be constructed two distinct
ways: with cartesian coordinates or polar coordinates. It so happens
that in both cases they are two numeric arguments (x,y or angle,length)
so a classmethod is perfect to differentiate cleanly.

Another common use I find for them is for classes for scripts or
daemons. In \__init__, I have all of the scripts command line options
broken out into separate arguments. Then I have a classmethod like:
"from_argv(cls, argv)" which takes the arguments as a list of strings as
they would be passed in from the system. This uses argparse or whatever
to parse them and delegates to \__init_\_ using normal arguments. This
makes everything, including the command line arg parsing easily unit
testable, but I'm not forced to fake out CL args to instantiate the
class when testing, unless I want to test that explicitly.


I use classmethods periodically and I don&#39;t fi...
-----------------------------------------------------

TheBashar99<noreply@blogger.com>

2010-08-17 18:05:55.387000-04:00

I use classmethods periodically and I don't find them particularly
confusing. They're a convenient way to define methods which do use some
class level data but do not use instance data.

::

    @classmethod
    def compute(cls, input1, input2)
        return (input1 / input2) * cls.scale


What I think we&#39;re struggling with here is the...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-08-17 11:29:39.727000-04:00

What I think we're struggling with here is the fact that all bound
methods in python are a mere convenience - you get "self" for free. But
whatever "self" is could have been an argument to an unbound function in
the first place.

When you start talking about classmethod, you give up even that small
convenience. When we use classmethod, we are typically trying to
represent one of two things:

1) Static data that could just be stored on the class or module in the
first place
or

2) A function that returns different values based on arguments passed
in, and not on "self". In this case, one might question why we want to
attach this seemingly unrelated function to the class at all, and not
simply leave leave it as an unbound function in the module's namespace.

This seems the simple, reasonable thing to do, which is why I think we
struggle to come up with practical examples.


Probably the best argument for class methods that ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-08-17 12:51:05.295000-04:00

Probably the best argument for class methods that I've seen is for
alternate constructors. \__init__() provides the most common one and
then class methods provide alternate forms of construction. E.g.
Decimal.from_float() or somesuch.





