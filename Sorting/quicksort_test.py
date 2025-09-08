import random



def printList(list,left, right,pivot):
 
 print("Pivot = " ,pivot)
 for k in range(left,right+1):
  print(list[k],"|",end=" ")
 print("\n")
  


def swap(a , b):
 return b , a

 

def particion(list, left, right):
    pivot = list[left]
    i = left + 1
    j = right
    
    while True:
        while i <= j and list[i] <= pivot:
            i += 1
        while i <= j and list[j] > pivot:
            j -= 1
            
        if i <= j:
            list[i], list[j] = list[j], list[i]
        else:
            break
    
    list[left], list[j] = list[j], list[left]
    return j

    
   
def sort(list, left, right):
    if left < right:
        pivot_index = particion(list, left, right)
        sort(list, left, pivot_index - 1)
        sort(list, pivot_index + 1, right)

def quicksort(list):     
    sort(list, 0, len(list)-1)





#list = [3,0,1,8,7,2,5,4,9,6]
#list = [23,11,-18,37,22,53,4,9,6]

for i in range(10):
    # Clear separator between test cases
    with open("TESTES", 'a', encoding='utf-8') as f:
        f.write("\nTest Case #{}\n".format(i + 1))
        f.write("-" * 40 + "\n")
    
    # Generate random list
    list = []
    j = random.randint(0, 10)
    for k in range(j + 1):
        list.append(random.randint(-100, 100))
    
    # Write unsorted list
    with open("TESTES", 'a', encoding='utf-8') as f:
        f.write("VETOR DESORDENADO: ")
        for l in range(len(list)):
            if l < len(list) - 1:
                f.write(str(list[l]) + "|")
            else:
                f.write(str(list[l]))
        f.write("\n")
    
    # Sort the list
    quicksort(list)
    
    # Write sorted list
    with open("TESTES", 'a', encoding='utf-8') as f:
        f.write("VETOR ORDENADO:    ")
        for l in range(len(list)):
            if l < len(list) - 1:
                f.write(str(list[l]) + "|")
            else:
                f.write(str(list[l]))
        f.write("\n")


  


