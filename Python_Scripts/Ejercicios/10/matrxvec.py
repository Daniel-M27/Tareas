import sys
import os

def dot(vec1, vec2):
    dot_prod = 0
    for n in range(len(vec1)):
        dot_prod = dot_prod + vec1[n] * vec2[n]
    return dot_prod

def floats(str):
    return list(map(float, str.split()))

def nonempty_lines(f):
    for l in f:
        line = l.strip()
        if line:
            yield line

path = sys.argv[1]


if not os.path.isfile(path):
    print(f"La ruta {path} no existe. \n")
    exit()
# Revisamos que la ruta introducida sea válida.

with open(path, "r") as f:
    matrx = [floats(line) for line in nonempty_lines(f)]
# Leemos la matriz.

vec = matrx[0]
del(matrx[0])
# El vector por el que vamos a multiplicar es la primera línea del archivo;
# almacenamos su valor y lo borramos de la lista para dejar solo la matriz.

gen = iter(matrx)
if not all(len(vec) == len(matrx[0]) for vec in gen):
    print("No todos los renglones tienen el mismo número de entradas.")
    exit()
# Verificamos que todos los renglones de la matriz tengan la misma longitud.

if len(vec) != len(matrx):
    print("Revise que la matriz y el vector sean de la forma (m x n) (n x 1)")
# La longitud del vector debe ser la misma que la del número de renglones de la
# matriz para que el producto sea válido.

prod = [dot(vec,row) for row in matrx]
print('\n', prod, '\n')
