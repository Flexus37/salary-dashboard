import pandas as pd

df = pd.read_csv('data/salary.csv', sep=',')
df[' SalaryUSD '] = df[' SalaryUSD '].str.replace(',', '').astype(float)
all_cont = df['Country'].unique()
