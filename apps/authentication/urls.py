from .views import LoginAPIView, LogoutAPIView, UserRegisterAPIView
from django.urls import path


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    # path('profile/', CustomRetrieveUpdateAPIView.as_view(), name='profile'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]