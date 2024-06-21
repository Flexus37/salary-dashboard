import pandas as pd

df = pd.read_csv('data/salary_update.csv', sep=',')
all_cont = df['country'].unique()
