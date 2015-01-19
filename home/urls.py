from django.conf.urls import patterns, include, url

from .views import home, test404


urlpatterns = patterns('',
    url(r'404', test404, ),
    url(r'^$', home, name='home', ),
)
