from django.conf.urls import include, url
from django.contrib import admin
from ozonid.views import hello, main

urlpatterns = [
    # Examples:
    # url(r'^$', 'ozonid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$', main),
    url('^hello/$', hello),
    url(r'^admin/', include(admin.site.urls)),
]
