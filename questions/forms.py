from django import forms
from questions.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditProfileForm(UserChangeForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        for fieldname in ['password']:
            self.fields[fieldname].help_text = ''

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password'
        )
