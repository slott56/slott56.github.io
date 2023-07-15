Architectural Boundaries: Which Package/Module/Class Owns That Responsibility?
==============================================================================

:date: 2021-06-22 09:19
:tags: #python,object-oriented design,Design Principles,SOLID
:slug: 2021_06_22-architectural_boundaries_which_packagemoduleclass_owns_that_responsibility
:category: Architecture & Design
:status: published

The SOLID design principles beat the design boundary issue to death.
Here are the principles in my preferred order.
(See https://www.linkedin.com/learning/learning-s-o-l-i-d-programming-principles)

#. **Interface Segregation** -- minimize the boundaries. Do this first.

#. **Liskov Substitution** -- keep the boundaries consistent. Do this
   for hierarchies.

#. **Open/Closed** -- keep the boundaries stable and allow subclasses.

#. **Dependency [Inversion] Injection** -- keep the implementation
   separate from the design.

#. **Single Responsibility** -- This is essentially a summary of the
   above four principles.

The point here is that these principles are pleasantly poetic, but there
are those edgy cases where an interface can go either way.

Specifically, here's an Edgy Case that can go either way.

We're reading GPX (GPS Exchange) data.
See https://www.topografix.com/GPX/1/1/.

Associated with this is what's known as the Lowrance USR file format. A
lot of devices include the same (or similar) underlying software, and
can exchange waypoint and route information in USR format.

We have this as part of the underlying model.

-  The underlying ``Angle`` as an abstraction. This has two subclasses:

   -  Latitude. An angle with "N" and "S" for its sign, conventionally
      shown as a two-digit number of degrees: ``25°42.925′N``

   -  Longitude. An angle with "E" and "W" for its sign, conventionally
      shown as a three-digit number of degrees: ``080°13.617′W``

-  A Point (or ``LatLon``) is a two-tuple, ``tuple[Lat, Lon]``.

A waypoint includes name, description, a time-of-last-update (TOLU), and
display symbol to be used. It may also include a GUID to track name
changes and assure uniqueness in spite of repeated names.

So far, so good. Nothing too edgy there. "Where's the problem?" you ask.

The problem is representation.

In GPX files, latitude and longitude are float values in degrees. You'll
see this: ``<wpt lon="-80.22695124" lat="25.7154147">...</wpt>``.

To do any useful computation, they need to be radians. Or a geocode that
supports proximity comparisons, like OLC.

And. If you work with a CSV export from a tool like
`OpenCPN <https://opencpn.org>`__, then you get strings. This can be any
combination of degrees and minutes or degrees, minutes, and seconds.
And, depending on the software, there may be either ° or º for the
degrees. Can't tell the apart? One is U+00B0, the DEGREE SIGN. The other
is U+00BA, the MASCULINE ORDINAL INDICATOR. Plus, of course, everyone
uses apostrophe (') and quote (") where they should have used prime (′)
and double prime (″). These are easy regular expression problems to
solve.

This leads to a class like the following:

::

   class Angle(float):
       @classmethod
       def fromdegrees(cls, deg: float, hemisphere: Optional[str] = None) -> "Angle":
           ...
       @classmethod
       def fromstring(cls, value: str) -> "Angle":
           ...

This Angle class converts numbers or strings into useful values; in
radians internally. Formatted in degrees externally.  (And yes, this
gets a warning from Python 3.9 that we can't usefully extend float like
this.)

The problem is USR files.

In USR files, they use millimeter mercator numbers for latitude and
longitude. These are distances from the equator or the prime meridian.
Because they're in millimeters, an integer will do nicely. A little
computation is done to extract degrees (or radians) from these values.

::

   SEMIMINOR_B = 6_356_752.3142

   lon = round(math.degrees(mm_lon / SEMIMINOR_B), 8)
   lat = round(
           math.degrees(2 * math.atan(math.exp(mm_lat / SEMIMINOR_B)) - math.pi / 2), 8
       )

These aren't too bad. But.

Here's the question.

Where does this belong? Is it part of the underlying ``Angle`` class? It
is separate?

Where does Millimeter Mercator representation belong?
-----------------------------------------------------

This raises a secondary question: Where does ANY representation belong?

Do we separate the essential object (an angle in radians, a float) from
all representation questions? If so, how do we properly bind value and
representation at run time?

Is our app full of complex mixins to bind the float with representation
choices?  ``class Latitude(float, DMS, MM, etc.): pass``. This seems
potentially annoyingly complex: we have to make sure names don't
collide, when defining all these aspects separately.

I think the representation for latitudes and longitudes \*is\* the
essential problem here. The math (i.e. computing the loxodromic distance
between points) is trivially separated from all of these representation
concerns.

If we buy into the centrality of representation issues, then, we're down
to the following argument.

**Resolution**: millimeter mercator belongs in the Angle class.

**Affirmative**: it's yet another representation of an angle's value.

**Negative**: it's not used outside USR files and belongs in the USR file parser module.

**Affirmative Rebuttal**: None of the other representations in Angle are tied specifically to a file format.

**Negative Rebuttal**: Because the other formats (float, string) are
intermixed in CSV files and text displays, making them "widely used."
While float is used consistently in GPX, this encoding is a pleasant
exception that relies on widely-used encodings.

Okay. We seem to have conflicting goals here. Some representation is a
generic thing that crosses file formats and some representation is
localized to a specific file format and not reused.

The SOLID design principles don't help chose between these designs.
Instead, they provide post-hoc justification for the design we chose.

We can exploit the SOLID principles in a variety of ways. Some Examples.

-  We could claim that LatitudeMM is a subclass of Latitude with the MM
   conversions mixed in. Open/Closed. Liskov Substitution.

-  We could claim that Latitude has several load/dump strategies
   available, including Load from MM. Open/Closed. Dependency is
   Injected at run-time.

Sigh.

Prior Art
---------

Methods like ``__str__()`` and ``__repr__()`` are generally considered
part of the essential class. That means the most common string
representations need to be provided. The parsing of a string, similarly,
is the constructor for  an instance of the ``float`` class.

So. Some representations are part of the class. Clearly, however, not
all representations are part of the class. Representation codecs like
``pickle``, ``struct``, or ``ctype`` are kept separate.

I'm going to make the case that there's a very, very fine line between
unique and non-unique-but-not-widely-used aspects of a class of objects.
And, in this specific case, the millimeter mercator should be kept
separate.

I'm going to rely on other representations like PlusCode (also called
`OLC <https://en.m.wikipedia.org/wiki/Open_Location_Code>`__) as yet
another obscure representation and insist these aren't essential to the
class. Indeed, I'm going to suggest that proximity-friendly geocoding is
clearly separate because it's a hack to replace complex distance
computations with substring comparisons.





