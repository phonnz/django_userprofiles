from django.conf.urls import patterns, include, url

from .views import AllUsersView, UserDetailView, SlugUserDetailView, CreateUserView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'userprofiles.views.home', name='home'),
    url(r'^usuarios/$', AllUsersView.as_view(), name='all_users'),
    url(r'^usuario/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^nombre-de-usuario/(?P<slug>[-\w]+)/$', SlugUserDetailView.as_view(), name='username_detail'),
    url(r'^registrar/$', CreateUserView.as_view(), name='create_user'),
    url(r'^cerrar-sesion/$', 'userprofiles.views.signout', name='signout'),

)
