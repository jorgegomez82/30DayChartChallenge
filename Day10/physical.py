import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('Revised_Players22.csv')

# Tomar solo los primeros 10 jugadores
df = df.head(10)

# Seleccionar las columnas necesarias
jugadores = df['short_name']
alturas = df['height_cm']

# Generar una paleta de colores única para cada jugador
num_jugadores = len(jugadores)
colormap = plt.cm.get_cmap('tab10', num_jugadores)  # 'tab10' es un mapa de colores predefinido
colores = [colormap(i) for i in range(num_jugadores)]

# Graficar
plt.figure(figsize=(10, 6))
bars = plt.bar(jugadores, alturas, color=colores)
plt.title('Alturas de los jugadores en la World Cup 2022 - Qatar')
plt.xlabel('Jugador')
plt.ylabel('Altura (cm)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar etiquetas dentro de las barras
for bar, altura in zip(bars, alturas):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(altura), ha='center', va='bottom')

# Mostrar la gráfica
plt.tight_layout()
plt.show()