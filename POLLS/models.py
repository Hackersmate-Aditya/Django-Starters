from django.db import models
import datetime



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
                                                                               #our 2 models question and choice

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Create your models here.
