from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from apps.sponsors.serializers import StudentSponsor, SponsorSerializer


class StudentSponsorListCreateView(ListCreateAPIView):
    queryset = StudentSponsor.objects.all().order_by('-created_at')
    serializer_class = SponsorSerializer
    search_fields = ['sponsor','student','amount']
    ordering_fields = ['sponsor','student','amount']
    filterset_fields = {
        'sponsor': ['exact'],
        'student': ['exact'],
        'amount': ['gte', 'lte'],
    }


class StudentSponsorUpdateView(UpdateAPIView):
    serializer_class = SponsorSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        student_sponsor_id = self.kwargs['id']
        return StudentSponsor.objects.filter(id=student_sponsor_id)

class StudentSponsorRetrieveView(RetrieveAPIView):
    serializer_class = SponsorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        student_sponsor_id = self.kwargs['id']
        return StudentSponsor.objects.filter(id=student_sponsor_id)

class StudentSponsorDeleteView(DestroyAPIView):
    serializer_class = SponsorSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def get_queryset(self):
        student_sponsor_id = self.kwargs['id']
        return StudentSponsor.objects.filter(id=student_sponsor_id)
