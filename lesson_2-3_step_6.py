from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.trollface")
button.click()

new_window = browser.window_handles[1]
browser.switch_to_window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(y)

button = browser.find_element_by_xpath('//button[text()="Submit"]')
button.click()
