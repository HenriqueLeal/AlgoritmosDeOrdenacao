import random
import time

def shellSort(lista):
    sublista = len(lista)//2
    while sublista > 0:

      for startposicao in range(sublista):
        gapInsertionSort(lista,startposicao,sublista)

      sublista = sublista // 2

def gapInsertionSort(lista,start,gap):
    for i in range(start+gap,len(lista),gap):

        valoratual = lista[i]
        posicao = i

        while posicao>=gap and lista[posicao-gap]>valoratual:
            lista[posicao]=lista[posicao-gap]
            posicao = posicao-gap

        lista[posicao]=valoratual



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
shellSort(lista)
fim = time.time()
print(lista)
print(fim - inicio)
