from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    # creates a field like is_owner field which is read only 
    is_owner = serializers.SerializerMethodField()
    # add a field to tell if the logged in user is the owner of the profile
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    class Meta:
        model = Profile
        fields = [
            'id','owner', 'nickname','about','created_at','updated_at','image','is_owner',
        ]
