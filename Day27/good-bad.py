import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('WHR2024.csv')

# Ordenar los países por su índice de felicidad de menor a mayor
df_sorted = df.sort_values(by='Ladder score')

# Tomar los 5 peores países y los 5 mejores países
peores_paises = df_sorted.head(5)
mejores_paises = df_sorted.tail(5)

# Concatenar los dataframes de los peores y mejores países
top_y_bottom = pd.concat([peores_paises, mejores_paises])

# Crear un gráfico de barras para visualizar los 5 peores y 5 mejores países
plt.figure(figsize=(10, 6))
bars = plt.bar(top_y_bottom['Country name'], top_y_bottom['Ladder score'], color=['red']*5 + ['green']*5)

# Agregar los valores de los índices encima de las barras
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), round(bar.get_height(), 2),
             ha='center', va='bottom', fontsize=8, color='black')

# Agregar leyenda
plt.legend(handles=[plt.Rectangle((0,0),1,1, color='red', ec="k"), 
                    plt.Rectangle((0,0),1,1, color='green', ec="k")],
           labels=['Índice de felicidad bajo', 'Índice de felicidad alto'])

plt.title('Índice de Felicidad 2024')
plt.xlabel('Países')
plt.ylabel('Índice de Felicidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
