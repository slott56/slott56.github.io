A Simple Graphic Learning Environment - Part 2
==============================================

:date: 2007-03-31 02:32
:tags: architecture,design,UX,UI,GUI,TUI
:slug: 2007_03_31-a_simple_graphic_learning_environment_part_2
:category: Architecture & Design
:status: published





Here's a simple graphic application which is
built on the graphicApp.py framework.  This isn't a beginner's hello world. 
This is the final project kind of program, and only for a student with some
trigonometry background.  The basic trig isn't too complex, but would require
rather detailed documentation to motivate the math behind the
solution.



This does show shading, text,
masks, filling and line drawing. 




**Overheads.** 



Here
are the essential module overheads.



::

    #!/usr/bin/env python
    """venn.py Application
    
    Draw the eight canonical 2-set Venn diagrams.
    
    This builds on basic "sketchpad" style application, which has general
    application framework surrounding a simple "drawImage" method.
    """
    
    from graphicApp import *
    import math





**Venn class, part 1.** 



Here's the beginning of the
drawing application class, it's a subclass of
graphicApp.GraphicApplication.



::

    class Venn( GraphicApplication ):
        """A Graphic Application which displays the canonical
        2-set Venn Diagrams.
    
        The control area has a combo box added to select which
        of the 8 diagrams to draw.
    
        The Pixmap drawing routine decodes the selected diagram
        and then draws the expected Venn diagram.
        """
    
        def __init__( self ):
            self.imageToDraw= 2
            GraphicApplication.__init__( self )
    
        def fileName( self ):
            return "venn-%d.png" % ( self.imageToDraw, )
    
        def selectImage( self, widget, data ):
            """Handle the image selection event on the Image selection button."""
            print "selectImage", widget.get_active()
            # Set the image selector
            self.imageToDraw= widget.get_active()
            # Invalidate the drawable's region to force a refresh
            self.graphic_area.queue_draw()
    
        def build_application_controls( self, controls ):
            self.b_choices= gtk.combo_box_new_text()
            self.b_choices.append_text( "Set()" )
            self.b_choices.append_text( "S1-S2" )
            self.b_choices.append_text( "S1&S2;" )
            self.b_choices.append_text( "S1" )
            self.b_choices.append_text( "S2-S1" )
            self.b_choices.append_text( "S1^S2" )
            self.b_choices.append_text( "S2" )
            self.b_choices.append_text( "S1|S2" )
            self.b_choices.set_property( "active", self.imageToDraw )
            self.b_choices.connect("changed", self.selectImage, None)
            controls.add(self.b_choices)





**Venn Class, Part 2.** 



Here's the application's
drawImage
method, which does the actual work of the
application.



