.. _GitHub: https://github.com
.. _GitHub repository: https://github.com/tyralla/hydpy
.. _online documentation: https://tyralla.github.io/hydpy/
.. _hydpy package: https://pypi.python.org/pypi
.. _Python Package Index: https://pypi.python.org/pypi
.. _Python tutorials: https://www.python.org/about/gettingstarted/
.. _book on object-oriented design: http://www.itmaybeahack.com/homepage/books/oodesign.html
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _The Python Standard Library: https://docs.python.org/2/library/
.. _Cython: http://www.cython.org/
.. _NumPy: http://www.numpy.org/
.. _matplotlib: http://matplotlib.org/
.. _End Of Life for Python 2.7: https://www.python.org/dev/peps/pep-0373/
.. _pandas: http://pandas-docs.github.io/pandas-docs-travis/contributing.html
.. _free GitHub account: https://github.com/signup/free
.. _source tree: https://www.sourcetreeapp.com/
.. _Pro Git: https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf
.. _How to Rebase a Pull Request: https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request
.. _Python 2-3 cheat sheet: http://python-future.org/compatible_idioms.html
.. _PyPy: https://pypy.org/
.. _mock object library: https://docs.python.org/3/library/unittest.mock.html
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Travis CI: https://travis-ci.com/
.. _Travis CI project: https://travis-ci.org/tyralla/hydpy
.. _test future Python: https://snarky.ca/how-to-use-your-project-travis-to-help-test-python-itself/
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _master branch: https://github.com/tyralla/hydpy/tree/master
.. _gh-pages branch: https://github.com/tyralla/hydpy/tree/gh-pages
.. _travis-sphinx: https://github.com/Syntaf/travis-sphinx
.. _Coverage.py: https://coverage.readthedocs.io/en/coverage-4.3.4/
.. _development:

Development
===========

You can install HydPy from the `hydpy package`_ available on the
`Python package index`_ or fork from this `GitHub repository`_ available
on `GitHub`_.  Afterwards, you can implement your own models or
change the framework's structure in a manner that meets your personal
goals and preferences.  There are many other Python tools freely
available, which will be of great help while trying to achieve more
complex tasks like parameter calibration or regionalization.  Cherry
picking from many different Python packages can be a huge time-saving.
Very often it is not necessary to write a "real" Python program.
Instead, just writing a simple script calling different functionalities
of different packages in the correct order often gets the job done.

However, if you intend to contribute to the further development of HydPy
(hopefully you will!), you must abdicate some parts of the freedom and
ease of use Python offers.  The number of dependencies to other Python
packages, in particular those with some relevant shortcomings and those
which might not be further supported in the future, should be kept as
small as possible.  Otherwise, it would be too hard to guarantee the
long-term applicability of HydPy.  Additionally, the Python code
contributed by different developers should be as consistent as possible.
Otherwise, there would be a risk of the code base becoming opaque, making
future extensions of HydPy impossible.

The following sections try to define a strategy allowing HydPy to be
developed as an open source project while maintaining sufficiently
high-quality standards for practical applications.  The hydrological
modelling community has not made that much progress in this field yet.
This is why the outlined strategy is highly influenced by other
non-hydrological open source projects like `pandas`_.  Discussions on
how to improve the outlined strategy are welcome!


How to contribute?
__________________

To work in collaboration on the same software code requires some kind
of version control.  It must be clear who is working on which part of
the code, when (and why) code changes were conducted, and which code
sections of one developer are compatible with some code sections of
another developer (or not).  Also, one always needs the possibility to
fall back on an older code version whenever some current changes turned
out to be a dead end.

For HydPy, we selected the version control software Git for these tasks.
The main `GitHub repository`_ is available on `GitHub`_.  So the first
step should be to sing up for a `free GitHub account`_.  After that,
you could contribute to HydPy online without to install anything on
your own computer.  If your only aim is to improve the documentation,
this could be reasonable.  But normally you need to handle Git
repositories on your own computer.  Git itself works via command lines.
Most likely, you would prefer to install Git together with a graphical
user interface like `source tree`_.

