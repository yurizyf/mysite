from cProfile import label
from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "新用户名", 'autofocus': ''}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "新密码"}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "确认密码"}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': "邮箱地址"}))
    phone = forms.CharField(label="电话",  max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "电话"}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')


