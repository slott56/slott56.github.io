Another HTML Cleanup
====================

:date: 2009-11-10 06:28
:tags: HTML,#python,beautiful soup
:slug: 2009_11_10-another_html_cleanup
:category: Technologies
:status: published

Browsers are required to skip over bad HTML and render something.

Consequently, many web sites have significant HTML errors that don't
show up until you try to scrape their content.

`Beautiful Soup <http://www.crummy.com/software/BeautifulSoup/>`__
has a handy hook for doing `markup
massage <http://www.crummy.com/software/BeautifulSoup/documentation.html#Sanitizing%20Bad%20Data%20with%20Regexps>`__
prior to parsing. This is a way of fixing site-specific bugs when
necessary.

Here's a two-part massage I wrote recently that corrects two common
(and show-stopping) HTML issues with quoted attributes values in a
tag.

::

  # Fix style="background-image:url("url")"
  background_image = re.compile(r'background-image:url\("([^"]+)"\)')
  def fix_background_image( match ):
     return 'background-image:url(&quote;%s&quote;)' % ( match.group(1) )

  # Fix src="url name="name""
  bad_img = re.compile( r'src="([^ ]+) name="([^"]+)""' )
  def fix_bad_img( match ):
     return 'src="%s" name="%s"' % ( match.group(1), match.group(2) )

  fix_style_quotes = [
     (background_image, fix_background_image),
     (bad_img, fix_bad_img),
  ]

The "fix_style_quotes" sequence is provided to the BeautifulSoup
contructor as the markupMassage value.