To contribute to HydPy requires essentially three or four steps, no matter
if working directly online on GitHub or with your local Git software.  For
simplicity and generality, these steps are explained using the example
of a single change to the documentation via GitHub:

  * Go to this `GitHub repository`_ and click on "Fork".  This is how you
    create your own working copy of HydPy, allowing you to add, change,
    or delete any files without interfering with the original repository.
  * Click on "Branch: master", type a name that reflects what you want
    to accomplish and press enter. Now that you have created a new
    branch, you can experiment without affecting the original branch or your
    own  master branch. (This step is not really required; you could
    apply the following steps on your own master branch likewise.
    But to create branches for different tasks helps to structure your
    work and to cooperate with others.)
  * Change something.  For example
      * click on ".gitignore"
      * click on the marker symbol ("Edit this file")
      * change the order of two lines (e.g. "*c." and "*.h")
      * write something under "Commit changes" to explain your doing
        (e.g. "change the order of lines in .gitignore")
      * click on the green "Commit changes" button

    Now you have changed the file .gitignore in your own branch
    specialized for this task.  Normally, you would commit multiple
    small changes to one branch.  Keeping single commits small allows
    for inspecting and reversing different changes.
  * At last, you can suggest your changes to be included in HydPy's
    main repository.  Click on "Compare" to visualize the relevant
    differences.  Click on "Create pull request" to ask others
    to discuss your changes and to eventually merge them into their
    projects.  In other words: you request other people to pull (get)
    your own changes and to merge (incorporate) these changes into their
    repositories.

Note that everyone is responsible for his or her own repository, you
do not have to be afraid to break another person's repository accidentally.
But you are responsible the make pull requests focussing on one issue
that is clearly explained.  Otherwise, your contribution is likely to be
refused.

Of course, it is not always as easy as in the given example.  Not only
your branches but also the main line of development evolves.  Often,
you will have to retrieve changes from the main branch and eventually
resolve some conflicts before you can make "good" pull request.  See
much more thorough explanations as `Pro Git`_ on how to improve your
skills in using Git.  Here is a very nice description on
`How to Rebase a Pull Request`_ (this could be a good starting point for
explaining how to add newly developed models into the main line in
this documentation).

HydPy Style Guide
_________________

Python allows for writing concise and easily readable software code,
that can be maintained and further developed with relative ease.
However, code quality does also depend on the experience (and available
time) of the programmer writing it.  In hydrology, much model code is
written by PhD students and other young scientists, who --- besides
having participated in some more or less comprehensive introductory
courses --- have often little programming experience and who are under
the pressure not only to get their model running, but also to tackle
their scientific questions and to publish as many research articles
as possible within a limited period of time.  The source code
resulting from such a rush is understandably often a mess.  And even
the better software results often prove inadequate when it comes
to transferring the software into practical applications or sharing it
with other researchers.

This is why we defined the HydPy Style Guide, which is a refinement
of `PEP 8`_ --- the "official" Style Guide for Python Code.
`PEP 8`_ gives coding conventions that help to write clear code.
And it eases diving into already existing source code, as one has
less effort with unravelling the mysteries of overly creative
programming solutions.

In some regards, the HydPy Style Guide deviates substantially from `PEP 8`_.
This is mostly due to following two aims.  First, that the HydPy framework
shall be applicable for hydrologists with little or even no programming
experience.  Ideally, such framework users should not even notice that they
are writing valid Python code while preparing their configuration files.
Secondly, that the common gap between model code, model documentation and
model testing should be closed as well as possible.  Understanding the
model documentation of a certain HydPy version should be identical with
understanding how the model actually works under the same HydPy version.
These two points are elucidated in the following subsections.


