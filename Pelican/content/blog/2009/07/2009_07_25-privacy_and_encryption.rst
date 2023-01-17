Privacy and Encryption
======================

:date: 2009-07-25 07:05
:tags: encryption,security
:slug: 2009_07_25-privacy_and_encryption
:category: Technologies
:status: published

See `Massachusetts Says Encrypt It
All! <http://cio.ulitzer.com/node/1046285>`__

This gives a hint as to the future of personal information collection
and dissemination.

This is potentially A Bad Thing.

I don't see a problem with using SSL to encrypt "over the wire" data
transfers. I don't see a problem with adding layers of encryption to
these transfers.

Everything else is going to require something like Apple's `File
Lock <http://www.apple.com/downloads/macosx/networking_security/filelock.html>`__
to assure that the file -- no matter where it goes -- is encrypted.
This will be a problem.

Non-Standards
-------------

A search for Windows File Encryption shows that there are a lot of
choices. Hopefully, they will all find a way to adhere to some
straightforward standard like
`AES <http://en.wikipedia.org/wiki/Advanced_Encryption_Standard>`__.
If we have to buy/download/install a pile of encryption applications,
data sharing will become expensive and complicated. Even if Microsoft
does their usual "standard + enhancements" offering, it will make
things very expensive.

Imagine buying the "Crypto-Crummo" file system encryption package,
deploying it enterprise-wide, finding a problem, and -- horrors --
being unable to unlock your files ever again. It's a bug, not a
feature, but you still can't open your files.

How do you prevent that risk? Right. Keep an illegal unencrypted copy
of everything.

Here's another scenario. Imagine buying the "Crypto-Locko" file
system encryption package. You deploy it enterprise wide. You stop
paying your license fees. It stop decrypting. You're corporate data
is being held hostage by your encryption vendor.

Here's the third strike. You buy the "Crypto-Uniqueo" file system
encryption package. It has a unique protocol, non-standard,
proprietary. It gets hacked. Your in violation of the law.

Or, the company making "Crypto-Uniqueo" ceases support. Now how do
you get into your files? Or, the company goes out of business? What
now?

Unintended Consequences
-----------------------

Without an applicable encryption standard -- and some boundaries on
what's really required -- I think these legal initiatives will do
more harm than good. To prevent the various risks, companies will do
dumb things. Things that are probably dumber than what they've done
that lead to leaks of personal information.





