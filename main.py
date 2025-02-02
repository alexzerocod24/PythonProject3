import pandas as pd

df = pd.read_csv('Europe_GDP.csv')

print("Первые 5 строк:")
print(df.head())

print("\nИнформация о данных:")
print(df.info())

print("\nСтатистическое описание:")
print(df.describe())