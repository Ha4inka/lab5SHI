import pandas as pd

data = {
    'Math': pd.Series([5, 4, 3, 5], index=['Student A', 'Student B', 'Student C', 'Student D']),
    'Physics': pd.Series([4, 5, 4, 3], index=['Student A', 'Student B', 'Student C', 'Student D']),
    'CS': pd.Series([3, 4, 5, 5], index=['Student A', 'Student B', 'Student C', 'Student D']),
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

print("\nСписок дисциплін:")
print(df.columns.tolist())

print("\nОцінки з Physics:")
print(df['Physics'])

print("\nОцінки Student A:")
print(df.loc['Student A'])

print("\nОцінки двох останніх студентів:")
print(df.tail(2))

print("\nОцінки Student A та Student B по Math і Physics:")
print(df.loc[['Student A', 'Student B'], ['Math', 'Physics']])

df['History'] = [4, 3, 5, 4]
print("\nDataFrame після додавання History:")
print(df)

print("\nСтатистика по дисциплінах:")
print(df.describe())

print("\nКількість входжень оцінок з Physics:")
print(df['Physics'].value_counts())

df.to_csv('grades.csv', index=True)
print("\nDataFrame збережено у файл grades.csv.")
