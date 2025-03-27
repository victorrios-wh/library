from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from contactos.forms import FormularioContactos

# Create your views here.
def contactos(request):
    if request.method == 'POST':
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(cd['asunto'], cd['mensaje'],
            #           cd.get('email', 'noreply@example.vom'),
            #           ['siteowner qexample.com'], )
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos(initial={
            'asunto':'Adoro su sitio'
        })
    return render(request, 'formulario_contactos.html', {
        'form':form
    })
