from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디 입력',
                'style': 'width: 350px',
            })
    )

    password = forms.CharField(
        label='비밀번호',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 입력',
                'style': 'width: 350px',
            })
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디 입력',
                'style': 'width: 350px',
            })
    )

    password1 = forms.CharField(
        label='비밀번호',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 입력',
                'style': 'width: 350px',
            })
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 재입력',
                'style': 'width: 350px',
            })
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)
