PyCrypto Experience
===================

:date: 2014-09-25 08:00
:tags: #python,encryption,pycrypto
:slug: 2014_09_25-pycrypto_experience
:category: Technologies
:status: published

Let me start with a wow.
`PyCrypto <https://www.dlitz.net/software/pycrypto/>`__ is very nice.
Let me emphasize the add-ons that go with PyCrypto. These are as
valuable as the package itself.
Here's the story. I was working with a Java-based AES encrypter that
used the "PBKDF2WithHmacSHA1" key generator algorithm. This was part of
a large, sophisticated web application framework that was awkward to
unit test because we didn't have a handy client to encode traffic.
We could run a second web application server with some client-focused
software on it. But that means tying up yet another developer laptop
running a web server just to encode message traffic. Wouldn't it be
nicer to have a little Python app that the testers could use to spew
messages as needed?
Yes. It would be nice. But, that the heck is the PBKDF2WithHmacSHA1
algorithm?
The JDK says this "Constructs secret keys using the Password-Based Key
Derivation Function function found in PKCS #5 v2.0." One can do a lot of
reading when working with well-designed crypto algorithms.
After some reading, I eventually wound up
here: https://www.dlitz.net/software/python-pbkdf2/ Perfect. A trustable
implementation of a fairly complex hash to create a proper private key
from a passphrase. An add-on to PyCrypto that saved me from attempting
to implement this algorithm myself.
The final script, then, was one line of code to invoke the pbkdf2 with
the right passphrase, salt, and parameters to generate a key. Then
another line of code to use PyCrypto's AES implementation to encrypt the
actual plaintext using starting values and the generated key.
Yep.  Two lines of working code. Layer in the two imports, a print(),
and a bit more folderol because the the character-set issues and URL
form encoding. We're still not up to anything more than a tiny script
with a command-line interface. "encrypt.py this" solved the problem.
At first we were a little upset that the key generation was so slow.
Then I read some more and learned that slow key generation is a feature.
It makes probing with a dictionary of alternative pass phrases very
expensive.
The best part?
PyCrypto worked the first time. The very first result matched the opaque
Java implementation.
The issue I have with crypto is that it's so difficult to debug. If our
Python-generated messages didn't match the Java-generated messages.
Well. Um. What went wrong? Which of the various values weren't salted or
padded or converted from Unicode to bytes or bytes to Unicode properly?
And how can you tell? The Java web app was a black box because we can't
-- easily -- instrument the code to see intermediate results.
In particular, the various values that go into PBKDF2WithHmacSHA1 were
confusing to someone who's new to crypto. And private key encryption
means that the key doesn't show up anywhere in the application logs:
it's transient data that's computed, used and garbage collected. It
would have been impossible for us to locate a problem with the key
generator.
But PyCrypto and the add-on pbkdf2 did everything we wanted.





