from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_name("firstname")
name.send_keys("Yolo")
lastname = browser.find_element_by_name("lastname")
lastname.send_keys("Puky")
email = browser.find_element_by_name("email")
email.send_keys("test@test.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')
file = browser.find_element_by_id("file")
file.send_keys(file_path)

button = browser.find_element_by_xpath('//button[text()="Submit"]')
button.click()

