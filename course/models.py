from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
AVAILABLE_COURSES = ( (0, "Introduction to Information Technology"),
                      (1, "Networking Fundamentals"),
                      (2, "Software Development"),
                      (3, "Cybersecurity"),
                      (4, "Database Management"),
                      (5, "Cloud Computing"),
                      (6, "Web Development"),
                      (7, "Data Science and Analytics"),
                      (8, "Project Management in IT"),
                      (9, "Ethical Hacking and Penetration Testing"),
                    )

# Create your models here.
class Course(models.Model):
    """
    Used to see what course the user will choose to 
    walk through
    """
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='Segment')
    title = models.IntegerField(choices=AVAILABLE_COURSES, default=0) 
    about = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    duration = models.TextField(blank=False)
    thumbnailImage = models.ImageField(
        upload_to='images/', default='../default_post_lkftsm', blank=True
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.id} {self.title}  {self.participant}  {self.category}"
