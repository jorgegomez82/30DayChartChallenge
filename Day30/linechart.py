import pandas as pd
import matplotlib.pyplot as plt

# Estilo
plt.style.use('fivethirtyeight')

# Cargar el archivo CSV
df = pd.read_csv('covid_approval_polls.csv')

# Filtrar los datos solo para Joe Biden y fechas desde 2022-01-01 hasta 2022-11-22
df_biden = df[(df['subject'] == 'Biden') & (df['start_date'] >= '2022-01-01') & (df['end_date'] <= '2022-11-22')]

# Convertir las fechas al formato datetime
df_biden['start_date'] = pd.to_datetime(df_biden['start_date'], errors='coerce')

# Eliminar filas con fechas incorrectas
df_biden = df_biden.dropna(subset=['start_date'])

# Extraer el mes de la fecha
df_biden['month'] = df_biden['start_date'].dt.to_period('M')

# Calcular la media de las tasas de aprobación y desaprobación por mes para el año 2022
df_monthly_mean = df_biden.groupby('month')[['approve', 'disapprove']].mean().reset_index()

# Convertir los objetos Period a cadenas de texto
df_monthly_mean['month'] = df_monthly_mean['month'].astype(str)

# Crear el gráfico de línea
plt.figure(figsize=(10, 6))
plt.plot(df_monthly_mean['month'], df_monthly_mean['approve'], label='Approve', marker='o')
plt.plot(df_monthly_mean['month'], df_monthly_mean['disapprove'], label='Disapprove', marker='x')

# Configurar etiquetas y título
plt.xlabel('Mes')
plt.ylabel('Porcentaje')
plt.title('Cómo ven los estadounidenses la respuesta de Biden a la crisis del coronavirus')

# Rotar las etiquetas del eje x para mejorar la legibilidad
plt.xticks(rotation=45)

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
