from django import forms


class FormUsuario(forms.Form):
    login = forms.CharField()
    # password = forms.PasswordField()
    email = forms.EmailField(required=False)
