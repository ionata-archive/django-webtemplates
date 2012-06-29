"""
A Django template loader that loads templates from a remote web site
"""
import requests

from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from django.core import cache
from django.conf import settings

try:
    WEBTEMPLATES = settings.WEBTEMPLATES
except AttributeError:
    raise AttributeError("WEBTEMPLATES must be defined in your settings.py")


class Loader(BaseLoader):
    """
    Load templates for Django from a remote web site
    """
    is_usable = True

    def __init__(self, templates=WEBTEMPLATES):
        try:
            self.cache = cache.get_cache('webtemplates')
        except InvalidCacheBackendError:
            self.cache = cache.cache


        if not isinstance(templates, (list, tuple)):
            raise ValueError("templates should be a list or tuple, not %s"
                % type(templates))

        self.templates = {}
        for template in templates:
            if isinstance(template, (tuple, list)):
                (remote, local) = template
            else:
                raise ValueError("Expected tuple for template name, not %s"
                    % type(template))
            
            self.templates[local] = remote

    def load_template_source(self, template_name, template_dirs=None):
        # We can only load templates that have been defined
        if template_name not in self.templates:
            raise TemplateDoesNotExist(template_name)

        url = self.templates[template_name]

        # Try and load from the cache
        cached = self.cache.get(url)
        if cached is not None:
            return (cached, url)

        # Go and get it from the internets
        r = requests.get(url)
        if r.status_code != 200:
            raise TemplateDoesNotExist(template_name)

        # Yay successful result! cache it a keep going
        self.cache.set(url, r.text)
        return (r.text, url)
