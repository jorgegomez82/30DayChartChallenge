import pandas as pd
import matplotlib.pyplot as plt
import textwrap

def wordwrap(s, width):
    return textwrap.wrap(s, width)

# Cargar el conjunto de datos desde un archivo CSV
df = pd.read_csv("ADB_Climate_Change_Financing_2023.csv")

# Filtrar los datos para el año 2023
df_2023 = df[df["Date Signed"].str.endswith("23")]

# Calcular el total de financiamiento para mitigación y adaptación
total_mitigation = 6168  # millones de dólares
total_adaptation = 4578  # millones de dólares

# Calcular el total de financiamiento
total_financing = total_mitigation + total_adaptation

# Convertir las columnas de financiamiento a valores numéricos
df_2023["Mitigation Finance ($ million)"] = pd.to_numeric(df_2023["Mitigation Finance ($ million)"], errors='coerce')
df_2023["Adaptation Finance ($ million)"] = pd.to_numeric(df_2023["Adaptation Finance ($ million)"], errors='coerce')

# Calcular el porcentaje de financiamiento para cada sector
df_sector = df_2023.groupby("Sector")[["Mitigation Finance ($ million)", "Adaptation Finance ($ million)"]].sum().reset_index()
df_sector["Total Finance"] = df_sector["Mitigation Finance ($ million)"] + df_sector["Adaptation Finance ($ million)"]
df_sector["Percentage of Financing"] = df_sector["Total Finance"] / total_financing * 100

# Excluir los sectores con inversión de 0 millones de dólares
df_sector = df_sector[df_sector["Total Finance"] != 0]

# Definir colores para las columnas
colors = ['skyblue', 'lightgreen', 'orange', 'pink', 'lightblue', 'yellow', 'purple', 'red', 'green', 'blue']

# Graficar los datos
plt.figure(figsize=(12, 8))
bars = plt.bar(df_sector["Sector"], df_sector["Total Finance"], color=colors[:len(df_sector)], edgecolor='black')

plt.xlabel("Sector", fontsize=14)
plt.ylabel("Monto ($ millones)", fontsize=14)
plt.title("Financiamiento para reducir el cambio climático por sector en el ADB el año 2023", fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=10)

# Agregar saltos de línea en los nombres de los sectores largos
labels = [('\n'.join(wordwrap(w, 15))) for w in df_sector["Sector"]]
plt.xticks(range(len(labels)), labels)

# Agregar etiquetas con el monto invertido redondeado en millones de dólares
for bar, amount in zip(bars, df_sector["Total Finance"]):
    height = bar.get_height()
    rounded_amount = round(amount)
    plt.text(bar.get_x() + bar.get_width() / 2, height, f"${rounded_amount}M", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
