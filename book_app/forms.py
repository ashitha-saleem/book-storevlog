from . models import shop
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['title','author','desc','img','price']