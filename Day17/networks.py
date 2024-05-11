import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel("submarcas.xlsx")

# Crear un gráfico de red
G = nx.from_pandas_edgelist(df, source="Empresa", target="Submarca")

# Dibujar el gráfico de red
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Calcula las posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("Red de Sub-marcas de Microsoft")  # Establecer el título antes de mostrar el gráfico
plt.show()
