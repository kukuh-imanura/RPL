from django import forms

class FormLogin(forms.Form) : 

    kode_petugas = forms.CharField(max_length=10)
    password = forms.PasswordInput()