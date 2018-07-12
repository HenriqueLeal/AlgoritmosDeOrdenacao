import random
import time

def insertionSort(lista):
   for index in range(1,len(lista)):

     atual = lista[index]
     posicao = index

     while posicao>0 and lista[posicao-1]>atual:
         lista[posicao]=lista[posicao-1]
         posicao = posicao-1

     lista[posicao]=atual



num = 1000
 #num = 5000
#num = 10000
#num = 15000
#num = 20000
#num = 25000


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
insertionSort(lista)
fim = time.time()
print(lista)
print(fim - inicio)