from django.conf.urls import patterns, include, url

from .views import image, image_set


urlpatterns = patterns('',
    url(r'show', image, name='image', ),
    url(r'list/(?P<gallery_slug>[\w\d]+)', image_set, name='image_set', ),
    url(r'list', image_set, name='image_set', ),
)
