Secure Salted Password Hashing
==============================

:date: 2013-12-12 08:00
:tags: #python,security
:slug: 2013_12_12-secure_salted_password_hashing
:category: Technologies
:status: published


An excellent exposition of secure salted password hashing.

https://crackstation.net/hashing-security.htm

This was really quite nice. It didn't have a Python version, but the
clarity of the exposition makes the Python easy to write.

A few months back, I had this mystery
conversation: http://slott-softwarearchitect.blogspot.com/2012/08/password-encryption-short-answer-dont.html.

While this is not going to produce identical results to the code shown
in the blog post, it seems to fit the requirements.

::

   from hashlib import sha256
   import os
   class Authentication:
       iterations= 1000
       def __init__( self, username, password ):
           """Works with bytes. Not Unicode strings."""
           self.username= username
           self.salt= os.urandom(24)
           self.hash= self._iter_hash( self.iterations, self.salt, username, password )
       @staticmethod
       def _iter_hash( iterations, salt, username, password ):
           seed= salt+b":"+username+b":"+password
           for i in range(iterations):
               seed= sha256( seed ).digest()
           return seed
       def __eq__( self, other ):
           return self.username == other.username and self.hash == other.hash
       def __hash__( self, other ):
           return hash(self.hash)
       def __repr__( self ):
           salt_x= "".join( "{0:x}".format(b) for b in self.salt )
           hash_x= "".join( "{0:x}".format(b) for b in self.hash )
           return "{username} {iterations:d}:{salt}:{hash}".format(
               username=self.username, iterations=self.iterations,
               salt=salt_x, hash=hash_x)
       def match( self, password ):
           test= self._iter_hash( self.iterations, self.salt, self.username, password )
           return self.hash == test # Constant Time is Best


It may be helpful to use ``__slots__`` with this to reduce the storage
and make the object less mutable.

Perhaps I didn't google well enough to find a clear explanation that
**also** included Python code samples.





