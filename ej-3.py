import random

def contar_pares(vector):
    contador = 0
    posiciones = []
    for j in range(0, len(vector)):
        if vector[j]%2 == 0:
            contador += 1
            posiciones.append(j)
    return posiciones, contador

vector = []
for i in range(0,10):
    vector.append(random.randint(0,100))
posiciones, contador = contar_pares(vector)
print(f"Hay {contador} pares que están en posiciones {posiciones}")