### generator
import random
import numpy as np
from random import randint
## juz jest
def basic_list(x,y,z):
    x= np.arange(x,y,z).tolist()
    return x
#juz jest
def factor_shuffle(l, factor):
    for i in range(factor):
        a, b = randint(0, (len(l)-1)), randint(0, (len(l)-1)) # pick two random indexes
        if a != b:
            l[b], l[a] = l[a], l[b] # swap the values at those indexes
        return l
#teraz
def random_value(x,y,z):
    myfavList = []
    for i in range(x):
        myfavList.append(random.randint(y,z))
    return myfavList
#juz jest
def reverse_List(x,y,z):
    c=np.arange(x, y, z).tolist() 
    c.reverse()
    return c
#juz jest
def random_shuffling(x,y,z):
    a = np.arange(x, y, z).tolist()
    random.shuffle(a)
    return a

def schuffling_connected():
    a = np.arange(0, 11, 1).tolist()
    b = np.arange(12,22,1).tolist()
    random.shuffle(a)
    for i in b:
        a.append(i)    
    return a

def rev_And_Shuff(x,y,a,b):
    listA = np.arange(x,y,a).tolist()
    listB = np.arange(y+1,b,a).tolist()
    listA.reverse()
    random.shuffle(listB)
    
    for i in listA:
        listB.append(i)

    return listB

    


