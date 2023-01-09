It appears that DevOps may be more symptom than solution
========================================================

:date: 2015-03-10 08:00
:tags: java,DevOps,spring framework
:slug: 2015_03_10-it_appears_that_devops_may_be_more_symptom_than_solution
:category: Technologies
:status: published

| It appears that DevOps may be a symptom of a bigger problem. The
  bigger problem? Java.
| Java development -- with a giant framework like Spring -- seems to
  accrete layers and layers of stuff. And more stuff.  And bonus stuff
  on top the the excess stuff.
| The in-house framework that's used on top of the Spring Framework
  that's used to isolate us from WebLogic that used to isolate us from
  REST seems -- well -- heavy. Very heavy.
| And the code cannot be built without a heavy investment in learning
  Maven. It can't be practically deployed without Hudson, Nexus, and
  Subversion. And Sonar and Hamcrest and mountains of stuff that's
  implicitly brought in by the mountain of stuff already listed in the
  Maven pom.xml files.
| The deployment from Nexus artifacts to a WebLogic server also involves
  uDeploy. Because the whole thing is AWS-based, this kind of overhead
  seems unavoidable.
| Bunches of web-based tools to manage the bunch of server-based tools
  to build and deploy.
| Let me emphasize this: bunches of tools.
| Architecturally, we're focused on building "micro services".
  Consequently, an API takes about a sprint to build. Sometimes a single
  developer can do the whole CRUD spectrum in a sprint for something
  relatively simple. That's five API's by our count: GET one, GET many,
  POST, PUT and DELETE: each operation counts as a separate API.
| Then we're into CI/CD overheads. It's a full sprint of flailing around
  with deployment onto a dev servers to get something testable and get
  back test results so we can fix problems. A great deal of time spent
  making sure that all the right versions of the right artifacts are
  properly linked. Doesn't work? Oh. Stuff was updated: fix your pom's.
| It's another sprint after that flailing around with the CI/CD folks to
  get onto official QA servers. Not building in Husdon? Wrong Nexus
  setup in Maven: go back to square one. Not deployable to WebLogic?
  Spring Beans that aren't relevant when doing unit testing are not
  being built by WebLogic on the QA server because the .XML
  configuration or the annotations or something is wrong.
| What's important here is that ⅔ of the duration is related to the
  simple complexity of Java.
| The DevOps folks are trying really hard to mitigate that complexity.
  And to an extent, they're sort of successful.
| But. Let's take a step back.

#. We have hellish complexity in our gigantic, layered software toolset.
#. We've thrown complicated tools at the hellish complexity, creating --
   well -- **more** complexity.

| 
| This doesn't seem right. More complexity to solve the problems of
  complexity just don't seem right.
| My summary is this: the fact that DevOps even exists seems like an
  indictment of the awful complexity of the toolset. It feels like
  DevOps is a symptom and Java is the problem.





