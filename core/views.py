from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')


def carrinho(request):
    return render(request, 'core/carrinho.html')


def login(request):
    return render(request, 'core/login.html')
    