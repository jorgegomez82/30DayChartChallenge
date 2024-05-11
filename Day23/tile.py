import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
data = pd.read_csv('ENPOVE 2022_V_300.csv')

# Convertir la columna 'P303_ANIO' a tipo numérico
data['P303_ANIO'] = pd.to_numeric(data['P303_ANIO'], errors='coerce')

# Calcular la afluencia de migrantes por departamento a lo largo de los años
afluencia_por_departamento = data.groupby(['DEPARTAMENTO', 'P303_ANIO']).size().unstack(fill_value=0)

# Determinar el número de filas y columnas para organizar los paneles en el gráfico Tile
num_departamentos = len(afluencia_por_departamento)
num_columnas = 3  # Número de columnas para organizar los paneles
num_filas = -(-num_departamentos // num_columnas)  # Redondeo hacia arriba de la división

# Crear el gráfico Tile
fig, axs = plt.subplots(num_filas, num_columnas, figsize=(15, num_filas*5))

# Recorrer cada departamento y crear el panel correspondiente
for i, (departamento, afluencia) in enumerate(afluencia_por_departamento.iterrows()):
    ax = axs[i // num_columnas, i % num_columnas] if num_filas > 1 else axs[i % num_columnas]
    ax.plot(afluencia.index, afluencia.values, marker='o', linestyle='-', color='skyblue')
    ax.set_title(departamento)
    ax.set_xlabel('Año')
    ax.set_ylabel('Número de Migrantes')
    ax.grid(True)

# Añadir título general
plt.suptitle('Proporción de migrantes Venezolanos por departamento Perú 1995-2020')

# Ajustar el espaciado entre los subplots
plt.tight_layout()
plt.show()
