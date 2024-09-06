from django.db import models
from django.contrib.auth.models import User
from course.models import Course, AVAILABLE_COURSES

# Create your models here.
class Review(models.Model):
    """
    Used to store user reviews of a course.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,related_name="reviews",on_delete=models.CASCADE)  # Direct reference to AVAILABLE_COURSES
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'course']  # Ensure a user can only review a course once

    def __str__(self):
        return f"{self.owner.username} reviewed {self.get_course_display()} - {self.content[:50]}"