from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Expert


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ('username', 'email', 'password1', 'password2', 'specialization', 'certification')

    def clean_certification(self):
        certification = self.cleaned_data.get('certification')
        if not certification:
            raise forms.ValidationError(('Ten pole jest wymagane.'))
        if not certification.name.endswith('.pdf'):
            raise forms.ValidationError(('Nieprawidłowy format pliku. Certyfikat musi być w formacie PDF.'))

        return certification
