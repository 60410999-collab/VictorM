a1 = float(input("Ingresa el primer término (a): "))
d = float(input("Ingresa la diferencia (d): "))
n = int(input("Ingresa el número de término que quieres (n): "))

an = a1 + (n - 1) * d
Sn = n * (a1 + an) / 2

print("El termino número", n, "es (an):", an)
print("La suma de los primeros", n, "términos es (Sn):", Sn)