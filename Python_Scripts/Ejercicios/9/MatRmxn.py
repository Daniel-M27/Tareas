import sys
import os

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
# Validamos la ruta.


with open(path, "r") as f:
    rows = [floats(line) for line in nonempty_lines(f)]
# Obtenemos las filas, recordando que ambas matrices están en el mismo archivo.

gen = iter(rows)
if len(rows) % 2 != 0 or not all(len(vec) == len(rows[0]) for vec in gen):
    print("Las matrices no tienen la misma dimensión")
    exit()
# La primera condición verifica que ambas matrices tengan el mismo número de
# renglones, y la segunda que dichos renglones tengan la misma longitud.

last = len(rows) // 2

matr1 = rows[0:last]
matr2 = rows[last:len(rows) + 1]
# Separamos las matrices, recordando que si tienen el mismo número de filas,
# La primera matriz acaba exactamente a la mitad de la lista.

row = []
matrsum = []

for i in range(len(matr1)):
    for j in range(len(matr1[0])):
        row.append(matr1[i][j] + matr2[i][j])
    matrsum.append(row)
    row = []
# Sumamos los elementos correspondientes de ambas matrices.

for i in range(len(matrsum)):
    print(matrsum[i])
