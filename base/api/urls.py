from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes),
    path('posts/', views.posts),
    path('post/<int:id>', views.post),
    path('categorias', views.categorias),
    path('temas', views.temas),
    path('post/<int:id>/comentarios',views.comentarios),
]