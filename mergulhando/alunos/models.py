from django.db import models 
from django.contrib import admin

# Mudei.

class Alunos(models.Model):
	id_aluno    = models.AutoField(primary_key=True, unique=True)
	nome        = models.CharField(max_length=100)
	telefone    = models.CharField(max_length=15)
	celula      = models.ForeignKey('Celula')
	email       = models.EmailField()
	observacoes = models.CharField(max_length=300)
	def __str__ (self):
		return 'Nome: %s, Lider: %s' % (self.nome,self.lider )

class AlunosAdmin(admin.ModelAdmin):
		list_display = ('nome', 'telefone', 'email')
		list_filter = ['nome']
		ordering = ['nome']
		search_fields = ('nome','lider')

class Celula (models.Model):
	id_celula = models.AutoField(primary_key=True, unique=True)
	nome      = models.CharField(max_length=100)
	lider     = models.CharField(max_length=100, default='Mohamed')
	bairro    = models.CharField(max_length=100, default='BDN Tapuapé')
	contato   = models.CharField(max_length=100, default='s/ contato')
	def __str__(self):
		return '%s, Líder: %s' % (self.nome,self.lider)
	
class Cursos(models.Model):
	id_curso  = models.AutoField(primary_key=True, unique=True)
	nome      = models.CharField(max_length=100)
	descricao = models.CharField(max_length=600)
	data_ini  = models.DateField()
	data_fim  = models.DateField()
	ativo     = models.BooleanField(default=True)
	def __str__(self):
		return '%s, %s, %s' % (self.nome,self.data_ini, self.data_fim)

class Modulo(models.Model):
	id_modulo = models.AutoField(primary_key=True, unique=True)
	curso     = models.ForeignKey('Cursos')
	nome      = models.CharField(max_length=100)
	ativo     = models.BooleanField(default=True)

class Turma(models.Model):
	id_turma  = models.AutoField(primary_key=True, unique=True)
	curso     = models.ForeignKey('Cursos')
	nome      = models.CharField(max_length=100)
	data_ini  = models.DateField()
	data_fim  = models.DateField()

class Presenca(models.Model):
	id_modulo = models.AutoField(primary_key=True, unique=True)
	aluno = models.ForeignKey('Alunos')
	modulo = models.ForeignKey('Modulo')
	data  = models.DateField()
	def __str__(self):
		return '%s, %s, %s' % (self.curso,self.aluno, self.data)		