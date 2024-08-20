from django.db import models
from django.contrib.auth.models import User
from article.models import Article

# Create your models here.
class Like(models.Model):
    """
    Like model, related to 'owner' and 'article'.
    'owner' is a User instance 
    'article' is a Article instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # 'unique_together' makes sure a user can't like the same article twice.
        unique_together = ['owner', 'article']

    def __str__(self):
        return f'{self.owner} {self.article}'