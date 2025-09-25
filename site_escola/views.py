from django.shortcuts import render
from .models import RespostaQuiz
from .forms import RespostaQuizForm  # Importar o formulário

def index(request):
    """
    Renderiza a página inicial do site.
    """
    return render(request, 'index.html')

def boas_praticas_view(request):
    """
    Renderiza a página de boas práticas.
    """
    return render(request, 'boaspraticas.html')

def o_que_e_view(request):
    return render(request, 'oque.html')

def phishing_view(request):
    return render(request, 'phishing.html')

def malware_view(request):
    return render(request, 'malware.html')

def redes_sociais_view(request):
    return render(request, 'sociais.html')

def ajuda_view(request):
    return render(request, 'autoridades.html')


def quiz_view(request):
    """
    Processa o formulário do quiz usando Django Forms para validação e segurança.
    """
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados da requisição (binding)
        form = RespostaQuizForm(request.POST)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva os dados limpos no banco de dados
            resposta_instance = form.save()

            # Define as respostas corretas para calcular a pontuação
            correct_answers = {
                'q1': 'b',  # Phishing
                'q2': 'c',  # Boa prática de segurança
                'q3': 'a',  # Função do antivírus
                'q4': 'b',  # E-mail suspeito
                'q5': 'b',  # Risco de exposição
            }
            
            # Calcula a pontuação do usuário
            score = 0
            user_answers = {
                'q1': resposta_instance.q1, 'q2': resposta_instance.q2,
                'q3': resposta_instance.q3, 'q4': resposta_instance.q4,
                'q5': resposta_instance.q5,
            }
            for question, answer in user_answers.items():
                if answer == correct_answers.get(question):
                    score += 1
            
            # Seleciona a mensagem de resultado com base na pontuação
            total_questions = len(correct_answers)
            if score == total_questions:
                title = "Parabéns, Hacker do Bem!"
                message = "Você passou pelo firewall de perguntas sem levar nenhum ataque. Seu antivírus mental está 100% atualizado e sua senha é mais forte que SHA-512! "
                result_class = "success"
            elif score >= 3:  # Acertou 3 ou 4 de 5
                title = "Quase lá, Agente Digital. "
                message = "Você conseguiu se defender de vários ataques, mas alguns phishing ainda passaram pela rede. Continue treinando e logo sua mente será impenetrável como uma VPN bem configurada! "
                result_class = "warning"
            else:  # Acertou menos de 3
                title = "Alerta Vermelho! "
                message = "Sua rede foi invadida por malwares de dúvidas! Mas não se preocupe: cada erro é um patch de aprendizado. Reforce suas senhas de conhecimento e tente novamente — segurança cibernética exige resiliência! "
                result_class = "danger"

            context = {'sucesso': True, 'score': score, 'total_questions': total_questions, 'result_title': title, 'result_message': message, 'result_class': result_class}
            return render(request, 'quiz.html', context)
    else:
        # Se for um GET, cria um formulário em branco
        form = RespostaQuizForm()

    # Renderiza o formulário (seja em branco ou com erros de validação)
    return render(request, 'quiz.html', {'form': form})
