import numpy as np
import pandas as pd
name=['hritik', 'random', 'ram', 'rang']
s=pd.Series([10,20,30,40],index=name)
d=pd.Series([20,30,40,10],index=name)
result=s+d
print(result)


#tail function
print(result.tail(2))

#head function
print(result.head(2))
