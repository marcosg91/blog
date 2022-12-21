from django import forms
from django.forms import TextInput, EmailInput
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class UserLoginForm(AuthenticationForm):
	#def __init__(self, *args, **kwargs):
	#	super(UserLoginForm, self).__init__(*args, **kwargs)

	
	username = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "text",
		"placeholder": "enter username"
	}), label='Username')

	password = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "password",
		"placeholder": "enter password"
	}))


class UserRegistrationForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "text",
		"placeholder": "enter username"
	}), label='Username')

	email = forms.EmailField(widget=forms.EmailInput(attrs={
		"class": "input",
		'type': 'email',
		"placeholder": "Enter email"
	}))

	password1 = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "password",
		"placeholder": "enter password"
	}))

	password2 = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "password",
		"placeholder": "re-enter password"
	}))

	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']