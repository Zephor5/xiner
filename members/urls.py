from django.conf.urls import patterns, url
from views import json_data

urlpatterns = patterns('',
    # Examples:
    url(r'^json', json_data),
)