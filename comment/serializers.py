from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethod()
    updated_at = serializers.SerializerMethod()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def ger_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    class Meta:
        model = Comment
        fields = [
            'id','owner','is_owner','profile_id','profile_image',
            'article','created_at','updated_at','content','article_id',
        ]


# using the following class to make comments be related to specific article.
class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Artiicle is a read only field so that we don't have to set it on each update
    """
    article = serializers.ReadOnlyField(source='artcile.id')