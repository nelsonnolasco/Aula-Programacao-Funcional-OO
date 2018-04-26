# -*- coding: utf-8 -*-
"""
Spyder Editor
Funcional e OO
Data Science com Pandas
Nelson de Campos Nolasco
Este é um arquivo de script temporário.
"""
import pandas as pd

pnad = pd.read_csv("https://raw.githubusercontent.com/neylsoncrepalde/introducao_ao_python/master/pes_2012.csv")

pnad.shape
pnad.columns

pnad.head()

pnad["V8005"].dtype
pnad["V0302"]
pnad["V4720"]

# Estudando a idade
pnad["V8005"].describe().round()


pnad["V8005"].mean()
pnad["V8005"].var()
pnad.describe()

pnad.head()
pnad["V0302"].value_counts()

tab_sexo = pd.crosstab(index = pnad["V8005"], columns =["count"])

print("Distibuição da Frequencia - Sexo" + "\n")
print(tab_sexo)

print("Porcentagens - sexo" +"\n")
print((tab_sexo / tab_sexo.sum()) * 100)

#Estudando a variável raça
tab_cor = pnad["V0404"].value_counts()
print("Distribuição de frequencia - cor" + "\n")
print(tab_cor)

print("Porcentagens - cor" +"\n")
print( (tab_cor / tab_cor.sum())*100)


#Cruzando variaveis - sexo X cor
sexo_cor = pd.crosstab(index = pnad["V0404"], columns = pnad["V0302"])
print(sexo_cor)


### Estudando a renda
pnad.columns

renda = pnad["V4720"]

renda = list(renda)
type(renda)
