from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from .models import Cliente

# Create your views here.
def cadastro(request):
    return HttpResponse('Cadastro de usuários')


def clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        queixa = request.POST.get('queixa')

        if not nome or not email or not queixa:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('clientes')
        elif len(nome) < 3:
            messages.error(request, 'O nome deve ter pelo menos 3 caracteres.')
            return redirect('clientes')
        
        elif Cliente.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('clientes')

        else:
            cliente = Cliente(
                nome=nome, 
                email=email, 
                queixa=queixa)
            cliente.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('clientes')
    else:
        return render(request, 'clientes.html')