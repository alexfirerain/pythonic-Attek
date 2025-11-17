# Импортируем необходимые модули
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
# Создаем экземпляр браузера (открываем Chrome)
try:
    driver = webdriver.Chrome()
# Открываем веб-сайт
    driver.get("https://ya.ru/")
# Ждем 3 секунды, чтобы страница загрузилась
    time.sleep(2)
# Получаем заголовок страницы и выводим его
    element=driver.find_element(By.TAG_NAME, "textarea")
# print(element.text)
# Закрываем браузер
    element.click()
    time.sleep(2)
    element.send_keys("сОбака")
    time.sleep(1)
    element.send_keys(Keys.RETURN)
    time.sleep(5)
    if "собака" in driver.title:
        print("тест пройден успешно")
    else:
        print("тест провален")

    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)

except Exception as e:
    print(f'Произошла ошибка - {e}')
finally:
    driver.quit()
driver.quit()