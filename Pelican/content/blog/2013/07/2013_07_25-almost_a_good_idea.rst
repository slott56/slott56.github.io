Almost a good idea
==================

:date: 2013-07-25 13:44
:tags: macintosh,data conversion,mac os x,#python
:slug: 2013_07_25-almost_a_good_idea
:category: Technologies
:status: published


Appleworks (formerly Clarisworks) is software that's been dead meat
since 2007.

See http://en.wikipedia.org/wiki/AppleWorks#End_of_Appleworks

Which is fine unless you have an old computer with old applications
that still works. For example, a 2002-vintage iMac
G4 http://www.imachistory.com/2002/ still works. Slowly.

When someone jumps 11 years to a new iMac, they find that their 2002
iMac with 2007 apps has files which are essentially unreadable by
modern applications.

How can someone jump a decade and preserve their content?

1.  `iWork Pages <http://www.apple.com/iwork/>`__ is cheap. Really.
    $19.99.  I could have used it to convert their files to their new iMac
    and then told them to ignore the app. Pages can be hard to learn. For
    someone jumping from 2007-vintage apps, it's probably too much.
    However, they can use
    `TextEdit <http://support.apple.com/kb/ht2523>`__ once the files are
    converted to RTF format.

2.  `iWork for iCloud <http://www.apple.com/iwork-for-icloud/>`__ may
    be a better idea. But they have to wait a while for it to come out.
    And they want their files now.

3.  Try to write a data extractor.

Here are some places to start.

-   https://github.com/teacurran/appleworks-parser

-   http://fossies.org/linux/misc/abiword-2.9.4.tar.gz/dox/ie__imp__ClarisWorks_8cpp_source.html This
    appears to have a known bug in chaining through the ETBL resources.

-   https://github.com/joshenders/appleworks_format This project is more
    notes and examples than useful code.

Documentation on the Appleworks file format does not seem to exist.
It's a very weird void, utterly bereft of information.
In the long run $19.99 for a throw-away copy of Pages is probably the
smartest solution.


However, if you're perhaps deranged, you can track down the content
through a simple brute-force analysis of the file. This is Python3
code to scrape the content out of a .CWK file.


::

  import argparse
  import struct
  import sys
  import os
  from io import open

  class CWK:
      """Analyzes a .CWK file; must be given a file opened in "rb" mode.
      """
      DSET = b"DSET"
      BOBO = b"BOBO"
      ETBL = b"ETBL"

      def __init__( self, open_file ):
          self.the_file= open_file
          self.data= open_file.read()

      def header( self ):
          self.version= self.data[0:4]
          #print( self.version[:3] )
          bobo= self.data[4:8]
          assert bobo == self.BOBO
          version_prev= self.data[8:12]
          #print( version_prev[:3] )
          return self.version

      def margins( self ):
          self.height_page= struct.unpack( ">h", self.data[30:32] )
          self.width_page= struct.unpack( ">h", self.data[32:34] )
          self.margin_1= struct.unpack( ">h", self.data[34:36] )
          self.margin_2= struct.unpack( ">h", self.data[36:38] )
          self.margin_3= struct.unpack( ">h", self.data[38:40] )
          self.margin_4= struct.unpack( ">h", self.data[40:42] )
          self.margin_5= struct.unpack( ">h", self.data[42:44] )
          self.margin_6= struct.unpack( ">h", self.data[44:46] )
          self.height_page_inner= struct.unpack( ">h", self.data[46:48] )
          self.width_page_inner= struct.unpack( ">h", self.data[48:50] )

      def dset_iter( self ):
          """First DSET appears to have content.

          This DSET parsing may not be completely correct.

          But it finds the first DSET, which includes all
          of the content except for headers and footers.

          It seems wrong to simply search for DSET; some part of the
          resource directory should point to this or provide an offset to it.
          """
          for i in range(len(self.data)-4):
              if self.data[i:i+4] == self.DSET:
                      #print( "DSET", i, hex(i) )
                      pos= i+4
                      for b in range(5): # Really? Always 5?
                          size, count= struct.unpack( ">Ih", self.data[pos:pos+6] )
                          pos += size+4
                      #print( self.data[i:pos] )
                      yield pos
      def content_iter( self, position ):
          """A given DSET may have multiple contiguous blocks of text."""
          done= False
          while not done:
              size= struct.unpack( ">I", self.data[position:position+4] )[0]
              content= self.data[position+4:position+4+size].decode("MacRoman")
              #print( "ENDING", repr(self.data[position+4+size-1]) )
              if self.data[position+4+size-1] == 0:
                  yield content[:-1]
                  done= True
                  break
              else:
                  yield content
                  position += size+4




The function invoked from the command line is this.

::

    def convert( *file_list ):
       for f in file_list:
           base, ext = os.path.splitext( f )
           new_file= base+".txt"
           print( '"Converting {0} to {1}"'.format(f,new_file) )
           with open(f,'rb') as source:
               cwk= CWK( source )
               cwk.header()
               with open(new_file,'w',encoding="MacRoman") as target:
                   position = next( cwk.dset_iter() )
                   for content in cwk.content_iter(position):
                       # print( content.encode("ASCII",errors="backslashreplace") )
                       target.write( content )
           atime, mtime = os.path.getatime(f), os.path.getmtime(f)
           os.utime( new_file, (atime,mtime) )




This is brute-force. But. It seemed to work. Buying Pages would have
been less work and probably produced better results.

This does have the advantage of producing files with the original date
stamps.  Other than that, it seems an exercise in futility because
there's so little documentation.

What's potentially cool about this is the sane way that Python3
handles bytes as input. Particularly pleasant is the way we can
transform the file-system sequence of bytes into proper Python strings
with a very simple bytes.decode().





