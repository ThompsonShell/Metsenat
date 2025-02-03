from django.urls import path

from apps.appeals.views import AppealListCreateView,AppealUpdateView, AppealRetrieveView, AppealDeleteView
from apps.sponsors.views import StudentSponsorListCreateView, StudentSponsorRetrieveView, StudentSponsorUpdateView, \
    StudentSponsorDeleteView

urlpatterns = [
    path('', StudentSponsorListCreateView.as_view(), name='student-sponsor-list'),
    path('<int:id>', StudentSponsorRetrieveView.as_view(), name='student-sponsor-retrieve'),
    path('<int:id>update', StudentSponsorUpdateView.as_view(), name='student-sponsor-update'),
    path('<int:id>delete', StudentSponsorDeleteView.as_view(), name='student-sponsor-delete')
]