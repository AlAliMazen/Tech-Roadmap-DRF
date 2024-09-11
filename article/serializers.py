from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from article.models import Article
from likes.models import Like


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    category_title = serializers.ReadOnlyField(source='category.title')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    # write a fucntion to validate the image size, width and height
    # common convension is to call validate_[name_of_field]
    def validate_image(self, value):
        if value.size > 1024*1024*2:
            raise serializers.ValidationError(
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

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, article=obj).first()

            print(like)
            return like.id if like else None
        return None

    class Meta:
        model = Article
        fields = '__all__'
