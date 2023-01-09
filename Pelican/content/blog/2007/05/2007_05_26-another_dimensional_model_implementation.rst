Another Dimensional Model Implementation
========================================

:date: 2007-05-26 01:14
:tags: #python,database
:slug: 2007_05_26-another_dimensional_model_implementation
:category: Python
:status: published







The `Cubulus <http://sourceforge.net/projects/cubulus/>`_  project and `Alexandru Toth <http://alxtoth.webfactional.com/>`_ 's page describe an "OLAP Aggregation Engine".  It is very nice to see advanced work done on the dimensional model.



The cited research dates from 1999 (V. Markl, F. Ramsak, R. Bayer, "Improving OLAP Performance by Multidimensional Hierarchical Clustering", :emphasis:`Proceedings of the Intl. Database Engineering and Applications Symposium` , pp. 165-177, 1999.)  I'm suspicious that it predates the "bit-mapped index".  



It may be that this technique helps a lot with an RDBMS that doesn't support the star schema via bit-mapped indexes.  It may be that this technique only helps a little with a more modern RDBMS.



However, the idea of a nice, tidy Python application that helps manipulate the dimensional model is a great thing.  





