from django import forms
from Tracker.models import User_Model,Job_detail
from django.contrib.auth.models import User

class User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class Job_Form(forms.ModelForm):
    class Meta:
        model=Job_detail
        fields=['company_name','job_title','location','application_date','status','salary','desgination']