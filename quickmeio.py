import random
import sys

def troca(array,a,b):
    array[a],array[b] = array[b],array[a]


def partition(array,inicio,fim):
    median = (fim - 1 - inicio) // 2
    median = median + inicio
    esquerda = inicio + 1
    if (array[median] - array[fim-1])*(array[inicio]-array[median]) >= 0:
        troca(array,inicio,median)
    elif (array[fim - 1] - array[median]) * (array[inicio] - array[fim - 1]) >=0:
         troca(array,inicio,fim - 1)
    pivot = array[inicio]
    for direita in range(inicio,fim):
        if pivot > array[direita]:
            troca(array,esquerda,direita)
            esquerda = esquerda + 1
    troca(array,inicio,esquerda-1)
    return esquerda-1

def meioquick(array,inicio,fim):
    if inicio < fim:
        splitPoint = partition(array,inicio,fim)
        meioquick(array,inicio,splitPoint)
        meioquick(array,splitPoint+1,fim)

def quickSort(array):
    meioquick(array,0,len(array))



num = 1000
#num = 5000
#num = 10000
#num = 15000
#num = 20000
#num = 25000


#lista de 1 a num

'''
lista = []
for i in range(num):
    lista.append(i + 1)
'''

#lista de num a 1


lista = []
i = num
while i <= num and i != 0:
    lista.append(i);
    i -= 1;


#lista aleatória
#lista = random.sample(range(num), num)

sys.setrecursionlimit(25000)

quickSort(lista)
print(lista)
