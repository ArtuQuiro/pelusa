from django.contrib import admin

# Register your models here.


from .models import Foro
from .models import Categoria
from .models import Tema
from .models import Post
from .models import Comentario

admin. site.register (Foro)
admin. site.register (Categoria)
admin. site.register (Tema)
admin. site.register (Post)
admin. site.register (Comentario)