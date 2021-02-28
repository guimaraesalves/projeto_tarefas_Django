from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime

def data(request):
    date = {}
    date['transacoes'] = ['Python', 'Django', 'Chatterbot']
    date['now'] = datetime.datetime.now()
    #html = "<html><body>A hora agora é:  %s.</body></html>" % now

    return render(request, 'contas/data.html', date)


def listagem(request):
    date = {}
    date['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', date)

def nova_transacao(request):
    date1 = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    date1['form'] = form
    return render(request, 'contas/form.html', date1)