General framework features
--------------------------
When trying to contribute code to the core tools of HydPy (meaning
basically everything except the actual model implementations), on has
to be aware that even slight changes can have significant effects
on the applicability of HydPy, and that future HydPy developers must
cope with your contributions.   So, always make sure to check the effects
of your code changes properly (as described below).  And try to structure
your code in a readable, object-oriented design.  This section describes
some conventions for the development of HydPy, but is no guidance on how
to write good source code in general.  So, if you have little experience
in programming, first make sure to learn the basics of Python through some
`Python tutorials`_.  Afterwards, improve your knowledge of code quality
through reading more advanced literature like this
`book on object-oriented design`_.

Python Version
..............
The `End Of Life for Python 2.7` is scheduled for 2020. Nevertheless,
still many scientists are using it.  This is why HydPy is continuously
tested both on Python 2 and Python 3. For the time being future HydPy
versions should be applicable on both Python versions.

Always insert

    >>> from __future__ import division, print_function

at the top of a new module.  This introduces the new (integer) division
and print statement of Python 3 into Python 2 (when using Python 3, this
import statement is automatically skipped).

Whenever there are two multiple options to achieve something, prefer
one that fits best with Python 3.  For example, always use |range|.
While under Python 2 often `xrange` would be preferable regarding time
and memory efficiency, just using |range| leads to a clean syntax
and is future-proof.  (Have a look at the `Python 2-3 cheat sheet`_
whenever in compatibility trouble.)

Sometimes incompatibilities of Python 2 and Python 3 require that specific
HydPy functionalities must be coded twice.  Use `pyversion` in these cases:

    >>> import sys
    >>> traceback_ = sys.exc_info()[2]
    >>> from hydpy import pub
    >>> if pub.pyversion == 2:
    ...     exec("raise SystemError, 'just a test', traceback_")
    ... else:
    ...     raise SystemError('just a test').with_traceback(traceback_)
    Traceback (most recent call last):
    ...
    SystemError: just a test

(The example above is already taken into account by function
|augment_excmessage|.)


site-packages
.............
Whenever reasonable, import only packages of
`The Python Standard Library`_ or at least restrict yourself
to mature and stable site-packages.  At the moment, HydPy relies
only on the highly accepted site-packages `Cython`_, `NumPy`_,
and `matplotlib`_.  Further developments of HydPy based on more
specialized site-packages (e.g. for plotting maps) might be
useful.  But the related import commands should be secured in
a way that allows for the application of HydPy without having
these specialized site-packages available.

Imports
.......
As recommended in `PEP 8`_, clarify the sources of your imports.
Always use the following pattern at the top of a new module
(with some example packages):

    >>> # import from...
    >>> # ...the Python Standard Library
    >>> from __future__ import division, print_function
    >>> import os
    >>> import sys
    >>> # ...site-packages
    >>> import numpy
    >>> # ...from HydPy
    >>> from hydpy.core import sequencetools
    >>> from hydpy.cythons import pointerutils

Note that each import command has its own line.  Always import
complete modules from HydPy without changing their names. ---
No wildcard imports!

The wildcard ban is lifted when writing configuration files.
Using the parameter control files as an example, it wouldn't be nice to
always write something like:

    >>> from hydpy.models import hland
    >>> model = hland.Model()
    >>> model.parameters = hland.Parameters({'model':model})
    >>> model.parameters.control = hland.ControlParameters(model.parameters.control)
    >>> model.parameters.control.nmbzones = 2
    >>> model.parameters.control.nmbzones
    nmbzones(2)

Here a wildcard import (and some magic, see below), allows for a much
cleaner syntax:

    >>>  # First delete the model instance of the example above.
    >>> del model
    >>> # Now repeat the above example in a more intuitive manner.
    >>> from hydpy.models.hland import *
    >>> parameterstep('1d')
    >>> nmbzones(2)
    >>> nmbzones
    nmbzones(2)

Note that the wildcard import is acceptable here, as there is only one
import statement.  There is no danger of name conflicts.

