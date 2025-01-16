import random

def crear_vectores():
    vector1 = []
    vector2 = []
    for i in range(0, 15):
        vector1.append(random.randint(0, 100))
        vector2.append(random.randint(0, 100))
    return vector1, vector2

def sumar_vectores():
    vector1, vector2 = crear_vectores()
    vector_suma = []
    for i in range(0, len(vector1)):
        vector_suma.append(vector1[i] + vector2[i])
    return vector_suma

print(sumar_vectores())