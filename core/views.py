from django.shortcuts import render

def index(request):
    context ={
        'nome':'carlos normando'
    }
    return render(request, 'index.html', context)
    

def contato(request):
    return render(request, 'contato.html')