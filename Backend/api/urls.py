from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter()
router.register('materials', views.ApiMaterials, basename='materials')
router.register('unit', views.ApiUnit, basename='unit')
router.register('category', views.ApiCategory, basename='category')

urlpatterns = [
    path("", include(router.urls)),
]
