from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class NewUserForm(UserCreationForm):

	class Meta:
		model = CustomUser
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user