Settings
========

Available settings
------------------

Here's a full list of available settings,
in alphabetical order,
and their default values.

PUPPETEER_PDF_CMD
~~~~~~~~~~~~~~~~~

Default: ``'puppeteer-pdf'``

The name of the ``puppeteer-pdf`` binary.

If there are no path components,
this app will look for the binary using the default OS paths.

PUPPETEER_PDF_CMD_OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``{'encoding': 'utf8', 'quiet': True}``

A dictionary of command-line arguments to pass to the ``puppeteer-pdf``
binary.
Keys are the name of the flag and values are arguments for the flag.

To pass a simple flag,
for example:
``puppeteer-pdf --landscape``:

.. code-block:: python

    PUPPETEER_PDF_CMD_OPTIONS = {'landscape': True}

To pass a flag with an argument,
for example:
``wkhtmltopdf --marginTop '100px'``:

.. code-block:: python

    PUPPETEER_PDF_CMD_OPTIONS = {'marginTop': '100px'}


PUPPETEER_PDF_DEBUG
~~~~~~~~~~~~~~~~~~~

Default: same as :py:data:`settings.DEBUG`

A boolean that turns on/off debug mode.

