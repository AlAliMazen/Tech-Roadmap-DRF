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
    course_title = course_title = serializers.SerializerMethodField()

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
        model = Enrollment
        fields = '__all__'
    
