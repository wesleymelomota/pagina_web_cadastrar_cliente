from django.shortcuts import render, redirect, HttpResponse
from app.form import PessoaForm
from app.form import Pessoa
from django.core.paginator import Paginator
# Create your views here.

"""
def paginas(request):
    data = {}
    all = Pessoa.objects.all()
    paginator = Paginator(all, 5)
    pages = request.Get.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)
"""

def home(request):
    data = {}
    data['db'] = Pessoa.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = PessoaForm
    return render(request, 'form.html', data)


def create(request):
    data = {}
    form = PessoaForm(request.POST or None)
    data['form'] = PessoaForm
    if form.is_valid():
        form.save()
    else:
        return render(request, 'form.html', data)
    return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    data['form'] = PessoaForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home')

