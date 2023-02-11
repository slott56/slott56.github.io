Jupyter Notebook for Tide Table Analysis
########################################

:date: 2023-02-14 08:00
:tags: #python,jupyter lab,functional programming,navigation
:slug: 2023_02_14-tide_table_analysis
:category: Architecture & Design,Books,Python
:status: draft

I'm undecided if this goes into the next book.
Maybe this is a teaser...
And yes, this is a **Python to the Rescue** story.

I live on a boat. See `Red Ranger Blog <https://itmaybeahack.com/TeamRedCruising2/index.html>`_ for details.
What's essential is this little complication.

The `South Gulf Cove Boat Lock <https://www.charlottecountyfl.gov/departments/public-works/maintenance-operations/south-gulf-cove-boat-lock.stml>`_.

The lock keeps saltwater from Charlotte Harbor out of the canal system
in South Gulf Cove.
The creek beyond the lock is subject to silting.
We'd like to be **sure** we don't run aground.

Filter Rules
============

There are two critical criteria for passing through the lock:

-   High tide.

-   In the afternoon.

The lock and the associated creeks and canals tend to silt
up over time. Water moves slowly through the water system.
High tide helps get us over the sandbars.

It's a bit over a three-hour trip from `Safe Cove Boat Storage and Marina <https://www.safecoveinc.com>`_
to the lock.
If we start at 06:00, we're not getting out before 10:00.
And.
Who wants to get up at 05:00 to prep for departure at first light?

(Okay. I've done that. See `Schooner Creek — Not our best idea <https://itmaybeahack.com/TeamRedCruising2/Schooner_Creek__Not_our_best_idea.html>`_.
It's not ideal, but we can make it work.)

How do we know when high tide is? NOAA provides that information.

Raw Data
========

The tides have a well-understood model.
This is a triumph of big-data analysis.

It leads to files like this:

https://tidesandcurrents.noaa.gov/noaatideannual.html?id=8725769

Okay. That's a right mess of data.

There's a big multi-line header.
It's followed by columns of details.
The details have slightly irregular tab characters, making parsing annoying.

Choices.

1. Load it into Numbers and fool with it more-or-less manually looking the afternoon high-tides we can make use of.

2. Load it into a Jupyter Lab Notebook.

It's a one-time thing, right?

Not exactly.

Every year, we're going to redo this little computation.

    I hear you. Once a year isn't very often.
    The principle is this: the manual steps are hard to record
    and reproduce.
    It's much, much more reliable to build a notebook for
    repeatable results.

I'll repeat that

    **Build a Notebook For Repeatable Results.**

Here's the essential features of that notebook.
It's a three-step process

1. Acquire
2. Clean
3. Analyze

We'll begin at the beginning: acquiring the raw data.

Step 1. Acquire
===============

Okay. The data was already downloaded. Done. Check.
We need to extract a meaningful structure from it.

First, strip that god-awful header.

::

    def header(source: TextIO) -> dict[str, str]:
        content = {}
        for row in source:
            if (clean := row.rstrip()) == '':
                break
            label, _, value = clean.partition(":")
            content[label] = value
        return content

This function extracts the header lines
to make a little dictionary with the metadata.
The value of ``metadata['StationName']`` is particularly
useful.

This changes the state of the ``source`` object.
It advances it to the first line after the header.
This line has the column titles.

(For some, this state change is a kind of functional programming no-no.
A proper functional approach might involve defining some kind
of monad that can be used to represent the file split,
preserving the order.)

The column titles are in wrong positions with regard
to the data. This offset makes them essentially useless except
as a visual cue.

Here's what we observe.

::

    tide_csv[0:2]

    [['Date ', '', 'Day', 'Time', '', 'Pred(Ft)', 'Pred(cm)', 'High/Low'],
     ['2023/01/01', 'Sun', '06:35 AM', '-0.13', '', '-4', '', '', 'L']]

We want columns 0, 1, 2, 3, 5, and 8.

Here's the first pass at a kind of named-tuple or dataclass
to structure the source text.

::

    from dataclasses import dataclass, field

    @dataclass
    class Tide:
        date: str
        day: str
        time: str
        pred_ft: str
        pred_cm: str
        high_low: str

        @classmethod
        def from_csvrow(cls, row):
            return cls(
                date=row[0],
                day=row[1],
                time=row[2],
                pred_ft=row[3],
                pred_cm=row[5],
                high_low=row[8]
            )

I'm a fan of including builders within the class
definition. With a tiny prevarication.

The ``from_csvrow()`` function is dependent
on something **outside** this class.
Therefore we can argue this breaks the **SOLID** design
principles -- this class has than one reason to change:
an internal representation change and an external parsing change.

(The Open-Closed principle still applies. Subclasses have have different parsers.)

If there are multiple sources, or the source is some hack
built as a temporary stop-gap as part of Enterprise software development,]
then separate parsers are helpful.

