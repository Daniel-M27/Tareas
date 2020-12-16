from random import randint

print("""
Dada una lista finita de enteros positivos, este programa permite determinar cuántos de ellos son pares y cuántos impares.
Puede especificar el límite superior del rango en el que están los números; el intervalo default es [1, 1000], para usarlo presione ENTER.
""")

ran = (input('Límite superior (opcional): '))

while True:
    N = []
    even = []
    odd = []

    nums = int(input('Cantidad de números a generar: '))

    for i in range(1, nums + 1):
        if ran == '':
            N.append(randint(1, 1000))
        else:
            N.append(randint(1, int(ran)))

    for i in N:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 == 1:
            odd.append(i)

    print(*N, sep = ', ')
    print(f"""
    \rPares: {len(even)}
    \rImpares: {len(odd)}
    """)
