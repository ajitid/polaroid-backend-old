from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

from post.views import UserPostListView

app_name = "users"

# router = DefaultRouter()
# router.register()
# router.register("<username:str>/followers", views.followers)
# router.register("m/<str:username>", views.UserViewSet)


urlpatterns = [
    path("", views.UserCreateView.as_view(), name="user-create"),
    path("<str:username>", views.UserView.as_view(), name="user-detail"),
    path("<str:username>/profile", views.ProfileView.as_view(), name="user-profile"),
    path("<str:username>/followers", views.FollowersListView.as_view()),
    path("<str:username>/following", views.FollowingListView.as_view()),
    path("<str:username>/follow", views.Follow.as_view()),
    path("<str:username>/posts", UserPostListView.as_view()),
]
