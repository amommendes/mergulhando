"""mergulhando URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from mergulhando.views import hora_atual
from mergulhando.views import horas_mais
from mergulhando.views import home
from mergulhando.alunos.views import busca
from mergulhando.views import user

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^hora/$', hora_atual),
    url(r'^horas/plus/(\d{1,2})/', horas_mais),
    url(r'^home|', home),
    url(r'^busca', busca),
    url(r'^user$', user),

]
