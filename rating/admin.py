from django.contrib import admin
from .models import Rating


# Register your models here.
@admin.register(Rating)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'course', 'rating', )
    search_fields = ['course', ]
    list_filter = ('course', )
