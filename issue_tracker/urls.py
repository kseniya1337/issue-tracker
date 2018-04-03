from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from issue_tracker import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<username>[0-9A-Za-z_]+)/$', views.profile, name='profile'),
    url(r'^profile/change-avatar/$', views.change_avatar, name='change_avatar'),
    url(r'^create/$', views.create_issue, name='create_issue'),
    url(r'^issue/(?P<id>\d+)/$', views.issue_detail, name='issue_detail'),
    url(r'^search/$', views.search_issue, name='search_issue'),
    url(r'^issue/(?P<id>\d+)/edit/$', views.edit_issue, name='edit_issue'),
    url(r'^issue/(?P<id>\d+)/comment/$', views.create_comment, name='create_comment'),
    url(r'^issue/(?P<issue_id>\d+)/comment/(?P<comment_id>\d+)/delete/$', views.delete_comment, name='delete_comment'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
