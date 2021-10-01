from django.contrib import admin
from .models import ImageDrop

@admin.register(ImageDrop)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')