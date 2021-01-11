import sys
import os

def floats(str):
    return list(map(float, str.split()))
# Toma un string de números separados por espacios ("1 2 3 4") y devuelve una
# lista de flotantes [1, 2, 3, 4].

def nonempty_lines(f):
    for l in f:
        line = l.strip()
        if line:
            yield line
# Devuelve las líneas no vacías de un objeto archivo. Python evalúa
# bool('') como False, y cualquier otro string como True. Si aplicamos .strip()
# a una línea que contiene únicamente espacios ('          '), obtenemos ''.
# Entonces line == False si la línea está en blanco.


path = sys.argv[1]
# Almacena la ruta del archivo introducida por el usuario.

if not os.path.isfile(path):
    print(f"La ruta {path} no existe. \n")
    exit()
# Revisa que la ruta introducida sea válida.

with open(path, "r") as f:
    vecs = [floats(line) for line in nonempty_lines(f)]
# Si la línea no está en blanco, transformamos sus elementos en una lista de
# flotantes y la almacenamos en `vecs`.

gen = iter(vecs)
if not all(len(vec) == len(vecs[0]) for vec in gen):
    print("No todos los vectores tienen el mismo número de entradas. \n")
    exit()
# Esta condición verifica que todas las listas de `vecs` sean del mismo tamaño.
# Si esto no se cumple, el condicional devuelve True y se aborta el proceso.
# La lista con los vectores se convierte en un generador para agilizar el proceso.


entries = []
vecsum = []

for i in range(len(vecs[0])):              # Dimensión de los vectores
    for j in range(len(vecs)):             # Número de vectores
        entries.append(vecs[j][i])

    vecsum.append(sum(entries))
    entries = []
# Agrega la i-ésima entrada de cada vector a `entries`, y luego agrega la suma
# de éstos a `vecsum`. Empezamos en la posición 0 de cada vector y agregamos
# la suma de vecs[0][0], vecs[1][0],..., vecs[m][0] a `vecsum`; luego vaciamos
# `entries` y nos movemos a la siguiente posición de cada vector.

print('\n', vecsum, '\n')
