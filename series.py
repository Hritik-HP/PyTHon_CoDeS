import numpy as np
import pandas as pd
a=np.array([1,2,3,4])
name=['hritik', 'aman', 'man', 'karan']
s=pd.Series(a,index=name)
print(s)

marks= np.array([20,30,40,50])
p=pd.Series(marks)
print(p)

o=pd.Series(marks,index=name)
print(o)
print(o[['hritik','karan']])

mar=marks+a
print(mar)