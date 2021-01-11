import numpy as np
import matplotlib.pyplot as plt

def floats(str):
    return list(map(float, str.split()))

vel = float(input("Velocidad(m/s): "))
init = float(input("Posición inicial: "))
# Parámetros necesarios.

interval = floats(input("Ingrese el intervalo [t0, tf] (s) como t0 tf: "))
t0 = interval[0]
tf = interval[1]

if t0 < 0 or tf < 0:
    print("Ingrese tiempos válidos.")
    exit()
# Parámetros necesarios para las ecuaciones de movimiento. El tiempo debe ser
# no negativo (a menos que seas hackerman o.O)

t = np.linspace(t0, tf)
lenght = range(len(t))
# Intervalo a graficar.

pos = vel * t + init
v = np.array([vel for i in lenght])
a = np.array([0 for i in lenght])
# Desplazamiento, velocidad y aceleración en movimiento rectilíneo uniforme.

with open('uniform.csv', 'w') as f:
    f.write('Tiempo,Posición,Velocidad,Aceleración\n')
    f.write('\n'.join('{},{},{},0'.format(t[i], pos[i], vel) for i in lenght))
# Datos del movimient, separados por columnas.

plt.plot(t, pos, color='#222288', label='Posición(m)')
plt.plot(t, v, color='#ffd700', linestyle='-.', label='Velocidad(m/s)')
plt.plot(t, a, color='#329932', linestyle='--', label='Aceleración(m/s²)')
# Gráficas del movimiento respecto al tiempo.

plt.xlabel("Tiempo")
plt.ylabel("Unidades respectivas")
plt.title("Movimiento Rectilíneo Uniforme")

plt.legend()
plt.tight_layout()

plt.show()

