import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('943.csv', encoding='latin1')

# Calcular el porcentaje total de cada servicio
total_usos = df['USOS'].sum()

# Obtener los 5 servicios más usados
top_10 = df.nlargest(5, 'USOS')

# Calcular el porcentaje total de los 10 servicios más usados
top_10['PORCENTAJE_TOTAL'] = (top_10['USOS'] / total_usos) * 100

# Crear el gráfico circular tipo donut con labels afuera y porcentaje adentro
fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(top_10['PORCENTAJE_TOTAL'], labels=top_10['SERVICIO'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.42), pctdistance=0.85)

# Ajustar el tamaño de fuente y color para los porcentajes de uso
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('white')

plt.title('Uso de servicios en los cajeros de la ciudad de Gijón - España (2022)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Mostrar el gráfico en una nueva ventana
plt.show()