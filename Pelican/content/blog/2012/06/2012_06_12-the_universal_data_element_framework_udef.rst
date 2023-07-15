The Universal Data Element Framework (UDEF)
===========================================

:date: 2012-06-12 08:00
:tags: #python,software design,UDEF
:slug: 2012_06_12-the_universal_data_element_framework_udef
:category: Technologies
:status: published

Okay.  This is seriously cool.

The Universal Data Element Framework (UDEF)  provides a controlled
vocabulary that should be used to seed a project's data model.

See http://www.udef.com/

See http://www.opengroup.org//udef/

We're looking at applying UDEF retroactively to an existing schema.

What a pain in the neck!

Step 1.  Parse the table names.  In our case, they're simply
CONTIGUOUSSTRINGSOFCHARS, so we have to work out a quick lexicon and use
that to break the names into words.  Then we can find the obvious
aliases, spelling mistakes and noise words.  'spec', 'quanitity' and
'for' are examples of each.

Step 2.  Look up the various words in the UDEF vocabulary to create
candidate matches.   Since each individual word is matched, each table
will have multiple candidate matches to seed the analyst's thinking.

Step 3.  Manually pick UDEF standard names or create internal extensions
to the standard for the problem domain or enterprise unique features.
Do a similar thing for the column names.  In that case, they're
CamelCaseWithSomeACRONYMS.  This is slightly easier to parse, but not
much.

Eventually, we have to apply real human business analyst grey matter to
locating standard names which might fit with the host of legacy names.

Here's the column name parser.

::

    def property_word_iter( prop_name ):
        """Find words via case changes.

        -   Lower to upper ends a word.
        -   Upper to lower ends a word.  However.
            Sometimes the Upper is an acronym that was all caps.
            A lookahead is required to disambiguate.
        """
        cc_iter= iter(prop_name)
        word=[ next(cc_iter) ]
        for c in cc_iter:
            if c.isdigit():
                yield ''.join(word)
                yield c
                word=[ next(cc_iter) ]
            if word[-1].islower() and c.islower():
                word.append(c)
            elif word[-1].isupper() and c.isupper():
                word.append(c)
            elif word[-1].islower() and c.isupper():
                yield ''.join(word)
                c2= next(cc_iter)
                if c2.isupper():
                    word= [c, c2]
                else:
                    word= [c.lower(), c2]
            elif word[-1].isupper() and c.islower():
                c0 = word[-1]
                yield ''.join(word[:-1])
                word= [c0.lower(), c]
            else:
                raise Exception( "What? {0!r} {1!r}".format( word[-1], c ) )
        if word:
            yield ''.join(word)



