import sys
import random

def quickSort(lista):
   meioquick(lista,0,len(lista)-1)

def meioquick(lista,primeiro,ultimo):
   if primeiro<ultimo:

       pivo = partition(lista,primeiro,ultimo)

       meioquick(lista,primeiro,pivo-1)
       meioquick(lista,pivo+1,ultimo)


def partition(lista,primeiro,ultimo):
   valorpivo = lista[primeiro]

   esquerda = primeiro+1
   direita = ultimo

   pronto = False
   while not pronto:

       while esquerda <= direita and lista[esquerda] <= valorpivo:
           esquerda = esquerda + 1

       while lista[direita] >= valorpivo and direita >= esquerda:
           direita = direita -1

       if direita < esquerda:
           pronto = True
       else:
           temp = lista[esquerda]
           lista[esquerda] = lista[direita]
           lista[direita] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[direita]
   lista[direita] = temp


   return direita

#num = 1000
#num = 5000
num = 10000
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

sys.setrecursionlimit(25000)

quickSort(lista)
print(lista)