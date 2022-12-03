from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput
from .models import HumanResource, Candidate, JobPost


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


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100'}),
            'email': forms.EmailInput(attrs={'class': 'input100'}),
            'first_name': forms.TextInput(attrs={'class': 'input100'}),
            'last_name': forms.TextInput(attrs={'class': 'input100'}),
        }


class HRProfile(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = ['company_name', 'company_logo', 'profile_pic']

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'input100'}),
        }


class CandidateProfile(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['phone', 'address', 'profile_pic']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input100'}),
            'address': forms.TextInput(attrs={'class': 'input100'}),
        }


class CreateJobPost(forms.ModelForm):
    class Meta:
        model = JobPost

        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input100'}),
            # 'description': forms.TextInput(attrs={'class': 'input100'}),
        }
