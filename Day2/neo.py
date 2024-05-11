import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde un archivo CSV
data = pd.read_csv('DataSetPlantaciones.csv', sep=';', encoding='latin1')

# Contar la frecuencia de cada especie
especies_frecuencia = data['ESPECIE'].value_counts()

# Seleccionar las 10 especies más comunes
top_10_especies = especies_frecuencia.head(10)

# Establecer el estilo
plt.style.use("seaborn-v0_8")

# Crear el gráfico de barras
plt.figure(figsize=(12, 8))
ax = sns.barplot(x=top_10_especies.index, y=top_10_especies.values, palette='viridis')
plt.title('Las 10 Especies de Árboles más Comunes Plantadas según la Normativa Forestal Peruana', fontsize=16, fontweight='bold')
plt.xlabel('Especie', fontsize=12, fontweight='bold')
plt.ylabel('Frecuencia', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Establecer el límite máximo en el eje y
plt.ylim(0, 3000)

# Agregar etiquetas con la cantidad de especies plantadas
for i, v in enumerate(top_10_especies):
    ax.text(i, v + 50, str(v), ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()
