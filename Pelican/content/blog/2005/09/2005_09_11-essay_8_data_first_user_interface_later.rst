Essay 8 - Data First, User Interface Later
==========================================

:date: 2005-09-11 16:30
:tags: architecture,design
:slug: 2005_09_11-essay_8_data_first_user_interface_later
:category: Architecture & Design
:status: published





Is data more important than processing?  Not
necessarily; the central issue is one of enduring impact on the problem,
solution, architecture and
implementation.



Generally, the
available or desired data has the most enduring impact.  Processing,
functionality, user interface nice-to-haves and other considerations are much
softer and more malleable than the actual
data.



Consider a postal envelope that
omits the city and zip code.  It is essentially
undeliverable.



Consider two postal
handling systems:

-   One version of the processing for mail
    pre-stages the outbound mail in a basket.  Each day the mail with checks payable
    on that day is moved from there to the post office box where the postal service
    commences delivery.

-   This postal handling system can be easily
    changed to use a piece of furniture with 31 slots, numbered by day of the month.
    This reduces the time required to locate today's outbound mail, but increases
    the time required to stage the
    mail.



The data elements of an envelope
cannot be changed without compromising the system.  However, within some very
broad limits, the processing can be very flexible and
dynamic.



The essential data
classifiers, relationships, attributes and operations are of enduring value. 
The application or user interface processing can be changed very freely on top
of this data model.

1.  The data elements are identified as nouns in
    the initial context and problem statements.

#.  The data elements are further elaborated as
    part of the use cases, and any supporting data model.  A set of data elements
    can easily be defined as absolutely required; without these, the software will
    not work or will be worthless.

#.  An implementation of the data elements are
    begins during architecture and is elaborated during
    design.



The processing, however, does
not have the same enduring value.  Often the processing concepts are negotiable
because the depth and degree of automation is negotiable.  In some cases, the
processing cannot be automated because it requires either intelligence or
judgement.



The user interface, is even
more flexible.  People, being intelligent, are able to form a mental model of
the underlying data model in spite of terrible user interfaces.













