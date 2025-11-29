from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.Email.EmailField(unique=True)
    course = models.CharField(max_length=100)
