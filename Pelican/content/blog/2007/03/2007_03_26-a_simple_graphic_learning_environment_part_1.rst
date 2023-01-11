A Simple Graphic Learning Environment - Part 1
==============================================

:date: 2007-03-26 16:31
:tags: architecture,design,UX,UI,GUI,TUI
:slug: 2007_03_26-a_simple_graphic_learning_environment_part_1
:category: Architecture & Design
:status: published





**Background.** 



The
suggested environment for learning to program using graphics instead of text was
`LiveWires <http://www.livewires.org.uk/python/index.html>`_ .  This includes a curriculum and
associated product, making it a tidy
package.



There are a number of
alternatives, however.

-   Python includes `tkinter <http://www.pythonware.com/library/tkinter/introduction/>`_ , `section 20.1 <http://docs.python.org/lib/module-Tkinter.html>`_  of the Python Library Reference, v2.5.

-   Python includes turtle, `section 20.4 <http://docs.python.org/lib/module-turtle.html>`_  of the Python Library Reference. v2.5.

-   `Section 20.5 <http://docs.python.org/lib/other-gui-packages.html>`_  of the Python Library reference
    lists 7 other toolkits -- most of which are for building GUI applications, and
    aren't terribly pedagogical.

-   OLPC's Sugar
    is based on GTK, and pyGTK.  For pedagogical purposes, this interests me. 
    Recently ("`Sugar, GTK and OLPC <{filename}/blog/2007/03/2007_03_13-sugar_gtk_and_olpc.rst>`_ ") I put together the PyGTK
    environment so I could look at updating my `Building Skills In Python <http://www.itmaybeahack.com/homepage/books/python.html>`_  book to align it with
    Dr. Ceder's approach to programming.  Also, I need to align the book with `CP4E <http://www.python.org/cp4e/>`_ .



Here's
some little scraps of code which might amount to a livewires-like environment
which is strictly PyGTK in
implementation.



**graphicApp.py** 



The
foundation is a small hierarchy of classes which embody a non-document graphic
application with an extensible control panel for simple controls.  By default, a
simple Save As... and Quit button can be
provided.



**Part 1 - Python Basics** 



::

    #!/usr/bin/env python
    """graphicApp module.
    
    Define a simple pyGTK Graphic Application with a simple
    user interface.
    
    This application is built in two layers:
    
    TinyApplication is a small pyGTK no-document application.
    It handles the basic GTK application initialization, run, and
    termination.  This superclass provides a build_main_area()
    method which must be overridden by a subclass.
    
    GraphicApplication is a subclass of TinyApplication which overrides
    build_main_area() to create an area with a control area and a graphic
    area.  The control area is seeded with a save button and quit button.
    
    The GraphicApplication provides two stub methods: build_application_controls()
    and drawImage().  An application will override these two methods to
    add controls and draw an image based on the control setting.
    
    This is usually imported with a
        from graphicApp import *
    
    So that the full gtk, gobject and pango libraries are brought in, also.
    
    A more sophisticated application would involve a document, and the
    main application window would be a document window, with a menu bar in addition
    to any other buttons and controls.
    """
    
    import pygtk
    pygtk.require('2.0') # Selects version library.
    import gtk
    print "Check for version 2.6:", gtk.check_version(2,6,3) or "V2.6.3 found"
    import gobject
    print "GLIB Version:", gobject.glib_version
    import pango
    
    import os
    
    _version_ = "0.2"





**Part 2 - TinyApplication** 



This class handles
the minimum GTK handshake to start and stop cleanly.  Subclasses will override
methods to extend this class into something more
useful.



