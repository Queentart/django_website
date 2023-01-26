from django import forms
from .models import File_Upload

class FileUploadForm(forms.ModelForm):
        class Meta:
            model = File_Upload
            fields = ['data', 'filename', 'upload_date']
            labels = {
                'data' : '첨부파일',
                'filename' : '파일명',
                'upload_date' : '업로드 날짜',
            }
            
class Fileuploader(ModelForm):
    class Meta:
        model = File_Upload
        fields = ['data', 'filename', 'upload_date']