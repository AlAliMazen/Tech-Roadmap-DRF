from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('id','owner','article','content')
    search_fields = ['article','owner']
    list_filter = ['article','owner']
    summernote_fields = ('content',)