The Pipeline Question when Bashing the Bash
===========================================

:date: 2017-08-29 08:00
:tags: #python,architecture,bash,design
:slug: 2017_08_29-the_pipeline_question_when_bashing_the_bash
:category: Technologies
:status: published


Background: https://medium.com/capital-one-developers/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989

And this

    I wonder how/why python did not pick up some sort/form of pipe
    operator. 🤨
    (although coroutine does have .send method 🤔)
    
    — Ivan Pejić (@nadrimajstor) `August 26,
    2017 <https://twitter.com/nadrimajstor/status/901235806714679296>`__


The answer to this is interesting because there are two kinds of
parallelism. I like to call them architectural and incidental (or
casual).  I'll look at architectural parallelism first, because it's
what we often think about. Then the incidental parallelism, which I'm
convinced is a blight.

Architectural Parallelism
-------------------------


The OS provides big-picture, architectural parallelism. This isn't --
necessarily -- a thing we want to push down into Python applications.
There are some tradeoffs here.

One example of big architectural parallelism are big map-reduce
processes where the mapping and reducing can (and should) proceed in
parallel. There are some constraints around this, and we'll touch on
them below.

Another common example is a cluster of microservices that are deployed
on the same server. In many cases, each microservice decomposes into a
cluster of processes that work in parallel and have a very, very long
life. We might have an NGINX front-end for static content and a
Python-based Flask back-end for dynamic content.  We might want the OS
init process to start these, and we define them in init.d. In other
cases, we allocate them to web-based servers where load-balancing
handles the details of restarting.

In the map-reduce example, the shell's pipe makes sense. We can define
it with a shell script like this: ``source | map | reduce``.  
It's hard to beat this for succinct clarity.

In the Ngnix + Flask case, they may talk using a named pipe that
outlives the two processes. *Conceptually*, they work as ``nginx | flask run``.

In some cases, we have log analysis and alerting that are part of
microservices management. We can pile this into the processing stream
with a conceptual pipeline of ``nginx | flask run | log reduce | alert``. The log reduce filters and reduces the log to find those events
that require an alert. If any data makes it into the alert process, it
sends the text for human intervention.

There are some distinguishing features.

-  They tend to be resource hogs. Either it's a big map-reduce
   processing request that uses a lot of CPU and memory resources. Or
   it's a log-running server.

-  The data being transported is bytes with a very inexpensive (almost
   free) serialization. When we think of map-reduce, these processes
   often work with text as input and output. There may be more complex
   data structures involved in the reduce, but the cost of serialization
   is an important concern. When we think of web requests, the request,
   response, and log pipeline is bytes more-or-less by definition.

-  The parallelism is at the process level because each element does a
   lot of work and the isolation is beneficial.

-  They compute high-value results for actual users.


The OS does this. The complexity is that each OS does this
differently. The Python subprocess module (and related projects
outside the standard library) provide an elegant mapping into
Python.


It's not built-in to the language. I think that it's because details
vary so widely by OS. I think trying to build this into the language
leads to a bulky featyre that's not widely-enough used.


Incidental Parallelism
----------------------


This is -- to me -- a blight. Here's a typical kind of thing we see
in the middle of a longer, more complex shell script.

::

   data=`grep pattern file | cut args | sort | head`
   # the interesting processing on $data


Computing a value that's assigned to data is a high-cost, low-value
step. It creates an intermediate result that's only part of the shell
script, and not really the final result. The parallelism feature of
the shell's ``|`` operator isn't of any profound value since only a tiny
bit of data is passed from step to step.


This can be rewritten into Python, but the resulting code won't be a
one-liner. It will be longer. It will also be much, much faster.
However, the speed difference is rarely relevant if this kind of
processing step inside a larger, iterative process.

A trivial rewrite of just one line of code misses the point. The goal
is to refactor the script so that this line of code because a simple
part of the processing and uses first-class Python data structures.
The reason for doing cut and sort operations is generally because the
data structure wasn't optimized for the job. A priority queue might
have been a better choice, and would have amortized sorting properly
and eliminated the need for separate cut and head operations.


This kind of computation can (and should) be done in a single
process. The shell pipeline legacy implementation is little more than
a short-hand for passing arguments and results among (simple)
functions.


We can rewrite this as nested functions.

::

   with Path(file).open() as source:
       head(sorted(cut_mapping(args, grep_filter(pattern, file))))


This will do the same thing. The gigantic benefits of this kind of
rewrite involves eliminating two kinds of overheads.

-  The fork/exec to spawn subprocesses. A single process will be
   faster.

-  The serialization and deserialization of intermediate results.
   Avoiding serialization will be faster.


When we rewrite bash to Python, we are able to leverage Python's
data structures to write processing that expressive, succinct, and
efficient.

This kind of rewriting will also lead to refactoring the adjacent
lines of the script -- the interesting processing -- into Python
code also. This refactoring can lead to further simplifications
and speedups.

The Two Cases
-------------

There seem to be two cases of parallelism:

-   Big and Architectural. There are many Python packages that
    provides these features. Look at plumbum, pipes, and joblib for
    examples. Since the OS implementation details vary so much,
    it's hard to imagine making this part of the language.

-   Small and Incidental.  The incidental parallelism is clever,
    but inefficient. In many cases, it doesn't seem to create
    significant value. It seems to be a kind of handy little
    workaround. It has costs that I find to outstrip the value.

      
When replacing the bash with Python, some of the parallelism is
architectural, and needs to be preserved. Careful engineering
choices will be required. The rest is incidental and needs to
be discarded.





