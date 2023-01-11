Java-related skills - response to a question
============================================

:date: 2007-06-20 18:59
:tags: books,building skills,#python
:slug: 2007_06_20-java_related_skills_response_to_a_question
:category: Books
:status: published







I think that learning Java is challenging.  You've got to learn the language, object-oriented programming, the libraries and the endless Java Technologies.  The Java landscape is crowded with J*tx*  and *tx* J add-ons, where *tx*  is some technology abbreviation; for example, JAXWS, JAXB, SAAJ, JMS, JFC, JCE, JAAS, etc.



The skills generally form layers.  The layers are often tangled, and sometimes there isn't a clear progression from "simple" to "complex".  That can make it all complex.  However, there's a great approach in an old book on `Structured Concurrent Programming <http://www.amazon.com/Structured-Concurrent-Programming-Applications-Addison-Wesley/dp/0201029375>`_  by Holt, Lazowska, Graham and Scott.  They have a sequence of layers that begin with simple expressions and output (the absolute minimum) and then folds in new features in a discrete series of steps.  With Java (and Python) you need this kind of guidance to work through these steps and build up your skills in an orderly progression.



On the language front, you've got to tackle the following.  I think this is the right order.




1.  The core procedural programming language is the start.  Basic assignment, if, for, while, try-catch, etc. come first.  This will, of necessity, focus on the primitive types and Strings.

#.  Some essential reference types.  java.io, java.math, java.text and java.util are full of these essential classes.

#.  OO Design using Classes, Interfaces and Packages.  This has to build on the `Design Patterns <http://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional/dp/0201633612>`_  material to help guide your understanding of classes and class design.




The hard part is to work through the following skills and technologies in addition to the language.





1.  **NetBeans Tool Use**.  This means creating a project, creating files and packages, etc.  Creating JUnit unit tests, and running the unit test tool is perhaps one of the most important of these “close-to-Java-but-not-the-language-itself” skills.  NetBeans is rather complex, nothing is obvious, and there are a million distracting plug-ins and add-ons.  Also, NetBeans provides a “virtual” view of your project, distinct from the physical files and directories on your disk; this can be confusing.

#.  **Unit Testing**.  Nothing matters more than solid JUnit tests wrapped around your Java components.  Because of the way Java works, the final presentation (as GUI, or as web page) can be separated from the data model or "guts" of the program.  (You can read up on the Model-View-Controller design pattern in many places, include `Wikipedia's MVC article) <http://en.wikipedia.org/wiki/Model-view-controller>`_ .  This is a really important consideration all through architecture, design, programming and testing.  You’ll design, code and test model components, which can then be assembled with a GUI or a web container.

#.  **JDBC**.  Java Database Connectivity is the way much of our data persistence is handled.  JDBC involves some hurdles because of the vendor-neutrality, and flexibility.  NetBeans has a skinny little RDBMS that can be used for development.  Oracle 10 Express is an alternative that is free and suitable for development.  Two of the big, ugly issues here is the “hard-coding passwords” and “hard-coding JDBC driver” information.  Hard-Coding is really, really bad.  Java has lots of techniques for putting key properties in property files or command-line parameters.  Part and parcel of JDBC is handling passwords in a graceful and reasonably secure way.

#.  **Web App Skills**. My experience is that desktop GUI apps aren’t as common as web apps – to our particular class of customers.  There are many desktop GUI apps in this world, many of which are Java-based.  However, our customers are more likely to build J2EE web applications than desktop applications.  This mans that there’s this whole side-light area of HTML, CSS, XML and what-not required to get a web app up and running.  Java has a rich set of components for separating Model, View and Control, using Java objects (sometimes called POJO, Plain Old Java Objects), Java Beans (not Enterprise Java Beans, just Java Beans), and Java Server Pages (JSP)’s.  The STRUTS framework pulls these together, and it’s essential for building good web applications.

#.  **Application Deployment**. Building a web app is challenging.  Getting it to behave well in a web server is a different kind of challenge.  It requires a fair amount of poking around in Tomcat to figure out how to start, stop, restart and manage a web server with your web application stuffed inside it.  Java web servers have a large number of configuration files, and it takes some trial and error to work out what they do.  Once you get it, however, the power of providing configuration information in the XML files means that your applications can be more generic and tailored by a specific web deployment.

After this, composite application skills are the **Next Big Thing**.  This means the various XML parsing tools (DOM and SAX).  It also means SOAP and XML-RPC, as well as the rest of the technology stack in Web Services world.  However, composite application tools and standards are a rapidly-evolving area.  By the time you get here, the technology will have moved on.




