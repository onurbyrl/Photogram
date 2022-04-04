from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    # name = forms.CharField(max_length=24, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    username = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(required=True, help_text='(Enter valid email adress)', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password again', 'style': 'width: 300px;', 'class': 'form-control'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password again', 'style': 'width: 300px;', 'class': 'form-control'}))

    field_order = ['name', 'username', 'email', 'password', 'confirm_password']

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password_value = self.cleaned_data['password']
        confirm_password_value = self.cleaned_data['confirm_password']

        if password_value != confirm_password_value:
            raise forms.ValidationError('Passwords does not match')