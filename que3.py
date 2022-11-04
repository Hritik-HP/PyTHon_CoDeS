# create a 1d array and split that array in  3 
import numpy as np
arr= np.array([15,17,18,20,22,99,100,48,17,50])
n=np.array_split(arr,4)
print(n)

#2 search the element 17 

x=np.where(arr==17)
print(x)                    

#3  sort an array

print(np.sort(arr))

#4 join both array

arr1=np.array([1,2,3,4])
k=np.concatenate((arr,arr1))
print(k)

#5  use hstack and vstack

arr2=np.array([5,6,7,8])
g=np.hstack((arr,arr1))
print(g)
t=np.vstack((arr2,arr1))
print(t)