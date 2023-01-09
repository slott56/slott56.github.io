10 common security gotchas in Python and how to avoid them
==========================================================

:date: 2018-07-10 08:00
:tags: #python,security
:slug: 2018_07_10-10_common_security_gotchas_in_python_and_how_to_avoid_them
:category: Technologies
:status: published

First, read this: `10 common security gotchas in Python and how to avoid
them <https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03?source=emailShare-879bf4230309-1531218424>`__
by Anthony Shaw

Of these, most are important, but not specific to Python at all. Only
items 3, 4, 7, and 8 are pretty specific to Python. They talk about the
assert statement, some timing vulnerabilities, and the bad idea of
transmitting pickle files.

Item 5 is also specific to Python, but I quibble about it's relevance.
It is at the very edge of "security." The PYTHONPATH environment
variable is most definitely not "...one of the biggest security holes in
Python." If the path is a security hole, then any code is a security
hole. If we view code as a security hole, then the only truly secure
system has no software.

(As someone who lived on a sailboat. I happen to subscribe the position
that the only **truly** secure system has no software. Use line,
shackles, and well-known knots if you want to stake your life on it. Use
fancy electronics with software to make it simple and fun.)

Bad programming is the **biggest** security hole. Failure to prevent SQL
injection. Failure to use CSRF tokens. Failure to properly handle
credentials. These are security holes of epic proportions.


The ``PYTHONPATH`` cannot be changed through any kind of request
handling. Even colossally dumb software that blindly uploads XML or
JPEG files without vetting them won't change the ``PYTHONPATH``.  You'd
have to write code that changed sys.path. Or you'd have to write code
that reset the os.environ and then started applications in the new
environment. This is seriously bad code, and has nothing to do with
Python.


Otherwise, the only way to change ``PYTHONPATH`` requires an Evil Super
Genius who has your compromised credentials. Once your credentials
are compromised anything is possible, including the setting the ``PATH``
environment variable, or deleting all the accounts, or ``rm -rf /``. None
of which is specific to Python.

Item 9 -- patching the system Python -- may be important, All OS's
should have patches applied early and often. However. We strongly
discourage our developers from using the system Python for anything.
We always build environments. We always install our own Python 3 with
our own packages. We generally ignore the system Python to the extent
possible.


Item 7, though, is a huge deal. We use OAS (formerly known as
swagger.) The old swagger.json end-point was -- clearly -- json. The
new OAS 3, however, suggests the specifications be provided at
openapi.yaml. This week we're rolling out a cluster of microservices
using our shiny new OAS 3 specifications. And we're using default
``yaml.load()`` instead of ``yaml.safe_load()`` as part of the contract
hand-shake among the services. All internally-facing handshakes, but
still unsafe with respect to a man-in-the-middle hacking our
specifications.


While I can quibble about two of the ten items, the other eight are
rock solid, and should be part of periodic in-house code reviews.


And number 7 is killer.





