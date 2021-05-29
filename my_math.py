##sorting file
def bubble(list):
    indexing_list = len(list) - 1 
    finished = False 
    while not finished:   
        finished = True  

        for i in range(0, indexing_list): 
            if list[i] > list[i+1]: 
                finished = False 
                list[i], list[i+1] = list[i+1], list[i]
    return list


def selection_sorting(list):
    indexing_len = range(0, len(list)-1);
    for i in indexing_len:
        min_value  = i 

        for j in range(i+1, len(list)):
            if list[min_value] > list[j]:
                min_value = j
        if  min_value != i:
            list[min_value], list[i] = list[i], list[min_value]

    return list

def insertion(list):
    indexing_len=range(1, len(list))
    for i in indexing_len:
        item_to_sort = list[i]

        while list[i-1]>item_to_sort and i>0:
            list[i-1], list[i]= list[i], list[i-1]
            i= i-1
        
    return list
    
def quick_sort(list):
      lengt = len(list) ### length.sequnece 
      if lengt <= 1:
          return list
      else:
          pivot = list.pop()
      items_greater = []
      items_lower = []  

      for item in list:
           if item > pivot:
               items_greater.append(item)
           else:
               items_lower.append(item)
     
      return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)

def division(list, first_index, last_index): 
    i = ( first_index - 1 ) 
    x = list[last_index] 
  
    for j in range(first_index, last_index): 
        if   list[j] <= x: 
            i = i + 1
            list[i], list[j] = list[j], list[i] 
  
    list[i + 1], list[last_index] = list[last_index], list[i + 1] 
    return (i + 1)  

def iterativeQick_ver(list, first_index, last_index): 

    size = last_index - first_index + 1 
    stack = [0] * (size) 
    top = -1
    top = top + 1  
    stack[top] = first_index  
    top = top + 1  
    stack[top] = last_index  
    while top >= 0: 
       
        last_index = stack[top] 
        top = top - 1 
        first_index = stack[top]  
        top = top - 1
      
        p = division( list, first_index, last_index ) 
        if p-1 > first_index: 
            top = top + 1
            stack[top] = first_index 
            top = top + 1
            stack[top] = p - 1
  
        if p + 1 < last_index: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = last_index 
    return list