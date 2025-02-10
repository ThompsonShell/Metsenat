from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.serializers import UserRegisterSerializer


class UserRegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        username, password = request.data.get('username'), request.data.get('password')
        if username and password:
            user = authenticate(request=request, username=username, password=password)
            if user is None:
                print(username, password, '>>>>>>>>>>>>>>>>>>>')
                raise ValidationError('invalid username or password')

            token_obj, _ = Token.objects.get_or_create(user_id=user.pk)
        else:
            raise ValidationError('Username or password is required')
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
#         return self.request.user