from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipamentoForm
from .models import Equipamento

def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all().order_by('nome')
    return render(request, 'lista_equipamentos.html', {'equipamentos': equipamentos})

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipamentos') 
    else:
        form = EquipamentoForm()
    
    return render(request, 'equipamento_form.html', {'form': form})

def detalhe_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'equipamento_detalhe.html', {'equipamento': equipamento})

def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        # Passamos a 'instance' para que o formulário saiba que está editando um objeto existente
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('detalhe_equipamento', pk=equipamento.pk)
    else:
        # Ao carregar a página (GET), o formulário já vem preenchido com os dados do equipamento
        form = EquipamentoForm(instance=equipamento)
    
    # Reutilizamos o mesmo template do formulário de cadastro
    return render(request, 'equipamento_form.html', {'form': form})

def deletar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('lista_equipamentos')
    # Para o método GET, mostramos uma página de confirmação
    return render(request, 'equipamento_confirm_delete.html', {'equipamento': equipamento})
