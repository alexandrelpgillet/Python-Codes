


def swap(a , b):
 
  return b,a


def bubblesort(list) : 
    
     
    
    
    for i in range(len(list),0, -1):
         
         trade = 0
         not_trade = 0
             
          
         for j in range(0,i-1):

              if(list[j]>list[j+1]):
                  
                  trade += 1
                  
 
                  list[j], list [j+1]=swap(list[j],list[j+1])    

              else:
                 
                  not_trade +=1
          
         if(not_trade+1>=trade): break
                  
list = [5,4,3,2,1]
#list = [3,1,7,2,6,4,5]

bubblesort(list)

print(list)