(Enterprise in-house programmers are sometimes told to build junk.)

This is from a government agency. Change will arise at a stately pace.
Including a parser/builder method in the class is fair because I *never* expect to see this source format change.

Step 2. Clean and Transform
===========================

There's only a little bit of this data we need:

-   The predicted height in feet "Pred(Ft)".
-   The timestamp built from "Date" and "Time".
-   The High/Low flag telling us the tide's state. We like to make trick transits **before** high-tide so the rising tide can help float us free of trouble.

The day, for example, is redundant and computed from the date.
The predicted height in cm is a multiplication.

We have two general approaches for this.

- For complex, fluid situations with multiple sources and formats, it helps to separate clean data from raw data. This means creating a secondary class, built from the raw ("all strings") source class. This class can have a more useful structure.
- For this kind of stable data, we can enrich the dataclass with ``init=False`` fields.

It looks like this.

::

    from dataclasses import dataclass, field
    from enum import Enum
    import datetime

    class HighLow(str, Enum):
        High = "H"
        Low = "L"

    @dataclass
    class Tide:
        date: str
        day: str
        time: str
        pred_ft: str
        pred_cm: str
        high_low: str
        timestamp: datetime.datetime = field(init=False)
        height: float = field(init=False)
        state: HighLow = field(init=False)

        @classmethod
        def from_csvrow(cls, row):
            return cls(
                date=row[0],
                day=row[1],
                time=row[2],
                pred_ft=row[3],
                pred_cm=row[5],
                high_low=row[8]
            )

        def __post_init__(self):
            date = datetime.datetime.strptime(self.date, '%Y/%m/%d').date()
            time = datetime.datetime.strptime(self.time, '%I:%M %p').time()
            self.timestamp = datetime.datetime.combine(date, time)
            self.height = float(self.pred_ft)
            self.state = HighLow(self.high_low)

The three ``field(init=False)`` attributes are **not** provided from the source.
These are derived.
The ``__post_init__()`` method computes the useful derived values.

These values can also be ``@property`` methods.
Indeed, they started out as properties.
There are only about 1200 rows of data, so the performance advantage of one-time computation is miniscule.

For completeness, here's the overall parser for this data.

::

    def tides(source_csv):
        for line in source_csv:
            if len(line) != 9:
                continue
            yield Tide.from_csvrow(line)

Given the list of CSV rows (or a generator for the CSV rows)
this will iterate over the rows, building ``Tide`` instances.

Step 3. When Do We Go?
=======================

Now, we can start analysis.
The fundamental question is this "When to we leave?"

The answer is "When the lock is passable."

::

    def passable(t):
        return all([
            t.state == HighLow.High,     # High tide
            11 <= t.timestamp.hour < 18  # Late morning and afternoon
        ])

We need to to know the high-tide time so we can back off three hours.
We need to arrive at the lock in daylight, and we don't want to get up at 05:00 (pre-dawn).

The final cell in this notebook?

::

    for t in tides(tide_csv):
        if passable(t) and t.timestamp.month in {3, 4, 5}:
            print(f"{t.timestamp} {t.height:6.2f} {t.state.name}")

This tells us what we need to know about making the lock
in daylight with a good probability of enough water out in the harbor.

We still have to fix Hurricane Ian damage.
We're not 100% the engine will start.
The solar panels are a wreck.

And.

We don't know where we might go.
A lot the South Florida Gulf Coast is still a right-awful mess.

Maybe all we'll be able to do is
drop the anchor at `Punta Gorda <https://activecaptain.garmin.com/en-US/pois/46419>`_ for a month.
