from django.db import models

# Create your models here.

CHOICE = ('danger', 'high'),('warning', 'normal'), ('primary', 'low')

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True)
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
        )
    duedate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title