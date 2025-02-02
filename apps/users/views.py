from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from apps.users.models import UserModel
from apps.users.serializers import UserListSerializer

class UserListAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = UserModel.objects.all().order_by('-pk')
    serializer_class = UserListSerializer

    search_fields = ['phone_number']
    ordering_fields = ['phone_number']
    # filterset_fields = ['is_active']
    filterset_fields = [
        'is_active'
    ]