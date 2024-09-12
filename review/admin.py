from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('id', 'owner', 'course', )
    search_fields = ['course', 'owner']
    list_filter = ('owner',)
    summernote_fields = ('content',)