::

    class TinyApplication( object ):
        """A simple single-window application superclass.
        A subclass must override the build_main_area() function
        to build the main window content.
    
        This parent application will provide
        self.window, which is the top-level window for the application.
        self.status, which is a status bar including a grow icon.
        """
        
        def delete_event(self, widget, event, data=None):
            """Handle delete of the top-level window.
            Override this to provide a confirm-to-quit dialog box.
            """
            # If you return FALSE in the "delete_event" signal handler,
            # GTK will emit the "destroy" signal. Returning TRUE means
            # you don't want the window to be destroyed.
            # This is useful for popping up 'are you sure you want to quit?'
            # type dialogs.
            print "delete-event signal occurred"
    
            # Change FALSE to TRUE and the main window will not be destroyed
            # with a "delete_event".
            return False
    
        def destroy(self, widget, data=None):
            """Handle destroy of the top-level window."""
            print "destroy-event signal occurred"
            gtk.main_quit()
    
        def __init__(self):
            """Build the top-level single-window application.
            This will call the subclass build_main_area() to
            construct the interesting bits of the application."""
            # create a new top-level window
            self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        
            # When the window is given the "delete_event" signal (this is given
            # by the window manager, usually by the "close" option, or on the
            # titlebar), we ask it to call the delete_event () function
            # as defined above. The data passed to the callback
            # function is NULL and is ignored in the callback function.
            self.window.connect("delete_event", self.delete_event)
        
            # Here we connect the "destroy" event to a signal handler.  
            # This event occurs when we call gtk_widget_destroy() on the window,
            # or if we return FALSE in the "delete_event" callback.
            self.window.connect("destroy", self.destroy)
        
            # Sets the border width of the window.
            self.window.set_border_width(2)
    
            # Build the main working area of the window.
            self.main_area= self.build_main_area()
    
            # Create a Statusbar to hold messages.
            self.status= gtk.Statusbar()
            self.status.set_has_resize_grip( True )
    
            # Create a VBox to hold the controls and the StatusBar
            self.app_box= gtk.VBox()
            self.app_box.add( self.main_area )
            self.app_box.add( self.status )
            
            # This packs the box into the window (a GTK container).
            self.window.add(self.app_box)
        
            # Show the status bar, the main control panel and the window
            self.status.show()
            self.app_box.show()
            self.window.show()
    
        def main(self):
            """Run the application."""
            # All PyGTK applications must have a gtk.main(). Control ends here
            # and waits for an event to occur (like a key press or mouse event).
            gtk.main()
    
        def hello_world( self, widget, param ):
            """A function to demonstrate that the application works."""
            ctx= self.status.get_context_id("hello world")
            print "hello: %r" % ( param, )
            self.status.pop(ctx)
            self.status.push(ctx,"hello: %r" % ( param, ) )
    
        def build_main_area( self ):
            """Build the main display area.
    
            A subclass will override this to build a more interesting
            main area.
            """
                
            controls= gtk.HButtonBox()
            controls.set_border_width(16)
            
            self.b_hello = gtk.Button("Hello")
            self.b_quit= gtk.Button("Quit",gtk.STOCK_QUIT)
            
            # When the button receives the "clicked" signal, it will call the
            # method hello_world() passing it None as its argument.  
            self.b_hello.connect("clicked", self.hello_world, "world")
        
            # This will cause the window to be destroyed by calling
            # gtk_widget_destroy(window) when "clicked".  Again, the destroy
            # signal could come from here, or the window manager.
            self.b_quit.connect_object("clicked", gtk.Widget.destroy, self.window)
    
            controls.add(self.b_hello)
            controls.add(self.b_quit)
        
            # The final step is to display this newly created widget.
            self.b_hello.show()
            self.b_quit.show()
            controls.show()
            return controls





**Part 3 - GraphicApplication** 



This class adds
structure for a graphic application with a simple control panel.  Specifically,
it narrows the final application down to providing a method that replaces
drawImage.



