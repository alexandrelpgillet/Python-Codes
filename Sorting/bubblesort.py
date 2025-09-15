
def  swap(a , b):
   
  return  b, a

def bubblesort(list):
  
  
  q = 0;
  

   
  for j in range (len(list)-1, 0, -1):
      
      trade = False;
      
      for i in range (0,j):
        
        
        q+=1
        
        if(list[i]>list[i+1]):     
          trade = True;
          list[i],list[i+1]= swap(list[i], list[i+1])
        
      if(trade==False):
        
        return q
        
          
  return q    
 
 
    
list = [3,0,1,8,7,2,5,4,9,6]



q= bubblesort(list)


print("q=",q)
print(list)     
        
  
      
     
     
       
