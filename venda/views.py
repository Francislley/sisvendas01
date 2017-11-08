from venda.models import Venda
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
    return render(request, 'index.html', {})

@login_required(login_url='/login/')
def main(request):
    context = { 
        'vendas':Venda.objects.filter(
            usuario=request.user) 
        }
    return render(request, 'main.html', context)
    
    
