from selenium import webdriver
import time
import math
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
try:
    browser.get("http://SunInJuly.github.io/execute_script.html")

    input1 = browser.find_element_by_xpath("//*[@id='input_value']")
    num1 = input1.text
    num2 = str(math.log(abs(12 * math.sin(int(num1)))))
    input2 = browser.find_element_by_xpath("//*[@id='answer']").send_keys(num2)
    browser.execute_script("window.scrollBy(0, 150);")

    option1 = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    button1 = browser.find_elements_by_xpath("//*[@class='btn btn-primary']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()