import os
import requests
import time

# Путь к файлу с ссылками
links_file = 'filtered_links.txt'
# Папка для сохранения HTML файлов
output_dir = 'downloaded_pages'
# Задержка между запросами в секундах
delay = 1  # Измените значение по необходимости, меньше ставить не рекомендую лочит запрос

# Создаем папку для сохранения, если её нет
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Чтение ссылок из файла
with open(links_file, 'r', encoding='utf-8') as file:
    links = file.readlines()

# Проход по каждой ссылке
for link in links:
    link = link.strip()  # Удаляем лишние пробелы и символы новой строки
    if link:  # Проверяем, что строка не пустая
        try:
            # Запрос к странице
            response = requests.get(link)
            response.raise_for_status()  # Проверка на наличие ошибок

            # Формирование названия файла на основе URL
            file_name = link.split('/')[-1] or 'index'  # Используем последний элемент URL или 'index'
            if not file_name.endswith('.txt'):  # Убедимся, что файл имеет правильное расширение
                file_name = f"{file_name}.txt"
            file_path = os.path.join(output_dir, file_name)

            # Сохранение HTML-кода в текстовом файле
            with open(file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(response.text)

            print(f"Download : {link} -> {file_path}")

            # Задержка между запросами
            time.sleep(delay)

        except requests.exceptions.RequestException as e:
            print(f"Error when working with the link {link}: {e}")