Setup
=====

1.  Get the source from the `Git repository`_ or install it from the Python
    Package Index by running ``pip install django-webtemplates``.

2.  Add ``webtemplates`` to the ``INSTALLED_APPS`` setting::

        INSTALLED_APPS += (
            'webtemplates',
        )

3.  Add ``webtemplates`` to the ``TEMPLATE_LOADERS`` setting::

        TEMPLATE_LOADERS += (
            'webtemplates.loaders.Loader',
        )

    Order is important. If you define ``webtemplates.loaders.Loader`` before
    other loaders, ``webtemplates`` will be used before any templates on your
    local system. If the ``webtemplates`` is defined after other loaders,
    the ``webtemplates`` loader will only be used if the template is not found
    locally.

4.  Define all of the remote templates you want to use in the ``WEBTEMPLATES``
    setting. This should be a list of two-tuples, which define the remote
    template location, and its local name::

        WEBTEMPLATES_BASE = 'http://example.com/templates/'
        WEBTEMPLATES = [
            (WEBTEMPLATES_BASE + 'site_base.html', 'site_base.html'),
            (WEBTEMPLATES_BASE + 'user_page.html', 'logged_in_base.html'),
        ]

    ``WEBTEMPLATES_BASE`` is used here to stop ourselves duplicating the full
    path of the remote template every time, but ``WEBTEMPLATES_BASE`` is NOT
    used anywhere by ``webtemplates``.

    Note how ``logged_in_base.html`` comes from an address with a different
    basename. The template names do not need to match up.

5.  ``site_base.html`` and ``logged_in_base.html`` will now be loaded from
    ``http://example.com/templates/site_base.html`` and
    ``http://example.com/templates/user_page.html``. You can use them just like
    any other template in your system.

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