Defensive Programming
.....................
HydPy is intended to be applicable by researchers and practitioners
who are no Python experts and may have little experience in programming
in general.  Hence it is desirable to anticipate errors due to misleading
input as good as possible and report them as soon as possible.
So, in contradiction to `PEP 8`_, it is recommended to not just expose
the names of simple public attributes.  Instead, use protected attributes
(usually properties) to assure that the internal states of objects remain
consistent, whenever this appears to be useful. One example is that it
is not allowed to assign an unknown string to the `outputfiletype` of a
|SequenceManager|:

    >>> from hydpy.core.filetools import SequenceManager
    >>> sm = SequenceManager()
    >>> sm.outputfiletype = 'test'
    Traceback (most recent call last):
      ...
    ValueError: The given sequence file type `test` is not implemented.  Please choose one of the following file types: npy and asc.

Of course, the extensive usage of protected attributes increases
the length of the source code and slows computation time.  But,
regarding the first point, writing a graphical user interface
would require much more source code.  And, regarding the second
point, the computation times of the general framework
functionalities discussed here should be negligible in comparison
with the computation times of the hydrological simulations,
which are discussed below, in the majority of cases.

Exceptions
..........
Unmodified error messages of Python (and of the imported
libraries) are often not helpful in the application of HydPy due
to two reasons: First, they are probably read by someone who has
no experience in understanding Pythons exception handling system.
And secondly, they do not tell in which context a problem occurs.
Here, "context" does not mean the relevant part of the source code,
which is of course referenced in the traceback; instead, it means
things like the concerned geographical location.  It would, for example,
be of little help to only know that the required value of a certain
parameter is not available when the same parameter is applied
thousands of times in different subcatchments.  Try to add as much
helpful information to error messages as possible, e.g.::

    raise RuntimeError('For parameter %s of element %s no value has been '
                       'defined so far.  Hence it is not possible to...'
                       % (parameter.name, objecttools.devicename(parameter)))

(The function |devicename| tries to determine the name of the |Node|
or |Element| instance (indirectly) containing the given object, which
is in many cases the most relevant information for identifying the
error source.)

Whenever possible, us function |augment_excmessage| to augment
standard Python error messages with `HydPy information`.


Naming Conventions
..................
The naming conventions of `PEP 8`_ apply.  Additionally, it is
encouraged to name classes and their instances as similar as
possible whenever reasonable, often simply switching from
**CamelCase** to **lowercase**. This can be illustrated based
on some classes for handling time series:

=============== ============== ===================================================================================
Class Name      Instance Name  Note
=============== ============== ===================================================================================
Sequences       sequences      each Model instance handles exactly one Sequence instance: `model.sequences`
InputSequences  inputs         "inputsequences" would be redundant for attribute access: `model.sequences.inputs`
=============== ============== ===================================================================================

If possible, each instance should define its own preferred name via
the property `name`:

    >>> from hydpy.models.hland import *
    >>> InputSequences(None).name
    'inputs'

For classes like |Element| or |Node|, where names (and not
namespaces) are used to differentiate between instances, the
property `name` is also implemented, but --- of course --- not
related to the class name, e.g.:

    >>> from hydpy import Node
    >>> Node('gauge1').name
    'gauge1'

In HydPy, instances of the same or similar type should be grouped in
collection objects with a similar name, but with an attached letter "s".
Different |Element| instances are storedin an instance of the class
|Elements|, different |Node| instances are stored in an instance of
the class |Nodes|...

Collection Classes
..................
The naming (of the instances) of collection classes is discussed just
above.  Additionally, try to follow the following recommendations.

Each collection object should be iterable, e.g.:

    >>> from hydpy import Nodes
    >>> nodes = Nodes('gauge1', 'gauge2')
    >>> for node in nodes:
    ...     node
    Node("gauge1", variable="Q")
    Node("gauge2", variable="Q")

