from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # creates a field like is_owner field which is read only 
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    # adding the annotation fields
    articles_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    

    # add a field to tell if the logged in user is the owner of the profile
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            print(following)
            return following.id if following else None
        return None
    
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = ['id','owner','is_owner','following_id','articles_count',
                  'following_count','nickname','about','created_at','updated_at',
                  'image','followers_count']
