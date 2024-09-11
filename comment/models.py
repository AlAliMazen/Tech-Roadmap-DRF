from django.db import models
from django.contrib.auth.models import User
from article.models import Article

# Create your models here.


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'[{self.id} {self.owner} {self.article.title} {self.content}'
