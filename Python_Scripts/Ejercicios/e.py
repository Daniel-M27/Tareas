def fac(num):                                       # Función factorial.
    fac = 1
    n = 1
    if num >= 0:
        while n < num:
            fac = fac * (n + 1)
            n = n + 1
        return fac

while True:
    lim = int(input('Ingrese el número de términos que desea sumar: '))
    n = 0                                           # Variable contadora.
    eul = 0                                         # Almacena el valor de la serie.

    if lim >= 0:                                    # Verifica que el límite superior tenga sentido.
        while n <= lim:                             # Se suman los términos de la serie hasta alcanzar el límite superior.
            eul = eul + 1 / float(fac(n))           # Definición de la serie.
            n = n + 1

        print(eul)                                  # Aproximación de e.

# Como la serie converge muy rápido, basta con introducir un número alrededor de 150 para obtener una aproximación con 15 o
# 16 decimales. Si se introduce un número más grande se rebasa la capacidad de float().
