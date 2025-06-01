import pandas as pd


df = pd.read_excel("US Superstore data.xls", engine="xlrd")  # Because it's .xls file

print(df.head())
print(df.info())