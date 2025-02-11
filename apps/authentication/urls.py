from .views import LoginAPIView, LogoutAPIView, SendAuthCodeAPIView
from django.urls import path


urlpatterns = [
    # path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
        path('send-verification-code/', SendAuthCodeAPIView.as_view(), name='logout'),
    # path('profile/', CustomRetrieveUpdateAPIView.as_view(), name='profile'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]