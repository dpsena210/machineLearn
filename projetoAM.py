"""
Aprendendo a usar Pandas
"""
import pandas as pd
import numpy as np

df = pd.read_csv('bike_buyers_clean_i_Educ_NoOcp_NoRegion1.csv')
df0 = pd.read_csv('bike_buyers_clean_i.csv')
#mostrar um determinado número de linhas ex 10 linhas
#print(dataframe.head(10))

#pegar as colunas
#print(df.columns)

#transforma em array
#print(df.to_numpy())

#principais métricas
#print(df.describe())

#filtrando por colunas
#print(df["Gender"])

#filtrando por indice da linha
#print(df[1:10])

#filtro loc com label, 1º param linha, segundo coluna
#print(df.loc[:,["Gender","Children"]])

#filtro iloc para index: linha de 0 a 10, linha de 2 a 5
# print(df.iloc[0:10,2:5])



#print(df.loc[0:50,"Marital Status"])
#df2 = df.drop(columns=['Unnamed: 0.2' ])
#print(df2.loc[0:60,"Occupation"])

#df.to_csv('C:\\Users\\danrl\\PycharmProjects\\machineHead\\bike_buyers_clean_i_Educ_NoOcp_NoRegion3.csv',index = True)

"""def validacao_conversao_binaria(coluna,possibilidade0):
    for index in df.index:
        val = 0
        if df.loc[index, coluna] == 0:
            if df2.loc[index, coluna] == possibilidade0:
                print("correto o ", df2.loc[index, coluna], " corresponde ao ", df.loc[index, coluna])
            else:
                print("esta errado aq")

        else:
            print("correto o ", df2.loc[index, coluna], " corresponde ao ", df.loc[index, coluna])
"""


def validacaoMultiplosValores(coluna):
    for index in df.index:
        if df.loc[index,coluna] == 1:
            if df0.loc[index,coluna] == 'Partial High School':
                pass
            else:
                print("nao bateu: ",df.loc[index,coluna], " : ", df0.loc[index,coluna])
                break
        elif df.loc[index,coluna] == 2:
            if df0.loc[index, coluna] == 'High School':
                pass
            else:
                print("nao bateu: ", df.loc[index, coluna], " : ", df0.loc[index, coluna])
                break
        elif df.loc[index,coluna] == 3:
            if df0.loc[index, coluna] == 'Partial College':
                pass
            else:
                print("nao bateu: ", df.loc[index, coluna], " : ", df0.loc[index, coluna])
                break

        elif df.loc[index, coluna] == 4:
            if df0.loc[index, coluna] == 'Bachelors':
                pass
            else:
                print("nao bateu: ", df.loc[index, coluna], " : ", df0.loc[index, coluna])
                break
        elif df.loc[index, coluna] == 5:
            if df0.loc[index, coluna] == 'Graduate Degree':
                pass
            else:
                print("nao bateu: ", df.loc[index, coluna], " : ", df0.loc[index, coluna])
                break
        else:
            print("passou um sem nada aq")
            break
        if index == 999:
            print("SUCESSO, TUDO CORRETO!")