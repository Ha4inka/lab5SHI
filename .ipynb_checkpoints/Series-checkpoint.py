import pandas as pd
import numpy as np

grades = pd.Series([5, 4, np.nan, 3, 4, 5], index=[1, 2, 3, 4, 5, 6])
print("Оригінальний Series:")
print(grades)

lab_names = ['Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5', 'Lab 6']
grades_named = pd.Series(grades.values, index=lab_names)
print("\nSeries із змістовними індексами:")
print(grades_named)

print("\nОцінка по Lab 3:", grades_named['Lab 3'])

grades_named.name = "Lab Grades"
print("\nSeries із назвою:")
print(grades_named)

print("\nОцінки по Lab 2-3:")
print(grades_named[['Lab 2', 'Lab 3']])

print("\nОцінки у зворотному порядку:")
print(grades_named[::-1])

print("\nЛабораторні роботи з оцінкою ≥ 4:")
print(grades_named[grades_named >= 4])

print("\nSeries, відсортований за індексами:")
print(grades_named.sort_index())
ог
print("\nSeries, відсортований за значеннями:")
print(grades_named.sort_values())