To ease working in the interactive mode, objects handled by a
collection object should be accessible as attributes:

    >>> nodes.gauge1
    Node("gauge1", variable="Q")
    >>> nodes.gauge2
    Node("gauge2", variable="Q")

Whenever usefull, define convenience functions which simplify the
handling of collection objects, e.g.:

    >>> nodes += Node('gauge1')
    >>> nodes.gauge1 is Node('gauge1')
    True
    >>> len(nodes)
    2
    >>> 'gauge1' in nodes
    True
    >>> nodes.gauge1 in nodes
    True
    >>> newnodes = nodes.copy()
    >>> nodes is newnodes
    False
    >>> nodes.gauge1 is newnodes.gauge1
    True
    >>> nodes -= 'gauge1'
    >>> 'gauge1' in nodes
    False


String Representations
......................
Be aware of the difference between |str| and |repr|.  A good string
representation (return value of |repr|) is one
that a Non-Python-Programmer does not identify to be a string.
The first ideal case is that copy-pasting the string representation
within a command line to evaluate it returns a reference to the same
object. A Python example:

    >>> repr(None)
    'None'
    >>> eval('None') is None
    True

A HydPy example:

    >>> from hydpy import Node
    >>> Node('gauge1')
    Node("gauge1", variable="Q")
    >>> eval('Node("gauge1", variable="Q")') is Node('gauge1')
    True

In the second ideal case is that evaluating the string representation
results in an equal object. A Python example:

    >>> 1.5
    1.5
    >>> eval('1.5') is 1.5
    False
    >>> eval('1.5') == 1.5
    True

A HydPy example:

    >>> from hydpy import Period
    >>> Period('1d')
    Period('1d')
    >>> eval("Period('1d')") is Period('1d')
    False
    >>> eval("Period('1d')") == Period('1d')
    True

For nested objects this might be more hard to accomplish, but sometimes it's
worth it.  A Python example:

    >>> [1., 'a']
    [1.0, 'a']
    >>> eval("[1.0, 'a']") == [1.0, 'a']
    True

A HydPy example:

    >>> from hydpy import Timegrid
    >>> Timegrid('01.11.1996', '1.11.2006', '1d')
    Timegrid('01.11.1996 00:00:00',
             '01.11.2006 00:00:00',
             '1d')
    >>> eval("Timegrid('01.11.1996 00:00:00', '01.11.2006 00:00:00', '1d')") == Timegrid('01.11.1996', '1.11.2006', '1d')
    True

ToDo: For deeply nested objects, this strategy becomes infeasible, of course.
SubParameters(None)...

Sometimes, additional information might increase the value of a
string representation.  Add comments in these cases, but only when
the |Options.reprcomments| flag handled in module |pub| is activated:

    >>> from hydpy.models.hland import *
    >>> parameterstep('1d')
    >>> nmbzones(2)
    >>> from hydpy.pub import options
    >>> options.reprcomments = True
    >>> nmbzones
    # Number of zones (hydrological response units) in a subbasin [-].
    nmbzones(2)
    >>> options.reprcomments = False
    >>> nmbzones
    nmbzones(2)

Such comments are of great importance, whenever the string representation
might be misleading:

    >>> simulationstep('12h')
    >>> percmax(2)
    >>> options.reprcomments = True
    >>> percmax
    # Maximum percolation rate [mm/T].
    # The actual value representation depends on the actual parameter step size,
    # which is `1d`.
    percmax(2.0)
    >>> options.reprcomments = False
    >>> percmax
    percmax(2.0)


Introspection
.............

One of Pythons major strengths is `introspection`, allowing you to analyze
(and modify) objects fundamentally at runtime.  One simple example would
be to access and change the documentation of a single HBV `number of zones`
parameter initialized at runtime.  Here, the given string representation
comment is simply the first line of the documentation string of class
|hland_control.NmbZones|:

    >>> from hydpy.models.hland.hland_control import NmbZones
    >>> NmbZones.__doc__.split('\n')[0]
    'Number of zones (hydrological response units) in a subbasin [-].'

