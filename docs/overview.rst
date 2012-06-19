Setup
=====

1.  Get the source from the `Git repository`_ or install it from the Python
    Package Index by running ``pip install django-webtemplates``.

2.  Add ``webtemplates`` to the ``INSTALLED_APPS`` setting::

        INSTALLED_APPS += (
            'webtemplates',
        )

3.  Add ``webtemplates`` to the ``TEMPLATE_LOADERS`` setting, defining all of
    the external templates you want to use::

        TEMPLATE_LOADERS += (
            ('webtemplates.loaders.Loader', 'http://example.com/templates/', (
                'site_base.html',
                'logged_in_base.html',
            )),
        )

    Order is important. If you define ``webtemplates.loaders.Loader`` before
    other loaders, ``webtemplates`` will be used before any templates on your
    local system. If the ``webtemplates`` is defined after other loaders,
    the ``webtemplates`` loader will only be used if the template is not found
    locally.

4.  ``site_base.html`` and ``logged_in_base.html`` will now be loaded from 
    ``http://example.com/templates/site_base.html`` and
    ``http://example.com/templates/logged_in_base.html``. You can use them
    just like any other template in your system.

Usage
=====

Once set up, you can use any of the templates defined as a web template just
like a normal templates. This works both ways - local templates can extend
remote templates, remote templates can include local templates, and remote
templates can use template tags and filters. Local and remote templates work
exactly the same.

Example
=======

An exmaple Django application is provided in the `example/ directory`_ in the
repository. It defined two pages that override two remote templates.

.. _Git repository: http://bitbucket.org/ionata/django-webtemplates/
.. _example/ directory: http://bitbucket.org/ionata/django-webtemplates/src/master/exmaple/
