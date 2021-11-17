from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from .models import Register
from .forms import RegisterForm

# Create your views here.


def index(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_register = RegisterForm(request.POST)
            new_register.save()
            messages.success(request, "Sukses Menambah Pendaftar Baru.")
            return redirect('index')
    else:
        form = RegisterForm()
        registers = Register.objects.all()[0:5]
        context = {
            'registers': registers,
            'form': form,
        }
    return render(request, 'index.html', context)
