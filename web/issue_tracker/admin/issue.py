from django.contrib import admin

from issue_tracker.models import Issue


class IssueAdmin(admin.ModelAdmin):

    list_display = ['id', 'title']


admin.site.register(Issue, IssueAdmin)
