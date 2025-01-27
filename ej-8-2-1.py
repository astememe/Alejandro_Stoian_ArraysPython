lista = [[], [], [], []]

def estaEnLista(lista, numero, i):
    if numero in lista[i]:
        return True
    else:
        return False

def mostrarListas(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j])
        print("\n")

for i in range(4):
    for j in range(6):
        numero = input(f"Número {j+1} de la apuesta {i+1}: ")
        estaEnLista(lista, numero, i)
        while estaEnLista(lista, numero, i):
            print("El número se repite")
            numero = input(f"Número {j + 1} de la apuesta {i + 1}: ")
            estaEnLista(lista, numero, i)
        lista[i].append(numero)
mostrarListas(lista)