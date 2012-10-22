from django.conf.urls import patterns, include, url
from simpleApp.views import WordDetailView
from simpleApp.functionalViews import my_word_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', WordDetailView.as_view()),
	url(r'^words$', my_word_view),
)
