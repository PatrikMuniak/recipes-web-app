from django import forms
from .models import FoodsModel

class FoodsForm(forms.Form):
    q = forms.CharField(label='', max_length=50)
