num =0


def printList(list,left, right,pivot):
 
 print("Pivot = " ,pivot)
 for k in range(left,right+1):
  print(list[k],"|",end=" ")
 print("\n")
  


def swap(a , b):
 return b , a

 

def particion(list,left,right,num):
 
 
 pivot = list[left]
 i = left
 j = right

 while(i<=j):
  
  while(pivot<list[j]):
    j-=1

  if(i<=j):
   
   print("swap ! " , "V[i] = ", list[i] , "V[j]=", list[j])
   num[0]+=1
   list[i], list[j] = swap(list[i],list[j])
   
   if(list[i]== pivot and list[j]== pivot and i!=j):
    
     i+=1
   
   elif (list[i]!=pivot): 
     i+=1
   
   if(i>=j): 
    
     printList(list,left,right,pivot)
     return i+1,j-1

  while(pivot>list[i]):
   i+=1

 printList(list,left,right,pivot) 
  

 return i+1,j-1  

    
   
def sort(list,left,right,num):
 
 i,j = particion(list,left,right,num)
 print("\n")



 if(left<j):
  sort(list,left,j,num)
 if (i<right):
  sort(list,i,right,num)


def quicksort(list,num):     
 
 sort(list,0,len(list)-1,num)



#list = [3,0,1,8,7,2,5,4,9,6]
#list = [23,11,-18,37,22,53,4,9,6]
#list =[ 78,-82,-100,67,74,67,93]


#Casos problemáticos de ordenação ainda :
#list =[ 67,82,100,67,74,67,93]
#list =[ 78,-82,-100,67,74,67,93]



list = [3,0,1,8,7,2,5,4,9,6]
num =[0]

#list =[78,56,78,58]

#list =[58,58,58,58]
quicksort(list,num)
print("QUANTIDADE DE TROCAS : ",num)
print("Vetor ordenado:", list)