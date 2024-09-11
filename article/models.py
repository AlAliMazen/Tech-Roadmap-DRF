from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.


class Article(models.Model):
    """
    Used to let logged in user write an article
    in a certain IT-World Segment
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='Category')  # noqa
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_lkftsm', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} {self.title}  {self.owner}"
