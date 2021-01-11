import numpy as np
import matplotlib.pyplot as plt

def floats(str):
    return list(map(float, str.split()))

vert = floats(input("Ingrese el vértice (h,k) como h k:  "))
c = float(input("Distancia del foco al vértice: "))
if c == 0:
    print("La distancia debe ser distinta de cero.")
    exit()
# Parámetros de la ecuación cuadrática.
h = vert[0]
k = vert[1]

inf = float(input("Límite izquierdo: "))
sup = float(input("Límite derecho: "))
# Límites del intervalo a graficar.

x = np.linspace(inf, sup)
y = (x - h) ** 2 / (4 * c) + k
lenght = range(len(x))
# Si se introduce un intervalo con inf > sup, las x se graficarán en el
# intervalo [sup, inf]

with open('cuadrados.csv', 'w') as f:
    f.write('X,Y\n')
    f.write('\n'.join('{},{}'.format(x[i], y[i]) for i in lenght))

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = (1/4c)(x - h)² + k')

plt.tight_layout()

plt.show()
