from django import forms
from marketplace.models import Produk, AccountUser
from django.contrib.auth.forms import UserCreationForm

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = AccountUser
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''