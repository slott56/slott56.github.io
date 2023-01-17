Something Else I Invented
=========================

:date: 2007-08-25 11:58
:tags: FOSS,open-source
:slug: 2007_08_25-something_else_i_invented
:category: FOSS
:status: published







`Recently <{filename}/blog/2007/07/2007_07_04-what_i_love_about_python_what_i_hate_about_the_word_of_open_source.rst>`_ , I found out that my HTML parser was only a mere shadow `Beautiful Soup <http://www.crummy.com/software/BeautifulSoup/>`_ .  I invented what is -- essentially -- a similar core structure.  I didn't carry it to the same level of completion.  From what little research I've done, my invention predates Beautiful Soup.



It's one of those "collective unconscious" or "synchronicity" things -- good ideas floating around, captured by people with different abilities.  I built a little thing that accomplished what I wanted.  At about the same time, someone else built something more complete and slightly cooler.



[If you try to read about `collective unconscious <http://www.google.com/search?hl=en&client=firefox-a&rls=org.mozilla%3Aen-US%3Aofficial&hs=UBG&q=collective+unconscious&btnG=Search>`_  and synchronicity, you find one of my favorite poems, "The Second Coming" as the Wikipedia redirect for `Spiritus Mundi <http://en.wikipedia.org/wiki/Spiritus_Mundi>`_ .  Proof, if any was needed, that smart people are uncomfortable with coincidence.  Many people feel compelled to explain coincidence; they either create a philosophy or a conspiracy theory.]



A client of mine is using `iBatis <http://ibatis.apache.org/>`_ , which was new to me.  Up until Monday, it had been little more than a name, on the mental shelf next to `Hibernate <http://www.hibernate.org/>`_ , `TopLink <http://www.oracle.com/technology/products/ias/toplink/index.html>`_ , `JDO <http://db.apache.org/jdo/>`_ , `Torque <http://db.apache.org/torque/>`_  and `OJB <http://db.apache.org/ojb/>`_ .  After reading the introduction to the tutorial, I realized that I had  already invented this.  At about the same time.



    **Arrrggh!**



My version of iBatis didn't manage the JDBC connection, but it did everything else that the basic SQLMap portion of iBatis does.  I didn't have as cool a DAO implemetation, but I had all kinds of parameter substitution and type conversion.



Back in 1981, I invented the spreadsheet.  Well, it was a batch COBOL program that did ETL processing (in a way), had flexible calculations, and had a great financial-reporting algorithm for handling rounding correctly.  Okay, it didn't run on an Apple II, and didn't change the world like `VisiCalc <http://www.bricklin.com/visicalc.htm>`_  did.



That does it.  Next good idea I have, I am going to open a `SourceForce <http://sourceforge.net/>`_  project right away.  If there is a collective unconscious, I just need to tap into it first.  If it's a conspiracy, they were out to get me anyway.





