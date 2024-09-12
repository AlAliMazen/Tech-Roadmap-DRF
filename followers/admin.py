from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Follower


# Register your models here.
@admin.register(Follower)
class FollowerAdmin(SummernoteModelAdmin):
    list_display = ('id', 'owner', 'followed')
    search_fields = ['owner', ]
    list_filter = ['owner']
