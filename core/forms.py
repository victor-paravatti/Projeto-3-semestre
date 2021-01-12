from django.forms import ModelForm
from core.models import Cliente, Funcionario, Produto, Fabricante, Setor, \
    Cargo, Status, TipoSolicitacao, Pagamento
from django import forms


class FormFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'


class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'


class FormCargo(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class FormStatus(ModelForm):
    class Meta:
        model = Status
        fields = '__all__'


class FormTipoSolicitacao(ModelForm):
    class Meta:
        model = TipoSolicitacao
        fields = '__all__'


class FormPagamento(ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'
    

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('email', 'senha')
        widgets = {
            'password': forms.PasswordInput(),
        }
