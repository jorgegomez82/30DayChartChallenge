import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el nuevo conjunto de datos
data = pd.read_csv("dinosaur.csv")

# Convertir los subtipos de período geológico a un período principal
period_mappings = {
    "Triassic": ["Triassic", "Triassic/Jurassic", "Triassic or Jurassic"],
    "Jurassic": ["Jurassic", "Early Jurassic", "Late Jurassic", "Middle Jurassic", "Jurassic/Cretaceous"],
    "Cretaceous": ["Cretaceous", "Early Cretaceous", "Early-Late Cretaceous", "Late Cretaceous"]
}

# Límites de tiempo en millones de años para cada período geológico (ejemplo)
time_limits = {
    "Triassic": (252, 201),
    "Jurassic": (201, 145),
    "Cretaceous": (145, 66)
}

# Calcular la cantidad de dinosaurios en cada período
period_counts = data['Period'].value_counts()
total_dinosaurs = period_counts.sum()

# Calcular el porcentaje de dinosaurios en cada período
period_percentages = {}
for main_period, sub_periods in period_mappings.items():
    period_percentages[main_period] = sum(period_counts.get(sub_period, 0) for sub_period in sub_periods) / total_dinosaurs * 100

# Crear el gráfico de línea de tiempo con columnas y curva de porcentaje
plt.figure(figsize=(12, 6))

# Barras verticales para los porcentajes
for i, (period, percentage) in enumerate(period_percentages.items()):
    bar_color = 'blue' if period == "Cretaceous" else 'green' if period == "Jurassic" else 'orange'
    plt.bar(i, percentage, color=bar_color)
    plt.text(i, percentage, f'{percentage:.2f}%', ha='center', va='bottom', fontsize=8)

    # Agregar etiquetas dentro de las barras
    plt.text(i, percentage / 2, period, ha='center', va='center', color='white', fontsize=10)

# Crear una curva suavizada que pase a través de los puntos de porcentaje
x = np.arange(len(period_percentages))
y = list(period_percentages.values())
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
x_new = np.linspace(x.min(), x.max(), 300)
y_smooth = p(x_new)

# Trazar la curva suavizada
plt.plot(x_new, y_smooth, color='red', linestyle='-')

# Etiquetas de los períodos
plt.xticks(range(len(period_percentages)), period_percentages.keys())

# Cambiar las etiquetas del eje X para que representen la línea de tiempo en millones de años
plt.gca().set_xticklabels([f'{time_limits[period][0]} - {time_limits[period][1]}' for period in period_percentages.keys()])

# Etiqueta del eje Y
plt.ylabel('Porcentaje de dinosaurios')

# Título del gráfico
plt.title('Porcentaje de dinosaurios por período geológico')

# Agregar una etiqueta debajo del eje X
plt.xlabel('Periodo de tiempo en Mill de años')

# Mostrar el gráfico
plt.grid(True)
plt.show()
