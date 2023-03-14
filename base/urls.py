from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/',views.loginPage),
    path('logout/',views.logoutPage),
    path('registro/',views.registerPage),
    path('Animales/',views.animales),
    path('Animales/Conejos',views.conejos),
    path('Animales/Perros',views.perros),
    path('Animales/Gatos',views.gatos),
    path('Tecnología/',views.tecnologia),
    path('Tecnología/Lenguajes de Programación',views.lenguajes),
    path('Cuentos/',views.cuentos),
    path('Cuentos/Conejín el Aventurero',views.conejin),
    path('post/<int:id>',views.post),
    path('post/',views.post),
    path('comment/',views.comment),
    path('edit_comment/<int:id>',views.edit_comment),
    path('post/<int:id>/eliminar/', views.borrar_post),
    path('comentario/<int:id>/eliminar/', views.borrar_comentario),
]