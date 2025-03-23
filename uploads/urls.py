from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('uploads/', views.uploaded_files, name='uploaded_files'),
    path('test/', views.test_view, name='test_view'),
]