However, we could define a unique documentation string for the specific
|hland_control.NmbZones| instance defined above:

    >>> nmbzones.__doc__ = NmbZones.__doc__.replace('a subbasin',
    ...                                             'the amazonas basin')

Now the representation string (only) of this instance is changed:

    >>> options.reprcomments = True
    >>> nmbzones
    # Number of zones (hydrological response units) in the amazonas basin [-].
    nmbzones(2)

As you can see, it is easy to retrieve information from living objects
and to adjust them to specific situations.  With little effort, one
can do much more tricky things. But when writing production code, one
has to be cautious.  First, do not all Python implementations support
each introspection feature of CPython.  Secondly is introspection often
a possible source of confusion.  For HydPy, only the second issue is of
importance, as the use of Cython rules out its application on alternative
Python implementations as `PyPy`_.  But the second issue needs to be
taken into account more strongly.

HydPy makes extensive use of Pythons introspection features, whenever it
serves the purpose of relieving non-programmers from writing code lines
that do not deal with hydrological modelling directly.  Section `Imports`_
discusses the usage of wildcard imports in parameter control files.
However, the real comfort comes primarily from the `magic` implemented
in the function |parameterstep|.  Through calling this function one does
not only define a relevant time interval length for the following parameter
values.  One also initializes a new model instance (if such an instance
does not already exist) and makes its control parameter objects available
in the local namespace.  Hence, for the sake of the user's comfort, each
parameter control file purports being a simple configuration file that
somehow checks its own validity.  On the downside, to modify the operating
principle of HydPy's parameter control files requires more thought than if
everything would have been accomplished in a more direct manner.

It is encouraged to implement additional introspection features into
HydPy, as long as they improve the intuitive usability for non-programmers.
But one should be particularly cautious when doing so and document the
why and how thoroughly.  To ensure traceability, one should usually add
such code to the modules like |modelutils| and |autodoctools|.  Module
|modelutils| deals with all introspection needed to `cythonize` Python models
automatically.  Module |autodoctools| serves for improving HydPy's online
documentation automatically.

Model specific features
-----------------------

Assuring code and documentation quality
_______________________________________

From a theoretical or even a philosophical point of view, the
capabilities and shortcomings of hydrological modelling have been
discussed thoroughly.  The negative impacts of low data quality
are addressed by many sensitivity studies.  By contrast, we are not
aware of any study focussing on the compromising effects of bugs
and misleading code documentation of hydrological computer models.
(Of course, such a study would be hard to conduct due to several
reasons.) Given the little attention paid during the peer-review
process to the correctness of model code and its transparent
documentation, the danger of scientific results being corrupted
by such flaws can --- carefully worded --- at least not be ruled
out.

This sections describes strategies on how to keep the danger
of severe bugs and outdated documentation to a (hopefully)
reasonable degree.

Conventional Unit-Tests
-----------------------

After installing HydPy through executing the `setup.py` module with
the argument `install`, the script `test_everything` is executed as well.
The first task of the latter module is to perform all `conventional`
unit tests.  Therefore, all modules within the subpackage `tests` named
'unittests_*.py' are evaluated based on the unit testing framework
|unittest| of Pythons standard library.  Each new HydPy module should
be complemented by a corresponding unittest file, testing its functionality
thoroughly.  Just write test classes in each unittest file.  These are
evaluated automatically by the script `test_everything`.  Let each class
name  start with 'Test', a consecutive number, and a description of the
functionality to be testet.  Each test class must inherit from
|unittest.TestCase|, allowing for using its assert methods.  Last but not
least, add the different test methods.  Again, each name should start with
'test' and a consecutive number, but this time in lower case letters
separated by underscores. By way of example, consider a snipplet of the
test class for the initialization of |Date| objects:

    >>> import unittest
    >>> import datetime
    >>> from hydpy.core import timetools
    >>> class Test01DateInitialization(unittest.TestCase):
    ...     def setUp(self):
    ...         self.refdate_day = datetime.datetime(1996, 11, 1)
    ...         self.refdate_hour = datetime.datetime(1996, 11, 1, 12)
    ...     def test_01_os_style_day(self):
    ...         self.assertEqual(self.refdate_day,
    ...                          timetools.Date('1996_11_01').datetime)
    ...     def test_02_os_style_hour(self):
    ...         self.assertEqual(self.refdate_hour,
    ...                          timetools.Date('1997_11_01_12').datetime)

