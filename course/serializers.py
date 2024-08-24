from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    category_title = serializers.ReadOnlyField(source='category.title' )
    course_title = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    # common convension is to call validate_[name_of_field]
    def validate_image(self, value):
        if value.size > 1024*1024*2:
            raise serializers.ValidationError (
                "Image size is larger than 2MB"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width is larger than 4096 inches !"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height is larger than 4096 inches !"
            )
        return value
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_course_title(self, obj):
       return obj.get_title_display()
    
    class Meta:
        model = Course
        
        fields = ['id','owner','profile_id','profile_image','category_title',
                  'title','about','created_at','updated_at','duration',
                  'thumbnailImage','category','course_title','is_owner']
    
    
    
    def create(self, validated_data):
        try:
            # create is a method in the super (parent class of ModeSerializer)
            # that is why we have to use super 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "possible duplicate - You can't a user twice"
            })
    
    