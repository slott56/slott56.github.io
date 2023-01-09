Notable Failure of Use Cases
============================

:date: 2005-10-26 22:43
:tags: architecture,design
:slug: 2005_10_26-notable_failure_of_use_cases
:category: Architecture & Design
:status: published





**Context** 

The
company,
*W* , is
an e-business startup with a successful, profitable business operation.  They
were using a mixture of PCs and small servers from various sources to conduct
business.  They had a base of customers, a positive cash-flow and investment
dollars. 




*W* 
contacted two large software and services companies for proposals to build a
complete web-based solution to replace the ad-hoc mixture of software and
outside services that formed the current operation.  The total bill for
development was over $10M from each vendor.  The job was beyond their investors
capabilities.  Unlike many e-business startups, they had limited in-house
technical expertise; and no in-house
developers.



*W* 
came to us with a document, prepared by one of the vendors, which was an
architecture and blueprint for the system to be developed.  It contained a
number of “use cases”; we were contracted to prioritize the use
cases, and deliver the required functionality
incrementally.



**Problems** 

The
initial set of use cases were not narrative in form; they did not contain
sequences of interactions between an actor and the system to create business
value.  In all but a few cases, they were bulleted lists of features, data
elements, business rules, constraints, and implementation hints.  The most
notable exception was the first use case, one that described how a particular
class of actors logs in to the
application.



Further, the description
of the various login scenarios provided by
*W* 
implied some additional use cases not present in the documentation.  This
quality problem, plus the egregious focus on login, indicated some kind of rush
to create a deliverable, even thought it was
incomplete.



We also noted that the most
critical business process, market place segmentation, was not covered at all. 
The entire marketing component was summarized in a single “use case”
with a few vague bullets as supporting
details.



One consequence of the project
history was that
*W*  was
firmly committed to the document.  It appeared that
*W*  had
spent considerable time and effort with their vendor arriving at the “use
case” descriptions.  They considered the document to be of considerable
value, even though we found it an opaque summary of features without any usable
narrative structure.  We could not mock up business transactions from the
information provided, but were not permitted to gather additional
information.



Additionally, our analysts
were able to develop use cases or scenarios from the end users.  The most
critical actor would only attend meetings when all other business principals
(including the CEO) were present, diluting the actor’s contributions. 
Further, one of the customers funding the business and serving on the board of
directors, was only able to speak hypothetically about what could be done.  It
was difficult to get the critical actor to say what actually needed to be done
to conduct
business.



**Conclusion** 

We
note that while there were numerous personnel and management issues, there is
also a problem with the use case technique.  The use case issue is that users
often cannot focus on the business problem, they will either describe a specific
solution or speak hypothetically about potential
solutions.



As developers, we often find
there is an intense focus on the login sequence.  The login or authentication
sequence seems to be the feature that is most often over-specified.  In many IT
operations, authentication is determined by existing standard procedures, and
not subject to specifications.  In other cases, as firms move toward single
sign-on (SSO), the details of login are delegated to the SSO component, and do
not need to be specified.



Our
preference is to simply state the user’s level of access as a precondition
for all use cases, and leave it out of the business description entirely.  We
feel that authentication, by itself, does not create business
value.








