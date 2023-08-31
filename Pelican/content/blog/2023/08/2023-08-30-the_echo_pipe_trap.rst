The Echo-Pipe Trap
##############################################

:date: 2023-08-30 09:00
:tags: python,community
:slug: 2023-08-30-the_echo_pipe_trap
:category: Python
:status: published

This is a **great** question.

https://fosstodon.org/@JustineSmithies/110979871574705636

This works, they said.

    echo -en "Firefox\\0icon\\x1fweechat" | fuzzel -d -w 100 -l 10

But. The superficial switch to ``subprocess.Popen()`` doesn't work.

Why?

The way ``echo`` works varies from shell to shell. When MacOSX changes to zsh, things can break.
Or when you share it with someone else, who uses YetAnotherShell, things break.

Two choices:

1. Specify which shell.

2. Stop using the ``echo ... |`` (echo-pipe) construct.

What's Better?
==============

The ``stdin`` parameter to ``Popen()`` can be used to provide the required stream of bytes.

::

    from pathlib import Path
    import subprocess

    temp = Path.cwd() / "temp.tmp"
    temp.write_text("Firefox\0icon\0x1fweechat")  # I think.

    with temp.open() as echo_file:
        subprocess.Popen(['fuzzel', '-d', '-w', '100', '-l', '10'], stdin=echo_file)

Something like the above will avoid the echo-pipe construct.

But. It leaves a temporary file lying around. What to do?

Slightly Better
===============

This will cleanup the file. And. You don't have to pick a name.

::

    import tempfile
    import subprocess

    temp = tempfile.TemporaryFile(mode='w+')
    with temp:
        temp.write("Firefox\0icon\0x1fweechat")  # I think.
        temp.seek(0)
        subprocess.Popen(['fuzzel', '-d', '-w', '100', '-l', '10'], stdin=temp)

Seems kind of long. And it involves an additional problem. A file.

But. There's a FILE!
====================

Yes. We **can** create a pipe.  I think it's kind of hideous, though.

::

    import os
    import subprocess

    r, w = os.pipe()
    readable = os.fdopen(r, 'r')
    writeable = os.fdopen(w, 'w')
    writeable.write("Firefox\0icon\0x1fweechat")  # I think.
    writeable.close()
    subprocess.Popen(['fuzzel', '-d', '-w', '100', '-l', '10'], stdin=readable)
    readable.close()


However. It's not too long.

We can create a pleasant wrapper in the form
of a context manager.

How's This?
===========

This seems pleasant, if you do a lot of this sort of thing.

::

    import os
    import subprocess

    class EchoPipe:
        def __init__(self, content):
            self.content = content

        def __enter__(self):
            r, w = os.pipe()
            self.readable = os.fdopen(r, 'r')
            writeable = os.fdopen(w, 'w')
            writeable.write(self.content)
            writeable.close()
            return self.readable

        def __exit__(self, exc_type, exc_value, traceback):
            self.readable.close()

Once you have the ``EchoPipe`` context, you can now write this.

::

    with EchoPipe("Firefox\0icon\0x1fweechat") as echo_pipe:
        subprocess.Popen(['fuzzel', '-d', '-w', '100', '-l', '10'], stdin=echo_pipe)

Which is pretty close to the original terse shell stuff.
