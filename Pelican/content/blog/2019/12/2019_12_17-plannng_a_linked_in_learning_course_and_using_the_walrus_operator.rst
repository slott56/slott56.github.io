Plannng a Linked-in Learning Course (and using the := walrus operator)
======================================================================

:date: 2019-12-17 08:00
:tags: #python,functional python programming,Data Science
:slug: 2019_12_17-plannng_a_linked_in_learning_course_and_using_the_walrus_operator
:category: Technologies
:status: published

I've recorded two courses for LinkedIn
Learning https://www.linkedin.com/learning/me


Let me emphasize that their production values take a lot of work.
While I think I'm a pretty good live presenter, a few days in the
recording booth with a producer, reveals all my weaknesses. so. um.
you know?


I'm starting down the road to at least one more, maybe another one or
two after that.


Which leads to code. Of course. And the code uses the assignment
expression ("walrus") operator.


Here's what's going on. I've got a directory full of CSV files with
the slide-by-slide scripts. Each file has a bunch of tabs, and the
relevant tables have a fixed heading that the production folks use.


::

      target_headings = ['Part', 'Voice', 'Visual Description', 'Storyboard / Description']


The "Voice" column in these tables is the script. Each row is a slide
or other visual. The overall management of the resources with all of
these spreadsheets doesn't seem ideal to me. However, it's the way
skilled professionals prefer to manage these multi-media assets.

The question is: "which sections are too long?"

Generally, we speak at a consistent rate. During rehearsals, I can
use my stopwatch to get timing for a particular script. This gives me
a seconds/word or words/second rate metric. Given an average rate,
and a script, I can predict a likely duration given the text of the
script.

