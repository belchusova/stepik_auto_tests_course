from selenium import webdriver
import time
import math
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
try:
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element_by_xpath("//*[@name='firstname']")
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_xpath("//*[@name='lastname']")
    input2.send_keys('Ivanov')
    input3 = browser.find_element_by_xpath("//*[@name='email']")
    input3.send_keys('Ivanov@ya.ru')
    with open("test.txt", "w") as file:
        content = file.write('automationbypython')
    input4 = browser.find_element_by_xpath("//*[@id='file']")
    input4.send_keys('path to file'
                    )
    button1 = browser.find_elements_by_xpath("//*[@type='submit']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()