from django.conf.urls import patterns, include, url

from .views import image_set


urlpatterns = patterns('',
    url(r'list/(?P<gallery_slug>[-_\w\d]+)', image_set, name='image_set', ),
    url(r'list', image_set, name='image_set', ),
)
