from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from course.models import Course, AVAILABLE_COURSES


# Create your models here.
class Rating(models.Model):
    """
    Used to store user reviews of a course.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')  # noqa
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])  # noqa
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        # Ensure a user can only rate a course once
        unique_together = ['owner', 'course']

    def __str__(self):
        return f"{self.owner.username} rated {self.course.get_title_display()} - {self.rating}"  # noqa
