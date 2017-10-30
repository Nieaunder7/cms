from django.contrib.auth.models import User
from django import forms
from member.models import Member

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_conf = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password_conf(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_conf']:
            raise forms.ValidationError("passwords not match")
        return cd['password']