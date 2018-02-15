Full Installation Notes
=======================

Installing the Package
----------------------

From PyPI
~~~~~~~~~

.. code-block:: bash

    pip install django-puppeteer-pdf


From source
~~~~~~~~~~~

.. code-block:: bash

    git clone git://github.com/namespace-ee/django-puppeteer-pdf.git
    cd django-puppeteer-pdf
    python setup.py install


Installing the puppeteer-pdf
---------------------

Find the relevant version of the ``puppeteer-pdf``
`downloads page`_.

.. _downloads page: https://www.npmjs.com/package/puppeteer-pdf

Setting up your Django
----------------------

Add ``puppeteer_pdf`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'puppeteer_pdf',
        # ...
    )

By default it will try to execute the ``puppeteer-pdf`` command from your ``PATH``.

If you can't add ``puppeteer-pdf`` to your ``PATH`` or you want to use some other
version, you can use the ``PUPPETEER_PDF_CMD`` setting:

.. code-block:: python

    PUPPETEER_PDF_CMD = '/path/to/my/puppeteer-pdf'

Display static files
----------------------

Set ``STATIC_ROOT`` in your ``settings.py``:

.. code-block:: python

    STATIC_ROOT = '/full/path/to/static/directory/'
    
Make sure your static files and directories are inside this directory.

**Note:**
In production static files are supposed to reside outside the project folder, in a public directory. The STATIC_ROOT-setting gives the path to this directory. However, django-puppeteer-pdf requires that STATIC_ROOT is also set on your local machine.

In development the static files reside in their respective apps folder or in a cross-app directory defined by the STATIC_DIRS-setting. Refer to the django documentation for how you can move static files to the STATIC_ROOT directory through a django script.

