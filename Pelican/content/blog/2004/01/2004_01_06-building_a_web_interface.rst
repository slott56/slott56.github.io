Building a Web Interface
========================

:date: 2004-01-06 11:01
:tags: architecture,design,UX,UI,GUI,TUI
:slug: 2004_01_06-building_a_web_interface
:category: Architecture & Design
:status: published





..

    I would like to build a web browser interface that has capabilities like a spreadsheet.
    
    At the same time, would like to use a tool like OpenROAD from Ingres/CA to do this.
    
    It seems that XUL is the way to go but the entire Mozilla thing is unstable.
    
    Perhaphs [there are] other alternatives ?



There are always
alternatives.  There are four processing locations in the architecture you're
describing:



1)  On the desktop via
    a separate application or component that a user downloads.  For example, in
    Windows, an ActiveX control can lodge on the desktop, interact with Excel (if
    present) and be a spreadsheet, not
    spreadsheet-like.



2)  In the
    browser as a Java applet.  Some other plugins are possible, also.  For non-Java
    plugins, the users must download and install the plugin, then your application
    will be handled by the plugin.  For instance, the Tcl plugin can do this by
    creating a Tk interface from the
    plugin.
    


3)  In the browser as a
    complex form with Javascript programming to handle all of the spreadsheet-like
    capabilities.  This implies a lot of Javascript and little
    persistence.
    


4)  In the web server
    as a complex form.  Each interaction will take a while, since it will all be
    done by the web server, but every step is now
    persistent.



None of these depend
on Mozilla's XUL.



The issue, BTW,
is not the stability of Mozilla -- it is a better-engineered piece of software
than most.  The issue is the adoption of XUL; if Explorer doesn't adopt it, then
it will languish in a nook somewhere with all the other great ideas that never
took off.








