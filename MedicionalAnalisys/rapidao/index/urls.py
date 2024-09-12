from django.contrib import admin
from .views import upload_image, render
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render, name="render"),
    path('upload-image/', upload_image, name="upload-image")
]