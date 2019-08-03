from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, 'index.php')
def home(request):
    return render(request, 'home.html')
def portfolio(request):
    return render(request, 'proiecte.html')
def services(request):
    return render(request, 'development.html')
def contact(request):
    return render(request, 'contact.html')
def error404(request):
    return render(request, '404.html')

def contact(request):
    form_class = ContactForm()
    return render(request, 'contact.html', {
        'form': form_class,
    })
