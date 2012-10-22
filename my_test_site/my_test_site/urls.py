from django.conf.urls import patterns, include, url
from simpleApp.views import WordDetailView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', WordDetailView.as_view()),
	url(r'^words$', WordDetailView.as_view()),
)
