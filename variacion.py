def variacion_con_modificacion(n, k):
    return n ** k

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (lugares a ordenar): "))

if k < 0 or k > n:
    print("k debe estar entre 0 y n.")
else:
    V = variacion_con_modificacion(n, k)
    print("V(", n, ",", k, ") =", V)
