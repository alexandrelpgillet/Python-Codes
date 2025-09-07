

def printList(list,left, right,pivot):
 
 print("Pivot = " ,pivot)
 for k in range(left,right+1):
  print(list[k],"|",end=" ")
 print("\n")
  


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
   print("swap ! " , "i = ", i , "j=", j)
   list[i], list[j] = swap(list[i],list[j])

   if(list[i]!=pivot):
    i+=1
   
   if(i>=j): 
    
    printList(list,left,right,pivot)
    return i+1,j-1

  while(pivot>list[i]):
   i+=1

 printList(list,left,right,pivot) 
  

 return i,j  

    
   
def sort(list,left,right):
 
 i,j = particion(list,left,right)
 print("\n")



 if(left<j):
  sort(list,left,j)
 if (i<right):sort(list,i,right)


def quicksort(list):     
    
 sort(list,0,len(list)-1)



#list = [3,0,1,8,7,2,5,4,9,6]
list = [23,11,-18,37,22,53,4,9,6]




quicksort(list)
print("Vetor ordenado:", list)