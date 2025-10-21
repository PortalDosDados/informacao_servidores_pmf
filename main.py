# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('arquivos_originais/relacao_202401.csv',sep=';', encoding='UTF-8')

print(df.columns)
#print(df.head())