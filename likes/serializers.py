from django.db import IntegrityError
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

    # handling the duplication of like to the same article
    def create(self, validated_data):
        try:
            # the method create is part of ModelSerializer
            # that's why we need to call it using super
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                "details":'possible duplicate'
            })
            
