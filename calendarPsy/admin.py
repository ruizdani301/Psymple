from django.contrib import admin
from calendarPsy.models import Professional, Patient, Date

class DateAdmin(admin.ModelAdmin):
    list_display=("professional", "patient", "availability")
    list_filter=("professional","patient")

class ProfessionalDateInline(admin.TabularInline):
    model = Date

class PatientDateInline(admin.TabularInline):
    model = Date
    
class ProfessionalAdmin(admin.ModelAdmin):
    list_display=("name", "profession")
    inlines = (ProfessionalDateInline,)

class PatientAdmin(admin.ModelAdmin):
    list_display=("name", "gender")
    inlines = (PatientDateInline,)

admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Date, DateAdmin)
