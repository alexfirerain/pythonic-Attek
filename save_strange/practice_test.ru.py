from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("https://practice-automation.com/form-fields/")
    time.sleep(3)

    # element1=driver.find_element(By.NAME, 'name-input')
    # element1.send_keys("Nick")
    # element2=driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    # element2.send_keys("1234")
    # ch1=driver.find_element(By.ID, 'drink1')
    # ch1.click()
    # time.sleep(3)
    # driver.execute_script("window.scrollBy(0, 500)")
    email = driver.find_element(By.ID, "email")
    # time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block: 'center'});", email)
    time.sleep(3)
    email.send_keys("1234@mail.ru")
    time.sleep(5)

except Exception as e:
    print(f"Произошла ошибка - {e}")
finally:
    driver.quit()
