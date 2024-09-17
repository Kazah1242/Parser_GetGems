import os
import requests

# Папка с текстовыми файлами
dir_name = 'NFT_img'
# Папка для сохранения изображений
output_dir = 'NFT_images'

def скачать_изображения(dir_name, output_dir):
    # Проверка, существует ли папка с текстовыми файлами
    if not os.path.exists(dir_name):
        print(f"Папка {dir_name} не найдена.")
        return

    # Создание папки для изображений, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Проход по каждому файлу в папке
    for filename in os.listdir(dir_name):
        if filename.endswith('.txt'):
            file_path = os.path.join(dir_name, filename)

            # Чтение ссылок из текстового файла
            with open(file_path, 'r', encoding='utf-8') as file:
                links = file.readlines()

            # Скачивание изображений по ссылкам
            for link in links:
                link = link.strip()  # Убираем пробелы и переносы

                if link:
                    image_name = filename.replace('.txt', '.jpg')  # Имя изображения
                    image_path = os.path.join(output_dir, image_name)  # Путь для сохранения изображения
                    print(f"Downloading: {image_path} from {link}")

                    try:
                        response = requests.get(link)
                        response.raise_for_status()  # Выбросить исключение для статуса 4xx или 5xx

                        # Запись изображения в файл
                        with open(image_path, 'wb') as img_file:
                            img_file.write(response.content)
                            print(f"Image {image_name} successfully downloaded.")

                    except requests.exceptions.RequestException as e:
                        print(f"Download error  {link}: {e}")

# Запуск функции
скачать_изображения(dir_name, output_dir)