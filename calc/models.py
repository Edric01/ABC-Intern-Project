from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()

class KYCdetails(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    add_line1=models.TextField()
    add_line2=models.TextField()
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    mobile=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    idtype=models.CharField(max_length=50)
    idnum=models.CharField(max_length=20,primary_key=True,unique=True)
    issue_date=models.CharField(max_length=50)
    expiry_date=models.CharField(max_length=50)
    verify=models.BooleanField(default=False)
    abcno=models.CharField(max_length=12,default="ABC202100000")

class abcacc(models.Model):
    abcno=models.CharField(max_length=12,primary_key=True,unique=True)
    acctype=models.CharField(max_length=10)
    balance=models.IntegerField()
    begindate=models.TextField()
    duration=models.IntegerField(default=1825)
    enddate=models.TextField(default="")
    rate=models.FloatField(default=4.5)
    
class RateofInterest(models.Model):
    typeofacc=models.TextField()
    duration=models.IntegerField()
    rate=models.FloatField()
