Making PDF's with and without XSL FO (Revised)
==============================================

:date: 2006-03-20 15:41
:tags: books,docbook,xml
:slug: 2006_03_20-making_pdfs_with_and_without_xsl_fo_revised
:category: Technologies
:status: published





I've been using the Apache FOP http://xmlgraphics.apache.org/fop/
to transform XSL:FO into PDF's.  FOP works well enough for some DocBook
processing, but it can't handle really complex stuff gracefully.  




Can we also use this XSL:FO technology
for producing PDF form letters as part of a Customer Relationship Management
solution?  Is FOP
suitable?



XSL:FO Products
---------------



A very complete list is
available at XMLSoftware.com http://www.xmlsoftware.com/xslfo.html.



The core list of tools include the following:

-   Adobe seems to own this space; they offer
    XSL:FO processing tools in a wide variety of forms.  Further, they have an
    on-line service http://createpdf.adobe.com/
    that can convert many things into PDF's.

-   ReportLab http://www.reportlab.com/ has an
    engine that will create PDF's from source files.  They also have an open source
    toolkit.

-   Antenna House http://www.antennahouse.com/ offers the
    **XSL Formatter**  product that seems to be widely
    regarded.

-   RenderX http://www.renderx.com/ offers the **XEP**
    product that does this job well.

-   Chive http://www.chive.com/ has their Apoc product, which is a .Net
    solution.

-   Ecrion http://www.ecrion.com/ also has a
    .NET product.

-   Alt-soft http://www.alt-soft.com/ has a beta
    product for xml2pdf conversion.

-   Stylus Studio http://www.stylusstudio.com/xsl_fo_processing.html has a tool that edits XSL:FO and runs
    Apache FOP for you.

-   The `W3Schools <http://www.w3schools.com>`_  site lists two more tools http://www.w3schools.com/xslfo/xslfo_software.asp:
    Xinc http://www.lunasil.com/ and
    Scriptura http://www.inventivedesigners.com/scriptura/what.html.   Lunasil looks like a very small
    company; Xinc appears to be their only product.  Scriptura's description sounds
    like Adobe's -- it's tough to go head-to-head with the
    leader.



A nice comparison between the
market-leaders **XEP**  and **XSL Formatter**  is available at XSLT.com http://www.xslt.com/html/xsl-list/2002-04/msg00227.html.



Beyond these tools, Altova has a product http://www.altova.com/dev_portal_xslfo.html%22%20target=%22NewWindow
to help design the XSL that controls document production.




Finally, a partial solution is iText
http://www.lowagie.com/iText, which is a set of Java libraries that
create PDF's.  



Personally, I would
prefer to use something like ReportLab Toolkit http://www.reportlab.org/, but the
customer will likely balk at anything non-Java.  Indeed, between Python, Cheetah
and ReportLab, I think I'd be done with a solution, rather than still studying
the problem.



**Additional Thoughts**.  The real question, however, is why
XSL:FO?  There are lots of products that produce PDF files.  We have to look at
the real purpose behind the task.  For converting DocBook files, the stylesheets
and XSL:FO components fit into a very nice processing pipeline that is driven by
Xalan.



However, in the case of Customer
Relationship Management, we are using an application to do "mail-merge"
processing, combining a template letter with details extracted from the
database.  We can imagine two families of architectures for
this:



Minimal Markup.  In this case,
either no markup or a home-brewed minimal markup language are used.  This has
the advantage of minimizing knowledge of XSL:FO.

1.  Custom software, using iText or similar, that
    has the letter template encoded in the application.  This is simple, but quite
    inflexible.

2.  Custom software, using iText or similar, that
    has the letter template in some home-brewed markup language.  It reads the
    template and the data, merges the data in and produces PDF output.  In this
    case, much of the formatting information is either implied or encoded in the
    home-brewed markup language.



Existing Markup.  In this case, existing markup languages are leveraged.

1.  Template processing.  Use an existing template
    engine (Velocity, Cheetah or similar) that uses a letter template in a
    meta-markup language.  This produces XSL:FO output that can then be processed by
    any of the XSL:FO tools.

2.  XSL processing.  Use Xalan to transform the
    source details into individual letters using an XSL template for the letter. 
    This produces XSL:FO output that can then be processed by any of the XSL:FO
    tools.



Adobe has products that handle
all of this, but they can be expensive.  The Minimal Markup solutions involve
some programming, but it is the kind of inflexible programming that makes every
minor change to the template a huge cost and expense.  The Existing Markup
solutions involve considerable learning, but also mean that letter changes are
handled by someone who knows the template language and the XSL:FO markup
language.  



The knowledge of XSL:FO can
be minimized with clever use of the Cheetah or Velocity templates.





















