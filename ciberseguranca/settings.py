
import os
from pathlib import Path
import dj_database_url
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# AVISO DE SEGURANÇA: mantenha a chave secreta usada em produção em segredo!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'troque-isto-por-uma-chave-secreta')

# Carrega as variáveis de ambiente do arquivo .env na raiz do projeto.
load_dotenv(BASE_DIR / '.env')

# AVISO DE SEGURANÇA: não execute com o debug ativado em produção!
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Definição da aplicação
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'site_escola.apps.SiteEscolaConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ciberseguranca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'site_escola' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ciberseguranca.wsgi.application'
ASGI_APPLICATION = 'ciberseguranca.asgi.application'

# --- Configuração do Banco de Dados ---
# A configuração agora lê a DATABASE_URL do seu arquivo .env.
# Isso é mais seguro e flexível do que deixar a senha diretamente no código.
DATABASE_URL = os.environ.get('DATABASE_URL')

# Se a variável não for encontrada, o Django não iniciará.
if not DATABASE_URL:
    raise ImproperlyConfigured(
        "A variável de ambiente DATABASE_URL não foi definida. "
        "Verifique se o arquivo .env existe na raiz do projeto (ao lado de "
        "manage.py) e contém sua chave de conexão do Neon, conforme "
        "instruções no README.md."
    )

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Belem'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'site_escola' / 'static']
