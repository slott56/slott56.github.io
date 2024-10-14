DBLock Context Manager
######################

:date: 2024-03-10 08:01
:tags: database,dbm,shelve,multiprocessing,context manager
:slug: 2024-03-10-dblock-context-manager
:category: Python
:status: published


Consider, for a moment, the ``shelve`` and ``dbm`` packages for storing things in a “database.”
Built-in. Lightweight. The database is essentially a mapping from identifiers to objects.
It can be quite nice.

The ``shelve`` module directly puts Python objects in a file.
It’s an ideal database structure for Python, with relatively little overhead.

If you don’t like using ``pickle``, you can use the underlying ``dbm`` with something like Pydantic for class definitions.
This means explicitly serializing a representation of object state as bytes before stuffing them into the ``dbm``-managed mapping.
Pydantic class definitions can deserialize the bytes and recover the object's state.

With a little effort at designing keys, these provide a persistent mapping for arbitrarily complex objects.
(Simple UUID's are nice, but sometimes it helps to provide a key with two parts: collection name and identifier.)

Why?

It lets you read and write objects without the complexity of an ORM layer and a SQL database.

This is often really helpful. But. What about concurrent writes in a multiprocessing context? The ``shelve`` page is clear:

    * The shelve module does not support concurrent read/write access to shelved objects. (Multiple simultaneous read accesses are safe.) When a program has a shelf open for writing, no other program should have it open for reading or writing. **Unix file locking can be used to solve this**, but this differs across Unix versions and requires knowledge about the database implementation used.

(Emphasis mine.) Okay. We get it; this is BYOL™  -- Bring Your Own Locking.

Which — it turns out — isn’t trivial.
See `https://en.wikipedia.org/wiki/Readers–writer_lock <https://en.wikipedia.org/wiki/Readers–writer_lock>`_ for information on multiple readers and single writers.

The Single Writer Locking Problem
=================================

We can use the ``fcntl`` module to lock files. This module (and the Linux OS) offers exclusive locks and shared locks.

(For Windows folks, get a package like ``portalocker`` or use the functions in ``pywin32``.)

The objectives are these:

* Take out an exclusive lock for transactions that will update the database.

* Take out a shared lock for transactions that read the database.

This Shared vs. Exclusive locking is elegant, but also habors a small problem.

Consider a web server. Each GET transaction acquires a shared lock, reads the data, prepares the response, and releases the shared lock. Because the shared lock prevents a writer from getting an exclusive lock, the data is untouched for the duration of the transaction.
There's no possibility of data file corruption mid-transaction because of a concurrent write.

Each POST/PUT/PATCH/DELETE transaction acquires an exclusive lock, reads and writes the data, prepares a response, and releases the exclusive lock. This forces the writer to wait for readers to finish. It prevents any reader from seeing incomplete
or uncreadable files.

The underlying ``dbm`` file is updated in one smooth, atomic event. Everyone sees the data in a consistent state at all times.

Yes, it's coarse-grained whole-database level locking. The point was to avoid the overheads of a huge SQL
server. A RESTful service can read and write local files. Emphasis on the read. Why have a super-elaborate database server
to provide rows and tables that have to be assembled into JSON documents? Maybe just read the JSON document from the database
and reply with it.

But.

There's a problem: a parade of readers can prevent the writer from getting in.

..  csv-table::
    :header: time,action,lock count

    T0,reader 1 starts,1 shared lock
    T1,reader 2 starts,2 shared locks
    T2,writer 3 waiting for an exclusive lock...,
    T3,reader 2 finishes,1 shared lock
    T4,reader 4 starts,2 shared locks
    T5,reader 1 finishes,1 shared lock

And so it goes: a sequence of overlapping readers will starve the writer.
This is called **Livelock**, and — while rare — it’s not impossible.

Preventing Livelock
=================================

One algorithm for preventing livelock is to have a “pending writer queue” that the readers have to acknowledge.

    Think of a velvet rope to get into the most exclusive club in town.

    The writer talks to the bouncer, and the line of readers is stopped. No one gets in. Once the club is empty of readers, the writer is allowed in and has the place to themself. When they’re done writing, then they’re out of there, so the readers can crowd the place again.

This is sometimes called the “preferred writer” solution. It’s unfair by design because many web requests are read requests; write requests are less common. Overall performance depends on getting any write out of the way as soon as possible.
There are other variants that are more equitable, but also a bit more complicated.

To prevent livelock, we need some kind of shared queue to broadcast to all concurrent processes that there’s a writer waiting.

We can do this using two lock files:

-   A “queue” lock. This is always Exclusive. It's always acquired first. In effect, it's a one-element queue.

-   The “working” lock. The working lock is either Shared or Exclusive.

The queue lock defines a mutual exclusion zone of code (called a *mutex*) where at most one process is able to run.
The idea is readers enter the mutex, get their shared working lock, and leave the mutex.
Once they have their shared lock, they can loiter, doing whatever it is they need to do.

When a writer enters the mutex, they have to wait for their exclusive working lock before they leave the mutex.
This stops the readers.

Here are some play-by-play views for a number of scenarios.

Reader following Readers
~~~~~~~~~~~~~~~~~~~~~~~~

Readers can get shared access freely.

..  csv-table::
    :header: time,action,queue lock,working lock

    T0,reader 1 acquire queue,1 ex,
    T1,reader 2 waiting,1 ex,
    T2,reader 1 acquire working,1 ex, 1 sh
    T3,reader 1 release queue,0 ex, 1 sh
    T4,reader 2 acquire queue,1 ex, 1 sh
    T5,reader 2 acquire working,1 ex, 2 sh
    T6,reader 2 release queue,0 ex, 2 sh
    T7,reader 1 release working,0 ex, 1 sh
    T8,reader 2 release working,0 ex,

And so it goes, readers acquiring and releasing working locks.

Reader following Writer
~~~~~~~~~~~~~~~~~~~~~~~

If there's a writer, the reader is forced to wait until
the writer releases their exclusive lock.

..  csv-table::
    :header: time,action,queue lock,working lock

    T0,writer 1 acquire queue,1 ex,
    T1,reader 2 waiting,1 ex,
    T2,writer 1 acquire working,1 ex, 1 ex
    T3,writer 1 release queue,0 ex, 1 ex
    T4,reader 2 acquire queue,1 ex, 1 ex
    T5,reader 2 waiting,1 ex, 1 ex
    T7,writer 1 release working,1 ex,
    T8,reader 2 acquire working,1 ex, 1 sh
    T9,reader 2 release queue,0 ex, 1 sh
    T10,reader 2 release working,0 ex,

Yes. Traffic will back up waiting for a writer.
If this is a problem, then finer-grained locking is required.
This can lead to the possibility of deadlocks; proceed with caution and consider sharding the data to avoid
contention for locks,

Writer following Reader
~~~~~~~~~~~~~~~~~~~~~~~

If there's a reader, the writer is forced to wait before they
can get their exclusive lock.


..  csv-table::
    :header: time,action,queue lock,working lock

    T0,reader 1 acquire queue,1 ex,
    T1,write 2 waiting,1 ex,
    T2,reader 1 acquire working,1 ex, 1 sh
    T3,reader 1 release queue,0 ex, 1 sh
    T4,writer 2 acquire queue,1 ex, 1 sh
    T5,writer 2 waiting,1 ex, 1 sh
    T7,reader 1 release working,1 ex,
    T8,writer 2 acquire working,1 ex, 1 ex
    T9,writer 2 release queue,0 ex, 1 ex
    T10,writer 2 release working,0 ex,

Clearly, if there are a **lot** of readers, the writer waits a long time
for them **all** to finish.
Some more clever lock definitions permit an upper bound on the number of
locks that can be acquired.

Our goal, however, is simplicity.

Python Implementation
=================================

This is intended to be used with **Flask**.

::

    from pathlib import Path
    from flask import Flask

    class DBLock:

        def __init__(self, app: Flask | None = None) -> None:
            if app:
                self.init_app(app)

        def init_app(self, app: Flask) -> None:
            self.lock_path = Path(cast(str, app.config.get("DB_LOCK_FILENAME", "dblock")))
            self.queue_path = self.lock_path.with_suffix(".dbqueue")
            self.thread_local = threading.local()

This could be refactored to work outside a Flask-specific context.

The ``thread_local`` storage is required to track each thread's unique open file handles.

The essence is acquiring a lock and releaing a lock.
The "lock mode" is one the ``fcntl.LOCK_EX`` or ``fcntl.LOCK_SH`` values.

::

    def acquire(self, lock_mode: int) -> Self:
        if "lock_file" not in self.thread_local.__dict__:
            # Enter Queue Mutex to acquire a database lock.
            queue_file = self.queue_path.open("w+")
            fcntl.flock(queue_file, fcntl.LOCK_EX)
            self.thread_local.lock_file = self.lock_path.open("w+")
            fcntl.flock(self.thread_local.lock_file, lock_mode)
            # Exit Queue Mutex. Permits another thread (or process) to acquire a lock.
            fcntl.flock(queue_file, fcntl.LOCK_UN)
        return self

    def release(self) -> None:
        if "lock_file" in self.thread_local.__dict__:
            fcntl.flock(self.thread_local.lock_file, fcntl.LOCK_UN)
            self.thread_local.lock_file.close()
            delattr(self.thread_local, "lock_file")

The acquire and release are the algorithm described above.
An exclusive lock defines a system-wide Mutex for **all** threads and processes.
The working lock is either shared or exclusive.

The cleanup on release undoes the lock, closes the file to release any OS resources,
and also purges the ``thread_local`` to make sure there's no confusion about the state.

Some useful overheads:

::

    close = release

    def is_locked(self) -> bool:
        # print(f"is_locked: {self.thread_local.__dict__=}")
        return "lock_file" in self.thread_local.__dict__

If we provide a ``close()`` method, then the ``contextlib.closing()`` context manager
can be used.

The ``is_locked()`` method can be helpful to know the state of the lock.
It's far better to use the ``with`` statement to define a context that eliminates any doubt.

While this can be used with ``contextlib`` functions, it seems helpful to provide explicit context management.

::

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[Exception],
        exc_val: Exception,
        exc_tb: TracebackException,
    ) -> Literal[False]:
        self.release()
        return False

