from django import forms

from issue_tracker.models import Issue, User
from issue_tracker.models import Comment


class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title',
            'assignee',
            'priority',
            'description',
        ]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
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
