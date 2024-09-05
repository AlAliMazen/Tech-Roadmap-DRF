from django.db import models
from django.contrib.auth.models import User
from course.models import Course, AVAILABLE_COURSES

# Create your models here.
class Enrollment(models.Model):
    """
    Represents the enrollment of a user in a course.
    Each user can only enroll in a specific course once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.IntegerField(choices=AVAILABLE_COURSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        # each user can enroll in a specific course only once
        unique_together = ('owner', 'course')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner.username} | {self.course}'
