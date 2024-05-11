import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("dengue_features_train.csv")

# Seleccionar las columnas relevantes
df = df[['reanalysis_relative_humidity_percent', 'total_cases']]

# Eliminar filas con valores nulos en cualquiera de las columnas seleccionadas
df = df.dropna()

# Ordenar el DataFrame por humedad relativa
df = df.sort_values(by='reanalysis_relative_humidity_percent')

# Crear el gráfico de línea con suavizado
plt.figure(figsize=(10, 6))
sns.lineplot(x='reanalysis_relative_humidity_percent', y='total_cases', data=df, ci=None)

# Añadir etiquetas y título
plt.xlabel('Humedad Relativa (%)')
plt.ylabel('Número de Casos de Dengue')
plt.title('Tendencia de Casos de Dengue en Relación con la Humedad Relativa')

# Mostrar el gráfico
plt.grid(True)
plt.show()