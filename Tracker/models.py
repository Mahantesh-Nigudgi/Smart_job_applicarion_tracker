from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_Model(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


class Job_detail(models.Model):
    company_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    application_date=models.DateField()
    status=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=10,decimal_places=1)
    desgination=models.CharField(max_length=100)
    user=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)