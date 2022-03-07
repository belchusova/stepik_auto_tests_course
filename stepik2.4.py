from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_xpath("//*[@id='book']")
    button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_xpath("//*[@id='input_value']")
    num1 = input1.text
    num2 = str(math.log(abs(12 * math.sin(int(num1)))))
    input2 = browser.find_element_by_xpath("//*[@id='answer']").send_keys(num2)
    button2 = browser.find_element_by_xpath("//button[@type='submit']")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()