from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# Import class Register dari file myfirstapp/model.py
from .models import Register


# Membuat class RegisterForm untuk membuat form registrasi
class RegisterForm(ModelForm):
    class Meta:
        # Merealisasikan form dengan model
        model = Register
        # Mengatur field apa saja yang akan ditampilkan pada form
        fields = ('name', 'email', 'number', 'city')
        # Mengatur teks label untuk setiap field
        labels = {
            'name': _("Nama Lengkap"),
            'email': _("Email"),
            'number': _("No Telp"),
            'city': _("Kota")
        }
        # Mengatur pesan error pada saat validasi field
        error_messages = {
            'name': {
                'required': _("Nama harus diisi."),
            },
            'email': {
                'required': _("Email harus diisi."),
            }
        }
