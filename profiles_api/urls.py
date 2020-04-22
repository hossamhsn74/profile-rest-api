from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename="simpleViewSet")

urlpatterns = [
    path("hello-apiview/", views.HelloApiView.as_view(), name="simpleApiView"),
    path("", include(router.urls))
]
