from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    balance = forms.DecimalField(label='Balance', max_digits=10, decimal_places=2)
    age = forms.IntegerField(label='Age')
