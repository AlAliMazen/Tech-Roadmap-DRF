from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course


# Register your models here.
@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'owner', 'category',)
    search_fields = ['title', 'owner']
    list_filter = ('title',)
    summernote_fields = ('about',)
