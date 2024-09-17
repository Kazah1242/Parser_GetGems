import os
import shutil

# Получаем путь к директории, в которой находится данный скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))

# Задаем пути к папкам NFT_images и output
nft_dir = os.path.join(current_dir, 'NFT_images')
output_dir = os.path.join(current_dir, 'output')

# Создаем папку для объединенных файлов
combined_dir = os.path.join(current_dir, 'combined_files')
os.makedirs(combined_dir, exist_ok=True)

# Функция для копирования файлов
def copy_files(src_dir):
    for filename in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, filename)
        dest_file_path = os.path.join(combined_dir, filename)

        # Копируем файл в общую директорию
        try:
            if os.path.isfile(src_file_path):  # Проверяем, что это файл
                shutil.copy(src_file_path, dest_file_path)
                print(f'Copied: {filename}')
            elif os.path.isdir(src_file_path):  # Если это папка, рекурсивный вызов
                shutil.copytree(src_file_path, dest_file_path)
                print(f'A folder has been copied: {filename}')
        except Exception as e:
            print(f'Error when copying {filename}: {e}')

# Копируем файлы из обеих папок
copy_files(nft_dir)
copy_files(output_dir)

print('The copy is completed.')