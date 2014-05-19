from django import forms
from .models import taximap

class SubmitForm(forms.ModelForm): #Simple form document
	class Meta:
		model = taximap
