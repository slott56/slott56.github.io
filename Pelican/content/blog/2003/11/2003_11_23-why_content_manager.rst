Why Content Manager?
====================

:date: 2003-11-23 19:49
:tags: web,cms
:slug: 2003_11_23-why_content_manager
:category: Technologies
:status: published





::

    >> A while back you mentioned the following book
    >>
    >> Book Title: Text, ConText, and HyperText Writing with and for the Computer edited by Edward Barrett
    >> ISBN 0-262-02275-3
    >>
    >> I bought and then scanned through the book. I picked the following article to read semi carefully
    >> Hypertext: A Way of Incorporating User Feedback into Online Documentation, Patricia Ann Carison
    >>
    >> Thanks for the reference. It is a welcome addition to my library.



Earlier I said the
following:

"But, you don't need a
database, SQL, or other stuff for simple content
management."

::

    
    > Can we attempt to define "simple".    
    > When I use the term hyperlink, I am using it the way the hyperlink is implemented in most current browsers.
    > Hyperlinks are great for uni-directional motion either forward or back.
    > Also, they are good if you want to go from your current location to n possible new locations.
    > If your "content management" only needs the above requirements, it is simple.
    > This is my attempt at defining simple. 
    >
    > I don't like hyperlnks because there is no back propagation. Once I am at a page, there is no way for me to determine all the possible ways that I can get to this page. I can only go back the way that I came.
    > This addresses the navigation from one chunk of info to another.
    > Also, a simple content management does not involve word searches or pattern matches.
    >
    > I would be interested in your definition of "simple"



Simple is as
simple does.  I'm not sure what the issue is, and why "simple content manager"
needs definition.



The
unidirectionality of links are a known limitation of the current structured text
world.  Indeed, the management of links is a huge problems, since links, labels
and targets are not kept under control.  A target moves, no link changes
automatically.  Or, one copy of a link changes, but another copy becomes
invalid.  All very sad; the best that can be done is to track links and generate
them as part of generating HTML from the
content.



The "Back Propagation"
is partly satisifed by the navigation crumbs left along the way.  Browsers keep
history, some web sites keep a path back to the home
page.



The question of all
places that reference a particular link is a kind contradiction.  The number of
references to content grows or shrinks over time.  Consider a link as a
bibliographic entry: no author can ever determine references to his work; the
can only determine work he
referenced.



Since word searches
are fast and almost free, it seems odd for you to exclude it.  Contrary to
Oracle's point of view (e.g. from Google's point of view) full text search is a
technical nothing, and everyone should offer
it.



The issue is one of the
depth of structure to your data:  highly structured, normalized data belongs in
a database; ill-structured, irregular data belongs in a content manager. 




Some data blurs the
distinction and difficult decisions arise.  For example, insurance contracts are
wonderfully complex, can be represented in a database, but require large
sophisticated programs.  Maybe a simple content manager to keep some information
about the clauses, terms and conditions associated with particular products.  A
database can track customers, products, premiums, payments, etc.  However, the
actual words that comprise the contract is ill-structured data and doesn't
really need to be in a database at all.








