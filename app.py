import pandas as pd
import numpy
import openpyxl
import nbformat
import ipykernel
import plotly.express as px


# Passo a passo do projeto
# Passo 1: Importar a base de ddados de Clientes
# Passo 2: Visualizar a base de dados
# Passo 3: Corrigir os problemas da base de dados
# Passo 4: Analise dos cancelamentos
# Passo 5: Analise da causa do cancelamento
# Passo 6: Analise dos dados de entrada

tabela = pd.read_csv("cancelamentos.csv")
# print(tabela)
tabela = tabela.drop(columns="CustomerID")
tabela = tabela.dropna()
# print(tabela.info())


# Passo 4: Analise dos cancelamentos
tabela["cancelou"].value_counts()
print(tabela["cancelou"].value_counts())
# print(tabela["cancelou"].value_counts(normalize=True))
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))


# Passo 5: Analise da causa do cancelamento
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x='idade', color='cancelou')
    grafico.show()


# Passo 6: Analise dos dados de entrada
tabela = tabela[tabela["duracao_contrato"]!= "Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts(normalize=True))
