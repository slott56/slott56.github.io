Configuration Files, Environment Variables, and Command-Line Options
====================================================================

:date: 2015-03-24 08:00
:tags: #python,configuration management
:slug: 2015_03_24-configuration_files_environment_variables_and_command_line_options
:category: Technologies
:status: published


We have three major tiers of configuration for applications. Within
each tier, we have sub-tiers, larding on yet more complexity. The
organization of the layers is a bit fungible, too. Making good choices
can be rather complex because there are so many variations on the
theme of "configuration". The desktop GUI app with a preferences file
has very different requirements from larger, more complex
applications.

The most dynamic configuration options are the **command-line
arguments**. Within this tier of configuration, we have two sub-tiers
of default values and user-provided overrides to those defaults. Where
do the defaults come from? They might be wired in, but more often they
come from environment variables or parameter files or both.

There's some difference of opinion on which tier is next in the tiers
of dynamism. The two choices are configuration files and environment
variables. We can consider environment variables as easier to edit
than configuration files. In some cases, though, configuration files
are easier to change than environment variables. Environment variables
are typically bound to the process just once (like command-line
arguments), where configuration files can be read and re-read as
needed.

The **environment variables** have three sub-tiers. System-level
environment variables tend to be fixed. The variables set by a
.profile or .bashrc tend to be specific to a logged-in user, and are
somewhat more flexible that system variables. The current set of
environment variables associated with the logged-in session can be
modified on the command line, and are as flexible as command-line
arguments.

Note that we can do this in Linux:

::

    PYTHONPATH=/path/to/project python3 -m some_app -opts

This will set an environment variable as part of running a command.

The **configuration files** may also have tiers. We might have a
global configuration file in /etc/our-app. We might look for a
~/.our-app-rc as a user's generic configuration. We can also look for
our-app.config in the current working directory as the final set of
overrides to be used for the current invocation.

Some applications can be restarted, leading to re-reading the
configuration files. We can change the configuration more easily than
we can bind in new command-line arguments or environment variables.

**Representation Issues**

When we think about configuration files, we also have to consider the
syntax we want to use to represent configurable parameters. We have
five common choices.

Some folks are hopelessly in love with Windows-style .ini files. The
configparser module will parse these. I call it hopelessly in love
because the syntax is rather quite limited. Look at the logging.config
module to see how complex the .ini file format is for non-trivial
cases.

Some folks like Java-style properties files. These have the benefit of
being really easy to parse in Python. Indeed, scanning a properties
file is great exercise in functional-style Python programming.

I'm not completely sold on these, either, because they don't really
handle the non-trivial cases well.

Using JSON or YAML for properties has some real advantages. There's a
lot of sophistication available in these two notations. While JSON has
first-class support, YAML requires an add-on module.

We can also use Python as the language for configuration. For good
examples of this, look at the `Django project
settings <https://docs.djangoproject.com/en/1.7/topics/settings/>`__
file. Using Python has numerous advantages. The only possible
disadvantage is the time wasted arguing with folks who call it a
"security vulnerability."

Using Python as the configuration language is only considered a
vulnerability by people who fail to realize that the Python source
itself can be hacked. Why waste time injecting a bug into a
configuration file? Why not just hack the source?

**My Current Fave**

My current favorite way to handle configuration is by defining some
kind of configuration class and using the class object throughout the
application. Because of Python's import processing, a single instance
of the class definition is easy to guarantee.

We might have a module that defines a hierarchy of configuration
classes, each of which layers in additional details.

::

    class Defaults:
       mongo_uri = "mongodb://localhost:27017"
       some_param = "xyz"

    class Dev(Defaults):
       mongo_uri = "mongodb://sandbox:27017"

    class QA(Defaults):
       mongo_uri = "mongodb://username:password@qa02:27017/?authMechanism=PLAIN&authSource=$external"


Yes. The password is visible. If we want to mess around with higher
levels of secrecy in the configuration files, we can use PyCrypto and
a key generator to use an encrypted password that's injected into the
URI. That's a subject for another post. The folks to can edit the
configuration files often know the passwords. Who are we trying to
hide things from?

How do we choose the active configuration to use from among the
available choices in this file? We have several ways.

-   Add a line to the configuration module. For example, Config=QA
    will name the selected environment. We have to change the
    configuration file as our code marches through environments from
    development to production. We can use from configuration import
    Config to get the proper configuration in all other modules of the
    application.

-   Rely on the environment variable to specify which configuration
    use. In enterprise contexts, an environment variable is often
    available.We can import os, and use
    Config=globals()[os.environ['OURAPP_ENVIRONMENT']] to pick a
    configuration based on an environment variable.

-   In some places, we can rely on the host name itself to pick a
    configuration. We can use os.uname()[1] to get the name of the
    server. We can add a mapping from server name to configuration,
    and use this: Config=host_map(os.uname()[1],Defaults).

-   Use a command-line options like "--env=QA". This can a little more
    complex than the above techniques, but it seems to work out nicely
    in the long run.

**Command-line args to select a specific configuration**

To select a configuration using command-line arguments, we must
decompose configuration into two parts. The configuration
alternatives shown above are placed in a config_params.py module. The
config.py module that's used directly by the application will import
the config_params.py module, parse the command-line options, and
finally pick a configuration. This module can create the required
module global, Config. Since it will only execute once, we can import
it freely.

The config module will use argparse to create an object named options
with the command-line options. We can then do this little dance:

::

  import argparse
  import sys
  import config_params

  parser= argparse.ArgumentParser()
  parser.add_argument("--env", default="DEV")
  options= parser.parse_args()

  Config = getattr(config_params, options.env)
  Config.options= options

This seems to work out reasonably well. We can tweak the
config_params.py flexibly. We can pick the configuration with a
simple command-line option.

If we want to elegantly dump the configuration, we have a bit of a
struggle. Each class in the hierarchy introduces names: it's a bit of
work to walk down the ``__class__.__mro__`` lattice to discover all of
the available names and values that are inherited and overridden from
the parents.

We could do something like this to flatten out the resulting values:


::

    Base = getattr(config_params, options.env)
    class Config(Base):
        def __repr__(self):
           names= {}
           for cls in reversed(self.__class__.__mro__):
               cls_names= dict((nm, (cls.__name__, val))
                   for nm,val in cls.__dict__.items()
                       if nm[0] != "_")
               names.update( cls_names )
           return ", ".join( "{0}.{1}={2}".format(class_val[0], nm, class_val[1])
               for nm,class_val in names.items() )

It's not clear this is required. But it's kind of cool for debugging.





