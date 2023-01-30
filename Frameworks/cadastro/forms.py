from django import forms
from cadastro.models import Framework
class frameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = '__all__'
        widgets = {
            'date_of_creation': forms.DateInput(attrs={'type': 'date'})
        }