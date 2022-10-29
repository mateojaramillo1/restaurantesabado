from django import forms


class FormularioEmpleado(forms.Form):
    CARGOS=(
        (1, "Cheff"),
        (2, "administrador"),
        (3, "mesero")
        (4, "ayudante")
    )
    
    nombre = forms.CharField(
        required=True,
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    apellidos = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    foto = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    cargo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        choices=CARGOS
    )
    salario = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    