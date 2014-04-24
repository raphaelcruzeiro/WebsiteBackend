from django.conf.urls import patterns, include, url
from core import urls as api_urls

urlpatterns = patterns('',
    url(r'^', include(api_urls)),
)