And. Two convenience methods to avoid having to muck around with ``fcntl.LOCK_SH`` and ``fcntl.LOCK_EX``.

::

    def shared(self) -> Self:
        """
        Context manager, equivalent to::

            with dblock.acquire(fcntl.LOCK_SH):
                pass
        """
        self.acquire(fcntl.LOCK_SH)
        return self

    def exclusive(self) -> Self:
        """
        Context manager, equivalent to::

            with dblock.acquire(fcntl.LOCK_EX):
                pass
        """
        self.acquire(fcntl.LOCK_EX)
        return self

The goal is to have relatively lightweight code like the following.

Some Flask app setup:
::

    dblock = DBLock()
    dblock.init_app(app)

Within a GET view function:
::

    with dblock.shared():
        with dbm.open(some_file) as db:
            item = SomeClass.model_validate_json(db[your_key_here])

Within a POST/PUT/PATCH/DELETE view function:
::

    with dblock.exclusive():
        with dbm.open(some_file, flag='c') as db:
            db[item.id] = item.model_dump_json().encode('utf-8')

By acquiring an exclusive access lock, all changes will be saved reliably and predictably: an atomic state change.

And yes, the explicit ``model_validate_json()`` and ``model_dump_json()`` is wordy.
I use a ``DB`` class to conceals these details.

Conclusion
==========

We can use ``dbm`` as a dictionary-like repository of objects serialized as JSON.

We have the benefits of a fancy relational database without the overheads.
