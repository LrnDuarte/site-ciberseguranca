# Projeto Django - Cibersegurança nas Escolas

Este é um site educativo sobre Cibersegurança adaptado para rodar com o framework Django.

## ✅ Como usar passo a passo:

### 1. Requisitos

- Python 3 instalado
- Pip

---

### 2. Passos para rodar

1.  **Clone ou extraia o projeto** para uma pasta no seu computador.

2.  **Configure o Banco de Dados (Neon):**

    - Crie um arquivo chamado `.env` na raiz do projeto (na mesma pasta do `manage.py`).
    - Dentro do arquivo `.env`, adicione a sua chave de conexão do Neon:
      ```
      DATABASE_URL="postgres://user:password@host/dbname?sslmode=require"
      ```

3.  **Configure o Ambiente e Instale as Dependências:**
    Abra um terminal na pasta do projeto e execute os seguintes comandos:

    ```bash
    # Crie o ambiente virtual
    python -m venv venv

    # Ative o ambiente virtual (no Windows PowerShell)
    .\venv\Scripts\activate

    # Instale todas as dependências do projeto
    pip install -r requirements.txt
    ```

4.  **Prepare o Banco de Dados:**
    Com o ambiente ativado, rode as migrações para criar as tabelas no seu banco Neon:

    ```bash
    python manage.py migrate
    ```

5.  **Rode o Servidor:**
    ```bash
    python manage.py runserver
    ```

Abra o navegador e acesse: [http://127.0.0.1:8000/quiz](http://127.0.0.1:8000/quiz)

### 3. Estrutura do Projeto

Esta é a estrutura de arquivos e pastas que compõem o código-fonte do projeto e devem ser versionados com Git.

```plaintext
site-ciberseguranca/
├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── manage.py           # Utilitário de linha de comando do Django
├── README.md           # Este arquivo
├── requirements.txt    # Dependências do projeto
├── ciberseguranca/     # Pasta do PROJETO Django (configurações globais)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── site_escola/        # Pasta do APP Django (lógica do site)
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── models.py
    ├── static/
    │   └── style.css
    ├── templates/
    │   ├── autoridades.html
    │   ├── boaspraticas.html
    │   ├── index.html
    │   ├── malware.html
    │   ├── oque.html
    │   ├── phishing.html
    │   ├── quiz.html
    │   └── sociais.html
    ├── tests.py
    ├── urls.py
    └── views.py

```

Você pode editar os arquivos HTML, CSS e JS diretamente.

---

### 💡 Dica

Se quiser adicionar mais páginas, basta criar novos arquivos `.html` dentro de `templates/` e adicionar novas `views` em `views.py`.

---

Pronto! Qualquer dúvida, estou aqui para te ajudar.
