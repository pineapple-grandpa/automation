from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(y)

checkbx = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbx)
checkbx.click()

radiobtn = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
radiobtn.click()

button = browser.find_element_by_xpath('//button[text()="Submit"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
