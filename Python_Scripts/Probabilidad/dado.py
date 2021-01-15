import random as rd
import matplotlib.pyplot as plt

lim = int(input("límite de tiros: "))
step = int(input("Paso: "))

if lim <= 0 or step < 1:
    raise ValueError("El límite debe ser mayor a 0, y el paso mayor o igual a 1")

throws = []
prob = []

for throw_num in range(step, lim + step, step):
    three = []
    for i in range(throw_num):
        result = rd.randint(1, 6)
        if result == 3:
            three.append(result)
    # Tira un dado el número de veces especificadas en el rango.
    # Si cae 3 guardamos el resultado.
    throws.append(throw_num)
    prob.append(len(three) / throw_num)
# Guardamos la probabilidad y el número de tiros

plt.plot(throws, prob, '.', color='#222288')
plt.axhline(y = 1/6, color='#444444', linestyle='--',
            label='Valor de Convergencia (1/6)')

plt.grid(b=True)
plt.xlim(0, lim)
plt.ylim(0, 1)

plt.xlabel("Tiros")
plt.ylabel("Probabilidad")
plt.title("Probabilidad de que caiga 3")

plt.tight_layout()

plt.show()
