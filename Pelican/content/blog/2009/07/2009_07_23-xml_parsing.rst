XML Parsing
===========

:date: 2009-07-23 20:14
:tags:
:slug: 2009_07_23-xml_parsing
:category: Technologies
:status: published

See `Python XML parsing <http://thomas.apestaart.org/log/?p=962>`__ and
`Parsing simple XML files in python using
etree <http://kaens.blogspot.com/2007/05/parsing-simple-xml-files-in-python.html>`__.

Originally, I used
`SAX <http://docs.python.org/library/xml.sax.html>`__ -- but built
DOM objects with it. I moved from application-specific DOM's to
generic DOM's.

Then I switched to the
`miniDOM <http://docs.python.org/library/xml.dom.minidom.html>`__
parser. It gave me structures I could walk with a pleasant
**Visitor** design.

Last year, I switched to `Element
Tree <http://docs.python.org/library/xml.etree.elementtree.html>`__.
Now I can use **Visitor** and the XPATH search.



-----

I still think of lxml as the only xml parsing libr...
-----------------------------------------------------

schmichael<noreply@blogger.com>

2009-07-24 13:12:44.434000-04:00

I still think of lxml as the only xml parsing library I'll ever need in
Python. :-)





