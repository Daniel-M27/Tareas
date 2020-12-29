def fac(num):
    fac = 1
    n = 1
    if num >= 0:
        while n < num:
            fac = fac * (n + 1)
            n = n + 1
        return fac

while True:
    n = int(input("Combinación de: "))
    k = int(input("en: "))

    if n >= 0 and k >= 0 and k <= n:
        print(fac(n) // (fac(k) * fac(n - k)))
