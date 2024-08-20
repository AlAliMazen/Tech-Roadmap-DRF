from django.db import models
from django.contrib.auth.models import User
from article.models import Article
# Create your models here.


class Likes(models.Model):
    """
    Used to reflect the Likes on an article by authenicated logged in User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_at']
        # unique together is to make sure that a user can't like the same article twice
        unique_together = ['owner', 'article']
    
    def __str__(self):
        return f"{self.owner}  {self.article}"
