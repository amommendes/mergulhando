from django.contrib import admin

# Register your models here.
from mergulhando.alunos.models import *
# from mergulhando.alunos.models import AlunosAdmin
# from mergulhando.alunos.models import Cursos

admin.site.register(Alunos,AlunosAdmin)
admin.site.register(Cursos)
admin.site.register(Modulo)
admin.site.register(Turma)
admin.site.register(Presenca)
admin.site.register(Celula)