from django.contrib import admin
from .models import Board
from .models import File_Upload

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
class File_Upload_Admin(admin.ModelAdmin):
    search_fields = ['filename']
    
admin.site.register(Board)
admin.site.register(File_Upload)