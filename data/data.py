import pandas as pd

df = pd.read_csv('data/salary.csv', sep=',')
df[' SalaryUSD '] = df[' SalaryUSD '].str.replace(',', '').astype(float)
df['Survey Year'] = df['Survey Year'].astype(int)
all_cont = df['Country'].unique()
