from django.db.models import Sum
from venda.models import Venda
from venda.models import Pagamento
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    return render(request, 'login.html', {})

def calculate_total_pagamentos_to_user(request):
    valor_total = Pagamento.objects.filter(
        usuario=request.user).\
        aggregate(valor_total=Sum('valor')).get('valor_total', 0.0)
    return valor_total if valor_total else 0.0

def calculate_total_vendas_to_user(request):
    valor_total = Venda.objects.filter(
        usuario=request.user).\
        aggregate(valor_total=Sum('valor')).get('valor_total', 0.0)
    return valor_total if valor_total else 0.0

@login_required(login_url='/login/')
def main(request):
    context = { 
        'vendas': Venda.objects.filter(
            usuario=request.user),
        'pagamentos': Pagamento.objects.filter(
            usuario=request.user),
        'total_saldo': calculate_total_vendas_to_user(request) - \
            calculate_total_pagamentos_to_user(request)
        }
    return render(request, 'main.html', context)