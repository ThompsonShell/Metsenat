from django.urls import path

from apps.users.views import UserListAPIView

urlpatterns = [
    path('user-list', UserListAPIView.as_view(), name='user-list')
]