from django.db.models import fields
from core.models import Cliente, Funcionario, Produto, Fabricante, \
     Setor, Cargo, Status, TipoSolicitacao, Pagamento
from django.forms import ModelForm





class FormCliente(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class FormFuncionario(ModelForm):

    class Meta:
        model = Funcionario
        fields = '__all_'


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


class  FormTipoSolicitacao(ModelForm):

    class Meta:
        model = TipoSolicitacao
        fields = '__all__'


class FormPagamento(ModelForm):
    
    class Meta:
        model = Pagamento
        fields = '__all__'