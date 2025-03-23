from django.contrib import admin
from .models import UploadedFile  # Use UploadedFile instead of FileUpload

admin.site.register(UploadedFile)
