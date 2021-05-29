import json
import time
import my_math as my

def saveToFile(list,unsorted):
    with open(unsorted, 'w') as filehandle:
        json.dump(list, filehandle)

def load(unsorted_file):
     rev=[]
     with open(unsorted_file, 'r') as filehandle:
        rev=(json.load(filehandle))
        return rev  

def print_time(name,data):
    if (name=="bubble"):
        s = time.time()
        my.bubble(data)
        e = time.time()
        score = e-s
        return("BubbleSort = {:f} s".format(score))
    elif (name=="selection"):
        s= time.time()
        my.selection_sorting(data)
        e = time.time()
        score=e-s
        return("Selection = {:f} s".format(score))
    elif (name=="insertion"):
        s= time.time()
        my.insertion(data)
        e = time.time()
        score=e-s
        return("Insertion = {:f} s".format(score))
    elif (name=="quick"):
        s= time.time()
        my.quick_sort(data)
        e = time.time()
        score=e-s
        return("Quick = {:f} s".format(score))    
    elif (name=="iteration"):
        s=time.time()
        my.iterativeQick_ver(data,0,(len(data)-1))
        e=time.time()
        score=e-s
        return("Iteration Qick = {:f} s".format(score))
    else:
        return "dont work uncle Bob!"

def check_time(name,data):
    if (name=="bubble"):
        s = time.time()
        my.bubble(data)
        e = time.time()
        score = e-s
        #print(score)
        return score ### tutaj mamy doczynienie z posortowaną listą 
    elif (name=="selection"):
        s= time.time()
        my.selection_sorting(data) ### kolejne wczytanie tej l
        e = time.time()
        score=e-s
        #print(score)
        return score  
    elif (name=="insertion"):
        s= time.time()
        my.insertion(data)
        e = time.time()
        score=e-s
        return score  
    elif (name=="quick"):
        s= time.time()
        my.quick_sort(data)
        e = time.time()
        score=e-s
        return score  
    elif (name=="iteration"):
        s=time.time()
        my.iterativeQick_ver(data,0,(len(data)-1))
        e=time.time()
        score=e-s
        #print(rest)
        return score
    else:
        return "dont work uncle Bob!"

def run_all(file1,file2,file3,file4,file5):
        part1=[]
        part1.append(check_time("bubble",file1))             ### wczęsniej było na sztywno rev5,6,7,8
        part1.append(check_time("selection",file2))
        part1.append(check_time("insertion",file3))
        part1.append(check_time("quick",file4))
        part1.append(check_time("iteration",file5))
        print(part1)
        return part1

def conversion(list):
    part=[]
    for i in list:
        new=i*(1)
        part.append(new)
    #print(part)
    return part


