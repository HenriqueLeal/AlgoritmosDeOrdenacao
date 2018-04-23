import random
import time

def troca(a, i, j):
  a[i], a[j] = a[j], a[i]
  
def monte(a):
  n = 0
  m = 0
  while True:
    for i in [0, 1]:
      m += 1
      if m >= len(a):
        return True
      if a[m] > a[n]:
        return False
    n += 1
    
def baixo(a, n, max):
  while True:
    maior = n
    c1 = 2*n + 1
    c2 = c1 + 1
    for c in [c1, c2]:
      if c < max and a[c] > a[maior]:
        maior = c
    if maior == n:
      return
    troca(a, n, maior)
    n = maior

def heapify(a):
  i = len(a) // 2 - 1
  max = len(a)
  while i >= 0:
    baixo(a, i, max)
    i -= 1

def heapsort(a):
  heapify(a)
  j = len(a) - 1
  while j > 0:
    troca(a, 0, j)
    baixo(a, 0, j)
    j -= 1


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
heapsort(lista)
fim = time.time()
print(lista)
print(fim - inicio)
