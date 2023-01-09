Improving the epub format -- hacking your ebooks
================================================

:date: 2017-01-31 08:00
:tags: #python,epub
:slug: 2017_01_31-improving_the_epub_format_hacking_your_ebooks
:category: Technologies
:status: published

From a reader.

    I recently purchased a copy of 'Modern Python Cookbook' but I found
    that the code listings in the epub file were indented which caused a
    problem when reading on my tablet. (I reverted to epub as the PDF
    version froze in the Bookari ereader software.)

    I unzipped the epub file, created and ran the following script to
    'unindent' the code listings then rezipped. (I also tweaked the
    epub.css file slightly.)
    Script:

::

     import os
     import codecs
     from textwrap import dedent
     from bs4 import BeautifulSoup

     ENCODING = 'utf8'

     def dedent_page(filepath):
         soup = load_soup(filepath)
         code = soup.findAll('pre')
         for c in code:
             # Dedent twice to cater for 'blank' lines with spaces.
             c.string = dedent(dedent(c.text))
         save_soup(filepath, unicode(soup))

     def load_soup(filepath):
         with codecs.open(filepath, encoding = ENCODING) as f:
             return BeautifulSoup(f)

     def save_soup(filepath, soup):
         with codecs.open(filepath, mode = 'w', encoding = ENCODING) as f:
             f.write(unicode(soup))

     if __name__ == "__main__":

         FOLDER = r'ebook\OEBPS'

         html_files = [fn for fn in os.listdir(FOLDER) if fn.endswith('.html')]
         total_files = len(html_files)
         for i, file_name in enumerate(html_files):
             print 'Processing file %s (%s/%s)' % (file_name, i + 1, total_files)
             dedent_page(os.path.join(FOLDER, file_name))

