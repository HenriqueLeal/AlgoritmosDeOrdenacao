import random 
import time

def ordena(lista):
    swapcount = 0, 0
    while True:
        ordenada = False
        for i in range(1, len(lista)):
            if lista[i-1] > lista[i]:
                lista[i-1], lista[i] = lista[i], lista[i-1]
                ordenada = True
        if not ordenada:
            break
    return lista


num = 1000
num = 5000
num = 10000
num = 15000
num = 20000
num = 25000


 #lista de 1 a num
lista = []
for i in range(num):
    lista.append(i + 1)


#lista de num a 1
'''
lista = []
i = num
while i <= num and i != 0:
    lista.append(i);
    i -= 1;
'''

#lista aleatória
#lista = random.sample(range(num), num)

inicio = time.time()
lista = ordena(lista)
fim = time.time()
print(lista)
print(fim - inicio)