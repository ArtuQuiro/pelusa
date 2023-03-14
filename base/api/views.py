from django.http import JsonResponse
from ..models import Post, Categoria, Tema, Comentario

def routes(request):
    routes=[
        'GET /api/posts',
        'GET /api/post/:id'
    ]
    return JsonResponse(routes, safe=False)

def posts(request):
    posts = Post.objects.all()
    posts_dict = []
    for p in posts:
        posts_dict.append({
            'titulo': p.titulo,
            'contenido': p.contenido,
            'usuario': p.usuario.username,
            'tema': p.tema.titulo,
            'id': p.id
        })
    return JsonResponse(posts_dict, safe=False)

def post(request, id):
    post = Post.objects.get(id=id)
    post_dict = {
        'titulo': post.titulo,
        'contenido': post.contenido,
        'usuario': post.usuario.username,
        'tema': post.tema.titulo
    }
    return JsonResponse(post_dict, safe=False)

def categorias(request):
    cat = Categoria.objects.all()
    cat_dict = []
    for c in cat:
        cat_dict.append({
            'nombre': c.nombre
        })
    return JsonResponse(cat_dict, safe=False)

def temas(request):
    temas = Tema.objects.all()
    tema_dict = []
    for t in temas:
        tema_dict.append({
            'titulo': t.titulo,
            'contenido': t.contenido,
            'categoria': t.categoria.nombre
        })
    return JsonResponse(tema_dict, safe=False)

def comentarios(request,id):
    com = Comentario.objects.filter(post=id)
    com_dict = []
    for c in com:
        com_dict.append({
            'usuario': c.usuario.username,
            'contenido': c.contenido
        })
    return JsonResponse(com_dict, safe=False)