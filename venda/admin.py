from django.contrib import admin
from django.contrib.auth.models import Group
from venda.models import Produto
from venda.models import Venda
from venda.models import Pagamento

# Register your models here.
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Pagamento)
admin.site.unregister(Group)
