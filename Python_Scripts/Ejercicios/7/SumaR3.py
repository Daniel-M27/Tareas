print("Ingrese las entradas del vector (a,b,c) con el formato a b c")

while True:
    vec1 = list(map(float,  input("> ").split()))   # Entradas del primer vector.
    vec2 = list(map(float,  input("> ").split()))   # Entradas del segundo vector.
    a = vec1[0]
    b = vec1[1]
    c = vec1[2]
    r = vec2[0]
    s = vec2[1]
    t = vec2[2]

    if len(vec1) == len(vec2) == 3:                 # Verifica que ambos vectores sean de R³.
        print(f"({a + r},{b + s},{c + t})")
    else:
        print('Ingrese vectores de R³.')
