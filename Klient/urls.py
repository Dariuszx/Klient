from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login, index, logout, my_ideas, show_idea, show_thread, new_note

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Klient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login$', login),
    url(r'^$', index),
    url(r'^logout$', logout),
    url(r'^my/idea$', my_ideas ),
    url(r'^show/idea/(?P<idea_id>\d+)', show_idea),
    url(r'^show/thread/(?P<thread_id>\d+)', show_thread),
    url(r'^new/note/(?P<thread_id>\d+)', new_note),
)
