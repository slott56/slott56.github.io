A plea to avoid sys.exit()  [Updated]
=====================================

:date: 2015-06-23 07:38
:tags: #python
:slug: 2015_06_23-a_plea_to_avoid_sysexit_updated
:category: Technologies
:status: published


Let me gripe about this for a moment.

::

    sys.exit()

The use case for this function is limited. Very, very limited.

Every place that this appears (except for one) is going to lead to
reusability issues.

Consider some obscure little function, deep within the app.

::

   def deep_within_the_app(x, y, zed):
       try:
           something -- doesn't matter what
       except SomeException:
           logging.exception( "deep_within_the_app")
           sys.exit(2)




What's so bad about that?

The function seizes control of every app that uses it by raising an
unexpected exception.

We can (partially) undo this mischief by wrapping the function in a
try/except which catches SystemExit.

::

   def reusing_a_feature():
       for i in range(a_bunch):
           try:
               print(deep_within_the_app(x,y,i))
           except SystemExit as e:
               print("error on {0}".format(i))




This will defeat the sys.exit(). But the cost is one of clarity. Why
SystemExit? Why not some meaningful exception?

This is important: **raise the meaningful exception instead of exit**.

Bottom Line.

--------------




The right place for sys.exit() is inside the
``if __name__ == "__main__":`` section.

It might look something like this:

::

   if __name__ == "__main__":
       try:
           main()
       except (KnownException, AnotherException) as ex:
           logging.exception(ex)
           sys.exit(2)




    **Use meaningful exceptions instead of sys.exit().**

This permits reuse of everything without a mysterious SystemExit
causing confusion.





