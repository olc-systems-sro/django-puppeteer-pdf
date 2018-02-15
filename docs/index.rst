==================
django-puppeteer-pdf
==================

``django-puppeteer-pdf`` allows a Django site to output dynamic PDFs. It utilises
the puppeteer_ library, allowing you to write using the technologies you know
- HTML and CSS - and output a PDF file.

.. _puppeteer: https://www.npmjs.com/package/puppeteer-pdf

Quickstart
==========

.. code-block:: bash

    pip install django-puppeteer-pdf

Install the puppeteer-pdf cli puppeteer-pdf_ for your platform.

.. _puppeteer-pdf: https://www.npmjs.com/package/puppeteer-pdf

``settings.py``

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'puppeteer_pdf',
        # ...
    )

``urls.py``

.. code-block:: python

    from django.conf.urls.defaults import url, patterns
    from puppeteer_pdf.views import PDFTemplateView

    urlpatterns = patterns('',
        url(r'^pdf/$', PDFTemplateView.as_view(template_name='my_template.html',
                                               filename='my_pdf.pdf'), name='pdf'),
    )

Contribute
==========

You can fork the project on Github_.

.. _Github: https://github.com/incuna/django-puppeteer-pdf

Contents
========

.. toctree::
    :maxdepth: 1

    installation
    usage
    settings
