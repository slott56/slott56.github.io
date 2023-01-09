Omni Outliner, XML Processing, and Recursive Generators
=======================================================

:date: 2013-09-12 08:00
:tags: data conversion,#python,xml,ETL,csv
:slug: 2013_09_12-omni_outliner_xml_processing_and_recursive_generators
:category: Technologies
:status: published

| First, and most important, `Omni
  Outliner <http://www.omnigroup.com/products/omnioutliner/>`__ is a
  super-flexible tool. Crazy levels of flexibility. It's very much a
  generic-all-singing-all-dancing information management tool.
| It has a broad spectrum of file export alternative formats. Most of
  which are fine for import into some kind of word processor.
| But what if the data is more suitable for a spreadsheet or some more
  structured environment? What if it was a detailed log or a project
  outline decorated with a column of budget numbers?
| We have two approaches, one is workable, but not great, the other has
  numerous advantages.
| In the previous post, "Omni Outliner and Content Conversion", we read
  an export in tab-delimited format. It was workable but icky.
| Here's the alternative. This uses a recursive generator function to
  flatten out the hierarchy. There's a trick to recursion with generator
  functions.
| **Answer 2: Look Under the Hood**
| At the Mac OS X level, an Omni Outline is a "package". A directory
  that appears to be a single file icon to the user. If we open that
  directory, however, we can see that there's an XML file inside the
  package that has the information we want.
| Here's how we can process that file.

::

   import xml.etree.ElementTree as xml
   import os
   import gzip

   packagename= "{0}.oo3".format(filename)
   assert 'contents.xml' in os.listdir(packagename)
   with gzip.GzipFile(packagename+"/contents.xml", 'rb' ) as source:
      self.doc= xml.parse(source)

| 
| This assumes it's compressed on disk. The outlines don't have to be
  compressed. It's an easy try/except block to attempt the parsing
  without unzipping. We'll leave that as an exercise for the reader.
| And here's how we can get the column headings: they're easy to find in
  the XML structure.

::

   self.heading = []
   for c in self.doc.findall(
           "{http://www.omnigroup.com/namespace/OmniOutliner/v3}columns"
           "/{http://www.omnigroup.com/namespace/OmniOutliner/v3}column"):
       # print( c.tag, c.attrib, c.text )
       if c.attrib.get('is-note-column','no') == "yes":
           pass
       else:
           # is-outline-column == "yes"? May be named "Topic".
           # other columns don't have a special role
           title= c.find("{http://www.omnigroup.com/namespace/OmniOutliner/v3}title")
           name= "".join( title.itertext() )
           self.heading.append( name )

| 
| Now that we have the columns titles, we're able to walk the outline
  hierarchy, emitting normalized data. The indentation depth number is
  provided to distinguish the meaning of the data.
| This involves a recursive tree-walk. Here's the top-level method
  function.

::

   def __iter__( self ):
       """Find  for outline itself. Each item has values and children.
       Recursive walk from root of outline down through the structure.
       """
       root= self.doc.find("{http://www.omnigroup.com/namespace/OmniOutliner/v3}root")
       for item in root.findall("{http://www.omnigroup.com/namespace/OmniOutliner/v3}item"):
           for row in self._tree_walk(item):
               yield row

| 
| Here's the internal method function that does the real work.

::

       def _tree_walk( self, node, depth=0 ):
           """Iterator through item structure; descends recursively.
           """
           note= node.find( '{http://www.omnigroup.com/namespace/OmniOutliner/v3}note' )
           if note is not None:
               note_text= "".join( note.itertext() )
           else:
               note_text= None
           data= []
           values= node.find( '{http://www.omnigroup.com/namespace/OmniOutliner/v3}values' )
           if values is not None:
               for c in values:
                   if c.tag == "{http://www.omnigroup.com/namespace/OmniOutliner/v3}text":
                       text= "".join( c.itertext() )
                       data.append( text )
                   elif c.tag == "{http://www.omnigroup.com/namespace/OmniOutliner/v3}null":
                       data.append( None )
                   else:
                       raise Exception( c.tag )
           yield depth, note_text, data
           children= node.find( '{http://www.omnigroup.com/namespace/OmniOutliner/v3}children' )
           if children is not None:
               for child in children.findall( '{http://www.omnigroup.com/namespace/OmniOutliner/v3}item' ):
                   for row in self._tree_walk( child, depth+1 ):
                       yield row

| 
| This gets us the data in a form that doesn't require a lot of external
  schema information.
| Each row has the indentation depth number, the note text, and the
  various columns of data. The only thing we need to know is which of
  the data columns has the indented outline.
| **The Trick**
| Here's the tricky bit.
| When we recurse using a generator function, we have to explicitly
  iterate through the recursive result set. This is different from
  recursion in simple (non-generator) functions. In a simple function,
  we it looks like this.
| def function( args ):
|     if base case: return value
|     else:
|         return calculation on function( other args )
|
| When there's a generator involved, we have to do this instead.
| def function_iter( args ):
|     if base case: yield value
|     else:
|         for x in function_iter( other args )
|             yield x
| **Columnizing a Hierarchy**
| The depth number makes our data look like this.
| 0, "2009"
| 1, "November"
| 2, "Item In Outline"
| 3, "Subitem in Outline"
| 1, "December"
| 2, "Another Item"
| 3, "More Details"
| We can normalize this into columns. We can take the depth number as a
  column number. When the depth numbers are increasing, we're building a
  row. When the depth number decreases, we've finished a row and are
  starting the next row.
| "2009", "November", "Item in Outline", "Subitem in Outline"
| "2009", "December", "Another Item", "More Details"
| The algorithm works like this.
| row, depth_prev = [], -1
| for depth, text in source:
|     while len(row) <= depth+1: row.append(None)
|     if depth <= depth_prev: yield row
|     row[depth:]= [text]+(len(row)-depth-1)*[None]
|     depth_prev= depth
| yield row
| 
| The yield will have to also handle the non-outline columns that may
  also be part of the Omni Outliner extract.





