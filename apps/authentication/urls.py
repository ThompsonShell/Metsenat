from rest_framework_simplejwt.views import TokenObtainPairView
from .views import LoginAPIView, LogoutAPIView, SendAuthCodeAPIView, UserLoginAPIView
from django.urls import path


urlpatterns = [
    # path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/', LoginAPIView.as_view(), name='login'),
        path('send-verification-code/', SendAuthCodeAPIView.as_view(), name='logout'),
    # path('profile/', CustomRetrieveUpdateAPIView.as_view(), name='profile'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('userlogin/', UserLoginAPIView.as_view(), name='user-login'),
]