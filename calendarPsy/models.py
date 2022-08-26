from django.db import models


class Professional(models.Model):
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Patient(models.Model):
    GENDER = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
        ('O', 'Otro'),
    )
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER)

    def __str__(self):
        return self.name

class Date(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)
    availability = models.DateTimeField()
    
    def __str__(self):
        return "{} {}".format(self.professional, self.availability)



