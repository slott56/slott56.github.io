Airport Extreme + Time Machine.  Wow!
=====================================

:date: 2008-04-07 13:55
:tags: technologies,web
:slug: 2008_04_07-airport_extreme_time_machine_wow
:category: Technologies
:status: published







:strong:`Attempt 1 - Plug in the disk.  Create users.  Fail.` 



Time Machine won't use a networked disk.  The `advertising <http://www.apple.com/macosx/features/timemachine.html>`_  and documentation is pretty clear that Time Machine wants USB or FireWire storage.



And this is Apple, it either works seamlessly, silently or automatically, or I've got the wrong use case.  So, I took the path of least resistance and took the USB hard drive off the Airport and put it on my desk.



Then I got the software update for Airport Admin and decided to do a little more reading.  I found this note on MacNN: `Airport Extreme supports Time Machine backup <http://www.macnn.com/articles/08/03/22/airport.extreme.backup/>`_ .



:strong:`Attempt 2 - Plug in the disk.  Fail.` 



Darn it!



However, the Airport Extreme utility has some additional file share options.  Did it have these before?  No idea.  But it has them now.



Disk Password.  That's the secret.



Rather than individual user access, grant overall disk access.  And choose that password wisely.  This is the case where a pass-phrase is a smart move.



:strong:`Attempt 3 - Change to Disk Passwords.  Victory!` 



Time Capsule is happily backing up through an airport-mounted disk.  



:strong:`Security` 



You can describe this as a security nightmare.  I'm broadcasting all of my personal files to everyone within 50m of my Airport Extreme base station.



On the other hand, who has the patience to intercept every byte, separate the various concurrent sockets of activity, and piece together my backup upload.  And when they're done, what kind of evil blackmailing plot will they hatch?



When I read about "security" breaches at places like the Veteran's Administration or TJX, I see that loss of the storage device and illegal access to software are the problems.  When I look at the `Data Breach Chronology <http://www.privacyrights.org/ar/ChrondataBreaches.htm>`_ , I see one wireless sniffing, and there are so many security problems that I hesitate to credit sniffing with being the actual exploited vulnerability.