::

    def drawImage( self, venn, widget ):
            """Venn Diagram 2: s1&s2;"""
            print "Drawing", self.imageToDraw
            # Fill pattern is diagonal lines
            stripe_bits= """\x83\x07\x0e\x1c\x38\x70\xe0\xc1"""
            stripe= gtk.gdk.bitmap_create_from_data(None, stripe_bits, 8, 8)
            # Blank pattern is solid
            solid_bits= """\xff\xff\xff\xff\xff\xff\xff\xff"""
            solid= gtk.gdk.bitmap_create_from_data(None, solid_bits, 8, 8)
            # Create our graphic contexts
            colorMap= venn.get_colormap()
            width2= venn.new_gc(
                line_width=2,
                background=colorMap.alloc_color("white"),
                foreground=colorMap.alloc_color("black"),
                )
            width1= venn.new_gc(
                line_width=1,
                background=colorMap.alloc_color("white"),
                foreground=colorMap.alloc_color("blue"),
                )
            fill= venn.new_gc(
                line_width=2,
                fill=gtk.gdk.STIPPLED,
                stipple= stripe,
                foreground=colorMap.alloc_color("dark slate grey"),
                )
            blank= venn.new_gc(
                line_width=2,
                fill=gtk.gdk.STIPPLED,
                stipple= solid,
                foreground=colorMap.alloc_color("white"),
                )
            
            # Compute the coordinates for our picture
            print "get_size", venn.get_size()
            width, height= venn.get_size()
    
            # Radius, r, is (h-48)/2; diameter is 2*r
            r= (height-48)/2
            
            # Left Center is (24+r, 24+r)
            print "Left Center", 24+r, 24+r
            # Left rectangle: x=24, width=2*r, y=24, height=2*r
            left_x, left_y = 24, 24
            
            # Spaing between circles, s, is r*5/4 (between 0 and 2r)
            s= r*5/4
            
            # Right Center is (24+r+s, 24+r)
            print "Right Center", 24+r+s, 24+r
            # Right rectangle: x=24+s, width=2*r, y=24, height=2*r
            right_x, right_y = 24+s, 24
            
            # x intercept is 24+r+s/2
            # y intercept is (24+r +/- r*sin( acos( (s/2)/r ) )
            # Fill rectangle: x = 24+r+s/2, width r-s/2, y = y+yd, height 2*yd
            x= 24+r+s/2
            yd= int(r*math.sin( math.acos( s/(2.0*r) ) ))
            y= 24+r
            print "Top Intersection", x, y+yd
            print "Bottom Intsection", x, y-yd
    
            # The angles of the arcs are from +acos(s/2/r) to -acos(s/2/r).        
            a= int(360*64*math.acos( s/(2.0*r) )/(2*math.pi))
            #print "radians", math.acos( s/(2.0*r) ), "64ths", a, "degrees", a/64.0
                    
            # Blank and Outline the Venn universe rectangle
            # Leave a 16-pixel edge border.
            venn.draw_rectangle( blank, True, 8, 8, width-16, height-16 )
            venn.draw_rectangle( width2, False, 8, 8, width-16, height-16 )
    
            # Now, we need to accumulate the selected regions.
            fill1= (self.imageToDraw & 1) != 0
            fill2= (self.imageToDraw & 2) != 0
            fill4= (self.imageToDraw & 4) != 0
            #print "Fills", fill1, fill2, fill4
    
            # NOTE that this is relatively simple looking, but
            # inefficient, since any combination with region 2 will lead to filling,
            # blanking and filling again.
            if fill1:
                # Left circle minus the center (region 1)
                # Shade the left circle
                venn.draw_arc( fill, True, left_x, left_y, 2*r, 2*r, 0, 64*360 )
                # Lay the cipped left arc on top of it
                blank.set_clip_rectangle( gtk.gdk.Rectangle(x, y-yd, r-s/2, 2*yd) )
                venn.draw_arc( blank, True, left_x, left_y, 2*r, 2*r, -a, 2*a )
                # Lay the clipped right arc on top of it
                blank.set_clip_rectangle( gtk.gdk.Rectangle(x-r+s/2, y-yd, r-s/2, 2*yd) )
                venn.draw_arc( blank, True, right_x, right_y, 2*r, 2*r, -a+180*64, 2*a )
    
            if fill4:
                # Right circle minus the center (region 4)
                # Shade the right circle
                venn.draw_arc( fill, True, right_x, right_y, 2*r, 2*r, 0, 64*360 )
                # Lay the cipped left arc on top of it
                blank.set_clip_rectangle( gtk.gdk.Rectangle(x, y-yd, r-s/2, 2*yd) )
                venn.draw_arc( blank, True, left_x, left_y, 2*r, 2*r, -a, 2*a )
                # Lay the clipped right arc on top of it
                blank.set_clip_rectangle( gtk.gdk.Rectangle(x-r+s/2, y-yd, r-s/2, 2*yd) )
                venn.draw_arc( blank, True, right_x, right_y, 2*r, 2*r, -a+180*64, 2*a )
    
            if fill2:
                # Center (region 2)
                # Left Arc, clipped by the right-side rectangle.
                fill.set_clip_rectangle( gtk.gdk.Rectangle(x, y-yd, r-s/2, 2*yd) )
                venn.draw_arc( fill, True, left_x, left_y, 2*r, 2*r, -a, 2*a )
                # Right Arc, clipped by the left-sie rectangle
                fill.set_clip_rectangle( gtk.gdk.Rectangle(x-r+s/2, y-yd, r-s/2, 2*yd) )
                venn.draw_arc( fill, True, right_x, right_y, 2*r, 2*r, -a+180*64, 2*a )
            
            # Outline the circles
            venn.draw_arc( width2, False, left_x, left_y, 2*r, 2*r, 0, 64*360 )
            venn.draw_arc( width2, False, right_x, right_y, 2*r, 2*r, 0, 64*360 )
    
            # Add set labels "S1" and "S2".
            # Create a Pango Context for applying text labels to the diagram
            # A 24-point font would look good.
            self.pangoContext= widget.get_pango_context()
            fontAttrList= pango.AttrList()
            fontAttrList.change( pango.AttrSize( 24*1000, 0, 2 ) )
            # Create Pango.Layouts using pangoContext.
            label_s1= pango.Layout( self.pangoContext )
            label_s1.set_text( "S1" )
            label_s1.set_attributes( fontAttrList )
            label_s2= pango.Layout( self.pangoContext )
            label_s2.set_text( "S2" )
            label_s2.set_attributes( fontAttrList )
    
            # Get ink size and logical size of label s1
            ex1_ink, ex1_log = label_s1.get_pixel_extents()
            log_x, log_y, width, height= ex1_log
            # Position the label centered half-way across and 3/5 of the way to the top
            lftLab_x, lftLab_y = left_x + r-width/2, left_y+3*r/5 - height/2
            venn.draw_layout( width2, lftLab_x, lftLab_y, label_s1 )
    
            # Get ink size and logical size of label s2
            ex2_ink, ex2_log = label_s2.get_pixel_extents()
            log_x, log_y, width, height= ex1_log
            rgtLab_x, rgtLab_y = right_x + r-width/2, right_y+3*r/5 - height/2
            # Position the label centered half-way across and 3/5 of the way to the top
            venn.draw_layout( width2, rgtLab_x, rgtLab_y, label_s2 )
    
            # Debugging rectangles
            #venn.draw_rectangle( width1, False, x, y-yd, r-s/2, 2*yd )
            #venn.draw_rectangle( width1, False, x-r+s/2, y-yd, r-s/2, 2*yd )





**Main program switch.** 



::

    if __name__ == "__main__":
        vennDiagram = Venn()
        vennDiagram.main()





In addition to the TODO's in part 1, I
have another complaint.  I don't really like separating the pixmap from the
widget which displays the pixmap.  It seems a little silly to do most of the
work in the pixmap, but still use the widget to get the Pango
context.



When I get some more time,
I'll look at cleaning it up and putting together some course material oriented
around the pedagogical framework I used in `Building Skills in Python <http://www.itmaybeahack.com/homepage/books/python.html>`_ .