The data is in spreadsheets -- generally the root cause of many
complications. There's no word-count in Numbers. So. Time to apply
Python. (I'm sure someone has a bunch of Excel macros that can do
word-counts. Good for you. I don't own a copy of Excel.)

Here's how this shakes out. There are three parts to the analysis,
modeling, and applying the model. The first is a functional flattener
to turn all of the files and tabs and tables into a single stream of
useful rows.

The Data Gathering
------------------

The essential data gathering has to flatten the relatively complex
file/sheet/table structure into something we can extract features
from. A sequence of the final text of the scripts is what we want.
Each script can be a mapping from the slide label to the voice
content. It's this content -- the script text -- where we'll find the
interesting features.

Here's how this starts.

::

      from pathlib import Path
      from fractions import Fraction
      import csv
      import re
      from typing import Tuple, Dict, Iterator, List

      sheet_table_pattern = re.compile(f"^(\w+): (.+)$")
      target_headings = ['Part', 'Voice', 'Visual Description', 'Storyboard / Description']

      def script_iter(source: Path) -> Iterator[Tuple[str, Dict[str, str]]]:
          for script_path in sorted(source.glob("*.csv")):
              # print(script_path)
              with script_path.open() as script_file:
                  reader = csv.reader(script_file)
                  row_iter = iter(reader)
                  for row in row_iter:
                      if len(row) == 1 and (match := sheet_table_pattern.match(row[0])):
                          if match and match.group(2).startswith('Table '):
                              headings = next(row_iter)
                              if headings == target_headings:
                                  section = match.group(1)
                                  text = {}
                                  # print(f"Analyzing {section}")
                                  for sub_row in row_iter:
                                      if len(sub_row) == 0:
                                          break
                                      dict_sub_row = dict(zip(headings, sub_row))
                                      text[dict_sub_row['Part']] = dict_sub_row['Voice']
                                  yield section, text

The outermost ``for`` statement locates all ``.csv`` files. All the rows
within a file will belong to a number of sheets and tables within
each sheet. The separator is a line with a Sheet: Table string,
described by the sheet_table_pattern. The second for statement picks
all the rows from a given sheet, looking for the separators.

There are a bunch of irrelevant tables. Hence the tall stack of
if-statements. The useful parts of the script all have names that
start with ``'Table '``. Weird, but true.

The ``match.group(2).startswith('Table ')`` check feels like some casual
ad-hoc test and should probably be made more visible and
configurable.

Once we've found a table with the right headings, we can iterate over
the following rows until we get to a blank line at end-of-table. We
accumulate a dictionary, named text, which has the 'Part' and 'Voice'
column values as a handy ``Dict[str, str]`` mapping.

Note that we're sharing an iterator, the row_iter variable, among two
for statements. This is a very handy trick when doing this kind of
partitioning. The outermost use of the iterator is rejecting
irrelevant rows. The inner use of the iterator is assembling
composite objects from a subset of rows, effectively partitioning the
raw data.

This *can* be decomposed into separate functions. Further
refactoring is left as an exercise for the reader.

The Benchmark Data
------------------

The result of benchmarking is a ``Fraction`` object with my unique
reading pace. And yes, a Fraction makes more sense than a float
value. We're working in int space, and introducing float seems wrong.

Here's the benchmarking to create a model.

::

      def rate() -> Fraction:
          Benchmarks = [
              {'time': 3*60 + 29, 'words': 568},  # 01_01
              {'time': 5*60 + 32, 'words': 732},  # 01_04
              {'time': 5*60 + 54, 'words': 985},  # 02_04
              {'time': 4*60 + 58, 'words': 663},  # 02_05
              {'time': 8*60 + 48, 'words': 1192},  # 03_02 (draft)
          ]
          time_bm = sum(b['time'] for b in Benchmarks)
          words_bm = sum(b['words'] for b in Benchmarks)
          time_per_word = Fraction(time_bm/words_bm)
          return time_per_word

For some sample sections, I read through the material in my best NPR
professional broadcasting voice. The sums of words and times give us
a time-per-word Fraction object. The resulting value is near 31
seconds for 75 words.

I really like using Fraction instead of float for this kind of
thing. The data doesn't support even one decimal place of supposed
accuracy.

Note that I didn't factor in any slide count. I **assumed** this is a
linear model from words to time. If I was a real scientist I might
have tried a bunch of models.

Applying the Model
------------------

The model is linear. It's a scaling factor applied to a specific
feature, the number of words. Here's one version of the code. I'm not
sure I like it.

::

      def main() -> None:
          time_per_word = rate()
          source = Path.cwd()
          print(f"script, slides, words, time")
          for script, body in script_iter(source):
              word_count = sum(len(text.split()) for text in body.values())
              slide_count = sum(1 for text in body.values() if len(text) > 0)
              m, s = divmod(int(word_count*time_per_word), 60)
              print(f"{script}, {slide_count}, {word_count}, {m}:{s:02d}")

There are three mappings going on here. This makes it a little tricky
to create a simple function to map from raw data to something the
model can use, then applying the model.

The 'word_count' is a mapping from raw data to one feature. The
'slide_count' is another mapping from raw data to a secondary
feature. The 'm' and 's' values represent another mapping from the
word_count to the estimated time.

We can hack this around to find another use for the assignment
operator.  But the following seems insane:

::

      divmod(int(word_count:=sum(len(text.split()) for text in body.values())*time_per_word), 60)

Let's not consider this assignment expression example as particularly
helpful. The above turns two simple statements into a mess.

Alternative Implementation
---------------------------

The relationships among the mappings can be built a pure functional
programming, but seems flirt with needless complexity. We can have a
pair of functions to map the body.values() to some named tuple with
feature values. We can use a third function to apply the model.

Something like this is an alternative that's slightly more
functional.

::

      class Features(NamedTuple):
          body: Dict[str, str]
          @property
          def word_count(self) -> int:
              return sum(len(text.split()) for text in self.body.values())
          @property
          def slide_count(self) -> int:
              return sum(1 for text in self.body.values() if len(text) > 0)
          def duration(self, time_per_word: Fraction) -> int:
              return int(self.word_count*time_per_word)

      def main_2() -> None:
          time_per_word = rate()
          source = Path.cwd()
          print(f"script, slides, words, time")
          for script, body in script_iter(source):
              details = Features(body)
              m, s = divmod(details.duration(time_per_word), 60)
              print(f"{script}, {details.slide_count}, {details.word_count}, {m}:{s:02d}")

I'm not sure this is dramatically "better". It isolates some aspects
of feature collection and model application. It also harbors a secret
inefficiency. The two feature values should be cached to avoid
recomputing them.

I'll leave the refactoring for the interested reader.
The durations over > 5:00 (300 seconds) need some rework. That's the
actual useful output: the list of scripts with excessive time becomes
the queue of content that needs rework.





