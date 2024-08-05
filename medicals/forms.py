from django import forms
from .models import login_details,signup_details,medicine_details



class LoginModelForm(forms.ModelForm):
    class Meta:
        model = login_details
        fields = ['username', 'password']


class signupModelFOrm(forms.ModelForm):
    class Meta:
        model = signup_details
        fields = ['username', 'password','Password_confirmation']


class DateInput(forms.DateInput):
    input_type = 'date'

class medicineForm(forms.ModelForm):
    class Meta:
        model = medicine_details
        fields = ['medicine','company_name','expiry_date','price']


        widgets = {
            'expiry_date' : DateInput()
        }



