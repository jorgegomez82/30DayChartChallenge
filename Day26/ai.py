import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset
df = pd.read_csv("scimagojr_country_rank_2021.csv")

# Seleccionar los países con más contribuciones
top_countries = df.nlargest(5, 'Documents')

# Crear una lista de colores distintos
colors = plt.cm.tab10(np.arange(len(top_countries)))

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(top_countries['Country'], top_countries['H index'], color=colors)

# Agregar la cantidad de contribuciones y el índice H en cada barra
for bar, documents, h_index in zip(bars, top_countries['Documents'], top_countries['H index']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{h_index}', ha='center', va='bottom')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 15, f'Docs: {documents}', ha='center', va='top', color='black', fontsize=8)

plt.xlabel('Países')
plt.ylabel('Índice H (Impacto)')
plt.title('Países con más contribuciones a la IA (2021)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para una mejor legibilidad
plt.tight_layout()  # Ajustar el diseño para evitar recortes en la visualización
plt.show()
