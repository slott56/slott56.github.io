The Web Mart Design Pattern.
============================

:date: 2007-05-03 13:28
:tags: web mart,Django,data model
:slug: 2007_05_03-the_web_mart_design_pattern
:category: News
:status: published





The **Web Mart**  design pattern identifies three aspects
to a piece of web content:

-   The **Core Concept**  - the "fact" that we will
    present.

-   The **Access Dimensions**  - objects that identify a concept
    or support navigation to the concept.

-   The **Details** - objects that provide details in support of a concept.



There are a number of things
to like about this.  First, and most important, is the close parallelism between
this design pattern and the **Star Schema**  (or
**Dimensional Model**  or
**Data Mart** ) design pattern.   I'm a big fan of the
dimensional model, and presented an implementation of the dimensional design
pattern at `PyCon 2007 <{filename}/blog/2007/02/2007_02_26-pycon_2007_revised.rst>`_ .  The dimensional model surrounds a
fact with independent dimensions of that fact.  The dimensions serve as
navigation and aggregation of the fact; the fact is the most granular detail in
the data structure.



What's important is
the recognition that navigation involves
**independent dimensions** . Many people attempt to force-fit
independent dimensions into a single hierarchical taxonomy.  Somewhere there's
this fantasy that a single taxonomy can represent all knowledge.  This fantasy
dates from the early efforts to create encyclopedias, thesauri and dictionaries,
and it permeates our lives through the Dewey Decimal Classification in
libraries.



No matter how we slice and
dice multiple dimensions, they don't fit into a single taxonomy well.  We can
always reslice and redice the independent variables to create a taxonomy which
has the same information in a different ordering.  Mathematically speaking, if
we have *n* independent dimensions, we can use any of the
*n* ! orderings of the available dimensions to create a distinct taxonomy.  All
*n* ! orders contain the same
information.



Which is more important,
to organize the files on your hard drive by date?  By subject?  Or by
application software?  All are viable dimensions.  There are six possible
orderings of those three
dimensions.



**Web Mart Data Model.** 



The **Web Mart** 
design pattern provides guidance that can constrain our data model in useful and
appropriate ways.  This guidance prevents us from fumbling around and creating a
data model that isn't easy to for people to navigate and maintain.  The
relational model, in many cases, offers us too much power.  Some constraints
help structure the data in familiar, usable
ways.



First, our **Core Concepts**  will be objects that have
interesting, often complex attributes, and will require a fairly sophisticated
page template in which they are displayed.  These are the central entities in
the data model, with the most relationships and the most attributes.  Further,
all of the user's navigation use cases have the same essential goal:  to view a
specific **Core Concept** 
page.



Second, our
**Access Dimensions**  will be lists or hierarchies that
facilitate navigation and search, define menus of various kinds, but aren't --
themselves -- the user's goal.  Access dimensions are the means to the user's
end.  These will have easy-to-manage 1-to-many relationships with
**Core Concepts** .  If they form a hierarchy, they will
have simple 1-to-many relationships among the levels of the
hierarchy.



What's important is that the
**Access Dimensions**  are independent of each other. 
There is no tangling or confusion of the access relationships.  The access
relationships are all ways to find a **Core Concept** .  Since a
**Core Concept**  will have a number of access
dimensions, this forms an easy-to-manage star, not a tangled knot of
relationships.



**Handling Details.** 



There are two kinds of
details that might be related to a **Core Concept** .  In some cases, the
**Core Concept**  has supporting details that are simply
collections of objects.   These details have a pleasant 1-to-many relationship
with the **Core Concept** .  For example, multiple phone numbers
for a person's contact information is just many detail objects collected into a
composite object.



The other kind of
detail is a relationship with another **Core Concept** .  For example, an Invoice has a number
of Line Items, each of which relates to a Product.  A Line Item isn't, itself, a
**Core Concept** .  However an Invoice and a Product are
**Core Concepts** . Invoices have a many-to-many
relationship with Products, and this relationship is implemented through an
association that we call a Line Item
Detail.



Our data model, then, is
dominated by **Core Concepts** , which have
**Access Dimensions** ,
**Details** ,
and associations with other **Core Concepts** .  This helps us structure our models,
and navigation.



**The Django Implication.** 



Each Django server has
access to a number of "applications", defined by the "INSTALLED_APPS" setting. 
Each Django application is a Python package with models, urls, and views; it may
also include templates, tags and media.  Django seems to make use of an
**Application-Model-View** 
design pattern.



By the way, an
application appears to fit into the overall Django world-view as follows.  We
have a Django server, configured by a settings file and started on a specific IP
address and port number.  This Django server may be one of many servers sharing
a common code base and database, or it may stand-alone.  Django servers are --
for production purposes -- usually front-ended by Apache, which handles static
content (known as "media files"), and which handles the slow-client, fast-server
balancing issue.



