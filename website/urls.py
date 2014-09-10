from django.conf.urls import patterns, include, url

import views,registration_views

urlpatterns = patterns('',
    url(r'^$', views.main_view, name="main_view"),
    url(r'^login/$', registration_views.login_view, name="login"),
    url(r'^logout/$', registration_views.logout_view, name="logout"),
    url(r'^register/$', registration_views.register_view, name="register"),
    url(r'^gig-view/(?P<gigid>[-\d]+)/$',views.gig_view, name="gig_view"),
    url(r'^search-view/$',views.search_view, name="search_view"),
    url(r'^order-complete-view/$',views.order_complete_view, name="order_complete_view")
)

