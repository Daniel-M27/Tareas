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
# argv[0] siempre es el nombre del script.

if not os.path.isfile(path):
    print(f"La ruta {path} no existe. \n")
    exit()
# Revisa que la ruta introducida sea válida.

with open(path, "r") as f:
    vecs = []
    for line in nonempty_lines(f):
        if len(vecs) < 2:
            vecs.append(floats(line))
# Agregamos a la lista los primeros dos renglones que no están en blanco; o sea,
# los dos vectores deben estar uno tras otro (sin contar líneas en blanco).
# El contenido de las líneas posteriores al segundo vector es irrelevante.


vec1 = vecs[0]
vec2 = vecs[1]

if len(vec1) == len(vec2):      # Ambos vectores deben ser del mismo tamaño.
    dot_prod = 0
    for n in range(len(vec1)):
        dot_prod = dot_prod + vec1[n] * vec2[n]
# Sumamos recursivamente el producto de las entradas correspondientes de
# ambos vectores.

    print(dot_prod, '\n')

else:
    print("Verifique que ambos vectores sean del mismo tamaño. \n")
