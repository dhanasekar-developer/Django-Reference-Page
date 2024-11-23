from django import forms
from . models import Ftp

class FtpForm(forms.ModelForm):
    class Meta:
        model = Ftp
        fields = ['image']