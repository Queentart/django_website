from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

#from .models import Board, File_Upload

# Create your views here.

def main(request):
    #data = Board.objects.all()
    return render(request, 'main.html') #{'data':data}

def result(request):
    return render(request, 'result.html')
        
def FileuploadView(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fs = FileSystemStorage(location='media/images', base_url='media/images')
        filename = fs.save(upload.name, upload)
        uploaded_file_url = fs.url(filename)
        return render(request, 'templates/pages/result.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'templates/pages/result.html')

def post(request):
    return render(request, 'post.html')

def fileupload(request):
    if request.method == 'POST':
        data = request.POST['data']
        filename = request.FILES['filename']
        upload_date = request.POST['upload_date']
        fileUpload = File_Upload(
            data = data,
            filename = filename,
            upload_date = upload_date,
        )
        
        fileUpload.save()
        return redirect('fileUpload')
    
    else:
        Fileuploader = Fileuploader
        filename = {'Fileuploader':Fileuploader,}
        return render(request, 'post.html', filename)