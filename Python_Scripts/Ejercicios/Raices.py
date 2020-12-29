import math as m
import cmath as cm    # Este módulo permite realizar cálculos con números complejos.

print("Ingrese los coeficientes del polinomio ax² + bx + c con el formato a b c ")

while True:
    coeff = list(map(float,  input("> ").split()))      # Almacena los coeficientes en una lista (siendo ya números).
    a = coeff[0]
    b = coeff[1]
    c = coeff[2]

    disc = b ** 2 - 4 * a * c      # Discriminante (radical) de la fórmula cuadrática. Su valor determina qué tipo de raices tiene el polinomio.

    print("Raices del polinomio ({})x² + ({})x + ({}) :".format(a, b, c))

    if a != 0:                                                   # La fórmula cuadrática implica dividir entre 2a, así que debemos considerar los casos con a = 0 a parte.
        if disc == 0:                                            # ± sqrt(0) = 0.
            print(f"""Raíz real única.
            \rx = {-b / (2 * a)}
            """)
            # simplificación de la fórmula cuadrática con discriminante 0.

        elif disc > 0:                                           # La raíz de un número positivo es un número real.
            print(f"""Raices reales dobles.
            \rx₁ = {(-b + m.sqrt(disc)) / (2 * a)}
            \rx₂ = {(-b - m.sqrt(disc)) / (2 * a)}
            """)
            # Se realizan las operaciones por separado para obtener ambas raíces. Se usa sqrt() del módulo math, que funciona
            # mejor para números reales.

        elif disc < 0:                                           # La raíz de un número negativo es un número complejo.
            print(f"""Raices complejas dobles.
            \rx₁ = {(-b + cm.sqrt(disc)) / (2 * a)}
            \rx₂ = {(-b - cm.sqrt(disc)) / (2 * a)}
            """)
            # Esencialmente igual al caso anterior, solo que ahora se usa la función sqrt de cmath, que también está definida
            # para valores negativos.

    elif a == 0 and b != 0:                                     # Si A = 0 y  B =/= 0, simplemente despejamos x en la ecuación Bx + C = 0.
        print(f"""Función lineal de la forma mx + b.
        \rx = {-c / b}
        """)
    elif a == 0 and b == 0:                                     # Caso trivial y casos sin solución.
        if c != 0:
            print("""
            \rNingún número es una solución de {}x² + {}x + ({}) = 0
            """.format(a, b, c))
        elif c == 0:
            print("""
            \rCualquier número es una solución de {}x² + {}x + {} = 0
            """.format(a, b, c))
