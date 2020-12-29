while True:
    lim = int(input('> '))                  # Convertimos el input en un número.

    if lim >= 0:                            # Verifica que el límite superior tenga sentido.
        print(lim * (lim + 1) // 2)         # Sabemos que el resultado de esta operación es un entero, así que
                                            # podemos usar la división de enteros, //, para obtener precisión arbitraria.
