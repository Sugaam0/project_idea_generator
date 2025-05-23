from django import forms
from .models import ProjectIdea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = ProjectIdea
        fields = ['field', 'type', 'genre', 'additional_info']
        widgets = {
            'field': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'type': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'genre': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }