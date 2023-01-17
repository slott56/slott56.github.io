Command Line Applications
=========================

:date: 2011-10-06 08:00
:tags: #python,java,CLI
:slug: 2011_10_06-command_line_applications
:category: Technologies
:status: published

I'm old -- I admit it -- and I feel that command-line applications are
still very, very important. Linux, for example, is packed full of almost
innumerable command-line applications. In some cases, the Linux GUI
tools are specifically just wrappers around the underlying command-line
applications.

For many types of high-volume data processing, command-line
applications are essential.

I've seen command-line applications done very badly.

Overusing Main
--------------

When writing OO programs, it's absolutely essential that the OS
interface (public static void main in Java or the if \__name_\_ ==
"__main__": block in Python) does as little as possible.

A good command-line program has the underlying tasks or actions
defined in some easy-to-work with class hierarchy built on the
**Command** design pattern. The actual main program part does just a
few things: gather the relevant environment variables, parse
command-line options and arguments, identify the configuration files,
and initiate the appropriate commands. Nothing application-specific.

When the main method does application-specific work, that application
functionality is buried in a method that's particularly hard to
reuse. It's important to keep the application functionality away from
the OS interface.
I'm finding that main programs should look something like this:

::

    if \__name_\_ == "__main__":
       logging.basicConfig( stream=sys.stderr )
       args= parse_args()
       logging.getLogger().setLevel( args.verbosity )
       try:
           for file in args.file:
               with open( file, "r" ) as source:
                   process_file( source, args )
           status= 0
       except Exception as e:
           logging.exception( e )
           status= 3
       logging.shutdown()
       sys.exit( status )

That's it.  Nothing more in the top-level main program.  The
process_file function becomes a reusable "command" and something
that can be tested independently.



-----

This is my standard main
-----------------------------------------------------

Chai<noreply@blogger.com>

2011-10-11 18:24:57.551000-04:00

This is my standard main.
::

    if __name__ == '__main__' :
        if os.path.exists( "logging.conf" ) :
            logging.config.fileConfig("logging.conf")
        else :
            logging.basicConfig(level=logging.INFO)
        fnName = sys.argv[ 1 ]
        logging.info( '** function %s', fnName )
        n = locals()[ fnName ]( args = sys.argv[ 2: ] )
        logging.info( '** bye' )


Thank you for posting this. This is actually somet...
-----------------------------------------------------

Kellan<noreply@blogger.com>

2011-10-06 18:08:52.652000-04:00

Thank you for posting this. This is actually something I knew I was
doing wrong but I didn't quite know exactly where I was making the wrong
turn. This gets me much closer to the clean code I would like to be
writing in python. Any chance you have a simple script you wrote you
would like to share with us, that uses this method? I would love to see
an example I can read over and use to learn from.


I myself like to wrap this in a main function...
-----------------------------------------------------

Ids<noreply@blogger.com>

2011-10-07 03:49:17.887000-04:00

Hi.
I myself like to wrap this in a main function like this:

::

    def main(argv):
        ...

    if __name__ == '__main__':
    main(sys.argv)

Also, the standard python fileinput module may come in handy.





