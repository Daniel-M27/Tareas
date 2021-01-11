import numpy as np
import matplotlib.pyplot as plt

m = float(input("Pendiente: "))
b = float(input("Intersección con eje Y: "))
inf = float(input("Límite izquierdo: "))
sup = float(input("Límite derecho: "))
# Pedimos al usuario los parámetros necesarios para una función de la forma
# f(x) = mx + b, así como el intervalo a graficar.

x = np.linspace(inf, sup)
# Generamos un rango uniforme de valores para x entre los límites especificados.
y = m * x + b
# Valores y correspondientes.
lenght = range(len(x))

with open('lineales.csv', 'w') as f:
    f.write('X,Y\n')
    f.write('\n'.join('{},{}'.format(x[i], y[i]) for i in lenght))
# Guardamos los pares (x,y) en un archivo, un par por renglón. De esta forma
# obtenemos una columna para 'x' y otra para 'y'.

plt.plot(x, y)
# Graficamos x vs y.

plt.xlabel("x")
plt.ylabel("mx + b")
plt.title("Función lineal")
# Etiquetas.

plt.tight_layout()

plt.show()
# Mostramos la gráfica
