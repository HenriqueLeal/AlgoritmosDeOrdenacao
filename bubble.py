import random
import time

 #FUNCAO BUBBLE
def bubbleSort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

num = 1000
num = 5000
num = 10000
#num = 15000
#num = 20000
#num = 25000

'''
lista = []
for i in range(num):
    lista.append(i + 1)
'''


lista = []
i = num
while i <= num and i != 0:
    lista.append(i);
    i -= 1;



#lista = random.sample(range(num), num)

inicio = time.time()
bubbleSort(lista)
fim = time.time()
print(lista)
print(fim - inicio)