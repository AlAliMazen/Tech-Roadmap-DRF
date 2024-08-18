from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Category
        fields = [
            'id','owner','title','description','is_owner','created_at','updated_at'
        ]