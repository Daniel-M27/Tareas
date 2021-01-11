import numpy as np
import matplotlib.pyplot as plt

def floats(str):
    return list(map(float, str.split()))

acc = float(input("Aceleración: "))
p_init = float(input("Posición inicial: "))
v_init = float(input("Velocidad Inicial: "))

interval = floats(input("Ingrese el intervalo [t0, tf] como t0 tf: "))
t0 = interval[0]
tf = interval[1]

if t0 < 0 or tf < 0:
    print("Ingrese tiempos válidos.")
    exit()

t = np.linspace(t0, tf)
lenght = range(len(t))

a = np.array([acc for i in lenght])
vel = acc * t + v_init
pos = acc * t ** 2 / 2 + v_init * t + p_init
# Aceleración, velocidad y desplazamiento en movimiento uniformemente acelerado.

with open('freefall.csv', 'w') as f:
    f.write('Tiempo,Posición,Velocidad,Aceleración\n')
    f.write('\n'.join('{},{},{},{}'.format(t[i], pos[i], vel[i], acc)
            for i in lenght))
# Datos del movimiento separados por columnas.

plt.plot(t, pos, color='#222288', label='Posición (m)')
plt.plot(t, vel, color='#ffd700', linestyle='-.', label='Velocidad (m/s)')
plt.plot(t, a, color='#329932', linestyle='--', label='Aceleración (m/s²)')
# Graficas del movimiento respecto al tiempo.

plt.xlabel("Tiempo")
plt.ylabel("Unidades respectivas")
plt.title("Movimiento Uniformemente Acelerado")

plt.legend()
plt.tight_layout()

plt.show()

fig.savefig('Acelerado.png')
