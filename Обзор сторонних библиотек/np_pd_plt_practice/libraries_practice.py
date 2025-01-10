import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Работа с pandas: Чтение таблицы из Excel"""
#есть excel файл, в нем содержится таблица, не разбитая по столбцами (а разбита запятыми),
#необходимо прочитать эту таблицу и записать её в txt
excel_path = 'exapmle_data.xlsx'
result_table_path = 'result_table'

START_READ_ROW = 22 - 1 # чтение начинаем с 22 строки, -1 т.к. будем применять skiprows
NUM_OF_ROWS = 40

df = pd.read_excel(excel_path, skiprows=START_READ_ROW) #чтение экселя
rows = []
for index, row in df.iterrows(): #заполнение списка значений в строках, разделяя их по запятым
    if isinstance(row[0], float):
        continue  # пропускаем пустые или неправильные строки
    data = str(row[0]).split(",")  # преобразуем данные в строку, затем разделяем по запятой
    rows.append(data)

columns = ["Point", "Elongation", "Force", "Position", "Code", "Samplerate", "Motorspeed"] # заголовки таблицы
df_parsed = pd.DataFrame(rows, columns=columns) #объединение строк в датафрейм

df_parsed.head(NUM_OF_ROWS).to_csv(result_table_path, index=False, sep=' ', header=True) # сохранение 40 строк таблицы в txt


"""Работа с numpy: усреднню две соседних строки в таблице, найдя средние значений в ней (по сути создать 2 матриц-вектора
    и найти средний вектор у 2х соседей"""
data = []
with open(result_table_path, 'r') as file:
    for line in file:
        values = line.strip().split() # разделяю строки на элементы
        try:
            row = [float(value) for value in values[:-1]] # исключение последнего столбца, тк там есть символы
        except(ValueError):
            continue
        data.append(row)

data_array = np.array(data) # создание матрицы из данных таблицы

average_data = []
for num_row in range(len(data_array)):
    if num_row < NUM_OF_ROWS - 1:
        average_vector = np.mean(np.array([data_array[num_row], data_array[num_row + 1]]), axis=0)
        average_data.append(average_vector)
        num_row += 1
    else: break

rows = []
df_average = pd.DataFrame(average_data, columns=columns[:-1])
print(df_average)
"""Работа с matplotlib: построить график зависимости одного столбца от другого"""

plt.plot(df_average['Point'], df_average['Force'], marker='o', label='Force of Point dependency')
plt.xlabel('Точка')  # Метка оси X
plt.ylabel('Сила')  # Метка оси Y
plt.title('Зависимость Силы от точки')  # Заголовок графика
plt.legend()  # Легенда
plt.grid(True)  # Включить сетку
plt.show()  # Отобразить график





