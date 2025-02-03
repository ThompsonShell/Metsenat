from django.urls import path

from apps.users.views import UserListAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list')
]