import numpy as np
import pandas as pd
df=pd.DataFrame(
    [[18000,110,189,1400],
    [36000,905,23.4,1800],
    [23000,230,14.0,1300],
    [60000,450,13.5,1500]],
    columns=['col1', 'col2', 'col3', 'col4'])
display(df)


import matplotlib.pyplot as plt
df.plot(kind = 'bar')
df.plot()

