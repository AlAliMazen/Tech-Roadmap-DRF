from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """
    Category of the article which the user will wrote.
    """

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.id}  | {self.owner} {self.title}"
    