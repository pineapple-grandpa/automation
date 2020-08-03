from selenium import webdriver
import time
try:
    link='http://suninjuly.github.io/registration1.html'
    browser=webdriver.Chrome()
    browser.get(link)
    firstname=browser.find_element_by_css_selector("div.first_block input.first")
    firstname.send_keys('SCrr')
    lastname=browser.find_element_by_css_selector("div.first_block input.second")
    lastname.send_keys('fff')
    email1=browser.find_element_by_css_selector("div.first_block input.third")
    email1.send_keys('222')
    button=browser.find_element_by_css_selector("button[type='submit']")
    button.click()
    time.sleep(1)
    txt1=browser.find_element_by_tag_name('h1').text
    assert "Congratulations! You have successfully registered!" == txt1
finally:
    time.sleep(6)
    browser.quit()