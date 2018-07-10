from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response

import datetime

def hora_atual(request):
	now= datetime.datetime.now()
	print (request)
	html="""<html>
		<head>
		  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
		  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
		</head>
	<body>
		<div class="row">
			<div class="col s4 offset-s4">
				<div class="card">
	            <div class="card-image">
	              <img src="http://materializecss.com/images/sample-1.jpg">
	              <span class="card-title">Card Title</span>
	            </div>
	            <div class="card-content">
	              <p>Se liga na hora a %s..</p>
	            </div>
	            <div class="card-action">
	              <a href="/admin">This is a link</a>
	            </div>
			</div>
		</div>
	</body>""" % now

	return HttpResponse(html)


def horas_mais(request, offset):
	#assert False
	offset=int(offset)
	now= datetime.datetime.now() + datetime.timedelta(hours=offset)
	print (request)
	html="""<html>
		<head>
		  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
		  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
		</head>
	<body>
		<div class="row">
			<div class="col s4 offset-s4">
				<div class="card">
	            <div class="card-image">
	              <img src="http://materializecss.com/images/sample-1.jpg">
	              <span class="card-title">Card Title</span>
	            </div>
	            <div class="card-content">
	              <p>Foram somadas %d a %s..</p>
	            </div>
	            <div class="card-action">
	              <a href="/admin">This is a link</a>
	            </div>
			</div>
		</div>
	</body>""" % (offset,now)

	return HttpResponse(html)

def home(request):
	#template = get_template('home.html')
	#html = template.render()
	#return HttpResponse(html)
	return render_to_response('home.html')

def user(request):
	return render_to_response('user.html')