def floats(str):
    return list(map(float, str.split()))

print("Ingrese los renglones de las matrices con el formato a b")

while True:
    Ar1 = floats(input("Renglón 1: "))
    Ar2 = floats(input("Renglón 2: "))
    Br1 = floats(input("\n Renglón 1: "))
    Br2 = floats(input(" Renglón 2: "))
# Obtenemos cada renglón individualmente.

    if len(Ar1) == len(Ar2) == len(Br1) == len(Br2) == 2:
        sumR1 = [Ar1[0] + Br1[0], Ar1[1] + Br2[1]]
        sumR2 = [Ar2[0] + Br2[0], Ar2[1] + Br2[1]]
# Revisamos que las matrices sean de 2x2.

        print(sumR1)
        print(sumR2)

    else:
        print("Ingrese renglones de dos elementos. \n")
