a1 = float(input("Ingresa el primer término (a1): "))
r = float(input("Ingresa la razón (r): "))
n = int(input("Ingresa el número de término que quieres (n): "))

Sn = a1 * (r ** n - 1) / r-1

print("El término número", n, "de la progresión geométrica es:", Sn)