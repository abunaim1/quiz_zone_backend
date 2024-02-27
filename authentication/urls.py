from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('participant', views.ParticipantViewSet)
router.register('image', views.UserImageViewSet)
router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('activate/<uid64>/<token>/', views.activate, name='activate'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('logout/', views.LogoutApiView.as_view()),
]
