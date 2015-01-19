from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog import urls as blog_urls
from home import urls as home_urls
from photo import urls as photo_urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jaywhiletwo.views.home', name='home'),

    url(r'^blog/', include(blog_urls, namespace="blog", )),
    url(r'^photo/', include(photo_urls, namespace="photo", )),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(home_urls, namespace="home", )),
)
