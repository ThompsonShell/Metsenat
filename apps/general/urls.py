from django.urls import path

from apps.appeals.views import AppealListCreateView,AppealUpdateView, AppealRetrieveView, AppealDeleteView
from apps.general.views import UniversityListCreateView, UniversityUpdateView, UniversityRetrieveView, \
    UniversityDeleteView, PaymentMethodCreateView, PaymentMethodRetrieveView

urlpatterns = [
    path('', UniversityListCreateView.as_view(), name='university-list'),
    path('<int:id>', UniversityUpdateView.as_view(), name='university-retrieve'),
    path('<int:id>update', UniversityRetrieveView.as_view(), name='university-update'),
    path('<int:id>delete', UniversityDeleteView.as_view(), name='university-delete'),
    path('payment-method', PaymentMethodCreateView.as_view(), name='payment-method-list'),
    path('payment-method<int:id>', PaymentMethodRetrieveView.as_view(), name='payment-method-retrieve'),

]