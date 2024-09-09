from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from review.models import Review
from course.models import AVAILABLE_COURSES

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    
    course_title = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def get_course_title(self, obj):
        return obj.course.get_title_display()
        
    
    class Meta:
        model = Review
        fields = '__all__'
    
    def create(self, validated_data):
        try:
            # create is a method in the super (parent class of ModeSerializer)
            # that is why we have to use super 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "possible duplicate - You can't write two reviews to the same course. Try to update your first review"
            })



# using the following class to make comments be related to specific article.
class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Comment model used in Detail view
    Artiicle is a read only field so that we don't have to set it on each update
    """
    course = serializers.ReadOnlyField(source='course.id')
