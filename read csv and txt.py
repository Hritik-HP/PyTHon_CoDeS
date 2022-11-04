import pandas as pd

df1=pd.read_table('C:\\Users\\hp\\OneDrive\\Desktop\\textfile.txt',sep=",")
print(df1)

df2=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\csvfile.csv',sep=",")
print(df2)
print("----------after concatenate----------")
print(pd.concat([df1, df2],axis=1))


deptid=['145','123','146']
df1['deptid']=deptid
print(df1)

print("-================================-")
print(pd.merge(df1,df2,on="deptid",how='outer'))