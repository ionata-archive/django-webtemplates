import requests

from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from django.core import cache
# import get_cache, InvalidCacheBackendError

try:
    webcache = cache.get_cache('webtemplates')
except InvalidCacheBackendError:
    webcache = cache.cache

class Loader(BaseLoader):
    is_usable = True

    def __init__(self, base, template_names):
        if not isinstance(template_names, (list, tuple)):
            raise ArgumentError("template_names should be a list or tuple, not %s" % type(template_names))

        self.setup(base, template_names)
        print "Loaded"

    def setup(self, base, template_names):
        templates = {}
        for template in template_names:
            print "Adding %s to the list" % (template, )
            if isinstance(template, (tuple, list)):
                (local, remote) = template
            elif isinstance(template, basestring):
                local = remote = template
            else:
                raise ArgumentError("Expected string or list for template name, not %s" % type(template))
            
            templates[local] = base + remote

        self.templates = templates

    def load_template_source(self, template_name, template_dirs=None):
        # We can only load templates that have been defined
        if template_name not in self.templates:
            raise TemplateDoesNotExist(template_name)

        url = self.templates[template_name]

        # Try and load from the cache
        cached = webcache.get(url)
        if cached is not None:
            return (cached, url)

        # Go and get it from the internets
        r = requests.get(url)
        if r.status_code != 200:
            raise TemplateDoesNotExist(template_name)

        # Yay successful result! cache it a keep going
        webcache.set(url, r.text)
        return (r.text, url)
