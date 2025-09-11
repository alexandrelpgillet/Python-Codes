import random




def swap(a , b):
 return b , a

 

def particion(list,left,right):
 
 
 pivot = list[left]
 i = left
 j = right

 while(i<=j):
  
  while(pivot<list[j]):
   j-=1

  if(i<=j):
   
   list[i], list[j] = swap(list[i],list[j])
  
   if(list[i]== pivot and list[j]== pivot and i!=j):
    i+=1
   elif(list[i]!=pivot):
    i+=1
   
   if(i>=j): 
    
    return i+1,j-1

  while(pivot>list[i]):
   i+=1

  

 return i,j  

    
   
def sort(list,left,right):
 
 i,j = particion(list,left,right)
 print("\n")



 if(left<j):
  sort(list,left,j)
 if (i<right):
  sort(list,i,right)

def quicksort(list):     
    
 sort(list,0,len(list)-1)





#list = [3,0,1,8,7,2,5,4,9,6]
#list = [23,11,-18,37,22,53,4,9,6]

for i in range(10000):
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


  


