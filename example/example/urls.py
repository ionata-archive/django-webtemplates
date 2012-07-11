from django.conf.urls import patterns, include, url

from example import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^alt$', views.alt, name='alt'),
)
