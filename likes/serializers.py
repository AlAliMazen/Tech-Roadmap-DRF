from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    #article_title = serializers.ReadOnlyField(source='article.title')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner','article']

   