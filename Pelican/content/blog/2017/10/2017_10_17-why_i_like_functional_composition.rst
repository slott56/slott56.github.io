Why I like Functional Composition
=================================

:date: 2017-10-17 08:00
:tags: functional python programming,functional programming,#python
:slug: 2017_10_17-why_i_like_functional_composition
:category: Technologies
:status: published

| After spending years developing a level of mastery over Object
  Oriented Design Patterns, I'm having a lot of fun understanding
  Functional Design Patterns.
| The OO Design Patterns are helpful because they're concrete
  expressions of the S. O. L. I. D. design principles. Much of the "Gang
  of Four" book demonstrates the Interface Segregation, Dependency
  Injection, and Liskov Substitution Principles nicely. They point the
  way for implementing the Open/Closed and the Single Responsibility
  Principles.
| For Functional Programming, there are some equivalent ideas, with
  distinct implementation techniques. The basic I, D, L, and S
  principles apply, but have a different look in a functional
  programming context. The Open/Closed principle takes on a radically
  different look, because it turns into an exercise in Functional
  Composition.
| I'm building an Arduino device that collects GPS data. (The context
  for this device is the subject of many posts coming in the future.)
| GPS devices generally follow the NMEA 0183 protocol, and transmit
  their data as sentences with various kinds of formats. In particular,
  the GPRMC and GPVTG sentences contain speed over ground   (SOG) data.
| I've been collecting data in my apartment. And it's odd-looking. I've
  also collected data on my boat, and it doesn't seem to look quite so
  odd. Here's the analysis I used to make a more concrete conclusion.

::

   def sog_study(source_path = Path("gps_data_gsa.csv")):
       with source_path.open() as source_file:
           rdr = csv.DictReader(source_file)
           sog_seq = list(map(float, filter(None, (row['SOG'] for row in rdr))))
           print("max {}\tMean {}\tStdev {}".format(
               max(sog_seq), statistics.mean(sog_seq), statistics.stdev(sog_seq)))

| 
| This is a small example of functional composition to build a sequence
  of SOG reports for analysis.
| This code opens a CSV file with data extracted from the Arduino. There
  was some reformatting and normalizing done in a separate process: this
  resulted in a file in a format suitable for the processing shown
  above.
| The compositional part of this is the *list(map(float, filter(None,
  generator)))* processing.
| The (row['SOG'] for row in rdr) generator can iterate over all values
  from the SOG column. The filter(None, generator) will drop all None
  objects from the results, assuring that irrelevant sentences are
  ignored.
| Given an iterable that can produce SOG values, the map(float,
  iterable) will convert the input strings into useful numbers. The
  surrounding list() creates a concrete list object to support summary
  statistics computations.
| I'm really delighted with this kind of short, focused functional
  programming.
| "But wait," you say. "How is that anything like the SOLID OO design?"
| Remember to drop the OO notions. This is functional composition, not
  object composition.
| ISP: The built-in functions all have well-segregated interfaces. Each
  one does a small, isolated job.
| LSP: The concept of an iterable supports the Liskov Substitution
  Principle: it's easy to insert additional or different processing as
  long as we define functions that accept iterables as an argument and
  yield their values or return an iterable result.
| For example.

::

   def sog_gen(csv_reader):
       for row in csv_reader:
           yield row['SOG']

| 
| We've expanded the generator expression, (row['SOG'] for row in rdr),
  into a function. We can now use sog_gen(rdr) instead of the generator
  expression. The interfaces are the same, and the two expressions enjoy
  Liskov Substitution.
| To be really precise, annotation with type hints can clarify this.
   Something like sog_gen(rdr: Iterable[Dict[str, str]]) ->
  Iterable[str] would clarify this.
| DIP: If we want to break this down into separate assignment
  statements, we can see how a different function can easily be injected
  into the processing pipeline. We could define a higher-order function
  that accepted functions like sog_gen, float, statistics.mean, etc.,
  and then created the composite expression.
| OCP: Each of the component functions is closed to modification but
  open to extension. We might want to do something like this: map_float
  = lambda source: map(float, source). The map_float() function extends
  map() to include a float operation. We might even want to write
  something like this.  map_float = lambda xform, source: map(xform,
  map(float, source)). This would look more like map(), with a float
  operation provided automatically.
| SRP: Each of the built-in functions does one thing. The overall
  composition builds a complex operation from simple pieces.
| The composite operation has two features which are likely to change:
  the column name and the transformation function. Perhaps we might
  rename the column from 'SOG' to 'sog'; perhaps we might use decimal()
  instead of float(). There are a number of less-likely changes. There
  might be a more complex filter rule, or perhaps a more complex
  transformation before computing the statistical summary.  These
  changes would lead to a different composition of the similar
  underlying pieces.





