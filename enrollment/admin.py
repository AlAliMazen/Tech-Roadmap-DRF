from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Enrollment


# Register your models here.
@admin.register(Enrollment)
class EnrollmentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'owner', 'course', 'created_at', )
    search_fields = ['owner', 'course']
    list_filter = ('course', )