The |unittest.TestCase.setUp| method allows for some preparations that
have to beconducted before the test methods can be called.  The status
defined in the |unittest.TestCase.setUp| method is restored before each
test method call, hence --- normally --- the single test methods do not
affect each other (the consecutive numbers are only used for reporting
the test results in a sorted manner).  In case the test methods affect
some global variables, add a |unittest.TestCase.tearDown| method to your
test class, which will be executed after each test method call. See the
documentation on |unittest.TestCase| regarding the available assert methods.

To elaborate the example above, the two test methods are executed manually
(normally, this is done by the script `test_everything` automatically).
First prepare an object for the test results:

    >>> result = unittest.result.TestResult()

Then initialize a test object engaging the first test method and run
all assertions (in this case, there is only one assertion per method):

    >>> tester = Test01DateInitialization('test_01_os_style_day')
    >>> _ = tester.run(result)

Now do the same for the second test method:

    >>> tester = Test01DateInitialization('test_02_os_style_hour')
    >>> _ = tester.run(result)

The test result object tells us that two tests have been executed, that
no (unexpected) error occured, and that one test failed:

    >>> result
    <unittest.result.TestResult run=2 errors=0 failures=1>

Here is the reason for the (intentional) failure in this example:

    >>> print(result.failures[0][-1].split('\n')[-2])
    AssertionError: datetime.datetime(1996, 11, 1, 12, 0) != datetime.datetime(1997, 11, 1, 12, 0)



Doctests
--------

