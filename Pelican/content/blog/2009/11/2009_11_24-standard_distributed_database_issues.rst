Standard "Distributed" Database Issues
======================================

:date: 2009-11-24 21:43
:tags: architecture,design,ESB,SOA
:slug: 2009_11_24-standard_distributed_database_issues
:category: Technologies
:status: published

Here's a quote "standard issues associated w/ a disitributed db". And
"There is the push versus pull of data. Say you use push and..." and
more stuff after that.

First, by "Distributed Database", the question could mean almost
anything. However, they provide the specific example of Oracle's
Multi-Master Replication. That narrows the question somewhat.

This appears to mean that -- for them -- Distributed Database means
two (or more) applications, two (or more) physical database instances
and at least one class of entities which exist in multiple
applications and are persisted in multiple databases.

That means multiple applications with responsibility for a single
class of objects.

That breaks at least one fundamental design principle. Generally, a
class has one responsibility. Now we have two implementations sharing
some kind of responsibility for a single class of objects.
Disentangling the responsibilities is always hard.

Standard Issues
---------------

There's one standard issue with this kind of distributed database. It
is horribly complex and never worth it.

Never.

You broke the `Single Responsibility
Principle <http://www.objectmentor.com/resources/articles/srp.pdf>`__.
You'll regret that.

The "distributed database" is like a spread sheet.

First, you have a problem that you think you can solve with a
distributed database.

Now you have two problems.

Sensible Alternatives
---------------------

There are two standard solutions to problems that appear to require a
distributed database.

**A data warehouse**. Often, there is no actual state change that is
part of a transactional workflow that moves back and forth between
the applications. In most cases, the information needs be merged for
reporting and analysis purposes. Occasionally, this merged
information is used for transactional processing, but that's easily
handled by the dimensional bus feeding back to source applications.

**An Enterprise Service Bus (ESB) and a Service-Oriented Architecture
(SOA)**. The rest of the time, one has a "Distributed Transaction".
This is better thought of as a Composite Applications. A composite
application is not part of any of the foundational ("distributed")
applications; a composite is fundamentally different and of a higher
level

Stay Out Of That Box
--------------------

In short, the "standard issues" with attempting a distributed
database are often insurmountable. So don't try.

Pick a fundamentally simpler architecture like Composite Applications
via an SOA using an ESB.

Yes, simpler. In the long run, a composite application exploits the
foundational applications without invoking a magical two-way
distributed coherence among multiple data stores. A composite
application leverages the foundational applications by creating a
higher-level workflow to pass data between the foundational
applications as needed by the composite application.

Read any vendor article on any ESB and you'll see numerous examples
of "distributed" databases done more simply (and more effectively) by
ditching the concept of "distributed".

`IBM <http://www-01.ibm.com/software/info/ebf/smartsoa/index.jsp?cm_mmc=agus_itebfsoatest-20090701-108AU1HW-_-k-_-google-_-ibm_soa_mkwid_scWvrWyxv_3064320991_4320hrybowu501022>`__,
`Oracle <http://www.oracle.com/webapps/dialogue/dlgpage.jsp?p_ext=Y&p_dlg_id=7747792&src=6818567&Act=5&sckw=NAMK09052542MPP001.GCM.8320.200>`__
(which now owns Sun's JCAPS),
`JBoss <http://www.jboss.com/products/platforms/soa/?s_kwcid=TC%7C8574%7Centerprise%20service%20bus%7C%7CS%7Ce%7C3689181351>`__,
`WSO2 <http://wso2.com/products/enterprise-service-bus/>`__,
`OpenESB <https://open-esb.dev.java.net/>`__, `Glassfish
ESB <http://www.sun.com/software/javaenterprisesystem/javacaps/glassfish_esb.jsp>`__






