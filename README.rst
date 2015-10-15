django-failedfirsttestrunner
-----

Reorders your test suite so failed tests are ran first on subsequent test runs:

.. code:: bash

    Creating test database for alias 'default'...
    .............................FF.........
    ----------------------------------------------------------------------
    Ran 40 tests in 160.597s
    ...
    FAILED (failures=2)

    Destroying test database for alias 'default'...

.. code:: bash

    Creating test database for alias 'default'...
    FF......................................
    ----------------------------------------------------------------------
    Ran 40 tests in 160.597s
    ...
    FAILED (failures=2)

    Destroying test database for alias 'default'...

Install
-----

::

    pip install -e git://github.com/leetreveil/django-failedfirsttestrunner.git#egg=django-failedfirsttestrunner

Then just set ``TEST_RUNNER`` in ``settings.py`` and you are good to go!

.. code:: python

    TEST_RUNNER = 'django_failedfirsttestrunner.FailedFirstRunner'

Licence
----
MIT