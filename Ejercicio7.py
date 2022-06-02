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

# Agrupar por columnas los resultados
data['Estado'].value_counts()

# Normalizar la columna de Estado
data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

#Normalizar la columna de nombre departamento
data.loc[data['Nombre departamento'] == 'Santander', 'Nombre departamento'] = 'SANTANDER'

data['Tipo de contagio'].value_counts()

data.rename(columns={'ID de caso': 'ID'}, inplace=True)
#Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
tipos_casos = data.groupby('Tipo de contagio').count()
print(tipos_casos['ID'].sort_values(ascending=False))