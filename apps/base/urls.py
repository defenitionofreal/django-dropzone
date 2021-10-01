from django.urls import path

from . import views
from .api import (user_view,
                  image_view)

from rest_framework import routers

app_name = 'base'

router = routers.DefaultRouter()

router.register(r'api/v1/user', user_view.UserViewSet, basename='user')
router.register(r'api/v1/image', image_view.ImageViewSet, basename='image')

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.file_upload),
]

urlpatterns += router.urls