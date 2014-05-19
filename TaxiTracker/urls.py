from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .views import *
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    (r'^$','TaxiTracker.views.MarkMap'),
    (r'^querymap/$', 'TaxiTracker.views.QueryMap'),
    url(r'^querymap/users/$', 'TaxiTracker.views.ajax_checks_area')
)
