from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

class Question(models.Model):
    q_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    datetime.timedelta(days=1)
    def __str__(self):
        return self.q_text
    @admin.display(

        boolean = True,
        ordering = 'pub_date',
        description = 'Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now


class Choice(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text




# Create your models here.
