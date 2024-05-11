import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('DATAGESADOLESCENTEENERO2024_0.csv', encoding='latin1')

# Sumar el total de adolescentes gestantes por rango de edad
data['Total'] = data['G_AD_9_11'] + data['G_AD_12_17'] + data['G_AD_18']

# Agrupar por distrito y calcular el total de adolescentes gestantes
total_por_distrito = data.groupby('DISTRITO')['Total'].sum().sort_values(ascending=False)

# Filtrar los distritos con las mayores cantidades
mayores_cantidades = total_por_distrito[total_por_distrito >= total_por_distrito.quantile(0.75)]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
bars = mayores_cantidades.plot(kind='bar', color='skyblue')
plt.title('Distritos con las Mayores Cantidades de Adolescentes Gestantes en la Región de Piura - Perú 2024')
plt.xlabel('Distrito')
plt.ylabel('Total de Adolescentes Gestantes')
plt.xticks(rotation=45, ha='right')

# Agregar etiquetas dentro de las barras
for bar in bars.patches:
    # Obtener el valor de la barra
    height = bar.get_height()
    # Colocar el valor como etiqueta dentro de la barra
    plt.text(bar.get_x() + bar.get_width() / 2, height / 2, '%d' % int(height),
             ha='center', va='center', color='black')

plt.tight_layout()
plt.show()