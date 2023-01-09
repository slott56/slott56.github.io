Read this: 10 Reasons to Learn Python in 2019
=============================================

:date: 2019-01-22 08:00
:tags: #python,community
:slug: 2019_01_22-read_this_10_reasons_to_learn_python_in_2019
:category: Technologies
:status: published

| See `10 Reasons to Learn Python in
  2019 <https://dzone.com/articles/why-every-programmer-should-learn-python>`__.
| I want to dwell on #4 for a moment.
| The Python community actually has a `Code of
  Conduct <https://www.python.org/psf/codeofconduct/>`__. We try to
  stick by it and conferences will have reporting mechanisms in place so
  we can educate folks who are being inconsiderate or disrespectful.
| The consequence of this is a welcoming and intentionally helpful
  community. It's hard to emphasize the "intentionally helpful" enough.
  We don't have much patience for snark. And we're willing to call each
  other out on being unhelpful.
| In my Day Job, we have an in-house Slack channel with well over 1,000
  Python folks. The single most common class of questions is a variation
  on "My Corporate Firewall Setup Doesn't Let Me Use PIP." This is
  ubiquitous. And confusing. And frustrating for folks who are surprised
  there is a corporate firewall.
| We have a number of pinned answers in Slack for this. And -- perhaps
  once a week -- someone will patiently repeated the pinned answers for
  someone who's truly and deeply in over their head trying to get pip to
  work. (We have an in-house PyPI, also, but it requires doing something
  in addition to typing \`pip install whatever\` at the command line,
  and that can require hand-holding.)
| As `Python2 winds to a close <https://pythonclock.org/>`__, and we
  uncover folks working with Python 2, we have to issue guidance. I've
  switched tone from "please consider rewriting your app/tool/framework"
  to "we strongly recommend you start using Python 3." In June, I'm plan
  to switch to "You have only six months to convert whatever you're
  working on."
| We've had some sidebar conversations on making sure I'm being properly
  positive, supportive, considerate, and respectful of the folks who
  think Python2 might be useful.
| The point of the Python community is to help each other. We're
  actively and intentionally trying to be helpful and inclusive.

Technical Sidebar -- Conda and Virtual Environments
----------------------------------------------------

| What about the trickle of people trying to make use of the built-in
  Python2 in Mac OS X or the Python2 that comes with Linux on a
  cloud-based server?
| Some important coaching: **Don't Use The OS Default Python**.
| This is kind of negative. It helps to state this positively. **Always
  Use A Virtual Environment**.
| Because we have a \*large\* community of data scientists, this
  becomes: Always Use A Conda Environment.
| And yes, there are some packages that also require a pip install. And
  yes, `XKCD 1987 <https://xkcd.com/1987/>`__ describes the consequence
  of the rapid growth of Python and the variety of ways it can be made
  to work. (While all the strands of spaghetti look like a negative,
  they reflect the variety of clever solutions, all of which work
  without any problems.)
| Therefore. This.
| 1. conda create --name=working python=3.7 --file conda_install.txt
| 2. conda activate working
| 3. python3 -m pip install pip_install.txt
| The absolute worst case is a project with two lists of requirements,
  one in a conda conda_install.txt and some extra stuff in a
  pip conda_install.txt. We're able to use \`python3 -m pip install
  requirements.txt\` for almost everything.
| If you're just starting out, you can use
  `miniconda <https://conda.io/miniconda.html>`__ to bootstrap
  everything else you might need.





