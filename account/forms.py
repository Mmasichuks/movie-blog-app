from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# john bull
class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data['full_name']
        first_name, last_name = full_name.split(' ', 1) # amara chidi
        user.first_name = first_name
        user.last_name = last_name
        if commit:
            user.save()
        return user

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'placeholder': 'Enter Full name', 'class': 'form-control'}
        )
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Enter Username', 'class': 'form-control'}
        )
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Enter Email', 'class': 'form-control'}
        )
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Enter Password', 'class': 'form-control'}
        )
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Password', 'class': 'form-control'}
        )