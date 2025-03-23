from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth.decorators import login_required

# Upload file view
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user  # Set the user who uploaded the file
            uploaded_file.save()
            return redirect('uploaded_files')
    else:
        form = UploadFileForm()

    return render(request, 'uploads/upload.html', {'form': form})

# Display uploaded files view
@login_required
def uploaded_files(request):
    files = UploadedFile.objects.filter(user=request.user)  # Only show files uploaded by the current user
    print("my modification 1 for git versioning")
    return render(request, 'uploads/uploads.html', {'files': files})

# uploads/views.py
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test View is working!")







