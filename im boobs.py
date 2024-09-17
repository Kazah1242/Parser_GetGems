import os
import shutil

# Папка с файлами
source_dir = 'combined_files'
# Словарь для хранения имён файлов
file_dict = {}

# Проходим по всем файлам в папке
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    
    # Если файл без расширения
    if os.path.isfile(file_path) and '.' not in filename:
        # Создаём файл с расширением .txt
        new_file_path = os.path.join(source_dir, f'{filename}.txt')
        with open(new_file_path, 'w') as new_file:
            new_file.write(f'Содержимое файла: {filename}')  # Здесь можно добавить другое содержимое

# Удаляем файлы без формата
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path) and '.' not in filename:
        os.remove(file_path)

# Собираем имена файлов .txt и изображений в словарь
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        name_key = filename[:-4]  # Убираем .txt
        if name_key not in file_dict:
            file_dict[name_key] = {'txt': [], 'images': []}
        file_dict[name_key]['txt'].append(filename)
    elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):  # Расширения изображений
        name_key = filename.rsplit('.', 1)[0]  # Убираем расширение
        if name_key not in file_dict:
            file_dict[name_key] = {'txt': [], 'images': []}
        file_dict[name_key]['images'].append(filename)

# Перемещение файлов в соответствующие папки
for name, files in file_dict.items():
    target_dir = os.path.join(source_dir, name)
    os.makedirs(target_dir, exist_ok=True)
    
    # Перемещаем .txt файлы
    for txt_file in files['txt']:
        shutil.move(os.path.join(source_dir, txt_file), os.path.join(target_dir, txt_file))
    
    # Перемещаем изображения
    for image_file in files['images']:
        shutil.move(os.path.join(source_dir, image_file), os.path.join(target_dir, image_file))

print('The script was executed successfully! The files are combined into folders.')