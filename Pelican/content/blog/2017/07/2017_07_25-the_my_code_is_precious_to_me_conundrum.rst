The "My Code Is Precious To Me" Conundrum
=========================================

:date: 2017-07-25 08:00
:tags: Design Principles
:slug: 2017_07_25-the_my_code_is_precious_to_me_conundrum
:category: Technologies
:status: published

I suspect some people sweat so hard over each line of code that it
becomes precious. Valuable. An investment wrung from their very soul. Or
something.
When they ask for comments, it becomes difficult.
The Pull Request context can be challenging. There the code is, beaten
into submission after Herculean toils, and -- well -- it's not really
very good. The review isn't a pleasant validation with some suggested
rewrites of the docstrings to remove dangling participles (up with which
I will not put.) Perhaps the code makes a fundamentally flawed
assumption and proceeds from there to create larger and larger problems
until it's really too awful to save.
How do you break the news?
I get non-PR requests for code reviews once in a while. The sincere
effort at self-improvement is worthy of praise. It's outside any formal
PR process; outside formal project efforts. It's good to ask for help
like that.
The code, on the other hand, has to go.
I'm lucky that the people I work with daily can create -- and discard --
a half-dozen working examples in the space of an hour.
I'm unlucky that people who ask for code review advice can't even think
rationally about starting again with different assumptions. They'd
rather argue about their assumptions than simply create new code based
on different (often fewer) assumptions.
I've seen some simple unit conversion problems turned into horrible
messes. The first such terrifying thing was a data query filter based on
year-month with a rolling 13-month window. Somehow, this turned into
dozens and dozens of lines of ineffective code, filled with wrong edge
cases.
Similar things happen with hour-minute windows. Lots of wrong code.
Muddled confusion. Herculean efforts doing the wrong thing. Herculean.
Both year-month and hour-minute problems are units conversion.
Year-month is months in base 12. Hour-minute is minutes in base 60.
Technically, they're mixed bases, simple polynomials in two terms. It's
a multiply and an add. 12\ *y*\ +\ *m*, where 0 ≤ *m* < 12. Maybe an
extra subtract 1 is involved.
The entire algorithm is a multiply and an add. There shouldn't very many
lines of code involved. In some cases, there's an additional conversion
from integer minutes to float hours. Which is a multiply by a constant
(1/720.) Or integer months to float years after an epochal year (another
add with a negative number and multiply by 1/12.)
I think it's common that ineffective code need to be replaced. Maybe
it's sad that it has to get replaced \*after\* being written? I don't
think so. All code gets rewritten. Some just gets written sooner.
I think that some people may need some life-coaching as well as code
reviews.
Perhaps they should be encouraged to participate in a design
walk-through before sweating their precious life's blood into code that
doesn't solve the problem at hand.