::

    class GraphicApplication( TinyApplication ):
        """A Tiny Application which displays a control panel
        and a graphic area.
    
        The control area has a save and quit
        button.  A subclass application can add controls
        to this area to adjust the image which is displayed.
    
        The save button will save the image as a PNG file.
        The quit button will quit.
    
        The graphic area is a simple DrawingArea into which
        a pixmap is drawn.  A subclass application will
        redefine the method for drawing this pixmap.
        """
    
        def fileName( self ):
            return "image.png"
    
        def fileFormat( self ):
            return "png"
    
        def defaultSize( self ):
            return 414, 256
        
        def save(self, widget, data=None):
            """Handle the clicked event on the Save As button."""
            ctx= self.status.get_context_id("save")
            self.status.pop(ctx)
            # show a file chooser
            # TODO: include a selector for file formats handled
            formats= [ f for f in gtk.gdk.pixbuf_get_formats() if f['is_writable'] ]
            for f in formats:
                print '  ', f['name'], f['extensions'][0]
            self.chooser= gtk.FileChooserDialog(
                title="Save the Drawing",
                parent=None,
                action=gtk.FILE_CHOOSER_ACTION_SAVE,
                buttons=( gtk.STOCK_SAVE, gtk.RESPONSE_ACCEPT,
                          gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL), )
            # TODO: add keyboard accelerators so Enter key works.
            self.chooser.set_current_name( self.fileName() )
            #self.chooser.set_do_overwrite_confirmation(True) # 2.8 only
            event= self.chooser.run()
            if event == gtk.RESPONSE_ACCEPT:
                name= self.chooser.get_filename()
                # TODO: Prior to 2.8, must manually Prevent Overwrite
                # If overwrite, need to confirm.
                #   If overwrite and confirmation == no, continue a loop
                # Create a Pixbuf from the drawing area Pixmap
                width, height= self.drawing.get_size()
                pb= gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, width, height)
                pb.get_from_drawable( self.drawing, self.drawing.get_colormap(),
                    0, 0, 0, 0, width, height )
                # Save the resulting Pixbuf as a PNG
                pb.save(name, self.fileFormat() )
                self.status.push(ctx,"Saved %s" % name)
            else:
                self.status.push(ctx,"File not saved.")
            self.chooser.destroy()
    
        def build_application_controls( self, controls ):
            pass
        
        def build_control_area( self ):
            """Build the top control area and the two default
            buttons (save and quit).
    
            Call build_application_controls to build
            any additional controls.
    
            A subclass would override build_application_controls
            to build application-specific buttons or fields.
            """
            # Create a ButtonBox to hold the buttons.
            controls= gtk.HButtonBox()
            controls.set_border_width(8)
    
            self.b_save = gtk.Button("Save As...", gtk.STOCK_SAVE_AS)
            self.b_quit= gtk.Button("Quit",gtk.STOCK_QUIT)
        
            # When the button receives the "clicked" signal, it will call the
            # method save() passing it None as its argument.  
            self.b_save.connect("clicked", self.save, None)
        
            # This will cause the window to be destroyed by calling
            # gtk_widget_destroy(window) when "clicked".  Again, the destroy
            # signal could come from here, or the window manager.
            self.b_quit.connect_object("clicked", gtk.Widget.destroy, self.window)
    
            # Add any additional controls, if necessary.
            self.build_application_controls( controls )
    
            # Pack the buttons into the box
            controls.add(self.b_save)
            controls.add(self.b_quit)
        
            # The final step is to display this newly created control area widget.
            for b in controls.get_children():
                b.show()
            controls.show()
            return controls
    
        def drawImage( self, pixmap, widget ):
            # Create a Pango Context for applying text labels to the diagram
            pangoContext= widget.get_pango_context()
            graphicContext= widget.get_style().fg_gc[gtk.STATE_NORMAL]
            fontAttrList= pango.AttrList()
            fontAttrList.change( pango.AttrSize( 24*1000, 0, 2 ) )
            label_s1= pango.Layout( pangoContext )
            label_s1.set_text( "Hello World" )
            page_width, page_height= pixmap.get_size()
            ex1_ink, ex1_log = label_s1.get_pixel_extents()
            x, y, label_width, label_height= ex1_log
            pixmap.draw_layout( graphicContext,
                page_width/2-label_width/2, page_height*2/5-label_height/2,
                label_s1 )
            
        def expose( self, widget, event, data=None ):
            """Connected to the expose-event for the graphic area.
            This will refresh the image by first creating the
            necessary Pixmap (self.drawing) and then drawing
            that Pixmap into the DrawingArea (widget).
            """
            # What are we drawing?
            x , y, width, height = event.area
            # Create the selected image
            self.drawImage( self.drawing, widget )
            # Apply to the Image widget
            widget.window.draw_drawable(
                widget.get_style().fg_gc[gtk.STATE_NORMAL],
                self.drawing, x, y, x, y, width, height)
            return False # We're not done; the Event can propagate
    
        def configure( self, widget, event, data ):
            """Connected to the configure-event for the graphic area.
            This will create the initial Pixmap, and set the default
            size for the DrawingArea.  It will also blank the Pixmap
            to assure that it has some initial content.
            """
            # Create an empty drawing that we will insert into the graphic_area
            width, height = self.defaultSize()
            self.drawing= gtk.gdk.Pixmap(widget.window, width, height)
            self.drawing.draw_rectangle(
                    widget.get_style().white_gc,
                    True, 0, 0, width, height)
            # Stake out the preferred size, since the drawing area has
            # no internal elements to request screen space.
            widget.set_property( "height-request", height )
            widget.set_property( "width-request", width ) # 1x1.6 ratio
            return False # We're not done; the Event can propagate
        
        def build_graphic_area( self ):
            """Build the Drawing Area, connect two events.
            The configure-event creates the initial, empty Pixmap, and
            establishes the default size.
            The expose-event then creates the Pixmap, and draws it into
            the graphic area widget.
            """
            graphic_area= gtk.DrawingArea()
            graphic_area.connect( "configure-event", self.configure, None )
            graphic_area.connect( "expose-event", self.expose, None )
            graphic_area.show()
            return graphic_area
            
        def build_main_area(self):
            """Build the graphic application panel."""
    
            # Create the main graphics + buttons area
            area= gtk.VBox()
            #area.set_property( "style", "draw-border", 1 ) # pyGTK 2.8
    
            # Create the content of the main area
            self.control_area= self.build_control_area()
            self.graphic_area= self.build_graphic_area()
            
            sep= gtk.HSeparator()
            sep.set_property("height-request",16)
            sep.show()
    
            area.add( self.control_area )
            area.add( sep )
            area.add( self.graphic_area )
            area.show()
    
            return area





