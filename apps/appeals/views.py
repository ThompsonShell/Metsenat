from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from apps.appeals.models import Appeal
from apps.appeals.serializers import AppealSerializer


class AppealListCreateView(ListCreateAPIView):
    queryset = Appeal.objects.all().order_by('-created_at')
    serializer_class = AppealSerializer
    search_fields = ['phone_number', 'status', 'payment_method', 'amount']
    ordering_fields = ['phone_number', 'status', 'payment_method', 'amount']
    filterset_fields = {
        'sponsor': ['exact'],
        'status': ['exact'],
        'payment_method': ['exact'],
        'amount': ['gte', 'lte'],
        'available': ['gte', 'lte']
    }


class AppealUpdateView(UpdateAPIView):
    serializer_class = AppealSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        appeal_id = self.kwargs['id']
        return Appeal.objects.filter(id=appeal_id)

class AppealRetrieveView(RetrieveAPIView):
    serializer_class = AppealSerializer
    lookup_field = 'id'

    def get_queryset(self):
        appeal_id = self.kwargs['id']
        return Appeal.objects.filter(id=appeal_id)

class AppealDeleteView(DestroyAPIView):
    serializer_class = AppealSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def get_queryset(self):
        appeal_id = self.kwargs['id']
        return Appeal.objects.filter(id=appeal_id)


