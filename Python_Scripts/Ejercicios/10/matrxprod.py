import sys
import os

def floats(str):
    return list(map(float, str.split()))

def nonempty_lines(f):
    for l in f:
        line = l.strip()
        if line:
            yield line

def dot(vec1, vec2):
    dot_prod = 0
    for n in range(len(vec1)):
        dot_prod = dot_prod + vec1[n] * vec2[n]
    return dot_prod
# Hace el producto punto de dos vectores.

def columns(matrx):
    columns = []
    column = []
    for j in range(len(matrx[0])):       # Longitud del renglón
        for i in range(len(matrx)):      # Número de renglones
            column.append(matrx[i][j])
        columns.append(column)
        column = []
    return columns
# Fijamos el número de columna (j) y nos movemos por los renglones, agregando
# a la lista matrx[1][j], matrx[2][j],..., matrx[m][j]. Al terminar tendremos
# la columna completa, y simplemente la agregamos a la lista de columnas antes
# de pasar a la columna j+1.

path1 = sys.argv[1]
path2 = sys.argv[2]

if not os.path.isfile(path1):
    print(f"La ruta {path1} no existe. \n")
    exit()

if not os.path.isfile(path2):
    print(f"La ruta {path2} no existe. \n")
    exit()
# Verificamos que los archivos existan.


with open(path1, "r") as f:
    matrx1 = [floats(line) for line in nonempty_lines(f)]

with open(path2, "r") as f:
    matrx2 = [floats(line) for line in nonempty_lines(f)]
# Leemos los archivos para obtener las matrices.


gen1 = iter(matrx1)
gen2 = iter(matrx2)
if not all(len(row) == len(matrx1[0]) for row in gen1):
    print("Revise que los renglones de la matriz 1 sean del mismo tamaño.")
    exit()
elif not all(len(row) == len(matrx2[0]) for row in gen2):
    print("Revise que los renglones de la matriz 2 sean del mismo tamaño.")
    exit()
elif len(matrx1[0]) != len(matrx2):
    print("Revise que las matrices sean de la forma (m x n) (n x p).")
    exit()
# Revisamos que sean matrices bien definidas, y que puedan multiplicarse.

columns = columns(matrx2)
prodmatrx = []
row = []

for i in range(len(matrx1)):
    for j in range(len(columns)):
        row.append(dot(matrx1[i], columns[j]))
    prodmatrx.append(row)
    row = []
# Fijamos el renglón (i) de la primera matriz, y tomamos su producto punto con
# cada columna de la segunda matriz. La fila resultante es la i-ésima fila del
# producto de ambas.

for i in range(len(prodmatrx)):
    print(prodmatrx[i])
