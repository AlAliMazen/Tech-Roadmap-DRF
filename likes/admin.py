from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Like

# Register your models here.
@admin.register(Like)
class LikesAdmin(SummernoteModelAdmin):
    list_display = ('id','owner','article')
    search_fields = ['article','owner',]
    list_filter = ['article','owner']