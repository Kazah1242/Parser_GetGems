import os
import re

# Директория с загруженными страницами
downloaded_pages_dir = 'downloaded_pages'
# Директория для сохраненных метаданных
output_dir = 'output'

# Создаем директорию для выходных файлов, если её нет
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Перебираем текстовые файлы в папке downloaded_pages
for filename in os.listdir(downloaded_pages_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(downloaded_pages_dir, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Извлечение имени для названия файла
            name_match = re.search(r'itemProp="name" content="([^"]+)"', content)
            # Извлечение значений traitType и value
            traits_and_values = re.findall(r'__typename":"NftAttribute","traitType":"([^"]+)","value":"([^"]+)"', content)

            if name_match:
                name = name_match.group(1).strip()

                # Путь для сохранения файла
                output_file_path = os.path.join(output_dir, f'{name}.txt')

                # Запись traitType и value в новый текстовый файл
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for trait, value in traits_and_values:
                        output_file.write(f'Trait: {trait}, Value: {value}\n')

print("The metadata has been successfully collected and saved in the output directory.")