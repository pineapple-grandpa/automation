from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(y)

checkbx = browser.find_element_by_id("robotCheckbox")
checkbx.click()

radiobtn = browser.find_element_by_id("robotsRule")
radiobtn.click()

button = browser.find_element_by_xpath('//button[text()="Submit"]')
button.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

