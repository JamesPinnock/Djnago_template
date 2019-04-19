from django.contrib.auth.models import User
from django.db import models



class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    platenumber = models.CharField(max_length=9)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
