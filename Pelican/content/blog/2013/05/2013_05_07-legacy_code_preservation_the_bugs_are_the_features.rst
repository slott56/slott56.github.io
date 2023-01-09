Legacy Code Preservation: The Bugs Are The Features  
=====================================================

:date: 2013-05-07 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_05_07-legacy_code_preservation_the_bugs_are_the_features
:category: Technologies
:status: published

The extreme end of "paving the cowpaths" are people for whom the bug
list is also the feature list.

This is a very strange phenomenon, rarely seen, but still relevant to
this review.

In this particular case, the legacy application was some kind of
publishing tool. It used MS-Word documents with appropriate style
tags, and built documents in HTML and PDF formats from the MS-Word
document. Badly.

To begin with, problems with MS-Word's style tags are very difficult
to diagnose. Fail to put the proper style tag around a word or phrase
and your MS-Word source file looks great, but it doesn't produce the
right HTML or PDF.

More importantly, the PDF files that got created were somewhat
broken, having bugs with embedded fonts and weirdness with
downloading, saving locally and printing.

And--of course--the vendor was long out of business.

What to do?


.. rubric:: Feature Review
   :name: feature-review

In order to replace this broken publishing app, we need to
identify what features are essential in the HTML and PDF output.
This shouldn't be rocket science.

For instance, there may be inter-document links that should be
magically revised when a document moves to a new URL. Or, there
must be embedded spreadsheets. Or there have to be fill-in forms
that can be printed.

The editor who worked with this tool could not---even after
repeated requests---provide a list of features.

Could not or would not, it didn't matter.

Instead, they had a list of 20 or so specific bugs that needed to
be fixed.

When we tried to talk about locating a **better** publishing
package, all the editor could bring to the table was this list of
bugs.

For example: "The downloaded document has to have the proper flags
set so that it uses local fonts."

We suggested that perhaps this should include "Or it has all the
fonts embedded correctly?"

We were told---firmly---"No. The local fonts must be used or the
document can't be saved and won't print."

Trying to explain that this font bugs doesn't even exist in other
packages that create proper PDF's went nowhere. There was a
steadfast refusal to understand that the bugs were not timeless
features of PDF creation. They were bugs.

Several meetings got sidelined with the Bug List Review.

Eventually, the editor had to be reassigned to something less
relevant and visible. A more rational editor was put into the
position to work with a technology team to bring in a new package
and convert the legacy documents.

.. rubric:: The Confusion
   :name: the-confusion

It's not easy to see where the confusion between feature and bug
comes from.

Why did the desirable feature set become a murky unknown? An
editor should be able to locate the list of styles actually used
and what those styles did in the resulting documents.
The confusion and bizarre behavior could possibly stem from the
stress or terror.

Perhaps learning a new package was too stressful.
Perhaps idea of converting several dozen complex documents from
MS-Word to some other markup was terrifying. So terrifying that
roadblocks needed to be put in place to prevent meaningful
discussion of the conversion effort.

Where was the business knowledge encoded? What needed to be
preserved?

Not the software. It was junk.

There was business knowledge represented in the documents in the
obvious way. But there was also some business knowledge encoded in
the markup that established links and references, emphasis,
spreadsheets, forms or whatever other features were being used.

Any semantic markup encodes additional knowledge above and beyond
the words being marked up. The semantic markup was what needed to
be preserved during the conversion. Maybe this was the source of
the terror and confusion.