When defining `conventional` unit tests, one tries to achieve a large
test coverage with few lines of code (don't repeat yourself!).
Therefore, sophisticated tools like the `mock object library`_ are
available.  Unit tests might also save the purpose to explain the
functioning of the main code, as they explicitly show how it can
be used.  However, the latter is pie in the sky when the unit tests
are interpreted by someone who has little experience in unit testing
and maybe little experience in programming at all.  This might not be
a relevant problem as long as we test such basic functionalities of
the HydPy framework, the user is not really interested in directly or
just expects to work.  However, at the latest when the implemented
hydrological models are involved, the clarity of the defined unit tests
is desirable even for non-programmers (and --- in our opinion ---
it is scientifically necessary).

Each model implemented in HydPy should be tested in a manner that is
as clear and comprehensible as possible.  To this end, the documentation
test principle defined by the module |doctest| should be applied
extensively.  At least, all code branches including (hydrological)
equations should be captured completely via doctests. (More technical
branches, e.g. those including the treatment of exceptions, can be
left to conventional unit tests.)  Often only one or two sentences
are required to explain a doctest in a way, allowing a non-programmer
to understand and repeat it.  And through repetition, he learns to
apply the model.

Besides their intuitiveness, doctests offer the big advantage of
keeping source code and documentation in sync.  Whenever either
a source line or its associated doctest contains errors, or
whenever the source code is updated but the associated doctests
not (or the other way round), it is reported.  Hence all examples
in the HydPy documentation should be written as doctests.  The more
doctests the documentation includes, the merrier the danger of
retaining outdated documentation sections.  In order to keep an
eye on a concrete example: as long as this three-line doctest...

    >>> from hydpy.core import objecttools
    >>> objecttools.classname(objecttools)
    'module'

...remains in the documentation, one can be sure that the current
core package contains a module named `objecttools`.

To support the frequent usage of doctests, one is allowed to use
them at any section of the documentation, accepting possible
redundancies with defined `conventional` unit tests.  The script
`test_everything` searches for doctests in all Python modules and
all `reStructuredText`_ files contained in the package hydpy and
executes them.


Continuous Integration
----------------------

To improve the code base of HydPy, you need your own working copy
(your own fork, see section `How to contribute?`_).  The existence
of multiple working copies inevitably leads to the danger of
integration problems, meaning that different changes in different
working copies lead to source code incompatibilities.  To reduce
this risk, the different working copies should be merged `continuously`.
This decreases the likelihood of simultaneous changes to the same
code sections and keeps the complexity of possible conflicts to
a minimum.

The current (online) development of HydPy relies, besides `GitHub`_,
on `Travis CI`_.  `Travis CI`_ is a hosted, distributed continuous
integration service.  This `Travis CI project`_ has been linked
to HydPy's `GitHub repository`_.  It is configured to accomplish
the following tasks for each new commit or pull request:

  * Install HydPy on the Debian based Linux operating system Ubuntu using
    different versions of CPython.
  * Cythonize all implemented models on the different Python versions.
  * Execute all `conventional` unit tests and all doctests on the
    different Python versions.
  * Prepare a `Test Coverage`_ report based on Python 2.7.
  * Update this `online documentation`_ based on Python 2.7.

Installation and testing are performed using Python 2.7, 3.4, 3.5 and 3.6.
2.7 still seems to be the Python version most frequently used by scientists.
Python versions 3.0 to 3.3 do not seem to be of great importance anymore.
Additionally, installation and testing are performed using the development
branches of version 3.5, 3.6 and (the still not released) version 3.7.
This offers the advantage of anticipating future problems and to
`test future Python`_ itself, possibly helping to avoid future bugs.

Whenever one single test fails under one single Python version, the total
process (build) is regarded as defective and will not be merged into
the master branch of the main fork.  The same is true, of course, when
one installation process itself fails.  So make sure all your changes
are compatible with each selected Python version.  But, in accordance with
one of Python's principle, it is easier to ask for forgiveness than
permission: let Travis evaluate your current working branch and see what
happens...

Not only the source code but also the contributed documentation
text is checked in two ways. Doctesting is discussed above and always
performed using each mentioned Python version.  Additionally, when
using  Python 2.7 the properness of the whole documentation text is
considered. `Sphinx`_ is applied to create the HTML pages of this
`online documentation`_ based on the given `reStructuredText`_ files.
In case problems occur, e.g. due to faulty inline markup, the
total build (including all Python versions) is regarded as defective.
This assures that each new HydPy version is accompanied by a
functioning online documentation.  If nothing goes wrong, the
`travis-sphinx`_ script is used to push the final HTML pages to the
`gh-pages branch`_ automatically, meaning, that this
`online documentation`_ is updated immediately.  This deploy process
is restricted to the `master branch`_ of the main development line
and has disabled pull request option for safety reasons.


Test Coverage
-------------

This is the :download:`latest coverage report <coverage.html>`.

One can never be sure, that all important aspects of a software
application are checked properly (instead, one can be quite certain,
one has always missed something...).  However, one can at least evaluate
the runtime behaviour of the tests themselves in order to find out
which code sections they do invoke and which not.  HydPy's
`Travis CI project`_ has been configured to perform such an evaluation
automatically for each build process based on `Coverage.py`_.  The
resulting HTML report is linked to this `online documentation`_
automatically.

The coverage report does only include modules with a percentage
coverage less than 100 %, as only those need further attention.
If a code section is covered one can at least be sure, that it does
not cause an unhandled exception or a total program crash on the
applied Python versions. But one cannot be sure, that the test(s)
actually covering the code section are meaningful.

Note that the coverage analysis is performed on Python 2.7 only.
Hence code sections only relevant for Python 3 might be reported
as uncovered erroneously.

