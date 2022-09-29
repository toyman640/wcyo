from django.contrib import admin
from .models import Post, UserProfile
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)