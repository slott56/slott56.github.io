Code Kata : Parse USPS ZIP3 table
=================================

:date: 2009-09-23 20:49
:tags: code-kata
:slug: 2009_09_23-code_kata_parse_usps_zip3_table
:category: Technologies
:status: published

**Situation**

The USPS ZIP codes have a multi-part structure. The first three
digits are a prefix that defines a sectional center facility.

The USPS table L005 3-Digit ZIP Code Prefix Groups—SCF Sortation
maps clusters of ZIP3 prefixes to Facility and State codes. The
following URL has this table.

http://pe.usps.gov/text/DMM300/L005.htm

**Your Job**

Your job is to write a library module that does two things:

1.  Read and parses this table.

2.  Support ZIP-code lookup (ZIP3, ZIP, ZIP+4) to return SCF and
    State information.

**Some Notes**

Finding and parsing the table is often done in Python with
components like `Beautiful
Soup <http://www.crummy.com/software/BeautifulSoup/>`__.
Equivalents aren't available in all languages. You might want to
copy and paste this table into a spreadsheet application, and save
it as a CSV file, which is much easier to work with than HTML.

There's a regular format to the ZIP3 ranges that makes parsing
them relatively simple.

The SCF names, however, have two different formats. Some have
names that begin with SCF. Others have names that don't begin with
SCF. Be careful to handle each version correctly.



-----

Life Insurance is the best option to scour our lif...
-----------------------------------------------------

surf accommodations<noreply@blogger.com>

2011-04-07 01:59:26.907000-04:00

Life Insurance is the best option to scour our life.So in this blog `US
zip codes <http://www.zipcodeinsights.com/>`__ many info and good
content.





