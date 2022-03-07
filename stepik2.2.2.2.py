from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
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