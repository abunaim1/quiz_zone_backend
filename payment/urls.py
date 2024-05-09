from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include


router = DefaultRouter()
router.register('pay', views.CheckViewset)

urlpatterns = [
    path('', include(router.urls)),
]