from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    # Tornar o email obrigatório (necessário pois o model possui um valor padrão)
    email = forms.EmailField(required=True, max_length=150)

    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'email', 'matriculado']

    # Adicionar validação customizada para evitar o email padrão
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == 'sememail@gmail.com':
            raise forms.ValidationError("Por favor, insira um endereço de e-mail válido, não o padrão.")
        return email