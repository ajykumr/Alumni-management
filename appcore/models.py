from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StaffAccount(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
#

class Alumni(models.Model):
    BRANCH = (
                ('CS', 'CS&E'),
                ('CV', 'CIVIL'),
                ('EC', 'E&C'),
                ('ME', 'MECH'),
                )
    GENDER = (
                ('Male', 'Male'),
                ('Female', 'Female'),
                ('Others', 'others'),
                )

    YEAR = (
                ('2012', '2012'),
                ('2013', '2013'),
                ('2014', '2014'),
                ('2015', '2015'),
                ('2016', '2016'),
                ('2017', '2017'),
                ('2018', '2018'),
                ('2019', '2019'),
                ('2020', '2020'),
                ('2021', '2021'),
                ('2022', '2022'),
                )
    STATUS = (
                ('Pending', 'Pending'),
                ('Accepted', 'Accepted'),
                ('Rejected', 'Rejected'),
                )
    usn = models.CharField(primary_key = True, max_length=10)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    staff = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    branch = models.CharField(max_length=20, null=True, choices=BRANCH)
    gender = models.CharField(max_length=20, null=True, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status =  models.CharField(default="Pending", max_length=20, null=True, choices=STATUS)
    pass_year =  models.CharField(max_length=4, null=True, choices=YEAR)

    def __str__(self):
        return self.usn

    def get_authors(self):
        return ', '.join(self.employers.all().values_list('Employer_name', flat=True))


class Employer(models.Model):
    alumni = models.ForeignKey(
            Alumni,
            related_name='employers', on_delete=models.SET_NULL, null=True)
    Employer_name = models.CharField(max_length=100, null=True)
    Employer_Designation = models.CharField(max_length=100, null=True)
    Employer_join_year = models.CharField(max_length=4, null=True)


    def __str__(self):
        return self.Employer_name
