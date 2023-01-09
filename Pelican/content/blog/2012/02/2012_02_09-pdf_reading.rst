PDF Reading
===========

:date: 2012-02-09 08:00
:tags: pdf,#python
:slug: 2012_02_09-pdf_reading
:category: Technologies
:status: published

PDF files aren't pleasant.

The good news is that they're documented (http://www.adobe.com/devnet/pdf/pdf_reference.html).

They bad news is that they're rather complex.

I found four Python packages for reading PDF files.

-  http://pybrary.net/pyPdf/ - weak
-  http://www.swftools.org/gfx_tutorial.html - depends on binary XPDF
-  http://blog.didierstevens.com/programs/pdf-tools/ - limited
-  http://www.unixuser.org/~euske/python/pdfminer/ - acceptable


I elected to work with PDFMiner for two reasons.  (1) Pure Python, (2)
Reasonably Complete.

This is not, however, much of an endorsement.  The implementation
(while seemingly correct for my purposes) needs a fair amount of
cleanup.

Here's one example of *remarkably* poor programming.

::

  # Connect the parser and document objects.
  parser.set_document(doc)
  doc.set_parser(parser)

Only one of these two is needed; the other is trivially handled as
part of the setter method.

Also, the package seems to rely on a huge volume of isinstance type
checking.  It's not clear if proper polymorphism is even possible.
But some kind of filter that picked elements by type might be nicer
than a lot of isinstance checks.

**Annotation Extraction**

While shabby, the good news is that PDFMiner seems to reliably
extract the annotations on a PDF form.

In a couple of hours, I had this example of how to read a PDF
document and collect the data filled into the form.

::

  from pdfminer.pdfparser import PDFParser, PDFDocument
  from pdfminer.psparser import PSLiteral
  from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, PDFTextExtractionNotAllowed
  from pdfminer.pdfdevice import PDFDevice
  from pdfminer.pdftypes import PDFObjRef
  from pdfminer.layout import LAParams, LTTextBoxHorizontal
  from pdfminer.converter import PDFPageAggregator

  from collections import defaultdict, namedtuple

  TextBlock= namedtuple("TextBlock", ["x", "y", "text"])

  class Parser( object ):
      """Parse the PDF.

      1.  Get the annotations into the self.fields dictionary.

      2.  Get the text into a dictionary of text blocks.
          The key to the dictionary is page number (1-based).
          The value in the dictionary is a sequence of items in (-y, x) order.
          That is approximately top-to-bottom, left-to-right.
      """
      def __init__( self ):
          self.fields = {}
          self.text= {}

      def load( self, open_file ):
          self.fields = {}
          self.text= {}

          # Create a PDF parser object associated with the file object.
          parser = PDFParser(open_file)
          # Create a PDF document object that stores the document structure.
          doc = PDFDocument()
          # Connect the parser and document objects.
          parser.set_document(doc)
          doc.set_parser(parser)
          # Supply the password for initialization.
          # (If no password is set, give an empty string.)
          doc.initialize('')
          # Check if the document allows text extraction. If not, abort.
          if not doc.is_extractable:
              raise PDFTextExtractionNotAllowed
          # Create a PDF resource manager object that stores shared resources.
          rsrcmgr = PDFResourceManager()
          # Set parameters for analysis.
          laparams = LAParams()
          # Create a PDF page aggregator object.
          device = PDFPageAggregator(rsrcmgr, laparams=laparams)
          # Create a PDF interpreter object.
          interpreter = PDFPageInterpreter(rsrcmgr, device)

          # Process each page contained in the document.
          for pgnum, page in enumerate( doc.get_pages() ):
              interpreter.process_page(page)
              if page.annots:
                  self._build_annotations( page )
              txt= self._get_text( device )
              self.text[pgnum+1]= txt

      def _build_annotations( self, page ):
          for annot in page.annots.resolve():
              if isinstance( annot, PDFObjRef ):
                  annot= annot.resolve()
                  assert annot['Type'].name == "Annot", repr(annot)
                  if annot['Subtype'].name == "Widget":
                      if annot['FT'].name == "Btn":
                          assert annot['T'] not in self.fields
                          self.fields[ annot['T'] ] = annot['V'].name
                      elif annot['FT'].name == "Tx":
                          assert annot['T'] not in self.fields
                          self.fields[ annot['T'] ] = annot['V']
                      elif annot['FT'].name == "Ch":
                          assert annot['T'] not in self.fields
                          self.fields[ annot['T'] ] = annot['V']
                          # Alternative choices in annot['Opt'] )
                      else:
                          raise Exception( "Unknown Widget" )
              else:
                  raise Exception( "Unknown Annotation" )

      def _get_text( self, device ):
          text= []
          layout = device.get_result()
          for obj in layout:
              if isinstance( obj, LTTextBoxHorizontal ):
                  if obj.get_text().strip():
                      text.append( TextBlock(obj.x0, obj.y1, obj.get_text().strip()) )
          text.sort( key=lambda row: (-row.y, row.x) )
          return text

      def is_recognized( self ):
          """Check for Copyright as well as Revision information on each page."""
          bottom_page_1 = self.text[1][-3:]
          bottom_page_2 = self.text[2][-3:]
          pg1_rev= "Rev 2011.01.17" == bottom_page_1[2].text
          pg2_rev= "Rev 2011.01.17" == bottom_page_2[0].text
          return pg1_rev and pg2_rev 

This gives us a dictionary of field names and values.  Essentially
transforming the PDF form into the same kind of data that comes from
an HTML POST request.

An important part is that we don't want much of the background text.
Just enough to confirm the version of the form file itself.

The cryptic ``text.sort( key=lambda row: (-row.y, row.x) )`` will sort
the text blocks into order from top-to-bottom and left-to-right.  For
the most part, a page footer will show up last.  This is not
guaranteed, however.  In a multi-column layout, the footer can be so
close to the bottom of a column that PDFMiner may put the two text
blocks together.

The other unfortunate part is the extremely long (and opaque) setup
required to get the data from the page.



-----

I ported PdfMiner to python 3 a couple of months a...
-----------------------------------------------------

Virgil Dupras<noreply@blogger.com>

2012-02-09 11:34:01.712000-05:00

I ported PdfMiner to python 3 a couple of months ago (
https://bitbucket.org/hsoft/pdfminer3k ) and a bit of cleanup was
involved. The risk of breaking something in the library while cleaning
up is significant which makes the effort harder. Let me know if you want
to get involved in a cleanup effort.


PDFMiner certainly looks very promising. If I have...
-----------------------------------------------------

David Boddie<noreply@blogger.com>

2012-02-09 16:27:28.223000-05:00

PDFMiner certainly looks very promising. If I have to deal with PDF
files in the future, I'll probably try it out before the other Python
solutions.

As an aside, I'm not intending to start a fight here, but you might want
to pick your words more carefully if you are aiming to deliver
constructive criticism to the author. Since the tool has been around for
a while, some of the "poor programming" might not be so easy to change,
particularly if users have built up a collection of scripts that rely on
the API remaining fixed.


How use your code ? I dont understood. Tried 1 hou...
-----------------------------------------------------

Piotr Pastuszka<noreply@blogger.com>

2012-10-13 15:05:11.003000-04:00

How use your code ? I dont understood. Tried 1 hour and not sucess.


Hi,
I have a trouble with table parsing in pdf. Pl...
-----------------------------------------------------

hoangnguyenminh<noreply@blogger.com>

2012-09-25 00:35:31.535000-04:00

Hi,
I have a trouble with table parsing in pdf. Please let me know how
pdfminer extract table!
Thank you very much!
hugo





