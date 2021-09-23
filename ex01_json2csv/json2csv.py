import pandas as pd

data = pd.read_json('test.json')
data.to_csv('test.csv')
