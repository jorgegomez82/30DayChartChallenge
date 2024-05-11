import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset desde el archivo CSV
# Dataset Source : https://www.kaggle.com/datasets/anshtanwar/metro-interstate-traffic-volume

df = pd.read_csv('Metro_Interstate_Traffic_Volume.csv')

# Convertir la columna 'date_time' a tipo datetime
df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')

# Filtrar por el año 2018
df_2018 = df[df['date_time'].dt.year == 2018]

# Reemplazar los valores nulos con una cadena vacía
df_2018['date_time'] = df_2018['date_time'].fillna('')

# Convertir el formato de fecha para los datos que contienen hora
df_2018['date_time'] = df_2018['date_time'].apply(lambda x: x.strftime('%d-%m-%Y') if isinstance(x, pd.Timestamp) else x)

# Convertir la columna 'date_time' a tipo datetime sin la hora
df_2018['date_time'] = pd.to_datetime(df_2018['date_time'], errors='coerce')

# Agregar una nueva columna 'month' para el mes
df_2018['month'] = df_2018['date_time'].dt.month

# Mapear los números de mes a sus nombres
month_names = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
               7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
df_2018['month'] = df_2018['month'].map(month_names)

# Calcular el promedio del volumen de tráfico por mes
avg_traffic_by_month = df_2018.groupby('month')['traffic_volume'].mean()

# Lista de colores para cada barra
colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow']

# Crear el gráfico
plt.figure(figsize=(10, 6))
bars = avg_traffic_by_month.plot(kind='bar', color=colors, label='Volumen de Tráfico Promedio')

# Agregar los valores dentro de las barras y redondearlos
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 50, 
             f"{round(bar.get_height())}",  # Redondear el valor y convertirlo a cadena
             ha='center', va='bottom')

plt.title('Promedio de Volumen de Tráfico Mensual en la Autopista I-94 (2018) - Minneapolis y St Paul, Minnesota - USA')
plt.xlabel('Mes')
plt.ylabel('Volumen de Tráfico Promedio')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()