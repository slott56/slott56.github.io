Small Not-For-Profit Web Presence -- What to do?
================================================

:date: 2008-07-28 22:45
:tags: architecture,design
:slug: 2008_07_28-small_not_for_profit_web_presence_what_to_do
:category: Architecture & Design
:status: published







Let's talk about a Small Not For Profit that has a number of web assets, but a web presence that isn't working well.



First, they have a Domain Name (pretend it's www.smallnfp.org). They have an associated organization which is hosting their web site.  Let's call them the Associated Org (www.assocd.org)  The site is big and complex with numerous sophisticated features.  Sadly, they're web 1.0 features, and are starting to show their age.



Only... there are issues.  The Associated Org has at least two Domain Names pointed at their server.  The Associated Org are nice folks, but not web developers.  Their IIS configuration can only handle minimal distinction between the domain names; one significant consequence is that the web pages can't have a meaningful ``<title>`` tags in the ``<head>``.  Really.  It says "Default Page", and that can't easily be fixed.



We'll call this application server -- with it's current set of problems -- the legacy web presence.



:strong:`Web 1.0`



The biggest issue is the Web 1.0 approach:  Provide a site where people can contribute.  "Interactivity" was the feature they wanted.  



The problem is that we're trying to target victims (and family and caregivers) of trauma.  We can't simply create a free-for-all wiki-wiki.  The postings must be moderated.



So, our legacy web application is a rather complex application:  it has a posting workflow.  Everything has to be approved by a moderator.  The problem is that there are two web sites, a number of status settings, and things can easily vanish.  The workflow is too hard to manage.



On conference calls with the Associates it became clear that the the Web 1.0 site wasn't working well.  It wasn't so much the bugs (hardly any) but the complexity of the thing.  There were many types of content; it wasn't at all clear where each type of posting showed up on the resulting web site.  It wasn't clear precisely which status codes lead to what behavior for postings.



:strong:`The Newsletter`



Nothing says "pre-web" more than a newsletter.  Knowledge sharing is important -- it's a big reason why some small not-for-profits exist -- but news in a monthly bundle is a hold-over from print media.



The bastard child of print media and Web 1.0 is the PDF newsletter.  It can be flashy and eye-catching.  But it's multiple pages; I have to download it and open it to read it.  Bleah.



A Web 1.1 compromise is the PDF newsletter with an email that summarizes the articles.  A little better -- I can judge if anything is interesting enough to justify downloading it.



A Web 1.2 compromise is an email that summarizes the articles with links to the full articles and no PDF newsletter.  Better still, because follow-up is easy.



:strong:`What Do We Need?`



The Small NFP has a number of distinct audiences.  The actual users of the services (in this case, victims of certain kinds of trauma); these are people who -- for various reasons -- may not seek help or may be suspicious of offers of help.  There are the family and friends of a victim; people who might be able to steer the victim to seek help.  There are caregivers who need help and support.  There is the wider circle of associated organizations, non-governmental and even in the government.  Finally, there are potential sources of donations and grant money.



We have a number of channels of communication:  email, print, a "web presence".  But what is this "web presence"?  The (nearly) static content at www.smallnfp.com?  Or something more?



We have a number of messages.  For each audience we have a distinct message.  Victims, families, caregivers, associated organizations and funding agencies all want to know different things.  There is some overlap, but there are also some distinctions.



:strong:`The Web 2.0 Newsletter Is a Blog`



First, let's dispose with the newsletter.  A newsletter isn't very targeted. (Indeed, a big question is "who's on the current email and print mailing lists?" and "what message :emphasis:`should`  they be getting?" and "how can one document serve all those distinct needs?")



A newsletter is a compendium of individual stories.  Each story has a byline, a dateline, and sometimes other information about the story.  A newsletter saves the stories until it fills enough pages to justify the cost of publication.



A Blog is a compendium of individual stories.  The information about the story (byline, dateline, etc.) is still present.  However, the cost of publication is nearly zero (compared with the cost of gathering information, writing and editing), so stories can published when they're still newsworthy.  The cost of publication and the bundling of stories ceases to be relevant.



An email notification can be sent with each story.  Additionally, there are syndication tools like RSS and ATOM that make email notification a little slow and old-fashioned.



Additionally, a print newsletter can bundle a recent batch of stories for publication to folks who don't use computers much.



:strong:`Web 2.0 Interactivity Is More Blogs`



One stumbling point in the current architecture is the "interactivity" wish.  It would be great to have victims (or families or caregivers) share their stories.



It would be great.  Indeed, they probably are sharing their stories.  We know they're not posting on www.smallnfp.org's site.  What's left is that they're probably posting on their own blogs, and `myspace <http://www.myspace.com>`_ , `google <pages.google.com>`_  or `geocities <http://geocities.yahoo.com>`_  sites.



In Web 1.0 world, no one could publish anything because publishing was still hard.  It required servers and programmers and knowledge of HTML, ASP and what-not.



In Web 2.0 world, everyone can publish everything because publishing is free.  Much of it is supported by advertisers.  The rest is supported by very simple, easy-to-use services like `www.mac.com <http://www.mac.com>`_ , or the pay versions of geocities or google pages.



:strong:`Email and Spamming`





Currently, the Small NFP's email list is split among several servers: the Associated Org's server, a Gmail account and an AOL account.  Any basic web mail account can keep a master list of contacts and appropriate groups within that master list.   There are a large number of web-based mail processing applications.  See the Wikipedia list of `webmail providers <http://en.wikipedia.org/wiki/Comparison_of_webmail_providers>`_ .  Google mail and Yahoo! mail are popular web email solutions.



However, a mail list is generally for distribution of reminders for web site or blog changes.  The RSS and ATOM syndication protocols (used directly by FireFox and Safari browsers) mean that email isn't required for change notification.  The Web Page and Blog tools provide the necessary feeds, mostly automatically.



Additionally, mail lists are endlessly being partitioned based on interest, focus, background, status, geography, demographics, etc.  The problem is that web-based contact management solutions (e.g., `salesforce.com <http://www.salesforce.com>`_  or `CLP Suite <http://www.clpsuite.com/>`_ ) are rather complex.  Also, it seems odd to use for-profit contact management for a not-for-profit organization.



There are two approaches: a simple mail list or a full-up CRM solution.  The fees for single-user CRM solutions are quite low.  Using a full CRM solution is probably the best way to go.



Small Not-For-Profit Web Strategy



Here's a way to structure the web presence of a small not-for-profit.



:strong:`Web Site`.  Get a Yahoo! Geocities or Google Pages site.  Pay the fees to suppress advertisements and get enough email addresses to handle the current staff.  Use this for your basic contact information, mission statement, strategy, funding sources, and other relatively static information.  This isn't the easiest way to manage information.  However, it's essential to show that the organization is permanent, and serious. 



:strong:`Get Google Accounts`.  Everyone should be using `Google Mail <http://mail.google.com>`_ , and `Google Documents <http://docs.google.com>`_ .  Stop emailing documents among the principals in the organization.



:strong:`Start a blog`.  The Wikipedia entry on Weblog software has a section on `developer-hosted blogs <http://en.wikipedia.org/wiki/Weblog_software#Developer-hosted>`_ .  These are all candidate pieces of easy-to-use blogging software.  Generally, you'll keep your blog and site separate.  You will have your blog reference your site and your site reference your blog.  Careful choice of names creates a single identity.



For example, `Blogger <http://www.blogger.com>`_  is a Google product, but it isn't part of `Google Pages <http://pages.google.com>`_ .  You could use any of the more popular blog tools like `LiveJournal <http://www.livejournal.com/>`_ , `TypePad <http://www.typepad.com/>`_ , `Yahoo 360 <http://360.yahoo.com/>`_  or `WordPress <http://wordpress.org/>`_ .



The hardest part of this is changing the current newsletter production cycle to get rid of the once-each-month schedule.  Instead, the newsletter becomes a continuous operation, with each new article turning into a blog posting.  The traditional print newsletter -- as summary of the Blog -- can still be issued, but the writing and editing is spread throughout the month, not jammed into a hectic rush with a deadline.



:strong:`Start a Calendar`.  The current web site offers an event list.  This can be replaced with `Google Calendar <http://www.google.com/calendar>`_  or`30 Boxes. <http://30boxes.com/welcome.php>`_   Again, this calendar must link to the primary web site, and the primary web site must link to the calendar.



:strong:`Start a Group or Two`.   A few constituencies should have some additional features -- often provided by tools like `Yahoo! Groups <http://groups.yahoo.com>`_  or `Google Groups <http://groups.google.com>`_ .  These tools keep web pages, calendars, documents, discussion forums and email lists.



Generally, a narrow audience (e.g., the trustees) can all be members of a Google Group that provides meeting schedules, agendas, and shared documents.   In some cases, there are audiences with frequent, less-formal contacts.  A group can work well for this.



:strong:`Pick a CRM Tool`.  Move all of the existing mailing lists into the CRM tool.  Identify each individual with enough characteristics to permit meaningful communication.





At this point, the Small NFP has the relevant capabilities of their current web site.  Each component is easier to use and more sophisticated than in the legacy web site.  The parts (site, blog, calendar) are spread around, but each is focused on one part of the problem.  Using a single set of names, colors and mutual links means that this amalgamation appears reasonably consistent to visitors.



The current administrative procedures will change.  Rather than interacting with multiple pages of the (hard-to-use) legacy site, the administrator will interact with multiple pages of multiple (easier-to-use) sites.



In some cases, there will be several alternatives for communication -- the central calendar, a web page change, a blog posting or a group calendar entry that's only visible to the relevant group.   This requires some care to pick the best and most appropriate place to put the information.





:strong:`Create a MySpace Page`.  MySpace has Blog, Calendar and Address Book capabilities.  However, each feature is relatively primitive.  Further MySpace is just one way to attract and retain some (but not all) members of the various target audiences.



Conversion



Here's how the Small NFP can move from their legacy web site to a Web 2.0 presence.  This is a multi-step operation.



First, get the existing content into easy-to-use files.  This will require working with the Associated organization that is currently providing web services.  The extracted content could come in a number of forms.



Second, post this content to the new blog and web pages.  Some blog tools have automated interfaces that make it possible to move large numbers of files with relatively little manual intervention.  A couple of quick Python programs can probably bulk load the blog postings and calendar events.



Third, direct the existing domain name to the new primary web site.   This finishes any relationship with the Associated organization, simplifying their life.



Fourth, drop all email accounts except the approved GMail accounts.  Stop using AOL.  Send email messages from all the legacy accounts announcing the new accounts.  



Fifth, merge all working email addresses into the chosen CRM solution.  



Announce the changes via blog postings, MySpace and email notification.




