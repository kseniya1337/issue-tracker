from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from issue_tracker import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),

    path('', views.index, name='index'),
    path('profile/change-avatar/', views.change_avatar, name='change_avatar'),
    path('profile/<username>/', views.profile, name='profile'),
    path('create/', views.create_issue, name='create_issue'),
    path('issue/<int:id>/', views.issue_detail, name='issue_detail'),
    path('search/', views.search_issue, name='search_issue'),
    path('issue/<int:id>/edit/', views.edit_issue, name='edit_issue'),
    path('issue/<int:id>/comment/', views.create_comment, name='create_comment'),
    path('issue/<int:issue_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('t/<path:template_name>', render),
    ]
