from django.apps import AppConfig


class IssueTrackerConfig(AppConfig):
    name = 'issue_tracker'
    verbose_name = 'Трекер задач'


default_app_config = 'issue_tracker.IssueTrackerConfig'
