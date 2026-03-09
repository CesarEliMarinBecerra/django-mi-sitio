from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('blog/', views.blog_view, name='blog'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    path('certificados/', views.certificados, name='certificados'),

]
