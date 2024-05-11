import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
df = pd.read_csv('co2_emissions_kt_by_country.csv')

# Filtrar los datos solo para Perú
peru_data = df[df['country_code'] == 'PER']

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(peru_data['year'], peru_data['value'], marker='o', linestyle='-')
plt.title('Emisiones de CO2 en Perú (1960-2019)')
plt.xlabel('Año')
plt.ylabel('Emisiones de CO2 (kt)')
plt.grid(True)
plt.xticks(range(1960, 2021, 5))  # Colocar marcas en el eje x cada 5 años
plt.tight_layout()
plt.show()