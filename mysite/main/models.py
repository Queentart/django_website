from django.db import models
import os
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=255)
    data = models.ImageField(blank=False, null=False, upload_to='media/')
    
    def __str__(self):
        return self.name
    
class File_Upload(models.Model):
    data = models.ImageField(blank=False, null=False, upload_to = 'media/images/')
    filename = models.ForeignKey('Board', related_name = 'post',\
        on_delete = models.PROTECT, null = True, db_column = 'filename')
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def get_filename(self):
        return self.filename