from django.urls import path

from apps.appeals.views import AppealListCreateView,AppealUpdateView, AppealRetrieveView, AppealDeleteView

urlpatterns = [
    path('', AppealListCreateView.as_view(), name='appeals-list'),
    path('<int:id>', AppealRetrieveView.as_view(), name='appeals-retrieve'),
    path('<int:id>update', AppealUpdateView.as_view(), name='appeals-update'),
    path('<int:id>delete', AppealDeleteView.as_view(), name='appeals-delete')
]