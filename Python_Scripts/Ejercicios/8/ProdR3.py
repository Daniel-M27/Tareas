print("Ingrese las entradas del vector (a,b,c) con el formato a b c")

def floats(str):
    return list(map(float, str.split()))
# Toma un string de números separados por espacios ("1 2 3 4") y devuelve una
# lista de flotantes [1, 2, 3, 4].

while True:
    vec1 = floats(input("> "))   # Entradas del primer vector.
    vec2 = floats(input("> "))   # Entradas del segundo vector.
    a = vec1[0]
    b = vec1[1]
    c = vec1[2]
    r = vec2[0]
    s = vec2[1]
    t = vec2[2]

    if len(vec1) == len(vec2) == 3:         # Verifica que ambos vectores sean de R³.
        print(a * r + b * s + c * t, '\n')        # Definición de producto punto.
    else:
        print('Ingrese vectores de R³. \n')
