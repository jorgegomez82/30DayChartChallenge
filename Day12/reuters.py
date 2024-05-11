import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('data_crimenes.csv', encoding='latin1')

# Convertir los datos en listas
modalidades = df['Modalidad'].tolist()
# Agregar un salto de línea en las modalidades
modalidades = [modalidad.replace(' ', '\n') for modalidad in modalidades]
tasas_por_cien = [(tasa * 100) for tasa in df['Tasa(%)'].tolist()]  # Convertir las tasas a tasas por cada 100 habitantes

# Colores
colors = ['#569ED3', '#F68E26']

# Crear gráfico de barras verticales
plt.figure(figsize=(10, 15))
bars = plt.bar(modalidades, tasas_por_cien, color=colors[0])

# Configurar colores específicos para cada barra
for i in range(len(bars)):
    bars[i].set_color(colors[i % len(colors)])

# Agregar etiquetas de datos a las barras (tasa por cada 100 habitantes)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, str(int(yval)), ha='center', va='bottom')

# Configuraciones adicionales
plt.xlabel('Modalidad')
plt.ylabel('Cantidad (por cada 100 habitantes)')
plt.title('Crímenes con mayor tasa de víctimas en áreas urbanas de Perú entre julio y diciembre del 2023')
plt.xticks(rotation=90)
plt.tight_layout()

# Crear una sola leyenda combinando ambos colores
legend_elements = [Patch(facecolor=colors[0], edgecolor='black'),
                   Patch(facecolor=colors[1], edgecolor='black')]

# Agregar leyenda personalizada
plt.legend(handles=legend_elements, loc='upper right', title='Colores')

# Ajustar márgenes para agregar espacio en la parte superior
plt.subplots_adjust(top=0.9)

# Agregar texto adicional
plt.text(0.5, -0.55, 'Fuente: Sans Serif Colores utilizados: #569ED3 | #F68E26 - Basado en Reuters Graphic',
         horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

# Mostrar el gráfico
plt.show()
