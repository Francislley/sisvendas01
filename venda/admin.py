from django.contrib import admin
from venda.models import Produto
from venda.models import Venda
from venda.models import Pagamento

# Register your models here.
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Pagamento)
