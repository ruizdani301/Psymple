from django.urls import path
from calendarPsy import views

urlpatterns = [
    path('professional', views.ProfessionalModelViewSet.as_view({'get': 'list', 'post':'create'}), name='professional'),
    path('patient', views.PatientModelViewSet.as_view({'get': 'list', 'post':'create'}), name='patient'),
    path('date', views.DateModelViewSet.as_view({'get':'list', 'post':'create'}), name='date'),
    path('professional/<pk>', views.ProfessionalPkModelViewSet.as_view({'get': 'retrieve', 'delete':'destroy'}), name='professionalpk'),
    path('patient/<pk>', views.PatientPkModelViewSet.as_view({'get': 'retrieve', 'delete':'destroy'}), name='professionalpk'),
    path('date/<pk>', views.DatePkModelViewSet.as_view({'get': 'retrieve', 'delete':'destroy'}), name='professionalpk'),
]