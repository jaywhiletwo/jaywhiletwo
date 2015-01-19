from django.conf.urls import patterns, include, url

from .views import list


urlpatterns = patterns('',
    url(r'list', list, name='list', ),
)
