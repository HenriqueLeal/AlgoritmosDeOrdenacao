import random
import time

def selectionSort(lista):
   for filtro in range(len(lista)-1,0,-1):
       maximo=0
       for localizacao in range(1,filtro+1):
           if lista[localizacao]>lista[maximo]:
               maximo = localizacao

       temp = lista[filtro]
       lista[filtro] = lista[maximo]
       lista[maximo] = temp




num = 1000
num = 5000
num = 10000
num = 15000
num = 20000
num = 25000


#lista de 1 a num

'''
lista = []
for i in range(num):
    lista.append(i + 1)
'''


#lista de num a 1

'''
lista = []
i = num
while i <= num and i != 0:
    lista.append(i);
    i -= 1;
'''


#lista aleatória
lista = random.sample(range(num), num)

inicio = time.time()
selectionSort(lista)
fim = time.time()
print(lista)
print(fim - inicio)
