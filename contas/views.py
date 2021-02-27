from django.shortcuts import render

from django.http import HttpResponse
import datetime

def data(request):
    now = datetime.datetime.now()
    #html = "<html><body>A hora agora é:  %s.</body></html>" % now
    return render(request, 'contas/data.html')
