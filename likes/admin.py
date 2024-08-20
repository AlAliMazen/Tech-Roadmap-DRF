from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Likes

# Register your models here.
@admin.register(Likes)
class LikesAdmin(SummernoteModelAdmin):
    list_display = ('id', 'owner', 'article')
    search_fields = ['owner', 'article']
    list_filter = ['owner', 'article']