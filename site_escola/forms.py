from django import forms
from .models import RespostaQuiz

class RespostaQuizForm(forms.ModelForm):
    """
    Formulário para coletar as respostas do quiz, gerado a partir do modelo.
    Isso garante validação automática e segurança dos dados.
    """
    class Meta:
        model = RespostaQuiz
        # Inclui todos os campos que o usuário preenche no formulário.
        # O campo 'data_envio' é preenchido automaticamente.
        fields = ['nome', 'email', 'idade', 'sexo', 'q1', 'q2', 'q3', 'q4', 'q5']
        # Adiciona widgets para customizar a aparência dos campos no HTML.
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}),
            'idade': forms.NumberInput(attrs={'placeholder': 'Digite sua idade'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona um 'empty_label' para o campo de seleção, que serve como placeholder.
        self.fields['sexo'].empty_label = "Selecione"