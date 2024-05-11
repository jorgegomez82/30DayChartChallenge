import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo CSV
df = pd.read_csv('DailyDelhiClimate.csv')

# Convertir la columna 'date' al formato datetime
df['date'] = pd.to_datetime(df['date'])

# Filtrar datos para el año 2016
df_2016 = df[df['date'].dt.year == 2016]

# Crear columnas para las temperaturas máximas y mínimas
df_2016['temp_max'] = df_2016['meantemp']
df_2016['temp_min'] = df_2016['meantemp']

# Comparar 'meantemp' con las temperaturas máximas y mínimas
df_2016.loc[df_2016['meantemp'] > df_2016['temp_max'], 'temp_max'] = df_2016['meantemp']
df_2016.loc[df_2016['meantemp'] < df_2016['temp_min'], 'temp_min'] = df_2016['meantemp']

# Crear matrices de datos para temperaturas máximas y mínimas
heatmap_max = df_2016.pivot_table(values='temp_max', index=df_2016['date'].dt.month, columns=df_2016['date'].dt.day, aggfunc='mean')
heatmap_min = df_2016.pivot_table(values='temp_min', index=df_2016['date'].dt.month, columns=df_2016['date'].dt.day, aggfunc='mean')

# Crear heatmap para temperaturas máximas
plt.figure(figsize=(10, 6))
plt.imshow(heatmap_max, cmap='coolwarm', aspect='auto', interpolation='nearest', vmin=15, vmax=35)
plt.colorbar(label='Temperatura Máxima (°C)')
plt.title('Heatmap de Temperaturas Máximas en Delhi, India - 2016')
plt.xlabel('Día del Mes')
plt.ylabel('Mes')
plt.xticks(range(0, 31, 5), ['1', '6', '11', '16', '21', '26', '31'])
plt.yticks(range(12), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])

plt.tight_layout()
plt.show()