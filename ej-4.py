def media_vector(numeros):
    sumapar = 0
    contadorpar = 0
    sumaimpar = 0
    contadorimpar = 0
    for j in range(0, len(numeros)):
        if j%2 == 0:
            sumapar += numeros[i]
            contadorpar += 1
        else:
            sumaimpar += numeros[i]
            contadorimpar += 1
    return sumapar/contadorpar, sumaimpar/contadorimpar

print("Introducir 10 números")
numeros = []
for i in range (0,10):
    numeros.append(int(input()))
mediapar, mediaimpar = media_vector(numeros)
print(f"La media de los pares es {mediapar} y la de los impares es {mediaimpar}")