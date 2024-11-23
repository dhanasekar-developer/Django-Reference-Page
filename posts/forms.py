from django import forms
from . models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','slug','banner','color']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'banner': forms.ImageField()
        }
