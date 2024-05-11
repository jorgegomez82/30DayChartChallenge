import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos desde el archivo CSV
df = pd.read_csv('fertility_rate.csv', encoding='utf-8')

# Seleccionar datos de Perú y España y filtrar por años 2010-2020
peru_data = df[df['Country'] == 'Peru'].iloc[0, -11:]
spain_data = df[df['Country'] == 'Spain'].iloc[0, -11:]
years = df.columns[-11:]

# Redondear años para evitar decimales en el eje X
years_rounded = [int(round(float(year))) for year in years]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(years_rounded, peru_data, marker='o', color='b', linestyle='-', label='Perú')
plt.plot(years_rounded, spain_data, marker='o', color='r', linestyle='-', label='España')
plt.title('Tasa de Fertilidad en Perú y España (2010-2020)')
plt.xlabel('Año')
plt.ylabel('Tasa de Fertilidad')
plt.grid(True)
plt.legend()

# Leyenda breve
legend_text = "Tasa de fertilidad de 2 hijos por mujer: población estable."
plt.figtext(0.5, 0.01, legend_text, wrap=True, horizontalalignment='center', fontsize=10)

plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mayor legibilidad
plt.tight_layout()
plt.show()