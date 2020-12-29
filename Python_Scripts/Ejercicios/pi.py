while True:
    lim = int(input('Ingrese el número de términos que desea sumar: '))
    n = 0                                                       # Variable contadora.
    pi = 0                                                      # Almacena el valor de la sumatoria

    if lim >= 0:                                                # Verifica que el límite superior tenga sentido.
        while n <= lim:                                         # Suma los términos de la serie hasta alcanzar el límite superior.
            pi = pi + ((-1) ** n / (float(2 * n + 1)))          # Definición de la serie.
            n = n + 1

        print(4 * pi)                                           # La serie se aproxima a pi/4, así que multiplicamos por 4.
