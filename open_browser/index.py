import pandas as pd

df = pd.read_json('./data.json')
df.to_csv()

print(df.to_string())
