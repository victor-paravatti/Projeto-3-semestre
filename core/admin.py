from django.contrib import admin
from core.models import Cargo, Cliente, Funcionario, Pagamento, Produto, Fabricante, Setor, Status, TipoSolicitacao

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Produto)
admin.site.register(Fabricante)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(Status)
admin.site.register(TipoSolicitacao)
admin.site.register(Pagamento)