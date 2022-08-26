from dataclasses import fields
from rest_framework import serializers
from calendarPsy.models import Professional, Patient, Date

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DateSerializer(serializers. ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'
