Dumb Info Security
==================

:date: 2010-04-05 15:07
:tags: security
:slug: 2010_04_05-dumb_info_security
:category: Technologies
:status: published

A truly great question came up the other day.

    "Why change passwords every 90 days? What is the threat scenario
    countered by that policy?"

Of course strong password policy means constantly changing passwords.
Right?

Then I started to think about it. What -- actually -- does a password
change protect you against?

The answer, it appears, is nothing. Changing passwords is largely a
waste of time and money. I suppose that a password change prevents
further abuse of the account. But generally, the abuse is not
ongoing. Once in to a system, the trick is to create an additional
privileged account that does not belong to any real user; all the
password changes in the world have no effect.

This post is spot-on: "`Password rules: Change them every 25
years <http://isc.sans.org/diary.html?storyid=7510>`__"

In short, there's no threat that's actually countered by changing
passwords. However, it's on everyone's checklist.

    [Look at http://passcracking.com/hybrid.html for information on
    rainbow table attacks. The time required is on the order of 10
    minutes.]

Since a weak password is broken in well under 90 days, there's no
"moving target" to this. A weak password is -- effectively --
broken instantly compared to the 90-day password change. Once
broken, the machine's freely available for -- on average -- 45
days.

The comments on this post are helpful also. Most people agree that
password changes do not have any possible impact on security.
Except that it gives security managers a chance to improve the
rules and enforce everyone to change their passwords to meet the
new rules.

Missing the Point
-----------------

One comment that's interesting is this:

    You've made two assumptions: 1) all password thieves will give
    up after a few tries in the case of brute-force attack, and 2)
    all thieves will give up after a few tries in the case of
    dictionary attacks.

This misses the point entirely. These two assumptions are not
*overlooked* by this posting. They're not part of it at all. None
of this is based on password thieves giving up.

Changing a password does not materially impact the thieves'
ability to crack a password. Phishing, and Key Logging always
work, no matter how often the password is changed.

A dictionary attack is trivially defeated by disabling the account
after a few failures. Changing the password is of no relevance at
all.

A rainbow table to undo a hashed password is defeated by using
long salt strings with the hash. Changing passwords every 90 days
has nothing to do with this, either. There's no "moving target"
concept, since a rainbow table attack takes much less than 90
days.



-----


Unknown<noreply@blogger.com>

2010-03-29 16:14:51.793000-04:00

This comment has been removed by a blog administrator.


Amen.  I wish more people would get this.
-----------------------------------------

Kevin H<noreply@blogger.com>

2010-03-29 12:10:34.157000-04:00

Amen. I wish more people would get this.


I agree with you 100%, but there are a few things ...
-----------------------------------------------------

Cade<noreply@blogger.com>

2010-03-29 12:44:03.339000-04:00

I agree with you 100%, but there are a few things (opportunistic
attacks) it protects against (which are flaws caused by bad account
management or the regular password expiry concept itself!):

People finding an old written down password taped under the desk.
Written down in the first place, because changing passwords and have
crazy password schemes makes people write down their passwords.

People using an old account which someone forgot to disable or notify
admainstrators to be disabled. This is only a problem when you aren't
managing your accounts properly in the first place. The nature of the
password age shouldn't matter - accounts have to be disabled as soon as
they shouldn't be used.

I guess you could argue defense-in-depth in the second case, but the
problems that regular password expiry causes are huge.

As long as security auditors have password expiry as a check box on
their lists, it's going to keep causing millions of dollars in
productivity waste and security problems for years to come.


Along these same lines, check out

My Top 5 Cyber ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-04-02 07:34:31.149000-04:00

Along these same lines, check out
My Top 5 Cyber Fallacies
Written by Jeffrey Carr
http://intelfusion.net/wordpress/2010/03/28/my-top-5-cyber-fallacies/


Because it provides a moving target.

See my reply...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-04-04 09:56:30.193000-04:00

Because it provides a moving target.
See my reply to
http://architects.dzone.com/news/dumb-info-security


After reading this post, I remember my cousin&#39;...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-07-30 02:40:38.844000-04:00

After reading this post, I remember my cousin's website that has a
malfunctioning "registry button" in the main page. Some clients
contacted him repeatedly since the "sign-in" button doesn't work for
them while they are registering in the website.

In that case, he researched for the best `web development
(Toronto) <http://www.modulusmedia.ca/toronto-web-development>`__
company to fix his website that would focus not only with the design but
also with its usability, and fast page loading time. I must say that the
`web designer
Toronto <http://www.modulusmedia.ca/web-designer-toronto>`__ that was
assigned to him did a remarkable job setting up his website. After a
month, there were no more calls or e-mails from clients reporting any
bugs and errors on his website.

I certainly enjoy reading your posts. Great job!





