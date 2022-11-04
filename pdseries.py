import pandas as pd
EmpID = pd.Series([101,102,103,104,105])
EmpName = pd.Series(['Aman', 'Amit', 'Roshan', 'Anil', 'Ram'])
EmpSalary =pd.Series([10000, 25000, 30000, 15000, 45000])

EmpID.index = ['D1', 'D2', 'D1', 'D3', 'D2']
EmpName.index = ['D1', 'D2', 'D1', 'D3', 'D2']
EmpSalary.index = ['D1', 'D2', 'D1', 'D3', 'D2']

D = {'EmpID' : EmpID, 'EmpName' : EmpName , 'EmpSalary' : EmpSalary}

Df = pd.DataFrame(D)
print(Df)