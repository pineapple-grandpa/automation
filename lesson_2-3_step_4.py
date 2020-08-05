from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element_by_css_selector(".btn")
btn.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(y)

button = browser.find_element_by_xpath('//button[text()="Submit"]')
button.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()