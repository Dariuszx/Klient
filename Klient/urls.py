from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Klient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login$', login)
)
