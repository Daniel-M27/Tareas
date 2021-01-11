import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

sin = np.sin
cos = np.cos

def floats(str):
    return list(map(float, str.split()))

v_init = float(input("Velocidad Inicial (m/s): "))
ang = float(input("Ángulo de disparo (radianes): "))

if v_init <= 0:
    print("Ingrese una velocidad válida para tiro parabólico.")
    exit()
# Parámetros iniciales.

vx0 = v_init * cos(ang)
# Velocidad inicial en X
vy0 = v_init * sin(ang)
# Velocidad inicial en Y

h_fin = input("""
Si la altura final supera a la inicial, especifíquela. \
De lo contrario, presione ENTER: """)

if h_fin != '':
    h_init = 0
    h_max = vy0 ** 2 / 19.62
    # Altura máxima del proyectil tomando la altura inicial como 0
    h_fin = float(h_fin)
    if h_fin > h_max:
        print(f"La altura final supera la altura máxima de {h_max} m.")
        exit()
else:
    h_init = float(input("\nIngrese la altura inicial(m): "))
    h_fin = 0
    h_max = vy0 ** 2 / 19.62 + h_init # Altura máxima.

# Básicamente, lo que se quiere hacer con este condicional es que el eje X de
# nuestro sistema de referencia coincida con el nivel de la altura más baja.
# La primera parte es el caso donde la altura final supera a la inicial, y la
# segunda parte es el caso contrario.

disc = vy0 ** 2 - 19.62 * (h_fin - h_init)
t_floor = (vy0 + sqrt(disc)) / 9.81
# Tiempo que tarda el proyectil en caer al piso.
reach = vx0 * t_floor
# Alcance horizontal del proyectil.

interval = floats(input(f"""
El proyectil cae al suelo tras {t_floor} segundos. \
Indique un tiempo final menor o igual a éste.
Ingrese el intervalo [t0, tf] como t0 tf: """))
# No tendría sentido graficar más allá de este punto.

t0 = interval[0]
tf = interval[1]

if t0 < 0 or tf < 0 or tf > t_floor:
    print("Ingrese tiempos válidos.")
    exit()
# Intervalo de tiempo a graficar

t = np.linspace(t0, tf)
lenght = range(len(t))

pos_x = vx0 * t
vel_x = np.array([vx0 for i in lenght])
acc_x = np.array([0 for i in lenght])
# Movimiento en la coordenada X. (Se asume que no hay aceleración horizontal).

pos_y = -9.81 * t ** 2 / 2 + vy0 * t + h_init
vel_y = -9.81 * t + h_init
acc_y = np.array([-9.81 for i in lenght])
# Movimiento en la coordenada Y. (Uniformemente acelerado por la gravedad).

with open('movimiento_x.csv', 'w') as f:
    f.write('Tiempo,Posición,Velocidad,Aceleración\n')
    f.write('\n'.join('{},{},{},{}'.format(t[i], pos_x[i], vel_x[i], acc_x[i])
            for i in lenght))
# Datos del movimiento en el eje X

with open('movimiento_y.csv', 'w') as f:
    f.write('Tiempo,Posición,Velocidad,Aceleración\n')
    f.write('\n'.join('{},{},{},{}'.format(t[i], pos_y[i], vel_y[i], acc_y[i])
            for i in lenght))
# Datos del movimiento en el eje Y

with open('trayectoria.csv', 'w') as f:
    f.write('Posición_X,Posición_Y\n')
    f.write('\n'.join('{},{}'.format(pos_x[i], pos_y[i]) for i in lenght))
# Datos de la posición en X vs posición en Y.

print(f"""
Altura máxima: {h_max} m.
Tiempo de vuelo: {t_floor} s.
Alcance horizontal: {reach} m.
""")
# Información relevante del tiro parabólico

fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
# Figura para el movimiento de cada coordenada respecto al tiempo. Ambas
# graficas están en una sola figura.
fig2, ax3 = plt.subplots()
# Figura para la trayectoria del proyectil.

ax1.plot(t, pos_x, color='#222288', label='Posición (m)')
ax1.plot(t, vel_x, color='#ffd700', linestyle='-.', label='Velocidad (m/s)')
ax1.plot(t, acc_x, color='#329932', linestyle='--', label='Aceleración (m/s²)')
# Datos graficados del movimiento en X

ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Unidades respectivas")
ax1.set_title("Movimiento en la Coordenada X")

ax1.legend()

ax2.plot(t, pos_y, color='#222288', label='Posición (m)')
ax2.plot(t, vel_y, color='#ffd700', linestyle='-.', label='Velocidad (m/s)')
ax2.plot(t, acc_y, color='#329932', linestyle='--', label='Aceleración (m/s²)')
# Datos graficados del movimiento en Y

ax2.set_xlabel("Tiempo")
ax2.set_title("Movimiento en la Coordenada Y")

ax2.legend()

ax3.plot(pos_x, pos_y, color='#222288', label='Posición (m)')
# Grafica de la trayectoria.

ax3.set_xlabel("Desplazamiento horizontal (m)")
ax3.set_ylabel("Altura (m)")
ax3.set_title("Trayectoria")

ax3.legend()

plt.tight_layout()

plt.show()

fig1.savefig('Movimiento.png')
fig2.savefig('Trayectoria.png')
