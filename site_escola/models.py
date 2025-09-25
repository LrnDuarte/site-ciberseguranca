from django.db import models

class RespostaQuiz(models.Model):
    # Adicionando as opções para o campo 'sexo' para garantir a consistência dos dados.
    SEXO_CHOICES = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outro', 'Outro'),
        ('Prefiro não informar', 'Prefiro não informar'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES)
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    q5 = models.CharField(max_length=1)
    data_envio = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Respostas de {self.nome} em {self.data_envio.strftime('%d/%m/%Y')}"
