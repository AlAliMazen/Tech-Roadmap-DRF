from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from course.models import AVAILABLE_COURSES

# Create your models here.


class Rating(models.Model):
    """
    Used to store user reviews of a course.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Direct reference to AVAILABLE_COURSES
    course = models.IntegerField(choices=AVAILABLE_COURSES)  
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        # Ensure a user can only rate a course once
        unique_together = ['owner', 'course'] 
    def __str__(self):
        return f"{self.owner.username} rated {self.get_course_display()} - {self.rating}"