import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("EAR_4MTH_SEX_ECO_CUR_NB_A-filtered-2024-04-25.csv", parse_dates=['time'])

# Convertir la columna "time" a tipo datetime
df['time'] = pd.to_datetime(df['time'])

# Obtener los años únicos presentes en el conjunto de datos
years = df['time'].dt.year.unique()

# Crear una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Listas para almacenar los promedios de ganancias por género para cada año
male_averages_usd = []
female_averages_usd = []

# Calcular el promedio de ganancias por género para cada año
for year in years:
    # Filtrar datos para el año actual
    data_year = df[df['time'].dt.year == year]
    # Filtrar datos para hombres y mujeres con moneda en dólares estadounidenses
    male_data_usd = data_year[(data_year['sex.label'] == 'Sex: Male') & (data_year['classif2.label'] == 'Currency: U.S. dollars')]
    female_data_usd = data_year[(data_year['sex.label'] == 'Sex: Female') & (data_year['classif2.label'] == 'Currency: U.S. dollars')]
    # Calcular el promedio de ganancias para hombres y mujeres con moneda en dólares estadounidenses
    male_avg_usd = male_data_usd['obs_value'].mean()
    female_avg_usd = female_data_usd['obs_value'].mean()
    # Agregar los promedios a las listas
    male_averages_usd.append(male_avg_usd)
    female_averages_usd.append(female_avg_usd)

# Crear barras para hombres y mujeres con moneda en dólares estadounidenses
bars1 = ax.bar(years, male_averages_usd, width=0.4, align='center', label='Hombres (USD)', color='blue')
bars2 = ax.bar([x + 0.4 for x in years], female_averages_usd, width=0.4, align='center', label='Mujeres (USD)', color='pink')

# Función para agregar valores en las columnas
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                round(height, 2),
                ha='center', va='bottom')

# Llamar la función para agregar los valores en las columnas
add_value_labels(bars1)
add_value_labels(bars2)

# Etiquetas y título
ax.set_xlabel('Año')
ax.set_ylabel('Sueldo promedio (USD)')
ax.set_title('Remuneracion promedio de empleados por mes en Egipto 2018-2022')

# Mostrar el gráfico
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor visualización
plt.legend()
plt.tight_layout()  # Ajustar el diseño para evitar cortes
plt.show()
