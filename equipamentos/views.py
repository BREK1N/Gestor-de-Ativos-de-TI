from django.shortcuts import render, redirect
from .forms import EquipamentoForm

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipamentos') 
    else:
        form = EquipamentoForm()
    
    return render(request, 'equipamento_form.html', {'form': form})
