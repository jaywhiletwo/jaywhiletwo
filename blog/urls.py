from django.conf.urls import patterns, include, url

from .views import blog


urlpatterns = patterns('',
    url(r'', blog, name='blog', ),
)
