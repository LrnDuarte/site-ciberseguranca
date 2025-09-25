from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oque/', views.o_que_e_view, name='oque'),
    path('boas-praticas/', views.boas_praticas_view, name='boas-praticas'),
    path('phishing/', views.phishing_view, name='phishing'),
    path('malware/', views.malware_view, name='malware'),
    path('redes-sociais/', views.redes_sociais_view, name='redes-sociais'),
    path('ajuda/', views.ajuda_view, name='ajuda'),
    path('quiz/', views.quiz_view, name='quiz'),
]
