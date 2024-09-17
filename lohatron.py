import os
import shutil

# Получаем путь к директории, где находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Списки папок и файла для удаления
folders_to_remove = [
    'downloaded_pages',
    'NFT_images',
    'NFT_img',
    'output'
]
file_to_remove = 'filtered_links.txt'

# Удаляем папки
for folder in folders_to_remove:
    folder_path = os.path.join(script_dir, folder)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)  # Удаление папки и её содержимого
        print(f'Папка {folder} была удалена.')
    else:
        print(f'Папка {folder} не найдена.')

# Удаляем файл
file_path = os.path.join(script_dir, file_to_remove)
if os.path.exists(file_path):
    os.remove(file_path)  # Удаление файла
    print(f'Файл {file_to_remove} был удален.')
else:
    print(f'Файл {file_to_remove} не найден.')