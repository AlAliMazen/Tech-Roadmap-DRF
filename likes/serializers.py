from rest_framework import serializers
from .models import Likes


class LikesSerializer(serializers.ModelSerializer):
    """
    
    """
    owner = serializers.ReadOnlyField(source='owner.username')
 
    # Note: We don't need a get_is_owner method here 
    # because we don't need to know if the currently
    # logged in user is the owner of a like.
    
    class Meta:
        model = Likes
        fields = ['id','owner','article','created_at']
