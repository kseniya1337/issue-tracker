from django.db import models
from django.utils import timezone


class Comment(models.Model):
    issue = models.ForeignKey(
        to='issue_tracker.Issue',
        related_name='comments',
    )
    author = models.ForeignKey(
        to='issue_tracker.User',
        on_delete=models.deletion.SET_NULL,
        null=True,
        verbose_name='автор',
        related_name='comments',
    )
    text = models.TextField(
        verbose_name='текст комментария',
    )

    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата создания',
    )

    def __str__(self):
        return self.text



