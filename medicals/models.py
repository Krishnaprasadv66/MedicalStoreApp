from django.db import models


class login_details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class signup_details(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)   
    Password_confirmation = models.CharField(max_length=50)



class medicine_details(models.Model):
    medicine = models.CharField(max_length=100)
    company_name =  models.CharField(max_length=100)
    expiry_date = models.DateField()
    price = models.FloatField(max_length=10)

