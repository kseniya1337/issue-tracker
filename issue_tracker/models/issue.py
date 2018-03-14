from django.db import models
from model_utils import Choices


class Issue(models.Model):
    STATUS = Choices(
        ('open', 'Открыта'),
        ('in_progress', 'В разработке'),
        ('testing', 'В тестировании'),
        ('production', 'В исполнении'),
        ('closed', 'Закрыта'),
    )

    PRIORITY = Choices(
        ('minor', 'Незначительная'),
        ('normal', 'Обычная'),
        ('major', 'Важная'),
        ('critical', 'Критическая')
    )

    title = models.CharField(
        max_length=255,
        verbose_name='название',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    assignee = models.ForeignKey(
        to='issue_tracker.User',
        related_name='issues',
        on_delete=models.deletion.SET_NULL,
        null=True,
        blank=True,
        verbose_name='исполнитель',
    )
    status = models.CharField(
        max_length=255,
        verbose_name='статус',
        choices=STATUS,
        default=STATUS.open,
    )
    priority = models.CharField(
        max_length=255,
        verbose_name='приоритет',
        choices=PRIORITY,
        default=PRIORITY.normal,
    )

    author = models.ForeignKey(
        to='issue_tracker.User',
        on_delete=models.deletion.SET_NULL,
        null=True,
        blank=True,
        verbose_name='автор',
        related_name='created_issues',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='дата обновления',
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return f'{self.pk} {self.title}'
