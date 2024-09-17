import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Укажите URL сайта
print("send you url")
url = input("url")

# Настройка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    print("send you url")
    driver.get(url)

    # Скролл до появления нужного видео
    while True:
        # Получаем текущую высоту страницы
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        # Скроллим вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Ждем несколько секунд для загрузки
        time.sleep(2)

        # Проверяем новую высоту страницы
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Останавливаем, если больше не скроллится

        # Если видео появляется, выходим из цикла
        if "dQw4w9WgXcQ" in driver.page_source:
            break

    # Поиск всех ссылок на странице
    links = driver.find_elements(By.TAG_NAME, 'a')
    filtered_links = []

    for link in links:
        href = link.get_attribute('href')
        if href and href.startswith("https://getgems.io/collection"):
            filtered_links.append(href)

    # Сохранение отфильтрованных ссылок в файл
    with open("filtered_links.txt", "w") as file:
        for filtered_link in filtered_links:
            file.write(filtered_link + "\n")
        
    print(f"Found and saved {len(filtered_links)} links.")

finally:
    driver.quit()