My Microsoft Blind-Spot
=======================

:date: 2006-05-04 14:08
:tags: microsoft,lamp
:slug: 2006_05_04-my_microsoft_blind_spot
:category: Management
:status: published





Hobbit says:

    "Everything in the windows world does not
    directly work with the "rapidly-evolving" windows api's (for example, c# devs
    rarely concern themselves with api calls.) If there is such a lack of clarity in
    these API's causing a "barrier to innovation," why is windows still the easiest
    and most popular platform to develop
    on?



    "I would argue that development
    tools, languages and technologies are one of the few areas that MS actually
    excels, and that love it or not, it's played a big role in their market
    dominance."



First, there's a
distinction being emphasized here, between application programming (in C#, apart
from low-level API's) and platform programming (where the low-level API's matter
more).  This is an important distinction and gets at the heart of my
complaint.



Tangentially, there's a the
question of "easy" and "popular", which are not what I'm complaining about. 
Many people are willing to pay top dollar for the "easy" part of Windows.  Other
people consider Windows to be essential to success because it's popular.  These
are different reasons; sometimes people will buy into both, sometimes only one
or the other.



One of my customers is
big on the "easy" and cares very little for the "popular", as an example.  They
feel that the Windows Visual Studio has so many easy-of-use factors that it is
worth every penny.  And they feel that they can -- at any time -- cut the cord
and switch to Mono http://www.mono-project.com/Main_Page.



Finally,
I reject the proposition that "tools, languages and technologies [have] played a
big role in their market dominance."  I think that marketplace dominance is a
herd-mentality feedback loop.  Other people are using it, so I'll use it, too. 
Popularity isn't about
*superior* 
technology, but about good-enough technology.  Popularity isn't about
innovation, but about stability.  Indeed, some claim that it's all about
predictability http://www.joelonsoftware.com/design/1stDraft/03.html.



The API Bottleneck
------------------



My problem may be
that I see the really innovative stuff in the LAMP (Linux, Apache, MySQL,
Python/PHP/Perl) or MARS (MySQL, Apache, Rails, Solaris) worlds first.
If it is viable, it moves into Windows.
One example is the sophisticated FFMPEG http://ffmpeg.sourceforge.net/index.php application suite, which doesn't seem to
be a Windows innovation.



This is not to say that the open source world *owns*
innovation.  Good stuff arises first in Windows, also, but it is generally not
so envelope-pushing.  In Windows, you can create a nice application, but you'd
be hard pressed to create a new *kind* of application.



This could be my bias
in watching LAMP-technology arena more closely than the Windows arena.  Or, it
could be that the open source world is free from constraints imposed by the MS
technology stack.  By constraints, I mean the "what does this do?" mystery. 
There's a limit to these efforts at "lower-level" innovation when you can't be
sure what the API rally does.



At the
end-user application-level, if the API's aren't visible in C# using .NET, then
the effect is indirect.  What happens is that upper-tier software (like
applications in C#) are only hampered slightly by the pace of innovation in C#;
C#, on the other hand, is hampered by the mysterious API's. 




I have to grant that C# does isolate
application developers from the opacity of the underlying OS.  However, in the
long run, I think this leads to complex and fragile architectures that will get
trumped by simpler and more effective
solutions.



Standards
---------



As a tangent, I notice that library definitions in Python are filled with "doesn't
work the same in Windows."  To me, this implies that there's a right way, a
wrong way, and a Windows way.  While it may be popular and easy-to-use, it seems
to have problems.  



If the
documentation said "doesn't work the same in Linux", then I'd have to agree that
Windows is the standard for correctness.  But given that there's a POSIX
standard http://www.posix.com/posix.html and no Windows standard, I'm left to think
that the presence of a standard for the API's is one of the reasons for
innovation in this arena.



On the other hand, it could be simply that I watch the LAMP community more closely than the
Windows community.








