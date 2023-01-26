from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from main.views import post

urlpatterns = [
    path('', views.main, name = 'main'),
    path('result/', views.result, name = 'result'),
    path('post/', post, name='post')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)