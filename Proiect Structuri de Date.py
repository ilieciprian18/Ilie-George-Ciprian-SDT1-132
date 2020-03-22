#Date de intrare: Pe prima linie nr de teste apoi pe fiecare linie nr de nr al vectorului si nr maxim din vector.
#Ex de date de intrare:
#4
#1000 20
#100 400
#10 60
#9 5
#Algoritmul afiseaza timpul de sortare pentru vectorul generat random apoi compara si gaseste cel mai scurt timp de sortat.

f=open("teste","r")
g=open("testeout","w")
from random import seed
from random import randint
import time
v=[]
def bubblesort(v,n) :
    #for in for si verific pereche cu pereche
    for i in range(n):
        for j in range(n-i-1) :
            if v[j]>v[j+1]  :
                aux=v[j]
                v[j]=v[j+1]
                v[j+1]=aux
def counting_sort(v):
    max_val=max(v)      #gasim o val max din vector
    m = max_val + 1
    count = [0] * m
    #creem un fel de vector de frecventa cu elementele
    for a in v:
        count[a] =count[a] + 1
    i = 0
    #refacem lista cu elementele ordonate din vect de frecv
    for a in range(m):
        for c in range(count[a]):
            v[i] = a
            i =i+ 1
    #returnam lista ordonata
    return v
def mergesort(v):
    if len(v) > 1:
        mid = len(v) // 2
        left = v[:mid]
        right = v[mid:]
        mergesort(left)
        mergesort(right)
        i = 0  #parcurg in stanga
        j = 0  #parcurg in dreapta
        k = 0  #parcurg in vector
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                v[k] = left[i]
                i =i + 1
            else:
                v[k] = right[j]
                j = j + 1
            k = k + 1
        #daca mai sunt elemente in stanga le pun in vector
        while i < len(left):
            v[k] = left[i]
            i = i + 1
            k = k + 1
        #daca mai sunt elemente in dreapta le pun in vector
        while j < len(right):
            v[k] = right[j]
            j = j + 1
            k = k + 1
def QuickSort(v):
    n=len(v)
    if n < 2:
        return v
    p = 0
    for i in range(1,n):
        if v[i] <= v[0]:
            p=p+1
            aux = v[i]
            v[i] = v[p]
            v[p] = aux
    aux = v[0]          #variabila de swap
    v[0] = v[p]         #schimb variabilele
    v[p] = aux
    left = QuickSort(v[0:p])      #obtin bucata stanga
    right = QuickSort(v[p+1:n])   #obtin bucata dreapta
    v = left + [v[p]] + right     #combin drepta cu stanga si mijloc
    return v
def radix_sort(v):

    RADIX = 10 #baza
    placement = 1
    cifmax = max(v) #cifra max
    #sortarea
    while placement < cifmax:
      buckets = [list() for _ in range( RADIX )]
      for i in v:
        d = int((i / placement) % RADIX)
        buckets[d].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          v[a] = i
          a =a + 1
      placement = placement * RADIX
    #intorc vectorul final ordonat
    return v
def test_sort(v):
    a=v.copy()
    a.sort()
    if a == v :
        g.write("Test : Vectorul a fost sortat, True" + '\n')
    else :
        g.write("Test : Vectorul nu a fost sortat, False" + '\n')

x=int(f.readline())
o=1
while o <= x :
    y = f.readline()
    p = y.split()
    v=[]
    vector = []
    for i in range(len(p)):
        vector.append(int(p[i]))
    seed(randint(0, 1000))   #generez seed random
    for j in range(vector[0]):      #generez vectorul cu elemente random
        value = randint(0, vector[1])
        v.append(value)
    g.write("Numarul de numere este "+ str(vector[0]) + '\n')
    g.write("Numarul maxim din secventa generata este " + str(max(v))+ '\n')
    # v este vectorul original cu numerele
    # b este o copie a vectorului pe care o sortam pentru a nu pierde vectorul original dupa prima sortare
    # bubble sort
    b = v.copy()
    start = time.time()
    bubblesort(b, vector[0])
    g.write("Timpul de sortare pentru bubble sort " + str(time.time() - start) + '\n')
    bubblesort_time = time.time() - start
    test_sort(b)
    # count sort
    b = v.copy()
    start = time.time()
    b = counting_sort(b)
    g.write("Timpul de sortare pentru count sort " + str(time.time() - start)+ '\n')
    counting_sort_time = time.time() - start
    test_sort(b)
    # merge sort
    b = v.copy()
    start = time.time()
    mergesort(b)
    g.write("Timpul de sortare pentru merge sort " + str(time.time() - start)+'\n')
    mergesort_time = time.time() - start
    test_sort(b)
    # Quick Sort
    b = v.copy()
    start = time.time()
    b = QuickSort(b)
    g.write("Timpul de sortare pentru Quick sort " + str(time.time() - start)+'\n')
    QuickSort_time = time.time() - start
    test_sort(b)
    # radix sort
    b = v.copy()
    start = time.time()
    radix_sort(b)
    g.write("Timpul de sortare pentru radix sort " + str(time.time() - start)+'\n')
    radixsort_time = time.time() - start
    test_sort(b)
    celmairapid = []
    celmairapid.append(mergesort_time)
    celmairapid.append(QuickSort_time)
    celmairapid.append(radixsort_time)
    celmairapid.append(bubblesort_time)
    g.write("Cea mai rapid timp pe acest exemplu este " + str(min(celmairapid))+'\n')
    b = v.copy()
    start = time.time()
    b.sort()
    g.write("Timpul de sortare standard al v.sort() din Python : " + str(time.time() - start) + '\n')
    o=o+1
#elimina spatiile
#adauga cod explicativ
