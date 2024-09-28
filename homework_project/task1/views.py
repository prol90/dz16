from django.shortcuts import render
from .models import Game

def index(request):
    return render(request, 'task1/index.html')

def product_list(request):
    games = Game.objects.all()
    return render(request, 'task1/product_list.html', {'games': games})

def cart(request):
    return render(request, 'task1/cart.html')

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Buyer

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if not Buyer.objects.filter(name=username).exists():
                Buyer.objects.create(
                    name=username,
                    balance=form.cleaned_data['balance'],
                    age=form.cleaned_data['age']
                )
                return redirect('index')
            else:
                form.add_error('username', 'Пользователь с таким именем уже существует.')
    else:
        form = RegistrationForm()

    return render(request, 'task1/register.html', {'form': form})
