from django import forms

from issue_tracker.models import Issue, User


class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title',
            'assignee',
            'priority',
            'description',
        ]


class EditIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title',
            'assignee',
            'priority',
            'status',
            'description',
        ]


class AvatarChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar',
        ]
