from django.conf.urls import patterns, include, url

import views,registration_views

urlpatterns = patterns('',
    url(r'^$', views.main_view, name="main_view"),
    url(r'^login/$', registration_views.login_view, name="login"),
    url(r'^logout/$', registration_views.logout_view, name="logout"),
    url(r'^register/$', registration_views.register_view, name="register"),
    url(r'^detail-view/(?P<gigid>[-\d]+)/$',views.detail_view, name="detail_view")
)

