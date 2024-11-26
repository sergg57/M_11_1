

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


s = pd.Series([1, 2, 3, 4, 5])
print(s)
s.plot()
plt.show()

data = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']

print(data)
df = pd.DataFrame(np.random.randn(7, 3), index=list(data), columns=['A', 'B', 'C'])
print(df)
print('----------------------------------------')
print(f'Матрица:\n {df.to_numpy()}')

print('----------------------------------------')

# Запись таблицы в файл
df.to_csv('data.csv', index=False)
df.to_csv('data.csv')

# Чтение из файла
df_read = pd.read_csv('data.csv', index_col=0)
print(f'Чтение из файла data.csv:\n {df_read}\n')
print('----------------------------------------')

# Среднее значение по столбцам
print(f'Среднее значение по столбцам:\n{df.mean(axis=0)}\n')
# Среднее значение по строкам
print(f'Среднее значение по строкам:\n{df.mean(axis=1)}\n')
print('----------------------------------------')
# Статистика по таблице
print(f'Статистика по таблице:\n{df.describe()}\n')
print('----------------------------------------')

# Добавление новых Столбцов
df['Среднее'] = df.mean(axis=1)
df['Сумма '] = df.sum(axis=1)
print(f'Добавление новых Столбцов:\n{df}\n')

# Добавление новых строк
df.loc['Среднее'] = pd.Series(df.mean(axis=0))
df.loc['Итого'] = pd.Series(df.sum(axis=0))
print(f'Добавление новых строк:\n{df}\n')






