from django.db import models

STATUS_CHOICES = (
    ('active', 'Active'),
    ('blocked', 'Blocked')
)

DEFAULT_STATUS = STATUS_CHOICES[0][0]


class Entry(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name')
    mail = models.EmailField(max_length=60, null=False, blank=False, verbose_name='Email')
    text = models.CharField(max_length=500, null=False, blank=False, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DEFAULT_STATUS, verbose_name='Status')

    def __str__(self):
        return f'{self.pk}.By: {self.name}. Status: {self.status}. Created at: {self.created_at}'