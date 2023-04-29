from django.db import models
from datetime import datetime

# Create your models here.

class Registro(models.Model):
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    valor = models.IntegerField(null=False)

    def __str__(self):
        return f"Registro [nome={self.descricao}]"
    

class Registro_Financeiro(models.Model):

    OPCOES_TIPO_CATEGORIA = [
        ("DESPESA FIXA","Despesa Fixa"),
        ("DESPESA PARCELADA","Despesa Parcelada"),
        ("DESPESA AVULSA","Despesa Avulsa"),
        ("RECEITA FIXA","Receita Fixa"),
        ("RECEITA PARCELADA","Receita Parcelada"),
        ("RECEITA AVULSA","Receita Avulsa"),
    ]

    OPCOES_TIPO = [
        ("DESPESA","Despesa"),
        ("RECEITA","Receita"),
    ]

    OPCOES_COMPETENCIA = [
        ("NOVEMBRO/2022","Novembro/2022"),
        ("DEZEMBRO/2022","Dezembro/2022"),
        ("JANEIRO/" + str(datetime.now().year),"Janeiro/" + str(datetime.now().year)),
        ("FEVEREIRO/" + str(datetime.now().year),"Fevereiro/" + str(datetime.now().year)),
        ("MARCO/" + str(datetime.now().year),"Março/" + str(datetime.now().year)),
        ("ABRIL/" + str(datetime.now().year),"Abril/" + str(datetime.now().year)),
        ("MAIO/" + str(datetime.now().year),"Maio/" + str(datetime.now().year)),
        ("JUNHO/" + str(datetime.now().year),"Junho/" + str(datetime.now().year)),
        ("JULHO/" + str(datetime.now().year),"Julho/" + str(datetime.now().year)),
        ("AGOSTO/" + str(datetime.now().year),"Agosto/" + str(datetime.now().year)),
        ("SETEMBRO/" + str(datetime.now().year),"Setembro/" + str(datetime.now().year)),
        ("OUTUBRO/" + str(datetime.now().year),"Outubro/" + str(datetime.now().year)),
        ("NOVEMBRO/" + str(datetime.now().year),"Novembro/" + str(datetime.now().year)),
        ("DEZEMBRO/" + str(datetime.now().year), "Dezembro/" + str(datetime.now().year)),
    ]
    
    OPCOES_VENCIMENTO = [
        ("JANEIRO/" + str(datetime.now().year),"Janeiro/" + str(datetime.now().year)),
        ("FEVEREIRO/" + str(datetime.now().year),"Fevereiro/" + str(datetime.now().year)),
        ("MARCO/" + str(datetime.now().year),"Março/" + str(datetime.now().year)),
        ("ABRIL/" + str(datetime.now().year),"Abril/" + str(datetime.now().year)),
        ("MAIO/" + str(datetime.now().year),"Maio/" + str(datetime.now().year)),
        ("JUNHO/" + str(datetime.now().year),"Junho/" + str(datetime.now().year)),
        ("JULHO/" + str(datetime.now().year),"Julho/" + str(datetime.now().year)),
        ("AGOSTO/" + str(datetime.now().year),"Agosto/" + str(datetime.now().year)),
        ("SETEMBRO/" + str(datetime.now().year),"Setembro/" + str(datetime.now().year)),
        ("OUTUBRO/" + str(datetime.now().year),"Outubro/" + str(datetime.now().year)),
        ("NOVEMBRO/" + str(datetime.now().year),"Novembro/" + str(datetime.now().year)),
        ("DEZEMBRO/" + str(datetime.now().year), "Dezembro/" + str(datetime.now().year)),
    ]

    OPCOES_CENTRO_DE_CUSTO= [
        ("JULIO","Julio"),
        ("JESSICA","Jessica"),
        ("CASA","Casa"),
    ]

    OPCOES_ORIGEM_DEBITO= [
        ("", ""),
        ("CARTAO ITAU MASTER CARD PLATINUM","Cartão Itaú Master Platinum"),
        ("CARTAO ITAU VISA PLATINUM","Cartão Itaú Visa Platinum"),
        ("CARTAO ITAU PAO DE ACUCAR VISA PLATINUM","Cartão Itaú Pão de Açucar Visa Platinum"),
        ("CARTAO ITAU XP VISA_INFINITIVE","Cartão Itaú XP Visa Infinitive"),
        ("CARTAO MERCADO PAGO VISA","Cartão Mercado Pago"),
        ("CONTA CORRENTE ITAU AG8584CC285855","Conta Corrente Itaú AG8584 CC285855"),
    ]

    # OPCOES_CONSOLIDADO = [
    #     ("DESPESA",True),
    #     ("RECEITA",False),
    # ]

    consolidado = models.BooleanField(default=False)
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    competencia = models.CharField(max_length=1000, choices=OPCOES_COMPETENCIA, default='')
    vencimento = models.CharField(max_length=1000, choices=OPCOES_VENCIMENTO, default='')
    parcela = models.IntegerField(null=False, default=1)
    total_parcela = models.IntegerField(null=False, default=1)    
    tipo = models.CharField(max_length=1000, choices=OPCOES_TIPO, default='')
    tipo_categoria = models.CharField(max_length=1000, choices=OPCOES_TIPO_CATEGORIA, default='')
    centro_de_custo = models.CharField(max_length=1000, choices=OPCOES_CENTRO_DE_CUSTO, default='')
    origem_debito = models.CharField(max_length=1000, choices=OPCOES_ORIGEM_DEBITO, default='', blank=True)
    origem_credito = models.CharField(max_length=1000, default='', null=True, blank=True)
    valor = models.DecimalField(null=False, max_digits=10,decimal_places=2)
    observacao = models.TextField(default='', blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return f"Registro [nome={self.descricao}]"