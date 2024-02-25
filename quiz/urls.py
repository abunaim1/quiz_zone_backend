from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('category', views.QuizCategoryViewSet)
router.register('list', views.QuizViewSet)

urlpatterns = [
    path('', include(router.urls))
]
