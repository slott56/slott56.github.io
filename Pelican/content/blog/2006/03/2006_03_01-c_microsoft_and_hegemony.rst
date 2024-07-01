C#, Microsoft and Hegemony
==========================

:date: 2006-03-01 01:26
:tags: microsoft,perl,c-sharp
:slug: 2006_03_01-c_microsoft_and_hegemony
:category: Management
:status: published





First, I've had some opinions on this "one
language" ideal `After PERL what? <{filename}/blog/2006/01/2006_01_27-after_perl_what_revised.rst>`_.  We have a variety of languages for a
good reason: the languages express different kinds of things.  Shell command
languages really have little to do with markup languages, database manipulation
languages or "general-purpose" programming
languages.



One of the C#/LINQ issues is
to collapse some higher-level predicates into the programming language.  The
problem is that predicates mean loops and loops mean proof of termination and
those proofs are impossible in general. 




Further, there is the difficulty in
optimizing those predicate loops.  Oracle has had years to work out cost-based
optimization, and it is still looked on with suspicion. 




If you have no persistent data, how do
you do optimization?  You have to know something about the data and the
algorithms.  This makes general-purpose predicates not terribly useful.




When looking at C# from a distance, I
have to ask about innovation in the Windows world.  Are there barriers or is it
my personal bias?



I think there are
barriers.  



First, and foremost,
everything in Windows world must play with the obscure and rapidly-evolving
Windows OS API's.  The lack of clarity and stability in the closed-source API's
is a barrier to innovation.



Second, you
are competing against Microsoft.  If your idea is good, it will show up in a
competing closed-source MS product.  While good for your idea, the innovation is
effectively clamped off once it becomes a closed-source product
offering.



Third, almost everything has
a large fee associated with it.  The tools, the platform and the libraries all
cost real money.  This is, I think, the reason why the open source folks have an
edge -- they can work for free.



I'm
happy that I don't have to sweat the details of this .NET, C#, LINQ, CLI,
Managed Code world.  Oracle's OAS, OC4J is complex enough, and much of it is
open source.  I can't imagine how I'd make a complex closed-source environment
work.








