Ouch, this is going to hurt
===========================

:date: 2006-01-11 12:06
:tags: spreadsheet,database
:slug: 2006_01_11-ouch_this_is_going_to_hurt
:category: Management
:status: published






While some spread-sheet
use is civilized numerical stuff, and other spread-sheet use is merely personal
organization, too much spread-sheet use is the poor-person's database management
system.  I call it the Spreadsheet Schema (SSS), different from normalized
relational schema and star
schema.



There is a serious problems
with people using spreadsheets as databases, and this has a number of
consequences.  Principally, the SSS isn't normalized, and doesn't allow for the
"Update Anomaly" problem.  Consequently, breakage is
inevitable.



1.  People do global find
and replace operations.  Failure to make a global change breaks a relationship. 
Now the manually tweaked rows have one set of relationships, while the rows
which were missed have a different
relationship.



2.  Small data quality
issues cause the procedure to break down.  I misspelled Mississippi on just one
row, and my global replace hits all but that one. 




3.  Spreadsheets are two-dimensional,
where the world is multi-dimensional.  The lesson learned from star-schema
design is that a 5-dimensional hypercube is often what we're talking about, and
a two-dimensional pivot table is a handy way to boil that information down to
something useful.



This is not an
indictment of the JotSpot Tracker's ability to absorb a spreadsheet.  It's the
elevation of spreadsheet to surrogate database that's the problem.  JotSpot just
makes it visible, and makes the resulting problems
inevitable.



Sadly, here's the saga as
it plays out on a daily basis.



First,
someone has an idea and slaps together a spreadsheet.  The boss and the rest of
the working group love it and use it.  It works, it's
great.



Then, someone extends the idea,
expands the spreadsheet and hits a wall.  Either the normalization problem
stings them or the multi-dimensionality stings them.  Or they get to so many
columns they can't manage it, or so many rows it takes 5 minutes to open, or
worse.  Worse, for example, is someone corrupting it and no one kept
backups.



So, they call in-house
computer folks to turn the spreadsheet into application software.  They can't
articulate all the use cases very clearly (since a spreadsheet doesn't enforce
much discipline) and when in-house IT wants to talk about it, the meetings drag
on, the costs rise.  It takes more time to explain it than it did to slap it
together and start using it.



Then, of
course, IT slaps on all the "missing" functionality to make a "real system" and
then begins to build the thing using the least effective set of tools ever
purchased as a corporate standard.  Meanwhile, the meetings to talk about use
cases have caused some thinking and use of the spreadsheet morphs while the
"real system" is being built.  Costs rise, the official IT version isn't very
good and the whole project collapses into
finger-pointing.



Someone calls in the
consultants.  I look at the situation, develop a plan, write up a statement of
work, and get thrown out on my ear.  Here's what I hear as I'm being flung down
the stairwell: "It didn't cost us that much to build it the first two
times!"








