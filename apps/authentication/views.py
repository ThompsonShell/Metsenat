from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SendAuthCodeSerializer, AuthCodeConfirmSerializer, LoginSerializer



class UserLoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        pass
#
# class UserRegisterAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserRegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

class SendAuthCodeAPIView(CreateAPIView):
    """
    API view to handle sending authentication codes to users.

    This view inherits from CreateApiView and is responsible for generating
    and sending authentication codes to users via their registered contact
    methods (e.g.SMS).

    Methods:
        post(request, *args, **kwargs):
            Handles the HTTP POST request to send the authentication code.
            Validates the request data and sends the code to the user.

    Attributes:
        serializer_class (Serializer):
            The serializer class used to validate and deserialize input data.
        permission_classes (tuple):
            The tuple of permission classes that determine access control.
    """
    serializer_class = SendAuthCodeSerializer
    authentication_classes = []


class LoginAPIView(APIView):
    def post(self, request):
        phone_number, auth_code = request.data.get('phone_number'), request.data.get('auth_code')
        if phone_number and auth_code:
            user = authenticate(request=request, phone_number=phone_number, auth_code=auth_code)
            if user is None:
                print(phone_number, auth_code, '>>>>>>>>>>>>>>>>>>>')
                raise ValidationError('invalid phone_number or auth_code')

            token_obj, _ = Token.objects.get_or_create(user_id=user.pk)
        else:
            raise ValidationError('phone_number or password is required')
        return Response({"token": token_obj.key})

class LogoutAPIView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
#
# class CustomRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get_object(self):
#         return self.request.user''



class AuthCodeConfirmAPIView(CreateAPIView):
    """
    API view to handle confirming authentication codes.

    This view inherits from CreateApiView and is responsible for confirming
    authentication codes sent to users via their registered contact methods
    (e.g. SMS).

    Methods:
        post(request, *args, **kwargs):
            Handles the HTTP POST request to confirm the authentication code.
            Validates the request data and confirms the code.

    Attributes:
        serializer_class (Serializer):
            The serializer class used to validate and deserialize input data.
        permission_classes (tuple):
            The tuple of permission classes that determine access control.
    """
    serializer_class = AuthCodeConfirmSerializer
    authentication_classes = []

    def perform_create(self, serializer):
        pass
