import os

# Путь к директории с файлами
directory = 'C:/Users/andre\Desktop/Ncorr_post_v2\export/virtualExtensometer_5'
# Имя файла для записи результата
output_file = 'average_results_y.txt'

# Получаем список всех текстовых файлов
files = [f for f in os.listdir(directory) if f.endswith('.txt')]

# Считываем строки из каждого файла
all_lines = []
for file_name in files:
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        # Разбиваем на строки, убирая переводы
        lines = f.read().splitlines()
        all_lines.append(lines)

# Находим максимальное количество строк среди всех файлов
max_lines = max(len(lines) for lines in all_lines) if all_lines else 0

# Открываем файл для записи результата
with open(os.path.join(directory, output_file), 'w', encoding='utf-8') as out:
    # Вычисляем среднее арифметическое по каждой строке
    for line_index in range(max_lines):
        values = []
        for lines in all_lines:
            if line_index < len(lines):
                line_value = lines[line_index].strip()
                if line_value:
                    try:
                        number = float(line_value)
                        values.append(number)
                    except ValueError:
                        # Если в строке не число, пропускаем
                        pass

        if values:
            avg = sum(values) / len(values)
            out.write(f" {avg}\n")
        else:
            out.write(f"Строка {line_index + 1}: нет данных для вычисления среднего\n")

print(f"Результаты записаны в файл: {os.path.join(directory, output_file)}")
# По результам работы программы получаем текстовый файл с значениями средних деформаций.
# Далее необходимо интерполировать значения на интервал всего нагружения и записать значения деформации с шагом в 0,1 с (как построена нагрузка). Для этого воспользуемся линейной интерполяцией.
# Код на Python, представленный ниже выписывает в файл






