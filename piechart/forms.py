from django import forms

from . models import Chart

class ProductForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_product': forms.TextInput(attrs={'class': 'form-control'})
        }