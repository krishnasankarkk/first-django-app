import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Function to store Question"""

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """Function to store Choices."""

    question_reference = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
