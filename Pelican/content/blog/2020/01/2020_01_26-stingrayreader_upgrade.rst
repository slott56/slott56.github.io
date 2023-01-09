StingrayReader Upgrade
======================

:date: 2020-01-26 12:27
:tags: stingray reader,#python,type hints
:slug: 2020_01_26-stingrayreader_upgrade
:category: Technologies
:status: published

| See https://github.com/slott56/Stingray-Reader
| It's time to add type hints.
| And.
| Learn some interesting lessons.
| Here's the interesting problem:

::

   some_data = {name: source[name] for name in the_names}
   the_object = SomeClass(**some_data)

| 
| While valid, this concerns **mypy**.
| The point here is to have a flexible source of data, source. Perhaps
  this is a spreadsheet row, or a complex JSON/YAML-formatted document
  with optional or irrelevant fields. The short list of relevant names
  is in the_names.  Ideally, this list of names matches the keyword args
  of SomeClass.
| This gives **mypy** fits because there's no way to match the
  dictionary with the object's parameters.
| We have two paths forward.

#. Eliminate the intermediate dictionary. Use SomeClass(x=source['x'],
   y=source['y'], ... etc.)
#. Consider using a TypedDict for the intermediate dictionary. But. Then
   the dictionary's types must be kept in sync with the SomeClass
   definition, which may be a little crazy.

| Item 2 isn't as crazy as it sounds, though. The SomeClass definition
  has a \**kwargs option, allowing extra attributes to be set. This is,
  perhaps also crazy. But, the framework needs to drag around extra
  attributes for the application's benefit.
| A possibility is to do away with \**kwargs, and replace it with other:
  Dict[Any, Any]. This cuts down on the expressivity of the framework.
  Now we support SomeClass.app_name. This change would mean we'd have
  SomeClass.other['app_name']. While possibly better for **mypy**, I
  don't think it's ideal for users.
| I can also rework SomeClass to use \__getattribute__() to look into
  self.other for extra attribute names.
| I'm very happy to have the rigorous static check. The rethinking is
  helpful.
| ("Wait," you say. "You didn't provide the recommended path forward."
   Correct.  I'll update.)





