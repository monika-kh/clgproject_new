from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class College(models.Model):
    college_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return str(self.college_name)

    class Meta:
        db_table = 'College'


class Student(AbstractUser):
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    address = models.TextField(max_length=100, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True, related_name='college_student')
    dob = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Student'



