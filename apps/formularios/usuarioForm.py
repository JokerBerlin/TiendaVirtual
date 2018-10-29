from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email',  'password1', 'password2')

    email = forms.EmailField(required=True, label = 'Correo Electrónico', widget=forms.TextInput(attrs={'placeholder': 'Correo Electrónico',}))
    first_name = forms.CharField(required=True, label = 'Nombres', widget=forms.TextInput(attrs={'placeholder': 'Nombre',}))
    last_name = forms.CharField(required=True, label = 'Apellidos', widget=forms.TextInput(attrs={'placeholder': 'Apellidos',}))
    username = forms.CharField(required=True,  label = 'Nombre de usuario', widget=forms.TextInput(attrs={'placeholder': 'Usuario',}))
    password1 = forms.CharField(required=True,  widget=forms.TextInput())
    password2 = forms.CharField(required=True,  widget=forms.TextInput())




# #clean email field
# def clean_email(self):
#     email = self.cleaned_data["email"]
#     try:
#         User._default_manager.get(email=email)
#     except User.DoesNotExist:
#         return email
#     raise forms.ValidationError('email duplicado')
#
# #modificamos el método save() así podemos definir  user.is_active a False la primera vez que se registra
# def save(self, commit=True):
#     user = super(RegistrationForm, self).save(commit=False)
#     user.email = self.cleaned_data['email']
#     if commit:
#         user.is_active = False # No está activo hasta que active el vínculo de verificación
#         user.save()
#
#     return user
