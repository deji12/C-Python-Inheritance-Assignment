from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):

    title = models.CharField(max_length=225)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.title