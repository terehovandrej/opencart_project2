from selenium import webdriver
import os


def test_load():
    link = "https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.switch_to.frame(0)
    choose_file = driver.find_element_by_xpath("//input[@name='myFile']")
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'iphone.jpg')
    choose_file.send_keys(file_path)
    driver.quit()
