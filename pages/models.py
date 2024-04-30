from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)


class DataStored(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    firstName = models.CharField(max_length=100, null=False, blank=False, default="Salma")
    familyName = models.CharField(max_length=100, null=False, blank=False, default="Hany")
    phoneNumber = models.DecimalField(max_digits=11, decimal_places=0, default=0)
    Nationality = models.CharField(max_length=100, null=False, blank=False, default="Egyptian")
    gamil = models.CharField(max_length=150, null=False, blank=False, default="add your gmail")
    password = models.CharField(max_length=150, null=False, blank=False, default="add your password")
    re_password = models.CharField(max_length=150, null=False, blank=False, default="confirm your password")
    sex = models.CharField(max_length=100, null=True, blank=True, choices=SEX_CHOICES)
    birth = models.DateField(default="2002-04-16")


    def __str__(self):
        return self.firstName


class Voter(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    firstName = models.CharField(max_length=100, null=True, blank=True)
    familyName = models.CharField(max_length=100, null=True, blank=True)
    phoneNumber = models.DecimalField(max_digits=11, decimal_places=0, default=0)
    Nationality = models.CharField(max_length=100, null=True, blank=True)
    gamil = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    re_password = models.CharField(max_length=150, null=True, blank=True)
    sex = models.CharField(max_length=100, null=True, blank=True, choices=SEX_CHOICES)
    birth = models.DateField(default="2002-04-16")


    def __str__(self):
        return self.firstName


class N_ID(models.Model):
    nationalID = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    activate = models.BooleanField(default=True)


class Election(models.Model):
    CANDIDATE_CHOICES = [
        ('sisi', 'Sisi'),
        ('hazem', 'Hazem'),
        ('abd el sanad', 'Abd El Sanad'),
        ('mohamed', 'Mohamed'),
    ]
    nationalID = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    candidateName = models.CharField(max_length=100, null=True, blank=True, choices=CANDIDATE_CHOICES)