The **Web Mart** 
design pattern seems to fit nicely with the Django's
**Application-Model-View** 
design pattern.  Each **Core Concept**  is a Django application.  The model
contains the Core Concept, the Access Dimensions and the Details.  We design the
URLs to provide navigation aids through the Access Dimensions.  We have two
kinds of view: core concept detail views and access dimension list views.  Each
kind of view, in turn, relies on either a core concept template or an access
list template.



**Building The Web Mart.** 



Let's say we're building a
web site to describe a church summer camp.  We have a number of Core Concepts in
our camping ministries web site: we have "About" statements, "Volunteer"
information, "Employment" information "Privacy and Safety" information, "Camps",
"Retreats", "Profiles" and "Forms and Paperwork".  Each of these is a separate
core concept, and can be implemented as a separate, small
application.



Let's look at Camps,
specifically.  The **Core Concept**  is Camp, which has relatively few
attributes.  It has a name, a description, and a few administrative details like
the number of campers and the number of counsellors. 




The access dimensions for a Camp
include the schedule dates, the appropriate age group, and perhaps some other
classification scheme that the camping program uses, like "outdoor" or
"adventure" or "creativity" or "special needs". 




The detail dimensions for a Camp might
include additional descriptions, photos from previous years, a list of things to
bring.



**Django Managers.** 



In Django, a Manager can
be used to simplify queries against the database.  In this case, each access
dimension may have a manager.  The camp schedule date dimension, for example,
should have a manager which uses the current date to filter only camps which are
scheduled to begin in the future.  This trivially filters past camps from web
queries, making the views and templates much simpler.




Here's something that looks like it
might be a reasonable model.  This has only a single access dimension,
Schedule.



::

    class CurrentCamp( models.Manager ):
        """Manager for currently scheduled camps only."""
        def imageScheduleList( self, aDate=None ):
            """Creates a nested-list structure of [ ( camp, image, ( sched, ... ) ), ... ]"""
            now= aDate or datetime.date.today()
            campSchedList= []
            qs= super(CurrentCamp, self).get_query_set()
            qs= qs.filter( site=settings.SITE_ID )
            qs= qs.filter( schedule__startDate__gte=now )
            for c in qs.distinct():
                imgList= c.campimage_set.filter( startDate__lte=now, expireDate__gt=now )
                if imgList:
                    img= random.choice( imgList )
                else:
                    img= None
                sch= c.schedule_set.filter( startDate__gte=now ) 
                campSchedList.append( ( c, img, sch ) )
            return campSchedList
        def get_query_set(self):
            now= datetime.date.today()
            qs= super(CurrentCamp, self).get_query_set()
            qs= qs.filter( site=settings.SITE_ID )
            qs= qs.filter(schedule__startDate__gte=now )
            return qs.distinct()
    
    class Camp( models.Model ):
        """A camping program.
        
        This is the generic description.  Only descriptions which have a schedule
        will be shown.  This allows you to have descriptions for programs that aren't
        scheduled in the current year.
        """
        site= models.ForeignKey( Site )
        name= models.CharField( maxlength=64 )
        description= models.TextField()
        staff= models.IntegerField( null=True )
        campers= models.IntegerField( null=True )
        duration= models.IntegerField( null=True, default=5, help_text='Days.' )
        objects = models.Manager() # default manager
        current= CurrentCamp() # currently scheduled camps only
        class Admin:
            list_display= ( 'name', 'site', 'duration', )
        def __str__( self ):
            return self.name
        def image( self, aDate ):
            img_set= self.campimage_set.filter( startDate__lte=aDate, expireDate__gt=aDate )
            if img_set:
                return random.choice( img_set )
        def __repr__( self ):
            return "Camp( name=%(name)r, description=%(description)r, \
    staff=%(staff)r, campers=%(campers)r, duration=%(duration)r )" % ( self.__dict__ )
    
    class Schedule( models.Model ):
        """A schedule for a Camping program.
        
        This is the actual schedule.  A camp which is scheduled in the future
        is shown to visitors.
        """
        camp= models.ForeignKey(Camp)
        startDate= models.DateField( help_text='Starting date for this camp' )
        class Admin:
            list_display= ( 'camp', 'startDate', )
        def __str__( self ):
            return "%s on %s" % ( self.camp, self.startDate.strftime( "%Y-%m-%d" ) )
        def __repr__( self ):
            return "Schedule( startDate=%(startDate)r )" % ( self.__dict__ )
    
    class CampImage( models.Model ):
        """An image that decorates a specific camp listing.
        
        Any number of images can be associated with a given camp.
        However, one is selected arbitrarily to show with a camp entry.
        """
        camp= models.ForeignKey( Camp, edit_inline=True, )
        caption= models.CharField( maxlength=128, core=True, )
        startDate= models.DateField( help_text='First date to display this image' )
        expireDate= models.DateField( default=datetime.date(2099,12,31), 
            help_text='Date on which this image is removed.', validator_list=[campValidators.checkExpireDate] )
        image= models.ImageField( upload_to="photos/%Y%m" )
        class Admin:
            list_display= ('caption', 'camp', 'startDate', 'expireDate', )
        def __str__( self ):
            return "%s: %s ( %s to %s )" % ( self.camp.name, self.caption, self.startDate, self.expireDate )
        def __repr__( self ):
            return "CampImage( caption=%(caption)r, startDate=%(startDate)r, \
    expireDate=%(expireDate)r, image=%(image)r )" % ( self.__dict__ )





