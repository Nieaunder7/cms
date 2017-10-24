from django import forms
from .models import Settopbox,AccessPoint,RemoteController,BaseDevice


class SettopboxCreateForm(forms.ModelForm):
    
    class Meta:
        model = Settopbox
        fields=['name', 'model','manufacturer','service','firmware','comment','mac_address']
    

class AccessPointCreateForm(forms.ModelForm):
    
    class Meta:
        model = AccessPoint
        fields=['name', 'model','manufacturer','service','firmware','comment','mac_address']


class RemoteControllerCreateForm(forms.ModelForm):
    
    class Meta:
        model = RemoteController
        fields=['name', 'model','manufacturer','service','firmware','comment']



