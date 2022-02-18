from django.db import models

# Create your models here.
class Student(models.Model):
  student_name = models.CharField(max_length=45)
  password = models.CharField(max_length=45)
  comment_flag = models.CharField(max_length=45)
