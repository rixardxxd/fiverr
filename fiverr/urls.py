from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^', include('website.urls',namespace="website")),
    url(r'^comments/', include('fluent_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

handler500 = 'website.error_views.server_error'