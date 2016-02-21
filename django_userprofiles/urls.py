from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from userprofiles.views import AllUsersView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', AllUsersView.as_view(), name='all_users'),
    # url(r'^post/(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('userprofiles.urls', namespace='userprofiles')),
)
