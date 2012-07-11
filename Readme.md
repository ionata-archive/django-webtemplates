django-webtemplates
==============================================

Fairly often at Ionata, we have built hybrid Django and `$other-framework`
applications. The Django application is for a completely custom booking
process, or a online catering page, or a frontend view to the customers custom
database. We then use something like Wordpress or Magento to provide a
familiar blogging, CMS, or shop platform. In an ideal world, we would use the
one framework for everything, but quite simply we do not want to reimplement
Wordpress in Django when Wordpress already exists!

Of course, then the problem of syncing templates across the two systems
arises. Usually, the `$other-framework` runs the majority of the site, and
defines a menu structure, footer links, etc. This content can change, so making
a static template on the Django side is not a thing that can happen.

By using `django-webtemplates`, you can define templates that live at a URI.
Simply set up a dummy page in `$other-framework` that has all the required
wrappings, and insert all the Django block hooks that you need. The template
will be loaded from the external site just like any other template, and local
templates can `{% extend %}` it as they desire.
