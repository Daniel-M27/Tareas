print("""
Este programa es un convertidor de enteros a diferentes bases numéricas. La versión actual soporta solamente bases entre
el 2 y el 10. Para salir oprima CTRL + C.

Para convertir un entero en Base-n a decimal, oprima [1].
Para convertir un entero decimal a Base-n, oprima [2].
""")

mode = input('> ')
if mode == '1':
    while True:
        base = int(input('Base: '))

        if base > 10:
            print("Base no soportada.")
            exit()

        bin = list(input('Número: '))
        order = int(len(bin)) - 1
        filter = all(int(x) < base for x in bin)

        num = []
        ind = []
        pow = []
        times = []


# El algoritmo puede hacerse de manera más simple, pero creo que vale la pena
# (en especial para bases pequeñas) excluir todos los ceros del número para
# agilizar el cálculo.

        if filter == True:
            for i, x in enumerate(bin):
                if x != '0':                                # Almacena la posición de los dígitos que no son 0.
                    ind.append(i)

            for x in ind:
                pow.append(base**(order - x))               # Almacena las potencias cuyos coeficientes no son 0.

            for x in bin:
                if x != '0':                                # Almacena los dígitos que no son 0.
                    num.append(int(x))

            for j in range(len(num)):                       # Multiplica todas las potencias con sus
                times.append(num[j] * pow[j])               # respectivos coeficientes.

            print('\n' + str(sum(times)) + '\n')

        else:
            print(f"\n Error, valor inválido en Base-{base}. \n")

#######################################################################################################################

elif mode == '2':
    def reverse(list):                                   # Invierte el orden de elementos en una lista.
        return [x for x in reversed(list)]

    def cat(list):                                       # Concatena los elementos de una lista en un string.
        blank = ''
        return blank.join(list)

    while True:
        num = int(input('Número: '))
        base = int(input('Base: '))

        if base > 10:
            print("Base no soportada.")
            exit()

        mod = []

        while base <= num:
            mod.append(str(num % base))
            num = num // base                            # Equivale a floor(num / base).
        mod.append(str(num))

        convert = reverse(mod)
        print('\n' + cat(convert) + '\n')
