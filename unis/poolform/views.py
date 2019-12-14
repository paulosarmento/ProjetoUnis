from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import pessoas
from django.template import loader
from django.urls import reverse
from .form import myForm

# My fucking views kkkk

def index(request):

    list_pessoas = pessoas.objects.all()
    template = loader.get_template('poolform/index.html')
    context = {
        'list_pessoas': list_pessoas,
    }

    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            #aqui eu salvo o form
            pessoa = pessoas()
            pessoa.nome = form.nome
            pessoa.endereco = form.endereco
            pessoa.peso = form.peso
            pessoa.altura = form.altura
            pessoa.imc = str( float(form.peso)/ float(form.altura ** 2) )
            pessoa.save()

            return HttpResponse(template.render(context, request))
        else:
            
            template = loader.get_template('poolform/index.html')
            return HttpResponse(template.render(context, request))

    else:
        form = myForm()
        return HttpResponse(template.render(context, request))

def form_Save(request):
    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            #aqui eu salvo o form
            pessoa = pessoas()
            pessoa.nome = form.nome
            pessoa.endereco = form.endereco
            pessoa.peso = form.peso
            pessoa.altura = form.altura
            pessoa.imc = str( float(form.peso)/ float(form.altura ** 2) )
            pessoa.save()

            return HttpResponseRedirect('index.html')
        else:
            template = loader.get_template('poolform/index.html')
            return HttpResponse(template.render())

    else:
        form = myForm()
        return render(request, 'index.html', {'form': form,})