from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('locations/', views.locations, name='locations'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)