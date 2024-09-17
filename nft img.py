import os
import re

# Названия директорий
downloaded_pages_dir = 'downloaded_pages'
nft_img_dir = 'NFT_img'

# Создаем папку для изображений, если её нет
if not os.path.exists(nft_img_dir):
    os.makedirs(nft_img_dir)

# Перебираем текстовые файлы в папке downloaded_pages
for filename in os.listdir(downloaded_pages_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(downloaded_pages_dir, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Извлечение ссылок
            links = re.findall(r'(https://i\.getgems\.io[^,]*),"baseUrl"', content)
            # Извлечение имени
            name_match = re.search(r'itemProp="name" content="([^"]+)"', content)

            # Если имя найдено, используем его как имя файла
            if name_match:
                name = name_match.group(1)

                # Очищаем ссылки
                cleaned_links = [link[:-1] for link in links]  # Удаляем '","baseUrl'

                # Путь для сохранения файла
                output_file_path = os.path.join(nft_img_dir, f'{name}.txt')

                # Запись очищенных ссылок в новый текстовый файл
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for link in cleaned_links:
                        output_file.write(link + '\n')

print("The links have been successfully copied and cleared.")