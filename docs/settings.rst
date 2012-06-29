========
Settings
========

.. _configuration:

Configuration
=============

The remote templates that you want to use must all be defined in the Django
``settings.py``. ``django-webtemplates`` does not have any functionality to
automatically discover remote templates.

To define remote templates, you must provide a list of two-tuples which define
where to find each remote template you want to load::

    WEBTEMPLATES_BASE = 'http://example.com/templates/'
    WEBTEMPLATES = [
        (WEBTEMPLATES_BASE + 'foo.html', 'foo.html'),
        (WEBTEMPLATES_BASE + 'bar.html', 'bar.html'),
    ]

This will instruct ``webtemplates`` to load two templates: ``foo.html`` and
``bar.html``. They will be loaded from 
``http://example.com/templates/foo.html`` and
``http://example.com/templates/bar.html`` respectively. ``webtemplates`` will
only try to load those two templates from those two locations, and nothing more.

.. note::   ``WEBTEMPLATES_BASE`` is used here to stop ourselves duplicating the
            full path of the remote template every time, but
            ``WEBTEMPLATES_BASE`` is NOT used anywhere by ``webtemplates``.

Application templates
---------------------

Templates can be loaded from subdirectories, just like they are from the
file system. This is usually done for separating app templates from one another::

    WEBTEMPLATES_BASE = 'http://example.com/templates/'
    WEBTEMPLATES = [
        (WEBTEMPLATES_BASE + 'polls/base.html', 'polls/base.html'),
        (WEBTEMPLATES_BASE + 'blog/base.html', 'blog/base.html'),
    ]

This will attempt to load ``polls/base.html`` from
``http://example.com/templates/polls/base.html``.

Different remote and local names
--------------------------------

Some times, the remote application does not allow you to name things in the same
manner you would expect of Django templates. Many frameworks remote the
``.html`` extension, for example, preferring to pretend everything is a
directory and ending in ``/``. Django itself does this. The remote name of a
webtemplate does not need to match up with the local name::

    WEBTEMPLATES_BASE = 'http://example.com/'
    WEBTEMPLATES = [
        (WEBTEMPLATES_BASE + 'templates_for_django/polls/', 'polls/base.html'),
        (WEBTEMPLATES_BASE + 'blog_template_for_django/', 'blog/base.html'),
    ]

This will attempt to load ``polls/base.html`` from
``http://example.com/templates_for_django/polls/``, and ``blog/base.html`` from
``http://example.com/blog_template_for_django/``.

.. _caching:

Caching
=======

Remote templates are cached by default, instead of requesting the template each
time it is required. It uses the `Django caching framework`_ to cache the result
of each template request.

``webtemplates`` uses the ``webtemplates`` cache settings, if they are defined,
falling back to the ``default`` cache if it is not. If you want to modify any of
the cache settings for ``webtemplates``, add a ``webtemplates`` key to the
Django ``CACHES`` setting::

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'DefaultCache:',
        },
        'webtemplates': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'WebTemplates:',
            'TIMEOUT': 10, # Cache for 10 seconds.
        },
    }

Note that a ``default`` cache is required by Django, even if you do not use it.
The local memory cache should be good enough for most applications, unless you
define a large number of remote templates.

During development, you will probably want to use the dummy cache backend,
``django.core.cache.backends.dummy.DummyCache``, which does not actually cache
anything.

Permanent caching
-----------------

Your templates can be cached indefinitely, in case the remote templates become
unavailable. A fresh copy of the templates will be requested as the main cache
expires, but if a fresh copy can not be obtained, the stale copy from the
permanent cache will be used in its place. You can enable this by setting
``WEBTEMPLATES_PERMANENT_CACHE`` to ``True`` in your ``settings.py``::

    WEBTEMPLATES_PERMANENT_CACHE = True

This is turned off by default. If you need a fall back in case the remote server
is unavailable, you can also use the normal Django template loader hierarchy.
If a template can not be loaded via webtemplates, the next template loader
defined in ``TEMPLATE_LOADERS`` will be used instead.

.. note:: If the remote server is not available when the template is initially
    loaded, and you are using a non-permanent cache like MemCache or
    LocMemCache, then there will be no permanently cached template to return.
    The template loading will fall through to the next template loader in the
    hierarchy. It is very important that you always create a local fall back
    template for each of your remote templates.

.. _Django caching framework: https://docs.djangoproject.com/en/dev/topics/cache/
