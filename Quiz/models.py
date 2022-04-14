from concurrent.futures.process import _ThreadWakeup
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    reference = models.URLField(max_length=200,null=True, blank=True)
    category = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.question

class ResultModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)
    date = models.DateTimeField(default = datetime.now)