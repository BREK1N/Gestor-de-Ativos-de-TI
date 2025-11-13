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
