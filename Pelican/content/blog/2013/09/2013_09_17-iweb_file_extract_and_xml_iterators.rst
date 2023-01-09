iWeb File Extract and XML Iterators
===================================

:date: 2013-09-17 08:21
:tags: xml,#python,iWeb
:slug: 2013_09_17-iweb_file_extract_and_xml_iterators
:category: Technologies
:status: published


Once upon a time, Apple offered iBlog. Then they switched to iWeb.
Then they abandoned that market entirely.

That leaves some of us with content in iBlog as well as iWeb. Content
we'd like to work with without doing extensive cutting and pasting. Or
downloading from a web server. After all, the files are on our
computer.

The iWeb files are essentially XML, making them relatively easy to
work with. We can reduce the huge, and hugely complex iWeb XML to a
simple iterator and use a simple **for** statement to extract the
content.

[*Historical note. I wrote a Python script to convert iBlog to RST. It
worked reasonably well, all things considered. This is not the first
time I've tried to preserve old content from obsolete tools. Sigh.*]

Some tools (like SandVox) have a "extract iWeb content" mode. But
that's not what we want. We don't want to convert from iWeb to another
blog. We want to convert from iWeb to CVS or some other more useful
format so we can do some interesting processing, not simple web
presentation.

This is a note on how to read iWeb files to get at the content. And
further, how to get at XML content in the form of a simple iterator.

**Opening The Package**

Here's how to overview the package.

::

   path="~/Documents/iWeb/Domain"
   path_full= os.path.expanduser(path+".sites2")
   for filename in os.listdir(path_full):
       name, ext = os.path.splitext( filename )
       if ext.lower() in ( ".jpg", ".png", ".mov", ".m4v", ".tiff", ".gif", ".m4a", ".mpg", ".pdf" ): continue
       print( filename )




This will reveal the files; we only really care about the
"index.xml.gz" file since that has the bulk of the content.

::

   with closing( gzip.GzipFile( os.path.join(path_full,"index.xml.gz") ) ) as index:
       index_doc= xml.parse( index )
       index_root= index_doc.getroot()




This gets us the XML version of the blog.

**Finding the Pages**

We can use the following to thread through the XML. We're looking for
a particular "Domain", a "Site" and a particular blog page within that
site. The rest of the blog is mostly text. This portion of the blog is
more structured.

For some reason, the domain is "Untitled". The site is "Cruising", and
the blog page is "Travel 2012-2013". We insert these target names into
XPath search strings to locate the relevant content.

::

    search= '{{http://developer.apple.com/namespaces/bl}}domain[@{{http://developer.apple.com/namespaces/sf}}name="{0}"]'.format(domain_name)
    domain= index_root.find( search )
    mdu_uuid_tag= domain.find('{http://developer.apple.com/namespaces/bl}metadata/{http://developer.apple.com/namespaces/bl}MDUUID')
    mdu_uuid_value= mdu_uuid_tag.find('{http://developer.apple.com/namespaces/bl}string').get('{http://developer.apple.com/namespaces/sfa}string')
    domain_filename= "domain-{0}".format( mdu_uuid_value )

    search= './/{{http://developer.apple.com/namespaces/bl}}site[@{{http://developer.apple.com/namespaces/sf}}name="{0}"]'.format(site_name)
    cruising= domain.find(search)
    mdu_uuid_tag= cruising.find('{http://developer.apple.com/namespaces/bl}metadata/{http://developer.apple.com/namespaces/bl}MDUUID')
    mdu_uuid_value= mdu_uuid_tag.find('{http://developer.apple.com/namespaces/bl}string').get('{http://developer.apple.com/namespaces/sfa}string')
    site_filename= "site-{0}".format(mdu_uuid_value)

    search= '{{http://developer.apple.com/namespaces/bl}}site-blog[@{{http://developer.apple.com/namespaces/sf}}name="{0}"]'.format(site_blog_name)
    site_nodes= cruising.find('{http://developer.apple.com/namespaces/bl}site-nodes')
    travel= site_nodes.find(search)
    mdu_uuid_tag= travel.find('{http://developer.apple.com/namespaces/bl}metadata/{http://developer.apple.com/namespaces/bl}MDUUID')
    mdu_uuid_value= mdu_uuid_tag.find('{http://developer.apple.com/namespaces/bl}string').get('{http://developer.apple.com/namespaces/sfa}string')
    site_blog_filename= "site-blog-{0}".format(mdu_uuid_value)




This will allow us to iterate through the blog entries, called
"pages". Each page, it turns out, is stored in a separate XML file
with the page details and styles. A lot of styles. We have to assemble
the path from the base path, the domain, site,  site-blog and
site-page names. We'll find an ".xml.gz" file that has the individual
blog post.

::

   for site_page in travel.findall('{http://developer.apple.com/namespaces/bl}series/{http://developer.apple.com/namespaces/bl}site-page'):
       mdu_uuid_tag= site_page.find('{http://developer.apple.com/namespaces/bl}metadata/{http://developer.apple.com/namespaces/bl}MDUUID')
       mdu_uuid_value= mdu_uuid_tag.find('{http://developer.apple.com/namespaces/bl}string').get('{http://developer.apple.com/namespaces/sfa}string')
       site_page_filename= "site-page-{0}".format(mdu_uuid_value)

       blog_path= os.path.join(path_full, domain_filename, site_filename, site_blog_filename, site_page_filename )
       with closing( gzip.GzipFile( os.path.join(blog_path,site_page_filename+".xml.gz") ) ) as child:
           child_doc= xml.parse( child )
           child_root= child_doc.getroot()
       main_layer= child_root.find( '{http://developer.apple.com/namespaces/bl}site-page/{http://developer.apple.com/namespaces/bl}drawables/{http://developer.apple.com/namespaces/bl}main-layer' )




Once we have access to the page XML document, we can extract the
content. At this point, we could define a function which simply
yielded the individual site_page tags.

**Summary Iterable**

The most useful form for the pages is an iterable that yields the
date, title and content text. In this case, we're not going to
preserve the internal markup, we're just going to extract the text in
bulk.

::

       content_map = {}
       for ds in main_layer.findall( '{http://developer.apple.com/namespaces/sf}drawable-shape' ):
           style_name= ds.get('{http://developer.apple.com/namespaces/sf}name')
           if style_name is None:
               #xml.dump( ds ) # Never has any content.
               continue
           for tb in ds.findall('{http://developer.apple.com/namespaces/sf}text/{http://developer.apple.com/namespaces/sf}text-storage/{http://developer.apple.com/namespaces/sf}text-body' ):
               # Simply extract text. Markup is lost.
               content_map[style_name] = tb.itertext()
       yield content_map




This works because the text has no useful semantic markup. It's
essentially HTML formatting full of span and div tags.

Note that this could be a separate generator function, or it could be
merged into the loop that finds the site-page tags. It's unlikely we'd
ever have another source of site-page tags. But, it's very like that
we'd have another function for extracting the text, date and title
from a site-page tag. Therefore, we *should* package this as a
separate generator function.  We didn't, however. It's just a big old
function named postings_iter().

There are three relevant style names. We're not sure why these are
used, but they're completely consistent indicators of the content.

-  "generic-datefield-attributes (from archive)"
-  "generic-title-attributes (from archive)"
-  "generic-body-attributes (from archive)"


These becomes keys of the content_map mapping. The values are
iterators over the text.


**Processing The Text**


Here's an iterator that makes use of the postings_iter() function
shown above.


::

  def flatten_posting_iter( postings=postings_iter(path="~/Documents/iWeb/Domain") ):
      """Minor cleanup to the postings to parse the date and flatten out the title."""
      for content_map in postings:
          date_text= " ".join( content_map['generic-datefield-attributes (from archive)'] )
          date= datetime.datetime.strptime( date_text, "%A, %B %d, %Y" ).date()
          title= " ".join( content_map['generic-title-attributes (from archive)'] )
          body= content_map['generic-body-attributes (from archive)']
          yield date, title, body


This will parse the dates, compress the title to remove internal
markup, but otherwise leave the content untouched.


Now we can use the following kind of loop to examine each posting.

::

      flat_postings=flatten_posting_iter(postings_iter(path="~/Documents/iWeb/Domain"))
      for date, title, text_iter in sorted(flat_postings):
          for text in text_iter:
             # examine the text for important content.

We've sorted the posting into date order. Now we can process the text
elements to look for the relevant content.




In this case, we're looking for Lat/Lon coordinates, which have rather
complex (but easy to spot) regular expressions. So the "examine" part
is a series of RE matches to collect the data points we're looking
for.

We'll leave off those application-specific details. We'll leave it at
the following outline of the processing.

::

    def fact_iter( flat_postings=flatten_posting_iter(postings_iter(path="~/Documents/iWeb/Domain")) ):
       for date, title, text_iter in sorted(flat_postings):
           fact= Fact()
           for text in text_iter:
              # examine the text for important content, set attributes of fact
              if fact.complete():
                  yield fact
                  fact= Fact()




This iterates through focused data structures that include the
requested lat/lon points.

**Final Application**

The final application function that uses all of these iterators has
the following kind of structure.

::

    source= flat_postings=flatten_posting_iter(postings_iter(path="~/Documents/iWeb/Domain"))
    with open('target.csv', 'w', newlines='') as target:
       wtr= csv.DictWriter( target, Fact.heading )
       wtr.writeheader()
       for fact in fact_iter( source ):
           wtr.writerow( fact.as_dict() )




We're simply iterating through the facts and writing them to a CSV
file.

We can also simplify the last bit to this.

::

    wtr.writerows( f.as_dict() for f in fact_iter( source ) )

The iWeb XML structure, while bulky and complex, can easily be reduced
to a simple iterator. That's why I love Python.





