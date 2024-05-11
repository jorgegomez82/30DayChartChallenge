import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('programming_language_trend_over_time.csv')

# Convertir la columna 'Week' a tipo datetime y extraer el año
df['Week'] = pd.to_datetime(df['Week'])
df['Year'] = df['Week'].dt.year

# Calcular el total de usuarios por fecha
df['Total'] = df['Python'] + df['Java'] + df['C++']

# Calcular el porcentaje de usuarios para cada lenguaje en cada fecha
df['Python_pct'] = (df['Python'] / df['Total']) * 100
df['Java_pct'] = (df['Java'] / df['Total']) * 100
df['C++_pct'] = (df['C++'] / df['Total']) * 100

# Calcular el promedio de los porcentajes para cada lenguaje por año
mean_by_year = df.groupby('Year')[['Python_pct', 'Java_pct', 'C++_pct']].mean().reset_index()

# Crear un gráfico de líneas para visualizar la tendencia por año para cada lenguaje de programación
plt.figure(figsize=(10, 6))

plt.plot(mean_by_year['Year'], mean_by_year['Python_pct'], marker='o', label='Python')
plt.plot(mean_by_year['Year'], mean_by_year['Java_pct'], marker='o', label='Java')
plt.plot(mean_by_year['Year'], mean_by_year['C++_pct'], marker='o', label='C++')

# Agregar etiquetas flotantes para mostrar los valores exactos en cada punto
for i, year in enumerate(mean_by_year['Year']):
    plt.annotate(f'{mean_by_year.iloc[i]["Python_pct"]:.2f}%', (year, mean_by_year.iloc[i]['Python_pct']), textcoords="offset points", xytext=(0,10), ha='center')

for i, year in enumerate(mean_by_year['Year']):
    plt.annotate(f'{mean_by_year.iloc[i]["Java_pct"]:.2f}%', (year, mean_by_year.iloc[i]['Java_pct']), textcoords="offset points", xytext=(0,10), ha='center')

for i, year in enumerate(mean_by_year['Year']):
    plt.annotate(f'{mean_by_year.iloc[i]["C++_pct"]:.2f}%', (year, mean_by_year.iloc[i]['C++_pct']), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Tendencia en las preferencias de Lenguajes de Programación 2019-2024')
plt.xlabel('Año')
plt.ylabel('Porcentaje de Usuarios')
plt.xticks(mean_by_year['Year'])
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
