from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element_by_id("num1")
num_2 = browser.find_element_by_id("num2")
sum = int(num_1.text) + int(num_2.text)

select = Select(browser.find_element_by_css_selector(".custom-select"))
select.select_by_value(str(sum))

submit = browser.find_element_by_css_selector(".btn")
submit.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

