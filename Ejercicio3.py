import pandas as pd
import matplotlib.pyplot as plt

url = 'Dataset/Casos_positivos_de_COVID-19_01_06_2022.csv'
data = pd.read_csv(url)

# Eliminar columnas de un dataset
data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

#Lista de municipios afectados (sin repetirlos)
municipios = data['Nombre municipio'].unique()
print('municipios afectados: \n' + str(municipios))