import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "lifting": [40,50,60]
}
df = pd.DataFrame(data)
print(df)