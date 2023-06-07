from django.urls import path
from .views import upload, upload_success

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('success/', upload_success, name='success'),

]
