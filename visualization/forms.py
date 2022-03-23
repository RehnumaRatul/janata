from django import forms
from .models import VisualData


class VisualDataFrom(forms.ModelForm):
    class Meta:
        model = VisualData
        fields = '__all__'