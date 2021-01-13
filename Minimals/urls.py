from django.contrib import admin
from django.urls import path, include
from core.views import Cadastrar, home, carinho, cadastrar_cliente, cadastrar_produto, \
    listar_produto, editar_produto, excluir_produto, exibir_produto, cadastrar_funcionario, \
    listar_funcionario, editar_funcionario, excluir_funcionario, cadastrar_cargo, listar_cargo, \
    editar_cargo, excluir_cargo, cadastrar_setor, listar_setor, editar_setor, excluir_setor, \
    cadastrar_fabricante, listar_fabricante, editar_fabricante, excluir_fabricante, cadastrar_status, \
    listar_status, editar_status, excluir_status, cadastrar_tipo_solicitacao, listar_tipo_solicitacao, \
    editar_tipo_solicitacao, excluir_tipo_solicitacao, cadastrar_pagamento, listar_pagamento, \
    editar_pagamento, excluir_produto
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', home, name='url_home'),
    path('cadastrar/', Cadastrar.as_view(), name='url_cadastrar'),
    path('carrinho/', carinho, name='url_carrinho'),
    path('cadastrar_cliente/', cadastrar_cliente, name='url_cadastrar_cliente'),
    path('cadastrar_produto/', cadastrar_produto, name='url_cadastrar_produto'),
    path('listar_produto/', listar_produto, name='url_listar_produto'),
    path('editar_produto/<int:id>/', editar_produto, name='url_editar_produto'),
    path('excluir_produto/<int:id>/', excluir_produto, name='url_excluir_produto'),
    path('exibir_produto/<int:id>/', exibir_produto, name='url_exibir_produto'),
    path('cadastrar_funcionario/', cadastrar_funcionario, name='url_cadastrar_funcionario'),
    path('listar_funcionario/', listar_funcionario, name='url_listar_funcionario'),
    path('editar_funcionario/<int:id>/', editar_funcionario, name='url_editar_funcionario'),
    path('excluir_funcionario/<int:id>/', excluir_funcionario, name='url_excluir_funcionario'),
    path('cadastrar_cargo/', cadastrar_cargo, name='url_cadastrar_cargo'),
    path('listar_cargo/', listar_cargo, name='url_listar_cargo'),
    path('editar_cargo/<int:id>/', editar_cargo, name='url_editar_cargo'),
    path('excluir_cargo/<int:id>/', excluir_cargo, name='url_excluir_cargo'),
    path('cadastrar_setor/', cadastrar_setor, name='url_cadastrar_setor'),
    path('listar_setor/', listar_setor, name='url_listar_setor'),
    path('editar_setor/<int:id>/', editar_setor, name='url_editar_setor'),
    path('excluir_setor/<int:id>/', excluir_setor, name='url_excluir_setor'),
    path('cadastrar_fabricante/', cadastrar_fabricante, name='url_cadastrar_fabricante'),
    path('listar_fabricante/', listar_fabricante, name='url_listar_fabricante'),
    path('editar_fabricante/<int:id>/', editar_fabricante, name='url_editar_fabricante'),
    path('excluir_fabricante/<int:id>/', excluir_fabricante, name='url_excluir_fabricante'),
    path('cadastrar_status/', cadastrar_status, name='url_cadastrar_status'),
    path('listar_status/', listar_status, name='url_listar_status'),
    path('editar_status/<int:id>/', editar_status, name='url_editar_status'),
    path('excluir_status/<int:id>/', excluir_status, name='url_excluir_status'),
    path('cadastrar_tipo_solicitacao/', cadastrar_tipo_solicitacao, name='url_cadastrar_tipo_solicitacao'),
    path('listar_tipo_solicitacao/', listar_tipo_solicitacao, name='url_listar_tipo_solicitacao'),
    path('editar_tipo_solicitacao/<int:id>/', editar_tipo_solicitacao, name='url_editar_tipo_solicitacao'),
    path('excluir_tipo_solicitacao/<int:id>/', excluir_tipo_solicitacao, name='url_excluir_tipo_solicitacao'),
    path('cadastrar_pagamento/', cadastrar_pagamento, name='url_cadastrar_pagamento'),
    path('listar_pagamento/', listar_pagamento, name='url_listar_pagamento'),
    path('editar_pagamento/<int:id>/', editar_pagamento, name='url_editar_pagamento'),
    path('excluir_pagamento/<int:id>/', excluir_pagamento, name='url_excluir_pagamento')
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
