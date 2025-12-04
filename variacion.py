def variacionConModificacion(n, k):
    return n ** k

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (lugares a ordenar): "))

if k < 0 or k > n:
    print("Error... debe estar entre 0 y n")
else:
    V = variacionConModificacion(n, k)
    print("V(", n, ",", k, ") =", V)
