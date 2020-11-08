
from django.db import models
import json


class Choice(models.Model):
    Choice_id = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

class People(models.Model):
    PName = models.CharField(max_length=20)
    PVote = models.CharField(max_length=1000)


   
