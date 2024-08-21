from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    title = serializers.ReadOnlyField(source='article.title')

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        try:
            # create is a method in the super (parent class of ModeSerializer)
            # that is why we have to use super 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "possible duplicate - You can't like an article twice"
            })