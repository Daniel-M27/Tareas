    base = int(input('Base: '  ))           # Convertimos el input en números.
    exp = int(input('Exponente: ' ))
    n = 1                                   # Variable contadora.
    pow = 1                                 # Almacena la potencia.


    if exp >= 0:                            # Potencias no negativas.
        while n <= exp:
            pow = pow * base                 # Multiplicamos la base por sí misma la cantidad de veces especificada
            n = n + 1                        # por el usuario.

    elif exp < 0:                           # Potencias negativas.
        while n <= -1 * exp:
            pow = pow / base                 # Dividimos la base por sí misma la cantidad de veces especificada
            n = n + 1                        # por el usuario.

    print(f"Resultado: {pow}")              # El algoritmo devuelve a ** 0 = 1, incluso cuando a = 0.
