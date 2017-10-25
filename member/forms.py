from django import forms
from .models import Member

class MemberCreateForm(forms.ModelForm):
    #password = forms.CharField(label="Password", widget=forms.PasswordInput)
    #password2 = forms.CharField(label="RepeatPassword",widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields =['name','department','email_address','phone_number']

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('비밀번호가 올바르지 않습니다.')
    #     return cd['password']

        
