from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("<user:pk>/followers", views.Followers)
router.register("<user:pk>/following", views.Following)


urlpatterns = [path("", include(router.urls))]
