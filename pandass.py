import pandas as pd
import numpy as np
data=pd.read_csv("C:\\Users\\hp\\Downloads\\test.csv")
d=pd.notnull(data['Sex'])
print(d)

data["Sex"]=data["Sex"].replace('male','boy')
print(data)

print(data.replace(to_replace=np.NaN,value=2105))
