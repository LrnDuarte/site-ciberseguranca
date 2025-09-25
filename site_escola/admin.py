from django.contrib import admin
from .models import RespostaQuiz

@admin.register(RespostaQuiz)
class RespostaQuizAdmin(admin.ModelAdmin):
    """
    Configura a exibição do modelo RespostaQuiz na interface de administração.
    """
    # Campos que serão exibidos na lista de respostas
    list_display = ('nome', 'email', 'data_envio', 'idade', 'sexo')
    
    # Adiciona um filtro lateral para facilitar a busca por data ou sexo
    list_filter = ('data_envio', 'sexo')
    
    # Adiciona um campo de busca para procurar por nome ou email
    search_fields = ('nome', 'email')