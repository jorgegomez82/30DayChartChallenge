import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('ai-performance-knowledge-tests-vs-training-computation.csv')

# Ordenar los datos por MMLU avg para una mejor visualización
df_sorted = df.sort_values(by='MMLU avg', ascending=False)

# Crear el gráfico de puntos
plt.figure(figsize=(10, 6))
plt.plot(df_sorted['Entity'], df_sorted['MMLU avg'], marker='o', linestyle='None', color='black')

# Agregar etiquetas y título
plt.xlabel('Modelos de lenguaje')
plt.ylabel('MMLU avg')
plt.title('Medición de la comprensión masiva del lenguaje multitarea (MMLU)')

# Mostrar el gráfico
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar etiquetas a cada punto
for x, y, label in zip(df_sorted['Entity'], df_sorted['MMLU avg'], df_sorted['MMLU avg']):
    plt.annotate(f'{label:.2f}%', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()
