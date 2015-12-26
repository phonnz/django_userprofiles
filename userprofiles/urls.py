from django.conf.urls import patterns, include, url

from .views import AllUsersView, UserDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'userprofiles.views.home', name='home'),
    url(r'^usuarios/$', AllUsersView.as_view(), name='all_users'),
    url(r'^usuario/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^cerrar-sesion/$', 'userprofiles.views.signout', name='signout'),

)
