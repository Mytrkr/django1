from django import forms


class FormLogin(forms.Form):
	username = forms.CharField(max_length = 75, label = 'Kullanıcı Adı')
	password = forms.CharField(widget = forms.PasswordInput, max_length = 75, label = 'Şifre')