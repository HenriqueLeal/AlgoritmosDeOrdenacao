import random
import time

def mergeSort(lista):
    if len(lista)>1:
        centro = len(lista)//2
        esquerda = lista[:centro]
        direita = lista[centro:]

        mergeSort(esquerda)
        mergeSort(direita)

        i=0
        j=0
        k=0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k]=esquerda[i]
                i=i+1
            else:
                lista[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            lista[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            lista[k]=direita[j]
            j=j+1
            k=k+1

num = 1000
num = 5000
num = 10000
num = 15000
num = 20000
num = 25000

 '''
lista = []
for i in range(num):
    lista.append(i + 1)
'''

'''
lista = []
i = num
while i <= num and i != 0:
    lista.append(i);
    i -= 1;
'''


lista = random.sample(range(num), num)

inicio = time.time()
mergeSort(lista)
fim = time.time()
print(lista)
print(fim - inicio)

