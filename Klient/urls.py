from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login, index, logout, my_ideas, show_idea, show_thread, new_note, new_thread, show_note, delete_note, edit_note

urlpatterns = patterns('',
    url(r'^login$', login),
    url(r'^$', index),
    url(r'^logout$', logout),
    url(r'^my/idea$', my_ideas ),
    url(r'^show/idea/(?P<idea_id>\d+)', show_idea),
    url(r'^show/thread/(?P<thread_id>\d+)', show_thread),
    url(r'^new/note/(?P<thread_id>\d+)', new_note),
    url(r'^new/thread/(?P<idea_id>\d+)', new_thread),
    url(r'^show/note/(?P<note_id>\d+)', show_note),
    url(r'^delete/note/(?P<note_id>\d+)', delete_note),
    url(r'^edit/note/(?P<note_id>\d+)', edit_note),
)
