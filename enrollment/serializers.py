from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from .models import Enrollment
from course.models import AVAILABLE_COURSES

class EnrollmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    course_title = serializers.SerializerMethodField()
    
    #course = serializers.ChoiceField(choices=AVAILABLE_COURSES)
    
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
        model = Enrollment
        fields = '__all__'
    
    def create(self, validated_data):
        try:
            # create is a method in the super (parent class of ModeSerializer)
            # that is why we have to use super 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "possible duplicate - You can't enroll in the same course twice"
            })
