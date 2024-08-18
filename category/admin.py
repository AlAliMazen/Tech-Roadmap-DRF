from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Category


# Register your models here.
@admin.register(Category)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id','title','owner','created_at')
    search_fields = ['title']
    list_filter = ['title','owner']
    summernote_fields = ('description',)