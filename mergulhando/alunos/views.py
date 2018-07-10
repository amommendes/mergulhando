from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Q
from mergulhando.alunos.models import Alunos 
from mergulhando.alunos.forms import NovoAluno 

# Create your views here.

def busca(request): 
	if request.method == 'GET':
		formulario = NovoAluno()
		query = request.GET.get('q','')
		if query:
			qset= (
				Q(nome__contains=query) |
				Q(lider__contains=query)
			)
			results = Alunos.objects.filter(qset).values()
	#		results = Alunos.objects.filter(qset)
		else:
			results=[]
		return render_to_response("../templates/busca.html",{
				"results":results,
				"query": query,
				"form": formulario})
	else:
		
		nome = request.POST.get('nome')
		telefone =  request.POST.get('telefone')
		celula   =  request.POST.get('celula')
		email   =  request.POST.get('email')
		lider   =  request.POST.get('lider')
		Alunos (nome=nome,telefone=telefone,celula=celula,email=email,lider=lider).save()
		return render_to_response('../templates/user.html')



