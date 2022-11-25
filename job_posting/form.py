from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100'}),
            'email': forms.EmailInput(attrs={'class': 'input100'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget = PasswordInput(attrs={'class': 'input100'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'input100'})


#class UserLoginForm()


