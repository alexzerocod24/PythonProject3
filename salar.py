import pandas as pd


file_path = 'dz.csv'
df = pd.read_csv(file_path)

print(df.head())

average_salary_by_city = df.groupby('City')['Salary'].mean()

print("\nСредняя зарплата по городу:")
print(average_salary_by_city)