from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 

from calendarPsy.models import Patient, Professional, Date
from calendarPsy.serializers import ProfessionalSerializer, PatientSerializer, DateSerializer

class ProfessionalModelViewSet(ModelViewSet):
    serializer_class = ProfessionalSerializer
    queryset = Professional.objects.all() 
   

class PatientModelViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DateModelViewSet(ModelViewSet):
    serializer_class = DateSerializer
    queryset = Date.objects.all()

class ProfessionalPkModelViewSet(ModelViewSet):
    serializer_class = ProfessionalSerializer
    queryset = Professional.objects.all()

class PatientPkModelViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DatePkModelViewSet(ModelViewSet):
    serializer_class = DateSerializer
    queryset = Date.objects.all()
