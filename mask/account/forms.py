from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User



class Team_taskForm(forms.ModelForm):
	class Meta:
		model=Team_task
		fields='__all__'
 
class Team_modelForm(forms.ModelForm):
	class Meta:
		model=Team_model
		fields='__all__'



class CreateUserForm(UserCreationForm):

	class Meta:

		model = User

		fields =["username",'email','first_name','last_name','password1','password2']
