from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class Form(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=5)
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.issue

    