**Part 4 - The Main Switch** 



This main switch is
essential, and shows how the final application is self-contained.  The main loop
is part of the application's main method.  I'm not a fan of having the main loop
outside the application class definition.



::

    if __name__ == "__main__":
        helloWorld = GraphicApplication()
        helloWorld.main()





**Some Design Issues** 



This is, essentially, a TODO
list.



First, I don't like doing so much
in __init__. 
While the pyGTK examples make heavy use of
__init__, and I
preserved that approach, I'm not generally happy with it.  Too many things
happen automagically.  In other GUI's, I have had an explicit three step build,
add, show.  However, those were big and complex applications, and I need to
split the difference between small applications for learning and large
expensive-to-maintain
applications.



Second, I'm unhappy with
the exposed sophistication of Pango.  Typesetting, while complex in reality,
seems simple, and should be simple for newbies.  A wrapper for Pango with a lot
of defaults and assumptions would be
helpful.



Third, I need to fold in the
Application-Document-Window abstractions.  This design pattern is central to the
most usable GUI's.  Apple describes it nicely in "`Windows Considerations <http://developer.apple.com/documentation/MacOSX/Conceptual/OSX_Technology_Overview/PortingTips/chapter_7_section_3.html>`_ ".   You can read some
interesting stuff, followed by pointless invective in Tom Yager's "`Mac sense and nonsense <http://www.infoworld.com/article/07/03/14/12OPcurve_1.html>`_ " in `InfoWorld <http://www.infoworld.com/>`_ .



The
old Think/Lightspeed C libraries had some great designs for this essential
application structure.  But that was long ago and far away; some of those design
patterns don't seem to be well preserved.  Or perhaps I'm just not looking in
all the right places.  Rather than find good stuff on Application, Document and
Window, I can only find things on Single Document Interface (SDI), which is a
Micro$oft-ism.








