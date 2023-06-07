from django import forms
from .models import Patient, Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'description', 'file','patient']
