from django.urls import path
from .views import UserRetrieveView, UserUpdateView

urlpatterns = [
    path("users/<int:user_id>/", UserRetrieveView.as_view(), name="user-detail"),
    path("users/<int:user_id>/update/", UserUpdateView.as_view(), name="user-update"),
]
