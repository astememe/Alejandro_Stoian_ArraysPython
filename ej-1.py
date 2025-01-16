print("Introduce 10 números")
numeros = []
maximo = 0
contador_max = 0
for i in range (0, 9):
    numeros.append(int(input()))
    if numeros[i] > maximo:
        maximo = numeros[i]
        contador_max = 0
    if maximo == numeros[i]:
        contador_max += 1
print(f"Número máximo: {maximo}\nVeces que aparece: {contador_max}")