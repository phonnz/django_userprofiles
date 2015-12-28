from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from web.views import PostDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'userprofiles.views.home', name='home'),
    url(r'^post/(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('userprofiles.urls', namespace='userprofiles')),
)
