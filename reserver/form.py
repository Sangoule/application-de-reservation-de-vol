from django import forms
from reserver.models import Compagnie
from django.contrib.auth.models import User
class CompagnieForm(forms.ModelForm):
    class Meta:
        model = Compagnie
        fields = ['nom','logo']
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']