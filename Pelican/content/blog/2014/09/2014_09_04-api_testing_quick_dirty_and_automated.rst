API Testing: Quick, Dirty, and Automated
========================================

:date: 2014-09-04 08:00
:tags: unit testing,#python
:slug: 2014_09_04-api_testing_quick_dirty_and_automated
:category: Technologies
:status: published

| When writing RESTful API's, the process of testing can be simple or
  kind of hideous.
| The `Postman REST
  Client <https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en>`__
  is pretty popular for testing an API. There are others, I'm sure, but
  I'm working with folks who like Postman.
| Postman 10 has some automation capabilities. Some.
| However. (And this is important.)
| It doesn't provide much help in framing up a valid complex JSON
  message.
| When dealing with larger and more complex API's with larger and more
  complex nested and repeating structures, considerably more help is
  required to frame up a valid request and do some rational evaluation
  of the response.
| Enter Python, httplib and json. While Python3 is universally better,
  these libraries haven't changed much since Python2, so either version
  will work.
| The idea is simple.

#. Create templates for the eventual class definitions in Python. This
   can make it easy to build the JSON structures. It can save a lot of
   hoping that the JSON content is right. It can save time in
   "exploratory" testing when the JSON structures are wrong.
#. Build complex messages using the template class definitions.
#. Send the message with httplib. Read the response.
#. Evaluate the responses with a simple script.

| Some test scripting is possible in Postman. *Some*. In Python, you've
  got a complete programming language. The "some" qualifier evaporates.
| When it comes to things like seeding database data, Python (via
  appropriate database drivers) can seed integration test databases,
  also.
| Further, you can use the Python unittest framework to write elegant
  automated script libraries and run the entire thing from the command
  line in a simple, repeatable way.
| What's important is that the template class definitions aren't working
  code. They won't evolve into working code. They're placeholders so
  that we can work out API concepts quickly and develop relatively
  complete and accurate pictures of what the RESTful interface will look
  like.
| I had to dig out my copy of
  https://www.packtpub.com/application-development/mastering-object-oriented-python
  to work out the metaclass trickery required.
| **The Model and Meta-Model Classes**
| The essential ingredient is a model class what we can use to build
  objects. The objective is not a complete model of anything. The
  objective is just enough model to build a complex object.
| Our use case looks like this.

::

   >>> class P(Model):
   ...    attr1= String()
   ...    attr2= Array()
   ...
   >>> class Q(Model):
   ...    attr3= String()
   ...
   >>> example= P( attr1="this", attr2=[Q(attr3="that")] )

| 
| Our goal is to trivially build more complex JSON documents for use in
  API testing.  Clearly, the class definitions are too skinny to have
  much real meaning. They're handy ways to define a data structure that
  provides a minimal level of validation and the possibility of
  providing default values.
| Given this goal, we need a model class and descriptor definitions. In
  addition to the model class, we'll also need a metaclass that will
  help build the required objects. One feature that we really like is
  keeping the class-level attributes in order. Something Python doesn't
  to automatically. But something we can finesse through a metaclass and
  a class-level sequence number in the descriptors.
| Here's the metaclass to cleanup the class \__dict__. This is the
  Python2.7 version because that's what we're using.

::

   class Meta(type):
       """Metaclass to set the ``name`` attribute of each Attr instance and provide
       the ``_attr_order`` sequence that defines the origiunal order.
       """
       def __new__( cls, name, bases, dict ):
           attr_list = sorted( (a_name
               for a_name in dict
               if isinstance(dict[a_name], Attr)), key=lambda x:dict[x].seq )
           for a_name in attr_list:
               setattr( dict[a_name], 'name', a_name )
           dict['_attr_order']= attr_list
           return super(Meta, cls).__new__( cls, name, bases, dict )

   class Model(object):
       """Superclass for all model class definitions;
       includes the metaclass to tweak subclass definitions.
       This also provides a ``to_dict()`` method used for
       JSON encoding of the defined attributes.

       The __init__() method validates each keyword argument to
       assure that they match the defined attributes only.
       """
       __metaclass__= Meta
       def __init__( self, **kw ):
           for name, value in kw.items():
               if name not in self._attr_order:
                   raise AttributeError( "{0} unknown".format(name) )
               setattr( self, name, value )
       def to_dict( self ):
           od= OrderedDict()
           for name in self._attr_order:
               od[name]= getattr(self, name)
           return od

| 
| The \__new__() method assures that we have an additional \_attr_order
  attribute added to each class definition. The \__init__() method
  allows us to build an instance of a class with keyword parameters that
  have a minimal sanity check imposed on them. The to_dict() method is
  used to convert the object prior to making a JSON representation.
| Here is the superclass definition of an Attribute. We'll extend this
  with other attribute specializations.

::

   class Attr(object):
       """A superclass for Attributes; supports a minimal
       feature set. Attribute ordering is maintained via
       a class-level counter.

       Attribute names are bound later via a metaclass
       process that provides names for each attribute.

       Attributes can have a default value if they are
       omitted.
       """
       attr_seq= 0
       default= None
       def __init__( self, *args ):
           self.seq= Attr.attr_seq
           Attr.attr_seq += 1
           self.name= None # Will be assigned by metaclass ``Meta``
       def __get__( self, instance, something ):
           return instance.__dict__.get(self.name, self.default)
       def __set__( self, instance, value ):
           instance.__dict__[self.name]= value
       def __delete__( self, *args ):
           pass

| 
| We've done the minimum to implement a data descriptor.  We've also
  included a class-level sequence number which assures that descriptors
  can be put into order inside a class definition.
| We can then extend this superclass to provide different kinds of
  attributes. There are a few types which can help us formulate messages
  properly.

::

   class String(Attr):
       default= ""

   class Array(Attr):
       default= []

   class Number(Attr):
       default= None

| 
| The final ingredient is a JSON encoder that can handle these class
  definitions.  The idea is that we're not asking for much from our
  encoder. Just a smooth way to transform these classes into the
  required dict objects.

::

   class ModelEncoder(json.JSONEncoder):
       """Extend the JSON Encoder to support our Model/Attr
       structure.
       """
       def default( self, obj ):
           if isinstance(obj,Model):
               return obj.to_dict()
           return super(NamespaceEncoder,self).default(obj)

   encoder= ModelEncoder(indent=2)

| 
| The Test Cases
| Here is an all-important unit test case. This shows how we can define
  very simple classes and create an object from those class definitions.

::

   >>> class P(Model):
   ...    attr1= String()
   ...    attr2= Array()
   ...
   >>> class Q(Model):
   ...    attr3= String()
   ...
   >>> example= P( attr1="this", attr2=[Q(attr3="that")] )
   >>> print( encoder.encode( example ) )
   {
     "attr1": "this", 
     "attr2": [
       {
         "attr3": "that"
       }
     ]
   }

| 
| Given two simple class structures, we can get a JSON message which we
  can use for unit testing. We can use httplib to send this to the
  server and examine the results.





