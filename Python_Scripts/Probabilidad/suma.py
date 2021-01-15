import random as rd
import matplotlib.pyplot as plt

lim = int(input("límite de tiros: "))
step = int(input("Paso: "))

if lim <= 0 or step < 1:
    raise ValueError("El límite debe ser mayor a 0, y el paso mayor o igual a 1")

throws = []
prob = []
not_prob = []

for throw_num in range(step, lim + step, step):
    sum = []
    for i in range(throw_num):
        d1 = rd.randint(1, 6)
        d2 = rd.randint(1, 6)
        if d1 + d2 == 8:
            sum.append(d1)
    # Tira dos dados el número de veces especificadas en el rango.
    # Si suman 8, guardamos d1. El valor de d1 no importa, simplemente la
    # estamos usando para contar cuántas veces se da la suma que queremos.

    throws.append(throw_num)
    prob.append(len(sum) / throw_num)
    not_prob.append(1 - len(sum) / throw_num)

    # Guardamos el número de tiros y las probabilidades de los eventos.

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(throws, prob, '.', color='#222288')
ax1.axhline(y = 5/36, color='#444444', linestyle='--',
            label='Valor de Convergencia (5/36)')

ax1.grid(b=True)
ax1.set_xlim(0, lim)
ax1.set_ylim(0, 1)

ax1.set_ylabel("Probabilidad")
ax1.set_title("Probabilidad de que sumen 8")
ax1.legend()

ax2.plot(throws, not_prob, '.r')
ax2.axhline(y = 31/36, color='#444444', linestyle='--',
            label='Valor de Convergencia (31/36)')

ax2.grid(b=True)
ax2.set_xlim(0, lim)
ax2.set_ylim(0, 1)

ax2.set_xlabel("Tiros")
ax2.set_ylabel("Probabilidad")
ax2.set_title("Probabilidad de que NO sumen 8")
ax2.legend()

plt.tight_layout()

plt.show()
