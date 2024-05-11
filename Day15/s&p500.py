import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv("SPX.csv")

# Convertir la columna 'Date' a formato de fecha
df['Date'] = pd.to_datetime(df['Date'])

# Elegir un valor de referencia histórico en dólares (por ejemplo, el precio de cierre en la primera fecha)
reference_price = df.loc[0, 'Close']

# Calcular el precio en dólares para cada punto de índice
df['Price_in_USD'] = df['Close'] * (reference_price / df.loc[0, 'Close'])

# Definir una función para mostrar el valor de y al pasar el cursor sobre la gráfica
def show_price(event):
    if event.xdata is not None and event.ydata is not None:
        plt.clf()  # Limpiar la figura actual
        y = event.ydata
        plt.plot(df['Date'], df['Price_in_USD'], color='blue')  # Graficar la serie nuevamente
        plt.title('Historico del precio de cierre del S&P 500 (1927-2020)', fontsize=14, pad=20)
        plt.xlabel('Fechas', fontsize=12)
        plt.ylabel('Precio de Cierre en USD', fontsize=12)
        plt.text(event.xdata, event.ydata, f'${y:.2f}', ha='center', va='top', color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
        plt.grid(True)
        plt.draw()

# Graficar el precio en dólares a lo largo del tiempo
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Price_in_USD'], color='blue')

# Conectar el evento de mover el cursor sobre la gráfica con la función show_price
plt.connect('motion_notify_event', show_price)

plt.title('Historico del precio de cierre del S&P 500 (1927-2020)', fontsize=14, pad=20)

plt.grid(True)

plt.tight_layout()
plt.show()
