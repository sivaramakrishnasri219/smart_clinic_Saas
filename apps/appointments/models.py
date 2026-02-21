from django.db import models

class Appointment(models.Model):
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE)
    doctor = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
