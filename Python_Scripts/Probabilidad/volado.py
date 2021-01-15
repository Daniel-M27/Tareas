import random as rd
import matplotlib.pyplot as plt

lim = int(input("límite de tiros: "))
step = int(input("Paso: "))

if lim <= 0 or step < 1:
    raise ValueError("Ingrese un número mayor a 0")
# Add step error

throws = []
prob_ag = []
prob_sol = []

for throw_num in range(step, lim + step, step):
    ag = []
    sol = []
    for i in range(throw_num):
        result = rd.randint(0, 1)
        if result == 0:
            sol.append(result)
        else:
            ag.append(result)
    # Tira una moneda el número de veces especificadas por el usuario.
    # 0 es sol y 1 es águila. Este ciclo genera los datos para un solo
    # punto de la gráfica.

    throws.append(throw_num)
    prob_ag.append(len(ag) / throw_num)
    prob_sol.append(len(sol) / throw_num)
    

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(throws, prob_ag, '.b')
ax1.axhline(y = 1/2, color='#444444', linestyle='--',
            label='Valor de Convergencia (1/2)')

ax1.set_ylabel("Probabilidad")
ax1.set_title("Probabilidad de Águila")

ax2.plot(throws, prob_sol, '.r')
ax2.axhline(y = 1/2, color='#444444', linestyle='--',
            label='Valor de Convergencia (1/2)')

ax2.set_xlabel("Número de tiros")
ax2.set_ylabel("Probabilidad")
ax2.set_title("Probabilidad de Sol")

plt.tight_layout()

plt.show()
