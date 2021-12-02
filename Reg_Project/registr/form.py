from django import forms
from .models import Patient


class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('archive', )
