from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "posts"

# router = DefaultRouter()
# router.register()
# router.register("<username:str>/followers", views.followers)
# router.register("m/<str:username>", views.UserViewSet)


urlpatterns = [
    # path("", include(router.urls)),
    path("", views.PostCreateView.as_view()),
    path("<str:id>", views.PostDetailView.as_view()),
    # path("<str:username>/followers", views.FollowersListView.as_view()),
    # path("<str:username>/following", views.FollowingListView.as_view()),
]
