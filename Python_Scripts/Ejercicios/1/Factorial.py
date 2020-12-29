while True:
    num = int(input('Factorial: '))
    n = 1                                       # Variable contadora.
    fac = 1

    if num >= 0:                                # El factorial no está definido para números negativos.
        while n < num:
            fac = fac * (n + 1)                 # Multiplicamos recursivamente los números del 1 hasta llegar al valor
            n = n + 1                           # especificado por el usuario.

        print (f"{num}! = {fac}")               # Notemos que esto devuelve 0! = 1.
