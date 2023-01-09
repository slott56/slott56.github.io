Handling Irregular File Formats
===============================

:date: 2016-11-28 08:05
:tags: #python,regular expressions,physical format,logical layout
:slug: 2016_11_28-handling_irregular_file_formats
:category: Technologies
:status: published


This is a common issue. We have a file which was printed for human
consumption. Consequently, it has many different kinds of lines.

These are the two kinds of lines of interest:

    900296268 4/9/16 Mobility, Data Mining and Privacy Expired

    900295204 4/1/16 Pro .NET Best Practices
    Expired

The first is a single physical line.  It has four data elements. The
second is two physical lines. The first has three data elements.

There are a number of other noise lines in the file which must be
filtered out.

The first "solution" pitched to me could be summarized with this:

**Move "Expired" on a line by itself to the previous line**

That was part of the email subject line. The body of the email was
some whining about regular expressions. Which I mostly ignored.
Multiline regular expressions are their own kind of challenge.

We (should) all know
this: https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/

Let's do this without regular expressions. There are two things we
need to know. One is buffering, and the other is the best way to split
each line. It turns out that there are spaces as well as tabs, and can
can, by splitting on tabs, make a lot of progress.

Instead of the good approach, I'll pick the other approach that
doesn't involve splitting on tabs.

Here's the simulated file, with data lightly redacted.

::


    sample_text = '''
    "Your eBooks"

    Show 200


    Page: 1


    Order # Date Title Formats Status Download
    -------
    xxx315605 9/30/16 R for Cloud Computing Available


    xxx304790 6/21/16 Java XML and JSON Available
    xxx304790 6/21/16 Accelerated DOM Scripting with Ajax, APIs, and Libraries Available

    xxx291633 2/28/16 Practical Google Analytics and Google Tag Manager for Developers
    Expired
    '''

It's not perfectly obvious (because of line wrapping) but there are
three examples of the "all-complete-in-one-line" records. There's one
example of the "two-lines" record.

Rather than mess with the file, we'll build a file-like object with
our sample data.

::

    import io

    file_like_object = io.StringIO(sample_text)

I like this because it lets me write proper unit test cases.

The file has four kinds of lines:

-  Complete Records
-  Record Headers (without Available/Expired)
-  Record Trailers (only Available/Expired)
-  Noise



We'll create some decision rules for the two obvious kinds of file
lines: complete records and trailers. We can deduce the headers based
on a simple adjacency rule: they precede a trailer. The fourth kind of
lines are those which are possible headers but are not immediately
prior to a trailer.

::

    def complete(words):
        return len(words) > 3 and words[-1] in ('Available', 'Expired')

    def trailer(words):
        return len(words) == 1 and words[0] in ('Available', 'Expired')


We can spot these two kinds of lines easily. The other kinds require a
Buffered Generator.

::

    def emit_clean(source):
        header = None
        for line in (line.strip() for line in source):
            words = [w.strip() for w in line.split()]
            if len(words) == 0: continue
            if complete(words):
                yield(line)
                header = None
            elif trailer(words) and header:
                yield(header + '\\t\\t' + line)
                header = None
            else:
                # Possible header
                # print('??', line)
                header = line

The Buffered Generator is a way to implement a "look ahead one item"
(LA1) algorithm. We do this by buffering rows. When we get to the next
row we can use the buffered row and the current row to implement the
look-ahead logic.

The actual implementation uses a look-behind buffer, header.

The (line.strip() for line in source) generator expression strips away
leading and trailing spaces. This gets rid of the newline characters
at the end of each input line.

The default behavior of split() is to split on whitespace. In this
case, it will create a number of words for complete records or header
records, and a single word for a trailer record. If we had split on
tab characters, some of this logic would be simplified.

That's left as an exercise for the reader.

If the len(words) is zero, the line is blank.

If the line matches the complete() function, we can yield it as one of
the iterable results of the generator function. We also clear out the
look-behind buffer, header.

If the line is a trailer and we have a buffered look-behind line, this
is the two-physical-line case. We can assemble a complete record and
emit it.

Otherwise, we don't know what the line is. It's a possible header
line, so we'll save it for later examination.

This algorithm involves no regular expressions.

With Regular Expressions
------------------------




An alternative would use three regular expressions to match the three
kinds of lines.

::

    import re

    all_one_pat =
      re.compile("(.*)\\t(.*)\\t(.*)\\t\\t((?:Available)|(?:Expired))")
    header_pat = re.compile("(.*)\\t(.*)\\t(.*)")
    trailer_pat = re.compile("((?:Available)|(?:Expired))")


This has the advantage that we can then use the groups() method of
each successful match to emit useful data instead of text which needs
subsequent parsing. This leads to a slightly more robust process.

::

      def emit_clean2(source):
          header = None
          for line in (line.strip() for line in source):
              if len(line) == 0: continue
              all_one_match = all_one_pat.match(line)
              header_match = header_pat.match(line)
              trailer_match = trailer_pat.match(line)
              if all_one_match:
                  yield(all_one_match.groups())
                  header = None
              elif header_match and not header:
                  header = header_match.groups()
              elif trailer_match and header:
                  yield header + trailer_match.groups()
                  header = None
              else:
                  pass # noise

The essential processing involves seeing which of the regular
expressions match the line at hand. If it's all-in-one, this is good.
We can yield the groups of meaningful data. If it's a header, we can
save the groups. If it's a trailer, we can combine header and trailer
groups and yield the composite.


This has the advantage of explicitly rejecting noise lines instead of
treating each noise line as a possible header.





