import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Lee los datos desde un archivo CSV
df = pd.read_csv('accidents_transito.csv', encoding='latin1', delimiter=';')

# Agrupa los datos por modalidad de accidente y calcula el recuento
df_modalidad = df.groupby('MODALIDAD').size().reset_index(name='COUNT')

# Filtrar las modalidades que tienen recuento mayor que cero
df_filtrado = df_modalidad[df_modalidad['COUNT'] > 0]

# Calcular el porcentaje de cada modalidad en relación con el total de accidentes
total_accidentes = df_filtrado['COUNT'].sum()
df_filtrado['PORCENTAJE'] = df_filtrado['COUNT'] / total_accidentes * 100

# Crear el gráfico de Waffle
fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    columns=10,
    values=df_filtrado['COUNT'],  # Utilizar el recuento de cada modalidad como valores
    labels=[f"{row['MODALIDAD']} ({row['PORCENTAJE']:.1f}%)" for index, row in df_filtrado.iterrows()],  # Agregar el porcentaje a las etiquetas
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'title': 'Modalidades'}  # Ubicación y título de la leyenda
)

plt.title('Proporción Accidentes de tránsito en carreteras 2020 a 2021 en Perú')
plt.show()