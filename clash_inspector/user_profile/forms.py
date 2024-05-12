from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from search.services import ClashAPI
from user_profile.models import UserProfile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = UserProfile
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    player_tag = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    def clean_player_tag(self):
        player = ClashAPI()
        player_tag = self.data.get('player_tag')

        if not player.player_info(player_tag):
            raise forms.ValidationError(f"Гравця з тегом '{player_tag}' не існує, введіть корректний тег.")

        return True

    class Meta:
        model = UserProfile
        fields = ('username', 'player_tag', 'email', 'password1', 'password2')
