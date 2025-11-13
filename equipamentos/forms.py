from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'serial', 'data_aquisicao', 'status', 'categoria'] # Ou liste os campos que deseja

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona a classe 'form-control' a todos os campos do formulário
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        # O campo de data precisa ser do tipo 'date' no HTML
        self.fields['data_aquisicao'].widget.attrs['type'] = 'date'
