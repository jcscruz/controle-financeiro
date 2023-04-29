from django.contrib import admin
from registro.models import Registro_Financeiro

# Register your models here.
from django.contrib import admin

class ListandoRegistros(admin.ModelAdmin):
    list_display = ("consolidado", "id", "tipo", "tipo_categoria", "descricao", "valor", "competencia", "vencimento", "parcela", "total_parcela", "centro_de_custo", "origem_debito", "origem_credito", "observacao")
    list_display_links = ("id","descricao")
    search_fields = ("descricao",)
    list_filter = ("tipo", "tipo_categoria", "consolidado", "centro_de_custo", "origem_debito", "competencia", "vencimento")
    list_per_page = 10

admin.site.register(Registro_Financeiro, ListandoRegistros)