Making a bad problem worse
==========================

:date: 2010-09-24 08:14
:tags: complexity,software design,database design,SQL
:slug: 2010_09_24-making_a_bad_problem_worse
:category: Technologies
:status: published

Imagine that you're a beer distributor who provides "just-in-time" beer
by type. You don't take orders for a specific brand, you take orders a
type: stout, lager, India pale ale, etc. You resolve the bill based on
what you actually delivered.

This can be kind of complex. However, there's no call for being crazy
about it. Yet, before we get to the end of this saga, it will get
crazy.

Your fulfillment (or "order-to-ship") process is rather complex.
There's the order as placed and there's the actual products that
got shipped. Your invoicing is also rather complex because you
have to reconcile the order with the fulfillment and the final
delivery.

Recently, I saw a piece of a "database" design for software
used to support this kind of business. The design was so
dysfunctional that there were heated arguments about how to
proceed.

Note that the real business with the dysfunctional database deals
in intellectual property, not beer. The fact that they deal in IP
instead of tangible assets seems to make them easily confused. One
thing I've heard -- but haven't seen -- is that they **update**
the order during the fulfillment process. After all, the
customer's order **should** match the invoice, right? Yes, but. In
this business, the fulfillment will diverge from the order; it
makes more sense to create a mapping from invoice to order than to
rewrite the order.

Not the Crazy Part
------------------

The hellish thing that I saw was the many-to-many association
between order and beer type. A many-to-many isn't bad. What they
did, however, was really bad. But not crazy. Not yet.

It's a many-to-many table. Order has one or more Beer Types. A Beer
Type can appear on any number of Orders. Could be simple.

In the world of atoms (tangible goods, not services) there's a pretty
standard model where an order is a composite object with multiple
line items. Each line item has a reference to a product. For this
business, each line item would have a reference to a product type,
instead of a specific product.

In a sensible software solution, there'd also be an invoice as a
composite object; separate from the order. Only a customer can change
an order. The invoice, however, would grow and change throughout the
fulfillment process. The invoice, like the order, would have multiple
line items. Each invoice line item would reference two things: the
product actually delivered, and the order line item that this product
fulfilled. This could include some "justification" or "rationale"
showing how the fulfillment matches the order.

Because the real business didn't separate order and invoice -- and
instead tried to massage the order to also be an invoice -- what they
had was a table with flags and 10 (ten, yes ten) business rules that
resolved whether or not this type of beer was or was not part of the
order.

I'll summarize. The many-to-many table had two columns with flag
values and ten business rules to interpret those flag values to
determine what the was ordered and what was fulfilled. Two columns of
flags. Ten rules. But that's not the crazy part.

Bad Data
--------

A database that requires ten business rules and procedural processing
to interpret the data is bad. It gets worse, however.

One of the ten business rules is a tie-breaker. The process that
fulfilled orders was so badly broken that it could (and did) create
multiple, conflicting invoice-to-type association rows. I was
shocked: multiple, conflicting invoice-to-type association rows. Rule
10 was "in the event of a tie, there's 'bad data', pick a row and
keep going."

There's "bad data"? Keep going? I would think this would be a
show-stopper. Whomever wrote the application that created the bad
data needs career guidance (guidance as in, "you're fired".)

It's Broken, But...
-------------------

Clearly, any database that requires ten procedural business rules is
not much of a database. A SQL query cannot be used to produce either
order or invoice. To fetch an order or an invoice requires a
procedure so complex that the organization cannot even figure out
what programming language to use.

*A procedure so complex that the organization cannot even figure out
what programming language to use.* Really.

The DBA's say it can be done as a stored procedure. And they have a
worse plan, too. We'll get to that.

The programmers want to do this in C# because -- clearly -- the
database is broken.

If you can't agree on the implementation, you've got big, big
problems.

The Crazy Part
--------------

The pitch from one of the DBA's was to add yet more complexity. There
are two flag columns and ten business rules to resolve nuances of
order and fulfillment. This is a mistake which requires someone sit
down and work out a fix.

Instead, the DBA pitched using Oracle's analytic functions to make
the complex procedural processing look like "ordinary" database
processing.

Wait, what?

That's right. Take a database design so complex that it's
dysfunctional and add complexity to it.

Call me crazy but anyone who uses Oracle analytic functions on this
problem now has two problems. They've got a analytic layer that only
one DBA understands. This wraps a broken many-to-many table that
(apparently) no one understands.

None of this reflects the actual business model very well, does it?

Bottom Line
-----------

If the database does not (1) reflect the actual business model and
(2) work in simple SQL, it's broken. Adding technology to a broken
database makes it more complex but leaves it essentially broken.

Stop. Adding. Complexity.



-----

Sounds scary. Couple typos for you: http://www.eme...
-----------------------------------------------------

John Tantalo<noreply@blogger.com>

2010-08-25 14:13:40.080000-04:00

Sounds scary. Couple typos for you:
http://www.emendapp.com/sites/slott-softwarearchitect.blogspot.com


you just describe magento's EAV design.

Just ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-08-25 17:29:19.932000-04:00

you just describe magento's EAV design.
Just admit it. You had a client who wanted to use Magento for services
rather than products.





