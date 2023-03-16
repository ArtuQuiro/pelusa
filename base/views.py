from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Categoria, Tema, Post, User, Comentario

# Create your views here.

def loginPage(request):
    if (request.method == 'POST'):
        username= request.POST.get('username')
        password= request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inició sesión correctamente')
                return redirect('/')
            
        messages.warning(request, 'Datos incorrectos')

    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    messages.success(request, 'Se cerró sesión correctamente')
    return redirect('/')

def registerPage(request):
    if (request.method=='POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.warning(request, 'Las contraseñas no coinciden')
            return redirect('/registro')
        User.objects.create_user(username, email=email, first_name=first_name, last_name=last_name, password=password)
        messages.success(request, 'Usuario creado correctamente')
        return redirect('/login')
    return render(request, 'register.html')

def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'home.html', { 'categorias': categorias })

def post(request, id = None):
    if request.method == "POST":
        id=request.POST.get('id')
        if(id is None):
            Post.objects.create(
                titulo = request.POST.get('titulo'),
                contenido = request.POST.get('contenido'),
                usuario=User.objects.get(id=request.POST.get('usuario')),
                tema = Tema.objects.get(id=request.POST.get('tema'))
            )
            messages.success(request, 'Se creó el post correctamente')
            return redirect('/')
        else:
            p = Post.objects.get(id=id)
            if(p.usuario == request.user):
                p.titulo= request.POST.get('titulo')
                p.contenido = request.POST.get('contenido')
                p.usuario=User.objects.get(id=request.POST.get('usuario'))
                p.tema = Tema.objects.get(id=request.POST.get('tema'))
                p.save()
                messages.success(request, 'Se editó el post correctamente')
                return redirect('/')
            else:
                messages.warning(request, 'No tienes permisos para editar este post')
                return redirect('/')

    context = {}
    temas = Tema.objects.all()
    context['temas'] = temas
    if id is not None:
        context['post'] = Post.objects.get(id = id)
    return render(request, 'Post.html', context)

def borrar_post(request, id):
    p = Post.objects.get(id=id)
    if p.usuario == request.user:
        p.delete()
        messages.success(request, 'Se post se eliminó correctamente')
    else:
        messages.warning(request, 'No tienes permisos para borrar este post')
    return redirect('/')

def comment(request):
    p = Post.objects.get(id=request.POST.get('post'))
    Comentario.objects.create(
        contenido = request.POST.get('contenido'),
        usuario = request.user,
        post = p
    )
    messages.success(request, 'Se comentó correctamente')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def edit_comment(request, id):
    if request.method == "POST":
        c = Comentario.objects.get(id=id)
        if(c.usuario == request.user):
            c.contenido = request.POST.get('contenido')
            c.usuario = User.objects.get(id=request.POST.get('usuario'))
            c.post = Post.objects.get(id=request.POST.get('post'))
            c.save()
            messages.success(request, 'El comentario se editó correctamente')
            return redirect('/')
        else:
            messages.warning(request, 'No tienes permisos para editar este comentario')
            return redirect('/')
    context = {} 
    context['comentario'] = Comentario.objects.get(id = id)
    return render(request, 'editar_comentario.html',context)

def borrar_comentario(request, id):
    c = Comentario.objects.get(id=id)
    if c.usuario == request.user:
        c.delete()
        messages.success(request, 'El comentario se borró correctamente')
    else:
        messages.warning(request, 'No tienes permisos para borrar este comentario')
    return redirect('/')

def animales(request):
    temas = Tema.objects.filter(categoria='1')
    return render(request, 'Animales.html', { 'temas': temas})
def tecnologia(request):
    temas = Tema.objects.filter(categoria='2')
    return render(request, 'Tecnología.html', { 'temas': temas})
def cuentos(request):
    temas = Tema.objects.filter(categoria='3')
    return render(request, 'Cuentos.html', { 'temas': temas})

def conejos(request):
    posts = Post.objects.filter(tema='1').order_by('-fecha_creacion')
    return render(request, 'Conejos.html', {'posts':posts})
def perros(request):
    posts = Post.objects.filter(tema='2').order_by('-fecha_creacion')
    return render(request, 'Perros.html', {'posts':posts})
def gatos(request):
    posts = Post.objects.filter(tema='3').order_by('-fecha_creacion')
    return render(request, 'Gatos.html', {'posts':posts})
def lenguajes(request):
    posts = Post.objects.filter(tema='4').order_by('-fecha_creacion')
    return render(request, 'Lenguajes de Programación.html', {'posts':posts})
def conejin(request):
    posts = Post.objects.filter(tema='5').order_by('-fecha_creacion')
    return render(request, 'Conejín el Aventurero.html', {'posts':posts})

def toggle_dark_mode(request):
    if 'dark_mode' not in request.session:
        request.session['dark_mode'] = False
    request.session['dark_mode'] = not request.session['dark_mode']
    return redirect('/')