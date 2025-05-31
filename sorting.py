l=[7,1,4,5,6,2]
for i in range(6):
  if(l[i]>=l[i+1]):
    l[i],l[i+1]=l[i+1],l[i]
print(l)
    
  
