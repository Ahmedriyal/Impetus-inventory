from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()
        password = cleaned_data.get('password1')

        # check for min length
        min_length = 8
        if len(password) < min_length:
            messages = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password1', messages)
            print(messages)

        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            messages = 'Password must contain at least 1 number.'
            self.add_error('password1', messages)
            print(messages)

        # check for uppercase letter
        if not any(c.isupper() for c in password):
            messages = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password1', messages)
            print(messages)

        # check for lowercase letter
        if not any(c.islower() for c in password):
            messages = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password1', messages)
            print(messages)

        password_confirm = cleaned_data.get('password2')

        if password and password_confirm:
            if password != password_confirm:
                messages = "The two password fields must match."
                self.add_error('password2', messages)
                print(messages)
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))
