
from django import forms
from datetime import date

# Definición de formularios:

class FormContacto(forms.Form):
    paises = [(1, 'España'), (2, 'Italia'), (3, 'Francia')]

    nombre = forms.CharField(max_length=25)
    usuario = forms.CharField(min_length=10)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'El password obligatorio'})
    email = forms.CharField(widget=forms.EmailInput(), required=False)
    edad = forms.IntegerField(min_value=18, max_value=99)
    # Mostrará la fecha inicializada al día de hoy
    fecha = forms.DateField(initial=date.today())
    publicidad = forms.BooleanField(required=False, label="Recibir publicidad")
    pais = forms.ChoiceField(choices=paises, required=False)
    observaciones = forms.CharField(max_length=200, widget=forms.Textarea)

    def clean_observaciones(self):
        # Extraer el contenido del campo observaciones
        aux = self.cleaned_data['observaciones']

        numPalabras = len(aux.split(" "))
        if numPalabras < 4:
            raise forms.ValidationError('Como mínimo 4 palabras', code='invalid')
        
        return aux