**The URLs and Views.** 



We have two overall kinds of
templates and views.  We have the Core Concept detail view, which locates a
specific Core Concept and associated details; this uses a template that shows
all of the relevant details.  This detailed view could be located in several
places in the URL scheme because there may be several access dimensions that
lead us to the resulting Core
Concept.



The other kind of templates
and views are the access dimensions.  Each access dimension defines one or more
list views, or menus.  When there are multiple dimensions, a menu may be used to
select which dimension is used for access.  Each dimension has URL's for
traversing the dimension, views for locating relevant rows in that dimension,
and a template for displaying the access dimension rows, and possibly Core
Concept rows.



In our Camp example, we
only have one access dimension defined.  However, we have to define our URL's to
permit additional access dimensions.  Many Django examples imply that a single
dimension is somehow "primary" for accessing a Core Concept.  This is rarely
true, and a slightly different URL naming scheme makes it possible to add and
change access dimensions without breaking an application.




Here's a portion of the URL
definitions.  Note that we use a ``/camp/byDate/11
URL to use the schedule access dimension.  We can then add ``/camp/byAgeGroup/``
to implement another access dimension.



::

    from django.conf.urls.defaults import *
    
    urlpatterns = patterns('campministry.apps.public.views',
        
        # The stmt_page matches the PAGE_CHOICE in the models.
        # The title should match the menu provided in the template.
        
        (r'^$', 'index', {'stmt_page':'Home',} ),
        (r'^home.*$', 'index', {'stmt_page':'Home',} ),
        (r'^index.*$', 'index', {'stmt_page':'Home',} ),
        ... other stuff ...
        (r'^camp/byDate/$', 'campByDate', {'stmt_page':'Camps', 'title':'Summer Camps'} ),
        (r'^camp/(?P\d+)/$', 'camp', {'stmt_page':'Camps', 'title':'Summer Camps'} ),
    )





Here's a portion of the view
definitions.  We have a generic view function (indexView)
that provides the common information used by all Core Concept views.  The
``campByDate`` and ``camp`` views
expand on this view with either a list of Camps, based on one of the access
dimensions, or a specific Camp.  



::

    def indexView( request, stmt_page, title=None ):
        """ Get Statements, Images and Profiles to fill this page.
        These items are Site-related.  The site qualifies Statements, Images and Profiles.
        """
        pageDict= baseView(request)
        pageDict['title'] = title or pageDict['site_name']
    
        now= today( request, pageDict )
        pageDict['stmt_list']= Statement.current.asof( now ).filter( page=stmt_page ).order_by('startDate')
    
        img_list = Image.current.asof( now ).filter( page=stmt_page )
        if img_list:
            pageDict['image'] = random.choice( img_list )
    
        pageDict['staff_list'] = Profile.activeProfile.filter( contact=True )
        return pageDict
    
    def campByDate( request, stmt_page, title ):
        """List of Camps, organized by the schedule access dimension."""
        pageDict= indexView( request, stmt_page, title )
        now= today( request, pageDict )
    
        pageDict['camp_list']= Camp.current.imageScheduleList( now )
        return render_to_response('camp.html', pageDict )
    
    def camp( request, object_id, stmt_page, title ):
        """A specific Camp."""
        pageDict= indexView( request, stmt_page, title )
        now= today( request, pageDict )
    
        pageDict['camp']= Camp.objects.get(pk=object_id)
        return render_to_response('camp.html', pageDict )





The important value of the **Web Mart** 
design pattern is to prevent thinking of a single taxonomy of camps.  We can
organize the list of Camps by any of the available access dimensions.  In this
case, we've only defined Schedule, but the design pattern helps us recognize
that we are unlikely to have a single access dimension for a
**Core Concept**.










