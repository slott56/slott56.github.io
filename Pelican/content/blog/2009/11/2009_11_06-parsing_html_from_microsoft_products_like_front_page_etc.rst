Parsing HTML from Microsoft Products (Like Front Page, etc.)
============================================================

:date: 2009-11-06 09:53
:tags: HTML,#python,beautiful soup
:slug: 2009_11_06-parsing_html_from_microsoft_products_like_front_page_etc
:category: Technologies
:status: published

Ugh. When you try to parse MS-generated HTML, you find some extension
syntax that is completely befuddling.

I've tried a few things in the past, none were particularly good.

In reading a file recently, I found that even `Beautiful
Soup <http://www.crummy.com/software/BeautifulSoup/>`__ was unable to
prettify or parse it.

The document was filled with <!--[if...]>...<![endif]--> constructs
that looked vaguely directive or comment-like, but still managed to
stump the parser.

The BeautifulSoup parser has a markupMassage parameter that applies a
sequence of regexps to the source document to cleanup things that are
baffling. Some things, however, are too complex for simple regexp's.
Specifically, these nested comment-like things were totally
confusing.

Here's what I did. I wrote a simple generator which emitted the text
that was unguarded by these things. The resulting sequence of text
blocks could be assembled into a document that BeautifulSoup could
parse.

::

    def clean_directives( page ):
        """
        Stupid Microsoft "Directive"-like comments!
        Must remove all <!--[if...]>...<![endif]--> sequences.  Which can be nested.
        Must remove all <![if...]>...<![endif]> sequences.  Which appear to be the nested version.
        """
        if_endif_pat= re.compile(  r"(\<!-*\[if .*?\]\>)|(<!\[endif\]-*\>)" )
        context= []
        start= 0
        for m in if_endif_pat.finditer( page ):
           if "[if" in m.group(0):
               if start is not None:
                   yield page[start:m.start()]
               context.append(m)
               start= None
           elif "[endif" in m.group(0):
               context.pop(-1)
               if len(context) == 0:
                   start= m.end()+1
        if start is not None:
           yield page[start:]



-----

Those if...endif (blogspot won&#39;t let me post t...
-----------------------------------------------------

Kevin H<noreply@blogger.com>

2009-11-06 10:50:52.352000-05:00

Those if...endif (blogspot won't let me post the real syntax...grrr)
things are called "conditional comments", and are used to do browser
detection and try and make up for the fact that MS couldn't be bothered
to follow web standards for a really long time.

see: http://www.quirksmode.org/css/condcom.html

Also, I'm curious, did you try using lxml.html? It's often handy when
dealing with broken pages, and sometimes it can even deal with pages
that BeautifulSoup chokes on.

I do like your solution, though.


+1 on lxml; it&#39;s the Swiss Army knife (tm) of ...
-----------------------------------------------------

Michael Watkins<noreply@blogger.com>

2009-11-06 13:18:24.816000-05:00

+1 on lxml; it's the Swiss Army knife (tm) of xml/html parsing and
munging. I'll let blogger screw up the formatting - this is pretty easy:

::

    # this strips all styles, id and class attributes
    from lxml.html import clean, fromstring, tostring
    cleaner = clean.Cleaner(page_structure=False,
    style=True,
    safe_attrs_only=True,
    comments=True,
    remove_unknown_tags=True,
    remove_tags=['span',])
    doc =
    fromstring(open('mswordexport.html').read().decode('windows-1252'))
    cleaner(doc)
    # clear certain attributes
    for el in doc.xpath('.//*'):
    el.attrib.pop('id', None)
    el.attrib.pop('class', None)
    el.attrib.pop('style', None)
    print tostring(doc).encode('utf-8')





