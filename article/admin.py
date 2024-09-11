from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'owner', 'category',)
    search_fields = ['title', 'owner']
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
