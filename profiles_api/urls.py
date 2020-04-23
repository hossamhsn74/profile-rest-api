from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename="simpleViewSet")
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path("hello-apiview/", views.HelloApiView.as_view(), name="simpleApiView"),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls))
]
