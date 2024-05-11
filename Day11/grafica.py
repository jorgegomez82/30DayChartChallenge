import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('Final.csv')

# Filtrar solo los datos de Perú y desde el año 2000 hasta el 2020
peru_data = df[(df['Entity'] == 'Peru') & (df['Year'] >= 2000) & (df['Year'] <= 2020)]

# Calcular la cantidad de personas que usan Internet en Perú
peru_data['Internet Users'] = (peru_data['Internet Users(%)'] / 100) * 34e6  # 34 millones de personas

# Crear una lista de colores distintivos para las barras
colors = plt.cm.viridis_r(range(len(peru_data)))

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(peru_data['Year'], peru_data['Internet Users'], color=colors)

# Añadir una leyenda al lado del grafico
legend_labels = []

for year, internet_users, color in zip(peru_data['Year'], peru_data['Internet Users'], colors):

    legend_labels.append(f'{int(year)}: {int(internet_users):,}')

plt.legend(bars, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))

plt.title('Uso de Internet en Perú (2000-2020)')
plt.xlabel('Año')
plt.ylabel('Cantidad de Usuarios de Internet')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Quitar los ticks del eje y
plt.tick_params(axis='y', which='both', left=False, labelleft=False)

# Mostrar la gráfica
plt.show()
