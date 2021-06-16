from django.urls import path, include
from rest_framework.routers import DefaultRouter #automatically generates URLs for our viewset

from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name='recipe' #when we identify the app, reverse function could look up the URLS

urlpatterns = [
    path('', include(router.urls))
]
