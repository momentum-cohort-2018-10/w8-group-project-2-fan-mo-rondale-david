from django import forms
from questions.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
