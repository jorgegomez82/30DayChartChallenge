import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('dengue_features_train.csv')

# Separar los datos por ciudad
df_iq = df[df['city'] == 'iq']
df_sj = df[df['city'] == 'sj']

# Agrupar por año y calcular el promedio de la humedad relativa y la suma total de casos de dengue
df_grouped_iq = df_iq.groupby('year').agg({'reanalysis_relative_humidity_percent': 'mean', 'total_cases': 'sum'}).reset_index()
df_grouped_sj = df_sj.groupby('year').agg({'reanalysis_relative_humidity_percent': 'mean', 'total_cases': 'sum'}).reset_index()

# Convertir la columna 'year' a enteros
df_iq['year'] = df_iq['year'].astype(int)
df_sj['year'] = df_sj['year'].astype(int)

# Crear el gráfico para la ciudad IQ
fig, ax = plt.subplots(figsize=(8, 6))

# Graficar la humedad relativa para la ciudad IQ
color = 'tab:blue'
ax.set_ylabel('Humedad Relativa (%)', color=color)
ax.plot(df_grouped_iq['year'], df_grouped_iq['reanalysis_relative_humidity_percent'], color=color, label='Humedad Relativa', linewidth=2)
ax.tick_params(axis='y', labelcolor=color)

# Crear el segundo eje y para los casos de dengue para la ciudad IQ
ax2 = ax.twinx()
color = 'tab:red'
ax2.set_ylabel('Total de casos de Dengue (Iquitos)', color=color)
ax2.plot(df_grouped_iq['year'], df_grouped_iq['total_cases'], color=color, label='Casos de Dengue', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)

# Añadir leyendas para la ciudad IQ
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')
ax.set_title('Ciudad Iquitos (Perú) - Total de casos de Dengue y Humedad Relativa por año', pad=20)

plt.tight_layout()
plt.show()

# Crear el gráfico para la ciudad SJ
fig2, ax3 = plt.subplots(figsize=(8, 6))

# Graficar la humedad relativa para la ciudad SJ
color = 'tab:blue'
ax3.set_xlabel('Año')
ax3.set_ylabel('Humedad Relativa (%)', color=color)
ax3.plot(df_grouped_sj['year'], df_grouped_sj['reanalysis_relative_humidity_percent'], color=color, label='Humedad Relativa', linewidth=2)
ax3.tick_params(axis='y', labelcolor=color)

# Crear el segundo eje y para los casos de dengue para la ciudad SJ
ax4 = ax3.twinx()
color = 'tab:red'
ax4.plot(df_grouped_sj['year'], df_grouped_sj['total_cases'], color=color, label='Casos de Dengue', linewidth=2)
ax4.tick_params(axis='y', labelcolor=color)

# Establecer el rango de años para las etiquetas del eje x
years_range = range(1990, 2009)
ax3.set_xticks(years_range)
ax3.set_xticklabels([str(year) for year in years_range])

# Añadir leyendas para la ciudad SJ
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()
ax4.legend(lines3 + lines4, labels3 + labels4, loc='upper left')
ax3.set_title('Ciudad San Juan (Puerto Rico) - Total de casos de Dengue y Humedad Relativa por año')

plt.tight_layout()
plt.show()
