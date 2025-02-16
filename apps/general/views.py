from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.general.models import PaymentMethod, University
from apps.general.serializers import UniversitySerializer, PaymentMethodSerializer


class UniversityListCreateView(ListCreateAPIView):
    queryset = University.objects.all().order_by('-created_at')
    serializer_class = UniversitySerializer
    search_fields = ['name', 'contract_amount']
    ordering_fields = ['name', 'contract_amount']
    # filterset_fields = []


class UniversityUpdateView(UpdateAPIView):
    serializer_class = UniversitySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        university_id = self.kwargs['id']
        return University.objects.filter(id=university_id)


class UniversityRetrieveView(RetrieveAPIView):
    serializer_class = UniversitySerializer
    lookup_field = 'id'

    def get_queryset(self):
        university_id = self.kwargs['id']
        return University.objects.filter(id=university_id)


class UniversityDeleteView(DestroyAPIView):
    serializer_class = UniversitySerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def get_queryset(self):
        university_id = self.kwargs['id']
        return University.objects.filter(id=university_id)


class PaymentMethodCreateView(CreateAPIView):
    queryset = PaymentMethod.objects.all().order_by('-name')
    serializer_class = PaymentMethodSerializer


class PaymentMethodRetrieveView(RetrieveAPIView):
    serializer_class = PaymentMethodSerializer
    lookup_field = 'id'

    def get_queryset(self):
        payment_method_id = self.kwargs['id']
        return PaymentMethod.objects.filter(id=payment_method_id)
