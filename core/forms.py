from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pdf
from django.contrib.auth.models import User

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('დასახელება', 'pdf',)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1', 'password2']